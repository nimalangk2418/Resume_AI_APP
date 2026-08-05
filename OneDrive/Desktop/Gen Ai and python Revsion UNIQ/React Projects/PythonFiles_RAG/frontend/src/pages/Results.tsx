import { useLocation, useNavigate } from "react-router-dom";

import {

    Box,
    Button,
    Card,
    CardContent,
    Chip,
    Container,
    Divider,
    Grid,
    List,
    ListItem,
    Typography

} from "@mui/material";

import CandidateCard from "../components/CandidateCard";
import ReportViewer from "../components/ReportViewer";


function Results() {

    const location = useLocation();

    const navigate = useNavigate();

    const data = location.state;


    if (!data) {

        return (

            <Container>

                <Typography variant="h5">

                    No Screening Results Available

                </Typography>

                <Button

                    variant="contained"

                    sx={{ mt: 3 }}

                    onClick={() => navigate("/dashboard")}

                >

                    Back to Dashboard

                </Button>

            </Container>

        );

    }


    const result = data.screening_result;

    const report = data.report;


    return (

        <Container

            maxWidth="lg"

            sx={{ mt: 4 }}

        >

            <Typography

                variant="h4"

                gutterBottom

            >

                Resume Screening Results

            </Typography>


            <Grid container spacing={3}>


                {/* Candidate Summary */}

                <Grid item xs={12} md={4}>

                    <CandidateCard

                        candidate={result}

                    />

                </Grid>


                {/* AI Analysis */}

                <Grid item xs={12} md={8}>

                    <Card>

                        <CardContent>

                            <Typography

                                variant="h5"

                                gutterBottom

                            >

                                AI Analysis

                            </Typography>

                            <Divider sx={{ mb: 2 }} />



                            <Typography

                                variant="h6"

                            >

                                Recommendation

                            </Typography>

                            <Typography>

                                {result.recommendation}

                            </Typography>



                            <Box mt={3}>

                                <Typography

                                    variant="h6"

                                >

                                    Technical Skills

                                </Typography>

                                {

                                    result.technical_skills?.map(

                                        (skill: string, index: number) => (

                                            <Chip

                                                key={index}

                                                label={skill}

                                                sx={{ m: 0.5 }}

                                            />

                                        )

                                    )

                                }

                            </Box>



                            <Box mt={3}>

                                <Typography

                                    variant="h6"

                                >

                                    Strengths

                                </Typography>

                                <List>

                                    {

                                        result.strengths?.map(

                                            (item: string, index: number) => (

                                                <ListItem key={index}>

                                                    • {item}

                                                </ListItem>

                                            )

                                        )

                                    }

                                </List>

                            </Box>



                            <Box mt={3}>

                                <Typography

                                    variant="h6"

                                >

                                    Skill Gap

                                </Typography>

                                <List>

                                    {

                                        result.skill_gap?.map(

                                            (item: string, index: number) => (

                                                <ListItem key={index}>

                                                    • {item}

                                                </ListItem>

                                            )

                                        )

                                    }

                                </List>

                            </Box>



                            <Box mt={3}>

                                <Typography

                                    variant="h6"

                                >

                                    Interview Questions

                                </Typography>

                                <List>

                                    {

                                        result.interview_questions?.map(

                                            (question: string, index: number) => (

                                                <ListItem key={index}>

                                                    {index + 1}. {question}

                                                </ListItem>

                                            )

                                        )

                                    }

                                </List>

                            </Box>

                        </CardContent>

                    </Card>

                </Grid>


                {/* Report */}

                <Grid item xs={12}>

                    <ReportViewer

                        report={report}

                    />

                </Grid>

            </Grid>


            <Button

                variant="contained"

                sx={{ mt: 3 }}

                onClick={() => navigate("/dashboard")}

            >

                Back to Dashboard

            </Button>

        </Container>

    );

}

export default Results;