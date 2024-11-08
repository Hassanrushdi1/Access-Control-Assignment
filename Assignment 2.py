from transformers import pipeline
speech_recognizer = pipeline("automatic-speech-recognition")
audio_file = "C:\Users\Desktop things\voice"
transcription = speech_recognizer(audio_file)["text"]