from gtts import gTTS

tts = gTTS(text="hello guys, welcome to mpr project once again.Let's go and rock with meeting summariser app", lang='en')
tts.save("audio1.mp3")
print("Text Converted Successfully ")