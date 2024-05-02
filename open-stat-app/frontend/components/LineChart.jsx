'use client';
import { useRef, useEffect } from "react";
import { Chart } from "chart.js/auto";

export default function LineChart(props) {
    const chartRef = useRef(null)


    useEffect(() => {
        if (chartRef.current) {
            if (chartRef.current.chart) {
                chartRef.current.chart.destroy()
            }

            const context = chartRef.current.getContext("2d")

            const newChart = new Chart(context, {
                type: "line",
                data: props.data,
                options: {
                    plugins:{
                        legend: {
                         display: false
                        },
                        title: {
                            text: props.title,
                            display: true
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
    }, [props.data, props.title])

    return <div>
        <canvas ref={chartRef}/>
    </div>
}