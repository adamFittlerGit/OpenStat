'use server';
import DataGridDemo from "../../components/DataGrid";
import { supabase } from "../../lib/supabase";

export default async function Home() {
  const getLifterData = async () => {
    const { data, error } = await supabase
      .from("Lifter_Info")
      .select("Name")
      .eq("Event", "SBD")
      .order('Date', { ascending: false });
      
    if (data) {
      return data; // Return the data array
    } 

    console.log(error);
    return []; // Return an empty array if there's an error
    
  };

  const fetchData = async () => {
    const data = await getLifterData();
    return data.length > 0 ? data : null 
  }

  const columns = [
    {
      field: 'Name',
      headerName: 'Lifter Name',
      width: 150,
      sortable: true,
      headerClassName: 'cellHeader',
      filterable: false,
      hideable: false,
      resizable: false
    },
    {
      field: 'Age',
      headerName: 'Age',
      sortable: true,
      headerClassName: 'cellHeader',
      filterable: false,
      hideable: false,
      resizable: false
    },
    {
      field: 'Weight',
      headerName: 'Weight',
      sortable: true,
      headerClassName: 'cellHeader',
      filterable: false,
      hideable: false,
      resizable: false
    },
    {
      field: 'Sex',
      headerName: 'Sex',
      sortable: true,
      headerClassName: 'cellHeader',
      filterable: false,
      hideable: false,
      resizable: false
    },
    {
      field: 'Squat',
      headerName: 'Squat',
      sortable: true,
      headerClassName: 'cellHeader',
      filterable: false,
      hideable: false,
      resizable: false
    },
    {
      field: 'Bench',
      headerName: 'Bench',
      headerClassName: 'cellHeader',
      filterable: false,
      hideable: false,
      sortable: true,
      resizable: false
    },
    {
      field: 'Deadlift',
      headerName: 'Deadlift',
      headerClassName: 'cellHeader',
      filterable: false,
      hideable: false,
      sortable: true,
      resizable: false
    },
    {
      field: 'Total',
      headerName: 'Total',
      headerClassName: 'cellHeader',
      filterable: false,
      hideable: false,
      sortable: true,
      resizable: false
    },
    {
      field: 'Dots',
      headerName: 'Dots',
      headerClassName: 'cellHeader',
      filterable: false,
      hideable: false,
      sortable: true,
      resizable: false
    },
  ];
  
  
const rows = [
  {
    id: 1,
    Name: 'Jon Snow',
    Age: 14,
    Weight: 60,
    Sex: 'Male',
    Squat: 100,
    Bench: 60,
    Deadlift: 120,
    Total: 280,
    Dots: 300.5,
  },
  {
    id: 2,
    Name: 'Cersei Lannister',
    Age: 31,
    Weight: 65,
    Sex: 'Female',
    Squat: 80,
    Bench: 50,
    Deadlift: 90,
    Total: 220,
    Dots: 250.7,
  },
  {
    id: 3,
    Name: 'Jaime Lannister',
    Age: 31,
    Weight: 70,
    Sex: 'Male',
    Squat: 110,
    Bench: 70,
    Deadlift: 130,
    Total: 310,
    Dots: 330.6,
  },
  {
    id: 4,
    Name: 'Arya Stark',
    Age: 11,
    Weight: 50,
    Sex: 'Female',
    Squat: 70,
    Bench: 40,
    Deadlift: 80,
    Total: 190,
    Dots: 220.1,
  },
  {
    id: 5,
    Name: 'Daenerys Targaryen',
    Age: 25,
    Weight: 60,
    Sex: 'Female',
    Squat: 90,
    Bench: 55,
    Deadlift: 100,
    Total: 245,
    Dots: 275.8,
  },
  {
    id: 6,
    Name: 'Melisandre',
    Age: 150,
    Weight: 55,
    Sex: 'Female',
    Squat: 50,
    Bench: 30,
    Deadlift: 60,
    Total: 140,
    Dots: 160.4,
  },
  {
    id: 7,
    Name: 'Ferrara Clifford',
    Age: 44,
    Weight: 85,
    Sex: 'Male',
    Squat: 150,
    Bench: 100,
    Deadlift: 180,
    Total: 430,
    Dots: 450.9,
  },
  {
    id: 8,
    Name: 'Rossini Frances',
    Age: 36,
    Weight: 75,
    Sex: 'Male',
    Squat: 140,
    Bench: 90,
    Deadlift: 160,
    Total: 390,
    Dots: 410.7,
  },
  {
    id: 9,
    Name: 'Harvey Roxie',
    Age: 65,
    Weight: 70,
    Sex: 'Female',
    Squat: 90,
    Bench: 55,
    Deadlift: 100,
    Total: 245,
    Dots: 270.5,
  },
];
  
  const result = await fetchData();

  return (
    <div className="contentContainer">
      <div className="tableContainer">
        <span></span>
        <DataGridDemo rows={rows} columns={columns}/>
        <span></span>
      </div>
    </div>
  )
}