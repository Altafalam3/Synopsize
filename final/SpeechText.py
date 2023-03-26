# direct .wav to text code
import speech_recognition as sr

def convert(audio_file):
    try:
        r = sr.Recognizer()
        with sr.AudioFile(audio_file) as source:
            audio = r.record(source)

        text = r.recognize_google(audio)
        print("Converted audio is: " + text)

        # write the converted speech to a file
        with open('text_file.txt', "w") as f:
           f.write(text)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    audio_file = "audio2.wav"
    convert(audio_file)


'''
#direct mp3 to wav to text code
import speech_recognition as sr
from pydub import AudioSegment


def convert_to_wav(audio_file):
    sound = AudioSegment.from_file(audio_file, format="mp3")
    wav_audio = sound.export(format="wav")
    return wav_audio


def convert(audio_file):
    # Convert audio file to WAV format using Pydub
    wav_audio = convert_to_wav(audio_file)
    try:
        r = sr.Recognizer()
        with sr.AudioFile(audio_file) as source:
            audio = r.record(source)

        text = r.recognize_google(audio)
        print("Converted audio is: " + text)

        # write the converted speech to a file
        #with open('text_file.txt', "w") as f:
        #    f.write(text)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    audio_file = "audio1.mp3"
    convert(audio_file)

'''