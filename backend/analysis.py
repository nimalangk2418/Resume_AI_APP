# print(git code upload code)
# # # Import the PDF extraction helper so resumes can be converted into readable text.
# # from pdf import read_pdf
# # # Import the logging module to report warnings and status messages during execution.
# # import logging
# # # Import the OS module to read environment variables such as the Groq API key.
# # import os
# # # Import time to create a timestamp-based unique element for cover letter generation.
# # import time
# # # Import the Groq client library for communicating with the Groq LLM API.
# # from groq import Groq
# #
# # # Create a logger for this module so messages can be recorded with context.
# # logger = logging.getLogger(__name__)
# #
# # # ---------------------------------------
# # # Initialize Groq Client
# # # ---------------------------------------
# # # Initialize the Groq client using the API key stored in the environment variables.
# # client = Groq(
# #     # Read the Groq API key from the environment and pass it to the client.
# #     api_key=os.getenv("GROQ_API_KEY")
# # )
# #
# # # Store the model name to be used for all AI-generated resume analysis requests.
# # MODEL = "openai/gpt-oss-120b"
# #
# #
# # # ---------------------------------------
# # # Resume Insights
# # # ---------------------------------------
# # # Define a function that compares a resume against a job description and returns an ATS report.
# # def profile(resume, job_desc):
# #     # Check whether the resume file is missing; if so, log the issue and stop early.
# #     if resume is None:
# #         # Log a warning explaining that no resume was uploaded.
# #         logger.warning("Resume not uploaded.")
# #         # Return an empty string because there is no resume content to analyze.
# #         return ""
# #
# #     # Extract the resume text from the uploaded PDF file.
# #     resume_doc = read_pdf(resume)
# #     # Log a success message after the resume was read successfully.
# #     logger.info("✅ Resume uploaded successfully")
# #
# #     # Build a prompt instructing the model to analyze the resume against the job description.
# #     prompt = f"""
# # You are an expert ATS Resume Analyzer and Senior HR Recruiter.
# #
# # Compare the following resume against the job description.
# #
# # Resume:
# # {resume_doc}
# #
# # Job Description:
# # {job_desc}
# #
# # Generate a professional report with the following sections:
# #
# # # ATS Resume Score
# # (Give score out of 100)
# #
# # # Overall Match Percentage
# #
# # # Chances of Getting Shortlisted
# #
# # # Matching Skills
# #
# # # Missing Skills
# #
# # # Resume Strengths
# #
# # # Weak Areas
# #
# # # Formatting Suggestions
# #
# # # Keyword Optimization Suggestions
# #
# # # Certifications Recommended
# #
# # # Final Recommendation
# # """
# #
# #     # Send the prompt to Groq's chat completion API using the configured model.
# #     response = client.chat.completions.create(
# #         # Select the model that will generate the ATS analysis.
# #         model=MODEL,
# #         # Pass the formatted message to the model as the user prompt.
# #         messages=[
# #             {
# #                 # Define the user role and include the analysis prompt.
# #                 "role": "user",
# #                 # Store the actual prompt text to be analyzed by the model.
# #                 "content": prompt
# #             }
# #         ],
# #         # Keep the response focused and deterministic with a low temperature.
# #         temperature=0.3,
# #         # Allow enough output length for a detailed professional report.
# #         max_tokens=2000
# #     )
# #
# #     # Return the generated response content from the model.
# #     return response.choices[0].message.content
# #
# #
# # # ---------------------------------------
# # # Cover Letter Generator
# # # ---------------------------------------
# # # Define a function that creates a professional cover letter based on the resume and job description.
# # def cover_page(resume, job_desc):
# #     # Check whether the resume file is missing before processing.
# #     if resume is None:
# #         # Log a warning when the resume is absent.
# #         logger.warning("Resume not uploaded.")
# #         # Return a blank string if no resume was uploaded.
# #         return ""
# #
# #     # Extract text from the uploaded resume PDF.
# #     resume_doc = read_pdf(resume)
# #     # Log that the resume content was successfully loaded.
# #     logger.info("✅ Resume Loaded")
# #
# #     # Create a timestamp to ensure the cover letter prompt includes a unique value.
# #     unique_element = f"Timestamp: {time.time()}"
# #
# #     # Build the prompt that instructs the model to write a one-page cover letter.
# #     prompt = f"""
# # You are an expert HR Recruiter.
# #
# # Using the resume and job description below, generate a professional,
# # one-page cover letter.
# #
# # Requirements:
# #
# # - Use actual resume information.
# # - Do NOT use placeholders.
# # - Mention projects.
# # - Mention technical skills.
# # - Mention achievements.
# # - Explain why the candidate is suitable.
# # - End professionally.
# #
# # Resume:
# # {resume_doc}
# #
# # Job Description:
# # {job_desc}
# #
# # {unique_element}
# # """
# #
# #     # Send the cover-letter prompt to the Groq model for generation.
# #     response = client.chat.completions.create(
# #         # Use the configured model for this generation task.
# #         model=MODEL,
# #         # Pass the user message with the cover letter instructions and resume details.
# #         messages=[
# #             {
# #                 # Set the role to user and attach the generated prompt.
# #                 "role": "user",
# #                 # Include the cover letter prompt text.
# #                 "content": prompt
# #             }
# #         ],
# #         # Use a slightly higher temperature to make the cover letter sound more natural.
# #         temperature=0.5,
# #         # Allow a sufficiently large answer for a complete cover letter.
# #         max_tokens=2000
# #     )
# #
# #     # Return the generated cover letter content.
# #     return response.choices[0].message.content
# #
# #
# # # ---------------------------------------
# # # Skill Performance Analysis
# # # ---------------------------------------
# # # Define a function to analyze the candidate's technical and soft skills against the job description.
# # def skill_performance(resume, job_desc):
# #     # Validate that the resume exists before performing analysis.
# #     if resume is None:
# #         # Log a warning if no resume is provided.
# #         logger.warning("Resume not uploaded.")
# #         # Stop execution and return nothing if the resume is missing.
# #         return ""
# #
# #     # Extract the text from the uploaded resume PDF.
# #     resume_doc = read_pdf(resume)
# #     # Log successful resume loading for debugging and tracking.
# #     logger.info("✅ Resume Loaded")
# #
# #     # Build a prompt requesting a detailed skill performance report in table format.
# #     prompt = f"""
# # You are a Senior Technical Interviewer and ATS Expert.
# #
# # Analyze the candidate's technical and professional skills.
# #
# # Resume:
# print(git code upload code)
# # {resume_doc}
# #
# # Job Description:
# # {job_desc}
# #
# # Generate a detailed Skill Performance Report using the following format.
# #
# # # Overall Skill Match (%)
# #
# # # Technical Skills Performance
# #
# # Create a markdown table like this:
# #
# # | Skill | Resume Level | Job Requirement | Match % |
# #
# # Evaluate all important technical skills such as:
# #
# # - Python
# # - SQL
# # - Power BI
# # - Excel
# # - Pandas
# # - NumPy
# # - Machine Learning
# # - Deep Learning
# # - Data Analysis
# # - AWS
# # - Azure
# # - Git
# # - Docker
# # - Linux
# # - REST APIs
# # - Flask
# # - Spark
# # - Databricks
# #
# # Also include any additional skills found in the resume or job description.
# #
# # # Soft Skills
# #
# # Evaluate:
# #
# # - Communication
# # - Leadership
# # - Problem Solving
# # - Teamwork
# # - Adaptability
# # - Time Management
# #
# # Rate each as:
# #
# # - Excellent
# # - Good
# # - Average
# # - Needs Improvement
# #
# # Finally include:
# #
# # # Candidate Strengths
# #
# # # Weakest Skill Areas
# #
# # # Interview Readiness Score (/100)
# #
# # # Overall Skill Performance Summary
# # """
# #
# #     # Submit the skill-analysis prompt to the Groq API.
# #     response = client.chat.completions.create(
# #         # Use the configured model that matches the resume-analysis workflow.
# #         model=MODEL,
# #         # Send the prompt to the model as the user's request.
# #         messages=[
# #             {
# #                 # Mark the message as being from the user.
# #                 "role": "user",
# #                 # Include the skill performance analysis prompt.
# #                 "content": prompt
# #             }
# #         ],
# #         # Keep the analysis focused and precise with a moderate temperature.
# #         temperature=0.3,
# #         # Allow enough tokens for a detailed skills evaluation report.
# #         max_tokens=2500
# #     )
# #
# #     # Return the generated skill performance analysis text.
# #     return response.choices[0].message.content
# #
# #
# # # ---------------------------------------
# # # Skill Gap Analysis
# # # ---------------------------------------
# # # Define a function to evaluate missing skills and generate a learning roadmap.
# # def skill_gap(resume, job_desc):
# #     # Confirm that a resume has been uploaded before continuing.
# #     if resume is None:
# #         # Log a warning if the resume is missing.
# #         logger.warning("Resume not uploaded.")
# #         # Return an empty string because there is no resume to compare.
# #         return ""
# #
# #     # Extract the text from the uploaded resume PDF.
# #     resume_doc = read_pdf(resume)
# #     # Log that the resume has been successfully read.
# #     logger.info("✅ Resume Loaded")
# #
# #     # Build a prompt that asks the model to compare the resume and job description for skills gaps.
# #     prompt = f"""
# # You are an ATS Resume Expert.
# #
# # Compare the resume with the job description.
# #
# # Resume:
# # {resume_doc}
# #
# # Job Description:
# # {job_desc}
# #
# # Generate a comprehensive Skill Gap Report.
# #
# # Include the following sections.
# #
# # # Skills Found in Resume
# #
# # List all technical and soft skills identified.
# #
# # # Skills Required by Job
# #
# # List all required skills from the job description.
# #
# # # Matching Skills
# #
# # List the skills present in both.
# #
# # # Missing Skills
# #
# # Highlight every missing skill.
# #
# # # High Priority Skills
# #
# # Mention the top skills that should be learned first.
# #
# # # Learning Roadmap
# # """
# #
# #     # Send the skill-gap analysis request to the Groq model.
# #     response = client.chat.completions.create(
# #         # Use the same configured LLM model for consistency.
# #         model=MODEL,
# #         # Pass the user message containing the resume and job description data.
# #         messages=[
# #             {
# #                 # Set the message role to the user.
# #                 "role": "user",
# #                 # Include the skill gap analysis prompt.
# #                 "content": prompt
# #             }
# #         ],
# #         # Use a controlled temperature to keep output practical and consistent.
# #         temperature=0.3,
# #         # Allow enough tokens for a detailed learning roadmap.
# #         max_tokens=2500
# #     )
# #
# #     # Return the generated skill gap analysis content.
# #     return response.choices[0].message.content
# #
# # # Summary of resume
# # # Define a function that creates a short summary of the resume in a few professional lines.
# # def resume_summary_func(resume):
# #
# #     # Read the text from the uploaded resume PDF.
# #     resume_text = read_pdf(resume)
# #
# #     # Prepare a brief prompt that asks the model to summarize the resume.
# #     prompt = f"""
# #     Summarize this resume in 4-5 professional lines.
# #
# #     Resume:
# #     {resume_text}
# #     """
# #
# #     # Send the summary request to the model.
# #     response = client.chat.completions.create(
# #         # Use the configured model for the resume summary task.
# #         model=MODEL,
# #         # Pass the summary request as a single user message.
# #         messages=[
# #             {"role": "user", "content": prompt}
# #         ]
# #     )
# #
# #     # Return the summary text produced by the model.
# #     return response.choices[0].message.content
# #
# # # new version 2.0
# #
#

# print(git code upload code)