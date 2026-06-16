import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_notes(transcript):
    prompt = f"""
Create organized notes from the following transcript.

Include:
1. Summary
2. Key Points
3. Action Items
4. Important Concepts

Transcript:
{transcript}
"""

    response = model.generate_content(prompt)

    return f"""
FULL TRANSCRIPT
----------------
{transcript}

ORGANIZED NOTES
----------------
{response.text}
"""