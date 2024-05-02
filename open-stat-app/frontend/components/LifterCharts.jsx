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
                    backgroundColor: "black",
                    borderColor: "red",
                    borderWidth: 1
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
                    borderColor: "green",
                    borderWidth: 1
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
                    borderColor: "blue",
                    borderWidth: 1
                }
            ]
          }}
          title = "Deadlift" 
          />
      </div>
  );
};

export default LifterCharts