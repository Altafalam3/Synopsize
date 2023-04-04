import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment
import spacy

from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from collections import Counter
from heapq import nlargest
import speech_recognition as sr

class AudioToTextGUI:

    def __init__(self, master):
        self.master = master
        self.summary = ''
        master.title("Audio to Text Converter")

        # Input field
        self.input_label = tk.Label(master, text="Select WAV file:")
        self.input_label.pack()
        self.input_field = tk.Entry(master, width=50)
        self.input_field.pack()

        # Browse button
        self.browse_button = tk.Button(master, text="Browse", command=self.browse_file)
        self.browse_button.pack()

        # Convert button
        self.convert_button = tk.Button(master, text="Convert to Text", command=self.convert_to_text)
        self.convert_button.pack()

        # Download button
        self.download_button = tk.Button(master, text="Download Text", command=self.download_text, state=tk.DISABLED)
        self.download_button.pack()

        # Text area
        self.text_area = tk.Text(master, height=10, width=50)
        self.text_area.pack()

    def browse_file(self):
        filename = filedialog.askopenfilename(filetypes=(("WAV files", "*.wav"), ("All files", "*.*")))
        self.input_field.delete(0, tk.END)
        self.input_field.insert(0, filename)
        self.download_button.config(state=tk.DISABLED)
        self.text_area.delete("1.0", tk.END)

    def convert_to_text(self):
        audio_file = self.input_field.get()
        try:
            r = sr.Recognizer()
            with sr.AudioFile(audio_file) as source:
                audio = r.record(source)

            text = r.recognize_google(audio)

            print("Converted audio is: " + text)

            # define the summary length as a percentage of the input message
            SUMMARY_PERCENTAGE = 0.25

            nlp = spacy.load('en_core_web_sm')
            text = nlp(text)

            # Use set() to eliminate duplicates
            stop_word  = list(STOP_WORDS)
            punctuations = list(punctuation)

            stopwords = set(stop_word+punctuations)
            
            # Use list comprehension for efficiency
            keyword = [token.text for token in text if token.text.lower() not in stopwords and token.pos_ in ['PROPN', 'ADJ', 'NOUN', 'VERB']]
            
            freq_word = Counter(keyword)
        
            # Use variable instead of repeating function call
            max_freq = freq_word.most_common(1)[0][1]
            
            # Use dictionary comprehension for efficiency
            freq_word = {word: freq / max_freq for word, freq in freq_word.items()}
            
            # compute the summary length based on the input message length and the summary percentage
            if(len(list(text.sents)) > 2):
                summary_length = int(len(list(text.sents)) * SUMMARY_PERCENTAGE)
            else:
                summary_length = 2

            sent_strength = {}
            for sent in text.sents:
                for word in sent:
                    if word.text in freq_word:
                        sent_strength[sent] = sent_strength.get(sent, 0) + freq_word[word.text]

            # filter out duplicate sentences from the top sentences
            summarized_sentences = []
            seen_sentences = set()
            for sentence in nlargest(summary_length, sent_strength, key=sent_strength.get):
                if str(sentence) not in seen_sentences:
                    summarized_sentences.append(sentence)
                    seen_sentences.add(str(sentence))

            final_sentences = [str(sentence) for sentence in summarized_sentences]
            self.summary = ' '.join(final_sentences)
            print("Summary is....")
            print(self.summary)

            # # write the converted speech to a file
            # with open('text_file.txt', "w") as f:
            # f.write(text)

        except Exception as e:
            print(e)

        if audio_file:
            self.text_area.insert(tk.END, self.summary)
            self.download_button.config(state=tk.NORMAL)

    def download_text(self):
        text = self.text_area.get("1.0", tk.END)
        filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if filename:
            with open(filename, "w") as file:
                file.write(text)

root = tk.Tk()
gui = AudioToTextGUI(root)
root.mainloop()
