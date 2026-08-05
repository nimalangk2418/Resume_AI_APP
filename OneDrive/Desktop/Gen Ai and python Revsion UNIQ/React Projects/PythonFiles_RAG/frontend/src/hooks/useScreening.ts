import { useState } from "react";

import { screenCandidate } from "../services/api";


interface ScreeningRequest {

    resume_id: number;

    job_id: number;

    recruiter_query: string;

    job_description: string;

}


export default function useScreening() {

    const [loading, setLoading] = useState(false);

    const [error, setError] = useState("");

    const [result, setResult] = useState<any>(null);


    // ===========================================
    // Start AI Screening
    // ===========================================

    const startScreening = async (

        data: ScreeningRequest

    ) => {

        try {

            setLoading(true);

            setError("");

            const response = await screenCandidate(

                data

            );

            setResult(

                response.data

            );

            return response.data;

        }

        catch (err: any) {

            setError(

                err.response?.data?.detail ||

                "AI Screening Failed"

            );

            return null;

        }

        finally {

            setLoading(false);

        }

    };


    // ===========================================
    // Reset State
    // ===========================================

    const reset = () => {

        setResult(null);

        setError("");

    };


    return {

        loading,

        error,

        result,

        startScreening,

        reset

    };

}