import axios from "axios";

// ======================================================
// Axios Instance
// ======================================================

const api = axios.create({

    baseURL: "http://localhost:8000",

    headers: {

        "Content-Type": "application/json"

    }

});


// ======================================================
// Add JWT Token
// ======================================================

api.interceptors.request.use(

    (config) => {

        const token = localStorage.getItem("access_token");

        if (token) {

            config.headers.Authorization = `Bearer ${token}`;

        }

        return config;

    },

    (error) => {

        return Promise.reject(error);

    }

);


// ======================================================
// Authentication APIs
// ======================================================

export const login = async (

    email: string,

    password: string

) => {

    return api.post("/auth/login", {

        email,

        password

    });

};


export const register = async (

    full_name: string,

    email: string,

    password: string

) => {

    return api.post("/auth/register", {

        full_name,

        email,

        password

    });

};


// ======================================================
// Resume Upload
// ======================================================

export const uploadResume = async (

    file: File

) => {

    const formData = new FormData();

    formData.append(

        "file",

        file

    );

    return api.post(

        "/upload/resume",

        formData,

        {

            headers: {

                "Content-Type":

                "multipart/form-data"

            }

        }

    );

};


// ======================================================
// Job Description Upload
// ======================================================

export const uploadJobDescription = async (

    data: any

) => {

    return api.post(

        "/upload/job-description",

        data

    );

};


// ======================================================
// Resume Screening
// ======================================================

export const screenCandidate = async (

    data: any

) => {

    return api.post(

        "/screen/candidate",

        data

    );

};


// ======================================================
// Reports
// ======================================================

export const getReports = async () => {

    return api.get(

        "/report/all"

    );

};


export const downloadReport = async (

    reportId: number

) => {

    return api.get(

        `/report/download/${reportId}`,

        {

            responseType: "blob"

        }

    );

};


// ======================================================
// Export Axios Instance
// ======================================================

export default api;