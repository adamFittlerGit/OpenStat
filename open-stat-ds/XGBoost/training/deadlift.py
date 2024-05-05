# ---- Imports ----
import pandas as pd
import seaborn as sns 
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from xgboost import XGBRegressor
from skopt import BayesSearchCV
from skopt.space import Real, Integer
from xgboost import plot_importance
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import joblib 


# ---- Data Loading and Cleaning ----
print("---- Cleaning Data ----\n")
df = pd.read_csv('../../clean_data/clean_data.csv')
# Drop unneeded features 
df = df.drop(columns=['Event', 'Age_Class', 'Weight_Class', 'Bench', 'Squat', 'Total', 'Place', 'Dots', 'Tested', 'Country', 'Federation'])
# Fill in missing data 
for col in df.columns:
    if df[col].dtype == 'float64' or df[col].dtype == 'int64':
        # Fill missing values with mean for numerical columns
        col_mean = df[col].mean()
        df[col] = df[col].fillna(col_mean)
    elif df[col].dtype == 'object':
        # Fill missing values with mode for categorical columns
        col_mode = df[col].mode()[0]
        df[col] = df[col].fillna(col_mode)
encoder = LabelEncoder() 
df['Sex'] = encoder.fit_transform(df['Sex'])
df['Equiptment'] = encoder.fit_transform(df['Equiptment'])
print(df.head())

print("---- Formatting Data ----\n")
df = df.sort_values(by='Date')
# Applying the groupby and apply operations
df = df.groupby('Name').apply(lambda x: pd.Series({
    'Sex': x['Sex'].iloc[0],
    'Age': x['Age'].iloc[0],
    'Bodyweight': x['Bodyweight'].iloc[0],
    'Equiptment': x['Equiptment'].iloc[0],
    'Deadlift_1': x['Deadlift'].iloc[-3] if len(x) >= 3 else None,
    'Deadlift_2': x['Deadlift'].iloc[-2] if len(x) >= 2 else None,
    'Deadlift_3': x['Deadlift'].iloc[-1] if len(x) >= 1 else None
})).reset_index()
df = df.drop(columns='Name')

print(df.shape)
df.head()
df = df.dropna()
# Assuming df is your DataFrame
df = df[(df['Deadlift_1'] != 0.0) & (df['Deadlift_2'] != 0.0) & (df['Deadlift_3'] != 0.0) & (df['Deadlift_1'] <= df['Deadlift_2']) & (df['Deadlift_2'] <= df['Deadlift_3'])]
print(df.shape)
        
df['Sex'] = df['Sex'].astype('Int64')
df['Equiptment'] = df['Equiptment'].astype('Int64')
df['Age'] = df['Age'].astype('Int64')
print(df.head())


# ---- Separate Features/Labels and Normalise/Scale ----
print("---- Seperating and Transforming Data ----\n")
X = df.drop(columns='Deadlift_3')
y = df['Deadlift_3']
# Normalize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


# ---- Perform the Train Test Split ----
print("---- Performing Train Test Split ----\n")
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.1, random_state=420)


# ---- Define and Run Model ----
print("---- Setting up pipeline----\n")
model = XGBRegressor(random_state=420)
# Create a pipeline
pipe = Pipeline([
    ('scaler', StandardScaler()),  # Ensure scaling is part of the pipeline to prevent data leakage
    ('xgb', model)
])
# Define the search space for hyperparameters
search_space = {
    'xgb__max_depth': Integer(3, 10),
    'xgb__learning_rate': Real(0.01, 0.3, 'log-uniform'),
    'xgb__subsample': Real(0.5, 1.0),
    'xgb__colsample_bytree': Real(0.5, 1.0),
    'xgb__colsample_bylevel': Real(0.5, 1.0),
    'xgb__colsample_bynode': Real(0.5, 1.0),
    'xgb__reg_alpha': Real(0.001, 10.0),
    'xgb__reg_lambda': Real(0.001, 10.0),
    'xgb__gamma': Real(0.0, 5.0),
    'xgb__n_estimators': Integer(100, 500)
}
# Using BayesSearchCV for optimization
opt = BayesSearchCV(pipe, search_space, cv=10, n_iter=30, scoring='neg_mean_squared_error', random_state=420)
print("---- Training Model ----\n")
opt.fit(X_train, y_train)
# Best estimator and scores
best_estimator_info = f"Best Estimator: {opt.best_estimator_}\n"
best_mse_info = f"Best MSE: {-opt.best_score_}\n"  # Convert back from negative MSE
test_r2 = opt.best_estimator_.score(X_test, y_test)
test_r2_info = f"Test R^2 score: {test_r2}\n"

print("---- Saving Model ----\n")
# ---- Save the Model ---- 
joblib.dump(opt.best_estimator_, '../models/xgb_model_deadlift.pkl')
joblib.dump(encoder, '../encoders/encoder_deadlift.pkl')
joblib.dump(scaler, '../scalers/scaler_deadlift.pkl')

# Save the printed variables in model_info.txt
with open('../info/stats/model_info_deadlift.txt', 'w') as f:
    f.write(best_estimator_info)
    f.write(best_mse_info)
    f.write(test_r2_info)
# Predictions
y_pred = opt.best_estimator_.predict(X_test)


# Feature Importance
xgboost_model = opt.best_estimator_.named_steps['xgb']
importance = pd.DataFrame({'Feature': X.columns, 'Importance': xgboost_model.feature_importances_}).sort_values(by='Importance', ascending=False)
sns.barplot(x='Importance', y='Feature', data=importance)
plt.title('Feature Importance')
plt.savefig('../info/graphs/deadlift/feature_importance.png')
plt.close()


# ---- Test Loss and R Squared ----
# Test Loss and R Squared
test_mse = mean_squared_error(y_test, y_pred)
test_r2 = r2_score(y_test, y_pred)
test_mse_info = f"Test MSE: {test_mse}\n"
test_r2_info = f"Test R^2: {test_r2}\n"

# Append the MSE and R2 info to model_info.txt
with open('../info/stats/model_info_deadlift.txt', 'a') as f:
    f.write(test_mse_info)
    f.write(test_r2_info)


# ---- Predictions and Residuals ----
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.5, edgecolor='k')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=3)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Actual vs. Predicted Values')
plt.savefig('../info/graphs/deadlift/actual_vs_predicted.png')
plt.close()
residuals = y_test - y_pred
plt.figure(figsize=(10, 6))
plt.scatter(y_pred, residuals, alpha=0.5, edgecolor='k')
plt.axhline(0, color='red', linestyle='--')
plt.xlabel('Predicted')
plt.ylabel('Residuals')
plt.title('Residual Plot')
plt.savefig('../info/graphs/deadlift/residual_plot.png')
plt.close()


# ---- Error Distribution ----
errors = residuals  # Which are y_test - y_pred
plt.figure(figsize=(10, 6))
sns.histplot(errors, bins=30, kde=True)
plt.title('Distribution of Residuals')
plt.xlabel('Prediction Error')
plt.ylabel('Frequency')
plt.savefig('../info/graphs/deadlift/error_distribution.png')
plt.close()


# ---- Save the Model ---- 
joblib.dump(opt.best_estimator_, '../models/xgb_model_deadlift.pkl')
joblib.dump(encoder, '../encoders/encoder_deadlift.pkl')
joblib.dump(scaler, '../scalers/scaler_deadlift.pkl')