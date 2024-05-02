'use client';
import { useRef, useEffect } from "react";
import { Chart } from "chart.js/auto";

export default function LineChart() {
    const chartRef = useRef(null)


    useEffect(() => {
        if (chartRef.current) {
            if (chartRef.current.chart) {
                chartRef.current.chart.destroy()
            }

            const context = chartRef.current.getContext("2d")

            const newChart = new Chart(context, {
                type: "line",
                data: {
                    labels: ["MON", "TUE", "WED", "THURS", "FRI"],
                    datasets: [
                        {
                            data: [34, 64, 50, 1, 4],
                            backgroundColor: "black",
                            borderColor: "red",
                            borderWidth: 1,
                        }
                    ]
                },
                options: {
                    plugins:{
                        legend: {
                         display: false
                        }
                    },
                    responsive: true,
                    scales: {
                        x: {
                            type: "category"
                        },
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });

            chartRef.current.chart = newChart
        }
    }, [])

    return <div>
        <canvas ref={chartRef}/>
    </div>
}