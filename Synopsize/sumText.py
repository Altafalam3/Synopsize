from tkinter import Toplevel
from customtkinter.windows.ctk_toplevel import CTkToplevel
import tkinter as tk
import customtkinter
from PIL import Image, ImageTk
from tkinter import filedialog
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from collections import Counter
from heapq import nlargest
import test1
import formatter


class CustomToplevel(CTkToplevel):
    def __init__(self, dayOfMonth, time, dayOfWeek, month, title, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self.title("Text Summary")
        self.dayOfMonth = dayOfMonth
        self.time = time
        self.dayOfWeek = dayOfWeek
        self.month = month
        self.sumTitle = title

    #GUI Elements

        # Create a PhotoImage object from an image file
        # image = Image.open("/Users/abhigyanbafna/Desktop/Synopsize/bg_for_python.png")
        # photo = ImageTk.PhotoImage(image)

        # Create a label widget and set its background image
        # self.label = customtkinter.CTkLabel(self, image=photo)
        # self.label.place(x=0, y=0, relwidth=1, relheight=1)

        #Main Page Logo
        # self.mainlogo = customtkinter.CTkImage(
        #     light_image=Image.open("/Users/abhigyanbafna/Desktop/Synopsize/assets/images/synopsize1500.png"),
        #     dark_image=Image.open("/Users/abhigyanbafna/Desktop/Synopsize/assets/images/synopsize1500.png"),
        #     size=(90, 90)
        # )

        self.logoBtn = customtkinter.CTkButton(
            self, 
            text="", 
            command=self.browseFile,
            fg_color="transparent",
            # image=self.mainlogo,
            state="disabled",
        )
        self.logoBtn.place(relx=0.065, rely=0.090, anchor=tk.CENTER)


        #Title Label
        self.title = customtkinter.CTkLabel(
            self,
            text="S Y N O P S I Z E",
            width=120,
            height=25,
            font=("Montserrat SemiBold", 34),
        )
        self.title.place(relx=0.50, rely=0.09, anchor=tk.CENTER)


        #Info and Credits Button
        self.infoBtn = customtkinter.CTkButton(
            self, 
            text="i", 
            command=self.browseFile,
            font=("Montserrat SemiBold", 30),
            width=60,
            height=60,
            corner_radius=20,
            border_color="gray",
            fg_color="transparent",
            text_color=("black","white"),
            border_width=3
        )
        self.infoBtn.place(relx=0.935, rely=0.08, anchor=tk.CENTER)


        # Browse Audio
        self.browseBtn = customtkinter.CTkButton(
            self, 
            text="Browse Text File",
            command=self.browseFile,
            font=("Montserrat SemiBold", 30),
            width=200,
            height=65,
            corner_radius=50
        )
        self.browseBtn.place(relx=0.5, rely=0.3, anchor=tk.CENTER)


        #Summary Title
        self.summarybox = customtkinter.CTkTextbox(
            self,
            width=600,
            height=200,
            font=("Montserrat SemiBold", 20),
            border_width=2,
            corner_radius=20,
            wrap="word"
        )
        self.summarybox.place(relx=0.5, rely=0.575, anchor=tk.CENTER)


        # Summarise using Audio
        self.sumAudioBtn = customtkinter.CTkButton(
            self, 
            text="Summarise",
            command=self.convertToTextt,
            font=("Montserrat SemiBold", 30),
            width=190,
            height=65,
            corner_radius=50
        )
        self.sumAudioBtn.place(relx=0.35, rely=0.85, anchor=tk.CENTER)


        # Download Summary
        self.downloadBtn = customtkinter.CTkButton(
            self, 
            text="Download Summary",
            command=self.downloadSummary,
            font=("Montserrat SemiBold", 26),
            width=190,
            height=65,
            corner_radius=50,
            state="disabled",
        )
        self.downloadBtn.place(relx=0.65, rely=0.85, anchor=tk.CENTER)
    
    def combobox_callback(self, choice):
        print("ComCTkComboBox dropdown clicked:", choice)

    def browseFile(self):
        self.filename = filedialog.askopenfilename(filetypes=(("Text Files", "*.txt"), ("All files", "*.*")))
        self.displayname = ".../" + self.filename.split("/")[-1]
        if self.displayname:
            self.browseBtn.configure(text=self.displayname)

    def convertToTextt(self):
        text_file = self.filename
        try:
            # Open file in read mode
            with open(text_file, "r") as f:
                # Read contents of the file
                text = f.read()

            print("Converted audio is: " + text)

            SUMMARY_PERCENTAGE = 0.25
            nlp = spacy.load('en_core_web_sm')
            text = nlp(text)
            # Use set() to eliminate duplicates
            stop_word = list(STOP_WORDS)
            punctuations = list(punctuation)
            stopwords = set(stop_word+punctuations)

            # Use list comprehension for efficiency
            keyword = [token.text for token in text if token.text.lower(
            ) not in stopwords and token.pos_ in ['PROPN', 'ADJ', 'NOUN', 'VERB']]

            freq_word = Counter(keyword)

            # Use variable instead of repeating function call
            max_freq = freq_word.most_common(1)[0][1]

            # Use dictionary comprehension for efficiency
            freq_word = {word: freq / max_freq for word, freq in freq_word.items()}

            # compute the summary length based on the input message length and the summary percentage
            if (len(list(text.sents)) > 2):
                summary_length = int(len(list(text.sents)) * SUMMARY_PERCENTAGE)
            else:
                summary_length = 2
            sent_strength = {}
            for sent in text.sents:
                for word in sent:
                    if word.text in freq_word:
                        sent_strength[sent] = sent_strength.get(
                            sent, 0) + freq_word[word.text]
            # filter out duplicate sentences from the top sentences
            summarized_sentences = []
            seen_sentences = set()
            for sentence in nlargest(summary_length, sent_strength, key=sent_strength.get):
                if str(sentence) not in seen_sentences:
                    summarized_sentences.append(sentence)
                    seen_sentences.add(str(sentence))
            final_sentences = [str(sentence) for sentence in summarized_sentences]

            self.summary = test1.summarise(str(text))

        except Exception as e:
            print(e)

        if text_file:
            self.summarybox.insert("0.0", self.summary)
            self.downloadBtn.configure(state="normal")

    def downloadSummary(self):
        formatter.wordDoc(self.dayOfMonth, self.time, self.dayOfWeek, self.month, self.sumTitle, self.summarybox.get("0.0", "end"))

    def start(self):
        self.progress.start()
        
    def stop(self):
        self.progress.stop()
        self.destroy()

    def start_loading():
        loading_screen = LoadingScreen(root)
        loading_screen.start()