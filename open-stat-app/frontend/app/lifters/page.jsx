'use client';
import LineChart from "../../components/LineChart";
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

const page = () => {
  
  useReloadOnResize();

  return (
      <div className="chartContainer">
        <LineChart 
          data = {{
            labels: ["MON", "TUE", "WED", "THURS", "FRI"],
            datasets: [
                {
                    data: [20, 30, 40, 50, 60],
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
            labels: ["MON", "TUE", "WED", "THURS", "FRI"],
            datasets: [
                {
                    data: [20, 30, 40, 50, 60],
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
            labels: ["MON", "TUE", "WED", "THURS", "FRI"],
            datasets: [
                {
                    data: [20, 30, 40, 50, 60],
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

export default page