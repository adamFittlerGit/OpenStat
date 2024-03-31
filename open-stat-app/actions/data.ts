import { createClient } from '@supabase/supabase-js';

export default async function getData(name: string) {
    // Directly access the environment variables
    const url = process.env.SUPABASE_URL;
    const key = process.env.SUPABASE_SECRET_KEY;

    // Throw error if undefined
    if (!url || !key) {
        throw new Error("Supabase URL and key must be defined");
    }

    const supabase = createClient(url, key); 
    
    
    const { data, error } = await supabase
        .from('Lifter_Info')
        .select('Squat')
        .eq('Name', 'John Haack')
    
    return data
}