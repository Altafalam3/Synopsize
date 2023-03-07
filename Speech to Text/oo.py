# NOT WORKING
#direct tried mp3 to text

import speech_recognition as sr
import soundfile as sf

filename = "audio1.mp3"

# Read in the audio file using pysoundfile
audio, sample_rate = sf.read(filename)

# Set up a SpeechRecognition recognizer instance
recognizer = sr.Recognizer()

# Convert the audio to text using the recognize_google() method
text = recognizer.recognize_google(audio, language="en-US")

# Print the resulting text
print(text)
