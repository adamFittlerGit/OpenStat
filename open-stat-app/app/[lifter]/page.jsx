import { supabase } from '@/lib/supabase';

export default async function Page() {
  const getLifterByName = async () => {
    const { data, error } = await supabase
      .from("Lifter_Info")
      .select("*")
      .eq("Name", "John Haack");

    if (data) {
      return data; // Return the data array
    } else {
      console.log(error);
      return []; // Return an empty array if there's an error
    } 
  };

  const fetchData = async () => {
    const data = await getLifterByName();
    return data.length > 0 ? data : null; // Return the Squat value of the first object, or null if data is empty
  };

  // Call fetchData to get the first Squat value
  const data = await fetchData();

  return (
    <>
      <h2>List of Names</h2>
        <ul>
          {data.map((row) => (
            <li key={row.ID}>{row.Squat}</li>
          ))}
        </ul>
    </>
  );
}
