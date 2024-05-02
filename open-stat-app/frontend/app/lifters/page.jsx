'use client';
import LineChart from "@/components/LineChart";
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
        <LineChart />
      </div>
  );
};

export default page