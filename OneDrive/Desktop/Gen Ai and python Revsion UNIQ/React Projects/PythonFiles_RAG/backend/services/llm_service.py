"""
services/llm_service.py

Groq LLM Service

Responsibilities
----------------
1. Connect to Groq API
2. Send Prompt
3. Receive AI Response
4. Parse JSON
5. Return Structured Result
"""

import json

from groq import Groq

from PythonFiles_RAG.backend.utils.config import settings
from PythonFiles_RAG.backend.utils.logger import logger


# ==========================================================
# Initialize Groq Client
# ==========================================================

client = Groq(
    api_key=settings.GROQ_API_KEY
)


# ==========================================================
# LLM Model
# ==========================================================

MODEL_NAME = settings.GROQ_MODEL


# ==========================================================
# Generate AI Response
# ==========================================================

def generate_response(prompt: str):

    """
    Generate Resume Screening Response
    """

    logger.info("Calling Groq LLM")

    try:

        completion = client.chat.completions.create(

            model=MODEL_NAME,

            temperature=0.2,

            max_tokens=2048,

            response_format={

                "type": "json_object"

            },

            messages=[

                {

                    "role": "system",

                    "content": "You are an AI Resume Screening Assistant."

                },

                {

                    "role": "user",

                    "content": prompt

                }

            ]

        )

        response = completion.choices[0].message.content

        logger.info("Groq Response Received")

        return response

    except Exception as e:

        logger.error(f"Groq Error : {e}")

        raise Exception("LLM Generation Failed")


# ==========================================================
# Parse JSON Response
# ==========================================================

def parse_response(response: str):

    """
    Convert LLM JSON String to Python Dictionary
    """

    try:

        return json.loads(response)

    except Exception as e:

        logger.error(f"JSON Parsing Error : {e}")

        return {

            "candidate_name": "",

            "match_score": 0,

            "technical_skills": [],

            "strengths": [],

            "skill_gap": [],

            "recommendation": "Unable to parse response.",

            "interview_questions": []

        }


# ==========================================================
# Main LLM Pipeline
# ==========================================================

def screen_candidate(prompt: str):

    """
    Complete LLM Pipeline
    """

    logger.info("Resume Screening Started")

    response = generate_response(prompt)

    result = parse_response(response)

    logger.info("Resume Screening Completed")

    return result