import { useState } from "react";

import {

    Box,
    Button,
    Paper,
    TextField,
    Typography

} from "@mui/material";

import {

    uploadResume,
    uploadJobDescription

} from "../services/api";


function UploadForm() {

    const [resume, setResume] = useState<File | null>(null);

    const [jobTitle, setJobTitle] = useState("");

    const [company, setCompany] = useState("");

    const [description, setDescription] = useState("");

    const [skills, setSkills] = useState("");

    const [experience, setExperience] = useState("");

    const [message, setMessage] = useState("");



    // ===================================================
    // Resume Upload
    // ===================================================

    const handleResumeUpload = async () => {

        if (!resume) {

            setMessage("Please select a resume.");

            return;

        }

        try {

            const response = await uploadResume(resume);

            setMessage(

                response.data.message

            );

        }

        catch (error) {

            setMessage(

                "Resume Upload Failed."

            );

        }

    };



    // ===================================================
    // Job Description Upload
    // ===================================================

    const handleJobUpload = async () => {

        try {

            const response = await uploadJobDescription({

                job_title: jobTitle,

                company_name: company,

                description: description,

                required_skills: skills,

                experience: experience

            });

            setMessage(

                response.data.message

            );

        }

        catch (error) {

            setMessage(

                "Job Description Upload Failed."

            );

        }

    };



    return (

        <Paper

            elevation={3}

            sx={{

                p: 3

            }}

        >

            <Typography

                variant="h6"

                gutterBottom

            >

                Upload Resume

            </Typography>

            <input

                type="file"

                accept=".pdf,.doc,.docx"

                onChange={(e) => {

                    if (

                        e.target.files &&

                        e.target.files.length > 0

                    ) {

                        setResume(

                            e.target.files[0]

                        );

                    }

                }}

            />

            <Button

                variant="contained"

                sx={{ mt: 2 }}

                onClick={handleResumeUpload}

            >

                Upload Resume

            </Button>


            <Box mt={5}>

                <Typography

                    variant="h6"

                    gutterBottom

                >

                    Upload Job Description

                </Typography>

                <TextField

                    fullWidth

                    margin="normal"

                    label="Job Title"

                    value={jobTitle}

                    onChange={(e) =>

                        setJobTitle(

                            e.target.value

                        )

                    }

                />

                <TextField

                    fullWidth

                    margin="normal"

                    label="Company"

                    value={company}

                    onChange={(e) =>

                        setCompany(

                            e.target.value

                        )

                    }

                />

                <TextField

                    fullWidth

                    multiline

                    rows={5}

                    margin="normal"

                    label="Job Description"

                    value={description}

                    onChange={(e) =>

                        setDescription(

                            e.target.value

                        )

                    }

                />

                <TextField

                    fullWidth

                    margin="normal"

                    label="Required Skills"

                    value={skills}

                    onChange={(e) =>

                        setSkills(

                            e.target.value

                        )

                    }

                />

                <TextField

                    fullWidth

                    margin="normal"

                    label="Experience"

                    value={experience}

                    onChange={(e) =>

                        setExperience(

                            e.target.value

                        )

                    }

                />

                <Button

                    variant="contained"

                    sx={{ mt: 2 }}

                    onClick={handleJobUpload}

                >

                    Upload Job Description

                </Button>

            </Box>


            {

                message &&

                <Typography

                    color="primary"

                    mt={3}

                >

                    {message}

                </Typography>

            }

        </Paper>

    );

}

export default UploadForm;