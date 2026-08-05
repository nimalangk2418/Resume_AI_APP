import {

    Card,
    CardContent,
    Typography,
    Chip,
    Box,
    LinearProgress

} from "@mui/material";


interface Candidate {

    candidate_name: string;

    match_score: number;

    recommendation: string;

    technical_skills: string[];

}


interface Props {

    candidate: Candidate;

}


function CandidateCard({

    candidate

}: Props) {

    // ============================================
    // Candidate Status
    // ============================================

    const getStatus = () => {

        if (candidate.match_score >= 80)

            return "Selected";

        if (candidate.match_score >= 60)

            return "Shortlisted";

        return "Rejected";

    };


    return (

        <Card

            elevation={5}

        >

            <CardContent>

                <Typography

                    variant="h5"

                    gutterBottom

                >

                    Candidate Summary

                </Typography>


                <Typography

                    variant="h6"

                >

                    {candidate.candidate_name}

                </Typography>


                <Box mt={3}>

                    <Typography>

                        Match Score

                    </Typography>

                    <LinearProgress

                        variant="determinate"

                        value={candidate.match_score}

                        sx={{

                            height: 10,

                            borderRadius: 5,

                            mt: 1

                        }}

                    />

                    <Typography mt={1}>

                        {candidate.match_score}%

                    </Typography>

                </Box>


                <Box mt={3}>

                    <Typography>

                        Recommendation

                    </Typography>

                    <Typography>

                        {candidate.recommendation}

                    </Typography>

                </Box>


                <Box mt={3}>

                    <Typography>

                        Status

                    </Typography>

                    <Chip

                        label={getStatus()}

                        color={

                            candidate.match_score >= 80

                                ? "success"

                                : candidate.match_score >= 60

                                ? "warning"

                                : "error"

                        }

                    />

                </Box>


                <Box mt={3}>

                    <Typography

                        gutterBottom

                    >

                        Technical Skills

                    </Typography>

                    {

                        candidate.technical_skills?.map(

                            (

                                skill,

                                index

                            ) => (

                                <Chip

                                    key={index}

                                    label={skill}

                                    sx={{

                                        m: 0.5

                                    }}

                                    color="primary"

                                />

                            )

                        )

                    }

                </Box>

            </CardContent>

        </Card>

    );

}

export default CandidateCard;