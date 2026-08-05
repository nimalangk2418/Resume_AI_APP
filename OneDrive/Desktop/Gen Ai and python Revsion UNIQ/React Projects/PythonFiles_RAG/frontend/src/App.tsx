import { Routes, Route, Navigate } from "react-router-dom";

import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import Results from "./pages/Results";


function App() {

    return (

        <Routes>

            {/* Default Route */}

            <Route

                path="/"

                element={<Navigate to="/login" replace />}

            />


            {/* Login */}

            <Route

                path="/login"

                element={<Login />}

            />


            {/* Recruiter Dashboard */}

            <Route

                path="/dashboard"

                element={<Dashboard />}

            />


            {/* Screening Results */}

            <Route

                path="/results"

                element={<Results />}

            />


            {/* Invalid Routes */}

            <Route

                path="*"

                element={<Navigate to="/login" replace />}

            />

        </Routes>

    );

}

export default App;