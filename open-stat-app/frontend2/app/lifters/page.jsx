'use client';

import React from 'react'
import { Line } from 'react-chartjs-2';
import { 
  Chart as ChartJS,
  LineElement,
  CategoryScale, // x axis
  LinearScale, // y axis
  PointElement
} from 'chart.js';

ChartJS.register(
  LineElement,
  CategoryScale, 
  LinearScale, 
  PointElement
)

const page = () => {

  const data = {
    labels: ['Mon, Tue, Wed, Thurs, Fri'],
    datasets: [{
      label: 'My First Dataset',
      data: [3, 6, 9, 12, 15],
      backgroundColor: 'aqua',
      borderColor: 'black',
      pointBorderColor: 'aqua',
      fill: true,
      tension: 0.4
    }]}

  const options = {
    plugins: {
      legend: true,
    },
    scales: {
      y: {
        min: 3,
        max: 15
      }
    }
  }

  return (
  <Line
    options={options}
    data={data}
  />
  )
}

export default page