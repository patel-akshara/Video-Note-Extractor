from audio_extractor import extract_audio
from transcriber import transcribe_audio
from summarizer import generate_notes

video_path = input("Enter video file path: ")

audio_path = "audio/extracted_audio.wav"

print("Extracting audio...")
extract_audio(video_path, audio_path)

print("Transcribing audio...")
transcript = transcribe_audio(audio_path)

with open("transcripts/transcript.txt", "w", encoding="utf-8") as file:
    file.write(transcript)

print("Generating notes...")
notes = generate_notes(transcript)

with open("notes/notes.txt", "w", encoding="utf-8") as file:
    file.write(notes)

print("Done!")
print("Transcript saved in transcripts folder.")
print("Notes saved in notes folder.")