import pyaudio
import wave
import tkinter as tk


class Recorder:
    def __init__(self):
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.CHUNK = 1024
        self.frames = []
        self.is_recording = False

        self.audio = pyaudio.PyAudio()

        self.root = tk.Tk()
        self.root.title("Meeting Recorder")

        # Label and entry for recording length
        self.length_label = tk.Label(
            self.root, text="Meeting length (seconds):")
        self.length_label.pack()
        self.length_entry = tk.Entry(self.root)
        self.length_entry.pack()

        # Record button
        self.record_button = tk.Button(
            self.root, text="Record", command=self.start_recording)
        self.record_button.pack()

        # Stop button
        self.stop_button = tk.Button(
            self.root, text="Stop Recording", command=self.stop_recording, state=tk.DISABLED)
        self.stop_button.pack()

        self.root.mainloop()

    def start_recording(self):
        # Disable record button and enable stop button
        self.record_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

        # Start recording
        self.is_recording = True
        self.frames = []

        # Get length of meeting from user input
        self.meeting_length = int(self.length_entry.get())

        # Open microphone stream
        self.stream = self.audio.open(format=self.FORMAT, channels=self.CHANNELS,
                                      rate=self.RATE, input=True,
                                      frames_per_buffer=self.CHUNK)

        # Record audio in chunks
        for i in range(0, int(self.RATE / self.CHUNK * self.meeting_length)):
            if not self.is_recording:
                break
            data = self.stream.read(self.CHUNK)
            self.frames.append(data)

        # Stop recording
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()

        # Save recorded audio as WAV file
        if self.is_recording:
            wf = wave.open("meeting.wav", 'wb')
            wf.setnchannels(self.CHANNELS)
            wf.setsampwidth(self.audio.get_sample_size(self.FORMAT))
            wf.setframerate(self.RATE)
            wf.writeframes(b''.join(self.frames))
            wf.close()

        # Reset UI
        self.record_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def stop_recording(self):
        self.is_recording = False
