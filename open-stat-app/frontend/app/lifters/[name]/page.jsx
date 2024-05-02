import { supabase } from '../../../lib/supabase';
import LifterCharts  from '../../../components/LifterCharts';
import LineChart from '../../../components/LineChart';

export default async function LifterPage({params}) {
  const name = params.name.replace(/([a-z])([A-Z])/g, '$1 $2');
  const getLifterByName = async () => {
    const { data, error } = await supabase
      .from("Lifter_Info")
      .select("*")
      .eq("Name", name)
      .order('Date', { ascending: true });

    if (data) {
      return data; // Return the data array
    } 

    console.log(error);
    return []; // Return an empty array if there's an error
    
  };

  const fetchData = async () => {
    const data = await getLifterByName();
    if (data.length > 0) {
      const latestSquat = data[data.length - 2].Squat;
      const latestBench = data[data.length - 1].Bench;
      const latestDeadlift = data[data.length - 1].Deadlift;
      const secondLatestSquat = data.length > 1 ? data[data.length - 3].Squat : latestSquat;
      const secondLatestBench = data.length > 1 ? data[data.length - 2].Bench : latestBench;
      const secondLatestDeadlift = data.length > 1 ? data[data.length - 2].Deadlift : latestDeadlift;
      console.log(secondLatestSquat)
      console.log(latestSquat)
  
      const squat_features = {
        features: {
          Sex: data[data.length - 1].Sex,
          Age: data[data.length - 1].Age,
          Bodyweight: data[data.length - 1].Bodyweight,
          Equiptment: data[data.length - 1].Equiptment,
          Squat_1: latestSquat,
          Squat_2: secondLatestSquat,
        }
      };

      const bench_features = {
        features: {
          Sex: data[data.length - 1].Sex,
          Age: data[data.length - 1].Age,
          Bodyweight: data[data.length - 1].Bodyweight,
          Equiptment: data[data.length - 1].Equiptment,
          Bench_1: latestBench,
          Bench_2: secondLatestBench,
        }
      };

      const dead_features = {
        features : {
          Sex: data[data.length - 1].Sex,
          Age: data[data.length - 1].Age,
          Bodyweight: data[data.length - 1].Bodyweight,
          Equiptment: data[data.length - 1].Equiptment,
          Deadlift_1: latestDeadlift,
          Deadlift_2: secondLatestDeadlift
        }
      };
  
      // Fetch predictions from Flask backend
      const squatPredictionResponse = await fetch('http://127.0.0.1:5000//predict/squat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify( squat_features )
      });
      const squatPrediction = await squatPredictionResponse.json();
      console.log(squatPrediction)
  
      //const benchPredictionResponse = await fetch('http://127.0.0.1:5000//predict/bench', {
       // method: 'POST',
        //headers: {
          //'Content-Type': 'application/json'
        //},
       // body: JSON.stringify( bench_features )
     // });
      //const benchPrediction = await benchPredictionResponse.json();
  
      //const deadliftPredictionResponse = await fetch('http://127.0.0.1:5000//predict/deadlift', {
       // method: 'POST',
        //headers: {
          //'Content-Type': 'application/json'
        //},
       // body: JSON.stringify( dead_features )
      //});
      //const deadliftPrediction = await deadliftPredictionResponse.json();
  
      return {
        data,
        squatPrediction: squatPrediction.prediction,
        //benchPrediction: benchPrediction.prediction,
        //deadliftPrediction: deadliftPrediction.prediction
      };
    };
  };

  // Call fetchData to get the first Squat value
  const result = await fetchData();
  const realdata = result.data;
  const labels = realdata.map((row) => row.Date);
  const squat_data = realdata.map((row) => row.Squat);
  const bench_data = realdata.map((row) => row.Bench);
  const dead_data = realdata.map((row) => row.Deadlift);
  
  return (
    <>
        <LifterCharts labels={labels} squat_data={squat_data} bench_data={bench_data} dead_data={dead_data}/>
    </>
  );
};




