AI Video Note Extractor is a Python-based application that automatically converts video content into structured notes using Artificial Intelligence.
The application extracts audio from a video, converts speech into text using OpenAI Whisper, and then uses Google's Gemini AI to generate organized notes including summaries, key points, action items, and important concepts
The workflow is:
i.User provides a video file.
ii. Audio is extracted from the video using FFmpeg and MoviePy.
iii. OpenAI Whisper converts speech into text.
iv. Gemini AI analyzes the transcript.
v. Structured notes are generated and saved.
