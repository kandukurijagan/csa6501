!pip install transformers torch librosa soundfile

from transformers import pipeline

speech_to_text = pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-small"
)

audio_file = input("Enter audio file path: ")

result = speech_to_text(audio_file)

print("\nRecognized Engineering Query:")
print(result["text"])
