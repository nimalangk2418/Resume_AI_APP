import { useState } from "react";
import { useNavigate } from "react-router-dom";

import {

    Box,
    Button,
    Container,
    Paper,
    TextField,
    Typography

} from "@mui/material";

import { login } from "../services/api";


function Login() {

    const navigate = useNavigate();

    const [email, setEmail] = useState("");

    const [password, setPassword] = useState("");

    const [loading, setLoading] = useState(false);

    const [error, setError] = useState("");


    // ============================================
    // Login Function
    // ============================================

    const handleLogin = async () => {

        try {

            setLoading(true);

            setError("");

            const response = await login(

                email,

                password

            );

            localStorage.setItem(

                "access_token",

                response.data.access_token

            );

            navigate("/dashboard");

        }

        catch (err: any) {

            setError(

                err.response?.data?.detail ||

                "Login Failed"

            );

        }

        finally {

            setLoading(false);

        }

    };


    return (

        <Container

            maxWidth="sm"

            sx={{

                mt: 10

            }}

        >

            <Paper

                elevation={5}

                sx={{

                    padding: 5

                }}

            >

                <Typography

                    variant="h4"

                    align="center"

                    gutterBottom

                >

                    Resume AI Screening

                </Typography>


                <Typography

                    align="center"

                    mb={3}

                >

                    Recruiter Login

                </Typography>


                <TextField

                    fullWidth

                    margin="normal"

                    label="Email"

                    type="email"

                    value={email}

                    onChange={(e) =>

                        setEmail(e.target.value)

                    }

                />


                <TextField

                    fullWidth

                    margin="normal"

                    label="Password"

                    type="password"

                    value={password}

                    onChange={(e) =>

                        setPassword(e.target.value)

                    }

                />


                {

                    error &&

                    <Typography

                        color="error"

                        mt={2}

                    >

                        {error}

                    </Typography>

                }


                <Button

                    fullWidth

                    variant="contained"

                    sx={{

                        mt: 3

                    }}

                    onClick={handleLogin}

                    disabled={loading}

                >

                    {

                        loading ?

                        "Signing In..." :

                        "Login"

                    }

                </Button>

            </Paper>

        </Container>

    );

}

export default Login;