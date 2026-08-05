import { useState } from "react";
import { useNavigate } from "react-router-dom";

import {

    Box,
    Button,
    Container,
    Grid,
    Paper,
    TextField,
    Typography

} from "@mui/material";

import UploadForm from "../components/UploadForm";

import { screenCandidate } from "../services/api";


function Dashboard() {

    const navigate = useNavigate();

    const [resumeId, setResumeId] = useState("");

    const [jobId, setJobId] = useState("");

    const [jobDescription, setJobDescription] = useState("");

    const [query, setQuery] = useState("");

    const [loading, setLoading] = useState(false);


    // ======================================================
    // AI Screening
    // ======================================================

    const handleScreening = async () => {

        try {

            setLoading(true);

            const response = await screenCandidate({

                resume_id: Number(resumeId),

                job_id: Number(jobId),

                recruiter_query: query,

                job_description: jobDescription

            });

            navigate(

                "/results",

                {

                    state: response.data

                }

            );

        }

        catch (error) {

            console.error(error);

        }

        finally {

            setLoading(false);

        }

    };


    return (

        <Container

            maxWidth="lg"

            sx={{

                mt: 4

            }}

        >

            <Typography

                variant="h4"

                gutterBottom

            >

                Resume AI Screening Dashboard

            </Typography>


            <Grid

                container

                spacing={3}

            >

                {/* Upload */}

                <Grid

                    item

                    xs={12}

                    md={6}

                >

                    <Paper

                        sx={{

                            p: 3

                        }}

                    >

                        <Typography

                            variant="h6"

                            gutterBottom

                        >

                            Upload Documents

                        </Typography>

                        <UploadForm />

                    </Paper>

                </Grid>


                {/* Screening */}

                <Grid

                    item

                    xs={12}

                    md={6}

                >

                    <Paper

                        sx={{

                            p: 3

                        }}

                    >

                        <Typography

                            variant="h6"

                            gutterBottom

                        >

                            AI Resume Screening

                        </Typography>


                        <TextField

                            fullWidth

                            label="Resume ID"

                            margin="normal"

                            value={resumeId}

                            onChange={(e) =>

                                setResumeId(

                                    e.target.value

                                )

                            }

                        />


                        <TextField

                            fullWidth

                            label="Job ID"

                            margin="normal"

                            value={jobId}

                            onChange={(e) =>

                                setJobId(

                                    e.target.value

                                )

                            }

                        />


                        <TextField

                            fullWidth

                            multiline

                            rows={6}

                            margin="normal"

                            label="Job Description"

                            value={jobDescription}

                            onChange={(e) =>

                                setJobDescription(

                                    e.target.value

                                )

                            }

                        />


                        <TextField

                            fullWidth

                            margin="normal"

                            label="Recruiter Question"

                            value={query}

                            onChange={(e) =>

                                setQuery(

                                    e.target.value

                                )

                            }

                        />


                        <Button

                            variant="contained"

                            fullWidth

                            sx={{

                                mt: 3

                            }}

                            onClick={handleScreening}

                            disabled={loading}

                        >

                            {

                                loading ?

                                "Screening..." :

                                "Start AI Screening"

                            }

                        </Button>

                    </Paper>

                </Grid>

            </Grid>

        </Container>

    );

}

export default Dashboard;