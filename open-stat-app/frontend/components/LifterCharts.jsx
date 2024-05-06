'use client';
import LineChart from "./LineChart";
import { useEffect } from "react";

function useReloadOnResize() {
  useEffect(() => {
    const handleResize = () => {
      window.location.reload();
    };

    window.addEventListener('resize', handleResize);

    return () => {
      window.removeEventListener('resize', handleResize);
    };
  }, []);
}

const LifterCharts = (props) => {
  
  useReloadOnResize();

  return (
      <div className="chartContainer">
        <LineChart 
          data = {{
            labels: props.labels,
            datasets: [
                {
                    data: props.squat_data,
                    backgroundColor: ["red", "red" , "red" , "red", "red", "red", "red", "red", "red", "red", "red", "red", "red", "red", "red", "red", "red", "red", "red", "red", "red", "red", "red","red", "red", "red", "white", "white", "white"],
                    borderColor: "black",
                    borderWidth: 1,
                    tension: 0.2
                }
            ]
          }}
          title = "Squat" 
          />
        <LineChart 
          data = {{
            labels: props.labels,
            datasets: [
                {
                    data: props.bench_data,
                    backgroundColor: "black",
                    borderColor: "black",
                    borderWidth: 1,
                    tension: 0.2
                }
            ]
          }}
          title = "Bench" 
          />
        <LineChart 
          data = {{
            labels: props.labels,
            datasets: [
                {
                    data: props.dead_data,
                    backgroundColor: "black",
                    borderColor: "black",
                    borderWidth: 1,
                    tension: 0.2
                }
            ]
          }}
          title = "Deadlift" 
          />
          <LineChart 
          data = {{
            labels: props.labels,
            datasets: [
                {
                    data: props.total_data,
                    backgroundColor: "black",
                    borderColor: "black",
                    borderWidth: 1
                }
            ]
          }}
          title = "Total" 
          />
      </div>
  );
};

export default LifterCharts