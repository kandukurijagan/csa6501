!pip install gtts

from gtts import gTTS
from IPython.display import Audio

text = input("Enter engineering text: ")

tts = gTTS(text=text, lang="en")

tts.save("engineering_audio.mp3")

print("Audio generated successfully")

Audio("engineering_audio.mp3")
