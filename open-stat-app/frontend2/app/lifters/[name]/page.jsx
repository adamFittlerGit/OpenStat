import { supabase } from '@/lib/supabase';

export default async function LifterPage({params}) {
  const name = params.name.replace(/([a-z])([A-Z])/g, '$1 $2');
  const getLifterByName = async () => {
    const { data, error } = await supabase
      .from("Lifter_Info")
      .select("*")
      .eq("Name", name);

    if (data) {
      return data; // Return the data array
    } 

    console.log(error);
    return []; // Return an empty array if there's an error
    
  };

  const fetchData = async () => {
    const data = await getLifterByName();
    return data.length > 0 ? data : null; // Return the Squat value of the first object, or null if data is empty
  };

  // Call fetchData to get the first Squat value
  const data = await fetchData();

  return (
    <>
        <ul>
          {data.map((row) => (
            <li key={row.ID}>{row.Date}: {row.Squat}</li>
          ))}
        </ul>
    </>
  );
};




