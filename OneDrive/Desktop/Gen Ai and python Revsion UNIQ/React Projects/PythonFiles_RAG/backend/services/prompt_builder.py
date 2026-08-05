"""
services/prompt_builder.py

Prompt Builder Service

Responsibilities
----------------
1. Build System Prompt
2. Build User Prompt
3. Assemble Retrieved Resume Context
4. Prepare Prompt for Groq LLM
"""

from PythonFiles_RAG.backend.utils.logger import logger


# ==========================================================
# SYSTEM PROMPT
# ==========================================================

SYSTEM_PROMPT = """
You are an AI Resume Screening Assistant.

Your responsibility is to evaluate candidates only using
the retrieved resume context.

Do not hallucinate.

Do not create information that is not available in the
resume.

Evaluate candidates based on:

• Technical Skills
• Professional Experience
• Education
• Certifications
• Projects
• Domain Knowledge

Return the response in JSON format.
"""


# ==========================================================
# Resume Context
# ==========================================================

def build_resume_context(documents):

    """
    Convert retrieved chunks into context.
    """

    context = ""

    for document in documents:

        context += f"""

Section:
{document['section']}

Content:
{document['text']}

------------------------------------------

"""

    return context


# ==========================================================
# Candidate Metadata
# ==========================================================

def build_metadata(metadata):

    """
    Candidate metadata
    """

    return f"""

Candidate Skills:
{metadata.get("skills","")}

Education:
{metadata.get("education","")}

Experience:
{metadata.get("experience","")}

Certifications:
{metadata.get("certifications","")}

Projects:
{metadata.get("projects","")}

"""


# ==========================================================
# Job Description
# ==========================================================

def build_job_description(job_description):

    return f"""

Job Description

{job_description}

"""


# ==========================================================
# Recruiter Question
# ==========================================================

def build_question(question):

    return f"""

Recruiter Request

{question}

"""


# ==========================================================
# Final Prompt
# ==========================================================

def build_prompt(

    recruiter_query,

    job_description,

    metadata,

    retrieved_documents

):

    logger.info("Building LLM Prompt")

    resume_context = build_resume_context(

        retrieved_documents

    )

    metadata_context = build_metadata(

        metadata

    )

    jd_context = build_job_description(

        job_description

    )

    question = build_question(

        recruiter_query

    )

    prompt = f"""

{SYSTEM_PROMPT}

===================================================

{jd_context}

===================================================

{metadata_context}

===================================================

Retrieved Resume Context

{resume_context}

===================================================

{question}

===================================================

Return ONLY valid JSON.

Expected JSON Format

{{
    "candidate_name": "",
    "match_score": "",
    "technical_skills": [],
    "strengths": [],
    "skill_gap": [],
    "recommendation": "",
    "interview_questions": []
}}

"""

    logger.info("Prompt Ready")

    return prompt