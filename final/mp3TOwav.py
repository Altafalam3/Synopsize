import speech_recognition as sr
from pydub import AudioSegment
import io

filename = "audio1.mp3"
try:
   # Load the audio file using pydub
   sound = AudioSegment.from_file(filename)
   # Convert to WAV format

   raw_data = io.BytesIO(sound.raw_data)
   wav_data = io.BytesIO()
   sound.export(wav_data, format="wav")
   wav_data.seek(0)

   # Set up a SpeechRecognition recognizer instance
   recognizer = sr.Recognizer()

   # Convert the audio to text using the recognize_google() method
   with sr.AudioFile(wav_data) as source:
       audio = recognizer.record(source)
   text = recognizer.recognize_google(audio, language="en-US")

   # Print the resulting text
   print(text)
except Exception as e:
   print(e)