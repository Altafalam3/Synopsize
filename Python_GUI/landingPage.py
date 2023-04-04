import tkinter as tk
import customtkinter
from PIL import Image
from tkinter import filedialog
from pydub import AudioSegment
import spacy

from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from collections import Counter
from heapq import nlargest
import speech_recognition as sr

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("900x600")
app.title("AI Inside ;)")

def download_text(self):
        text = self.text_area.get("1.0", tk.END)
        filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if filename:
            with open(filename, "w") as file:
                file.write(text)

def browseFile():
        global filename 
        filename = filedialog.askopenfilename(filetypes=(("WAV files", "*.wav"), ("All files", "*.*")))
        global displayname 
        displayname = ".../" + filename.split("/")[-1]
        if displayname:
            browseBtn.configure(text=displayname)
            # self.download_button.config(state=tk.DISABLED)
            # self.text_area.delete("1.0", tk.END)

def convertToText():
        audio_file = filename
        try:
            r = sr.Recognizer()
            with sr.AudioFile(audio_file) as source:
                audio = r.record(source)

            text = r.recognize_google(audio)

            #Dummy text to test functionality

            text = """Machine learning (ML) is the scientific study of algorithms and statistical models that computer systems use to progressively improve their performance on a specific task. Machine learning algorithms build a mathematical model of sample data, known as "training data", in order to make predictions or decisions without being explicitly programmed to perform the task. Machine learning algorithms are used in the applications of email filtering, detection of network intruders, and computer vision, where it is infeasible to develop an algorithm of specific instructions for performing the task. Machine learning is closely related to computational statistics, which focuses on making predictions using computers. The study of mathematical optimization delivers methods, theory and application domains to the field of machine learning. Data mining is a field of study within machine learning, and focuses on exploratory data analysis through unsupervised learning. In its application across business problems, machine learning is also referred to as predictive analytics.
            Machine learning (ML) is the scientific study of algorithms and statistical models that computer systems use to progressively improve their performance on a specific task. Machine learning algorithms build a mathematical model of sample data, known as "training data", in order to make predictions or decisions without being explicitly programmed to perform the task. Machine learning algorithms are used in the applications of email filtering, detection of network intruders, and computer vision, where it is infeasible to develop an algorithm of specific instructions for performing the task. Machine learning is closely related to computational statistics, which focuses on making predictions using computers. The study of mathematical optimization delivers methods, theory and application domains to the field of machine learning. Data mining is a field of study within machine learning, and focuses on exploratory data analysis through unsupervised learning. In its application across business problems, machine learning is also referred to as predictive analytics."""

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
            if len(list(text.sents)) > 2:
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
            global summary
            summary = ' '.join(final_sentences)
            print("Summary is....")
            print(summary)

            # # write the converted speech to a file
            # with open('text_file.txt', "w") as f:
            # f.write(text)

        except Exception as e:
            print(e)

        if audio_file:
            print(summary)
            # self.text_area.insert(tk.END, summary)
            # self.download_button.config(state=tk.NORMAL)


def button_function():
        print("button pressed")


#GUI Elements

#Main Page Logo
mainlogo = customtkinter.CTkImage(
    light_image=Image.open("/Users/abhigyanbafna/Desktop/Synopsize/assets/images/synopsize1500.png"),
    dark_image=Image.open("/Users/abhigyanbafna/Desktop/Synopsize/assets/images/synopsize1500.png"),
    size=(90, 90)
)

logoBtn = customtkinter.CTkButton(
    master=app, 
    text="", 
    command=button_function,
    fg_color="transparent",
    image=mainlogo,
    state="disabled",
)
logoBtn.place(relx=0.065, rely=0.090, anchor=tk.CENTER)

#Title Label
label = customtkinter.CTkLabel(
    master=app,
    text="S Y N O P S I Z E",
    width=120,
    height=25,
    font=("Montserrat SemiBold", 34),)
label.place(relx=0.50, rely=0.09, anchor=tk.CENTER)

#Info and Credits Button
infoBtn = customtkinter.CTkButton(
    master=app, 
    text="i", 
    command=button_function,
    font=("Montserrat SemiBold", 30),
    width=60,
    height=60,
    corner_radius=20,
    border_color="gray",
    fg_color="transparent",
    text_color=("black","white"),
    border_width=3
)
infoBtn.place(relx=0.935, rely=0.08, anchor=tk.CENTER)

# #User Data Fields
# nameField = customtkinter.CTkEntry(
#     master=app,
#     placeholder_text="iron man",
#     width=250,
#     height=60,
#     font=("Montserrat SemiBold", 20),
#     border_width=2,
#     corner_radius=20
# )
# nameField.place(relx=0.35, rely=0.3, anchor=tk.CENTER)


#Day of Month Options
dayOfMonth = ["Day of Month"]

for i in range(1, 32):
    dayOfMonth.append(str(i))

combobox_var = customtkinter.StringVar(value=dayOfMonth[0])  # set initial value

def combobox_callback(choice):
    print("ComCTkComboBox dropdown clicked:", choice)

combobox = customtkinter.CTkComboBox(
    master=app,
    values=dayOfMonth,
    command=combobox_callback,
    variable=combobox_var,
    width=250,
    height=60,
    font=("Montserrat SemiBold", 20),
    corner_radius=20
)

combobox.place(relx=0.35, rely=0.225, anchor=tk.CENTER)


#Month Options
month = ["Month"]

for i in range(1, 13):
    month.append(str(i))

combobox_var = customtkinter.StringVar(value=month[0])  # set initial value

def combobox_callback(choice):
    print("ComCTkComboBox dropdown clicked:", choice)

combobox = customtkinter.CTkComboBox(
    master=app,
    values=month,
    command=combobox_callback,
    variable=combobox_var,
    width=250,
    height=60,
    font=("Montserrat SemiBold", 20),
    corner_radius=20
)

combobox.place(relx=0.65, rely=0.225, anchor=tk.CENTER)


#Day of Week Options
dayofWeek = ['Day','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

combobox_var = customtkinter.StringVar(value=dayofWeek[0])  # set initial value

def combobox_callback(choice):
    print("ComCTkComboBox dropdown clicked:", choice)

combobox = customtkinter.CTkComboBox(
    master=app,
    values=dayofWeek,
    command=combobox_callback,
    variable=combobox_var,
    width=250,
    height=60,
    font=("Montserrat SemiBold", 20),
    corner_radius=20
)

combobox.place(relx=0.35, rely=0.375, anchor=tk.CENTER)


#Time of Day Options
timeOfDay = ['Time']

for hour in range(0, 24):
    for minute in ['00', '30']:
        time = f'{hour:02d}:{minute} hrs'
        timeOfDay.append(time)

combobox_var = customtkinter.StringVar(value=timeOfDay[0])  # set initial value

def combobox_callback(choice):
    print("ComCTkComboBox dropdown clicked:", choice)

combobox = customtkinter.CTkComboBox(
    master=app,
    values=timeOfDay,
    command=combobox_callback,
    variable=combobox_var,
    width=250,
    height=60,
    font=("Montserrat SemiBold", 20),
    corner_radius=20
)

combobox.place(relx=0.65, rely=0.375, anchor=tk.CENTER)


#Summary Title
nameField = customtkinter.CTkEntry(
    master=app,
    placeholder_text="i am iron man",
    width=520,
    height=60,
    font=("Montserrat SemiBold", 20),
    border_width=2,
    corner_radius=20
)
nameField.place(relx=0.5, rely=0.525, anchor=tk.CENTER)


# Browse File Btn
browseBtn = customtkinter.CTkButton(
    master=app, 
    text="Browse Audio File", 
    command=browseFile,
    font=("Montserrat SemiBold", 25),
    width=350,
    height=55,
    corner_radius=20
)
browseBtn.place(relx=0.5, rely=0.675, anchor=tk.CENTER)



# Summarize button
sumBtn = customtkinter.CTkButton(
    master=app, 
    text="Summarize", 
    command=convertToText,
    font=("Montserrat SemiBold", 30),
    width=190,
    height=65,
    corner_radius=50
)
sumBtn.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

app.mainloop()

