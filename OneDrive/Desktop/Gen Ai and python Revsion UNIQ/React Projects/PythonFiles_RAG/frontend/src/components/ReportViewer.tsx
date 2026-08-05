import {

    Card,
    CardContent,
    Typography,
    Button,
    Box,
    Divider

} from "@mui/material";

import DownloadIcon from "@mui/icons-material/Download";

import { downloadReport } from "../services/api";


interface Report {

    report_id: number;

    screening_id: number;

    report_name: string;

    report_path: string;

}


interface Props {

    report: Report;

}


function ReportViewer({

    report

}: Props) {


    // =====================================================
    // Download PDF Report
    // =====================================================

    const handleDownload = async () => {

        try {

            const response = await downloadReport(

                report.report_id

            );

            const url = window.URL.createObjectURL(

                new Blob([response.data])

            );

            const link = document.createElement("a");

            link.href = url;

            link.download = report.report_name;

            document.body.appendChild(link);

            link.click();

            link.remove();

        }

        catch (error) {

            console.error(

                "Download Failed",

                error

            );

        }

    };


    return (

        <Card

            elevation={4}

        >

            <CardContent>

                <Typography

                    variant="h5"

                    gutterBottom

                >

                    Screening Report

                </Typography>

                <Divider sx={{ mb: 2 }} />


                <Box mb={2}>

                    <Typography>

                        <strong>Report ID:</strong>

                        {" "}

                        {report.report_id}

                    </Typography>

                </Box>


                <Box mb={2}>

                    <Typography>

                        <strong>Screening ID:</strong>

                        {" "}

                        {report.screening_id}

                    </Typography>

                </Box>


                <Box mb={2}>

                    <Typography>

                        <strong>Report Name:</strong>

                        {" "}

                        {report.report_name}

                    </Typography>

                </Box>


                <Button

                    variant="contained"

                    startIcon={<DownloadIcon />}

                    onClick={handleDownload}

                >

                    Download PDF Report

                </Button>

            </CardContent>

        </Card>

    );

}

export default ReportViewer;