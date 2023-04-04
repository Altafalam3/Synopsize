import spacy
# import streamlit as st
# from transformers import pipeline
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from collections import Counter
from heapq import nlargest
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkcalendar import Calendar
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
from tkinter import font
from tkinter import messagebox
import openai


doc = """Machine learning (ML) is the scientific study of algorithms and statistical models that computer systems use to progressively improve their performance on a specific task. Machine learning algorithms build a mathematical model of sample data, known as "training data", in order to make predictions or decisions without being explicitly programmed to perform the task. Machine learning algorithms are used in the applications of email filtering, detection of network intruders, and computer vision, where it is infeasible to develop an algorithm of specific instructions for performing the task. Machine learning is closely related to computational statistics, which focuses on making predictions using computers. The study of mathematical optimization delivers methods, theory and application domains to the field of machine learning. Data mining is a field of study within machine learning, and focuses on exploratory data analysis through unsupervised learning. In its application across business problems, machine learning is also referred to as predictive analytics.
Machine learning (ML) is the scientific study of algorithms and statistical models that computer systems use to progressively improve their performance on a specific task. Machine learning algorithms build a mathematical model of sample data, known as "training data", in order to make predictions or decisions without being explicitly programmed to perform the task. Machine learning algorithms are used in the applications of email filtering, detection of network intruders, and computer vision, where it is infeasible to develop an algorithm of specific instructions for performing the task. Machine learning is closely related to computational statistics, which focuses on making predictions using computers. The study of mathematical optimization delivers methods, theory and application domains to the field of machine learning. Data mining is a field of study within machine learning, and focuses on exploratory data analysis through unsupervised learning. In its application across business problems, machine learning is also referred to as predictive analytics."""
SUMMARY_PERCENTAGE = 0.25

root = tk.Tk()

root.configure(background='#242124')

nlp = spacy.load('en_core_web_sm')
doc = nlp(doc)
stop_word = list(STOP_WORDS)
punctuation = list(punctuation)

stopwords = set(stop_word+punctuation)
keyword = [token.text for token in doc if token.text.lower(
) not in stopwords and token.pos_ in ['PROPN', 'ADJ', 'NOUN', 'VERB']]

freq_word = Counter(keyword)

# Use variable instead of repeating function call
max_freq = freq_word.most_common(1)[0][1]

# Use dictionary comprehension for efficiency
freq_word = {word: freq / max_freq for word, freq in freq_word.items()}
summary_length = int(len(list(doc.sents)) * SUMMARY_PERCENTAGE)
sent_strength = {}
for sent in doc.sents:
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
summary = ' '.join(final_sentences)
summary = openai.summarise(str(doc))


def com_as():
    root.destroy()
    import aboutus


def SUA():
    root.destroy()
    import SUA


def extra():
    root.destroy()
    import extra


root.title("Summarizer using Text")
root.geometry("1000x900")

# background_image = PhotoImage(file="./bg_for_python.png")
# background_label = Label(root, image=background_image)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)


heading_font = font.Font(family="Arial", weight="bold")
menu_font = font.Font(family="Arial")

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
main_page = tk.Menu(menu_bar, tearoff=0, foreground='purple', font=12)
menu_bar.add_cascade(label="Index", menu=main_page)
main_page.add_command(label="Index", command=extra)
about_menu = tk.Menu(menu_bar, tearoff=0, foreground='purple', font=12)
menu_bar.add_cascade(label="About", menu=about_menu)
about_menu.add_command(label="About", command=com_as)

audio_menu = tk.Menu(menu_bar, tearoff=0, foreground='purple', font=12)
menu_bar.add_cascade(label="Summarizer using Audio", menu=audio_menu)
audio_menu.add_command(label="Summarize Audio", command=SUA)

date_label = tk.Label(root, text=" Date Of The Meeting",
                      font="allerta_stencil", bg='#413839', foreground='white', pady=0)
date_label.pack()
date_label.place(relx=0.001, rely=0.01)

cal = Calendar(root, selectmode='day', year=2020, month=5, day=22)
cal.pack(pady=20)
cal.place(relx=0.1, rely=0.075678)


def open_file():
    file = filedialog.askopenfile(
        mode='r', filetypes=[('Python Files', '*.py')])
    if file:
        content = file.read()
        file.close()
        print("%d characters in this file" % len(content))


def grad_date():
    date.config(text="Selected Date is: " + cal.get_date())


def save_text():
    # get all the text in the textbox
    text_to_save = T.get("1.0", "end-1c")
    with open("file.txt", "w") as f:
        f.write(text_to_save)
        messagebox.showinfo("Success", "File saved successfully!")


# Add Button and Label
calb = Button(root, text="Get Date", command=grad_date,
              font=65, bg='#C7B4F7', bd=4.5, relief='raise')
calb.pack()
calb.place(relx=0.5, rely=0.2)

date = Label(root, text="", font=75, bg='#C7B4F7', bd=4, relief='raise')
date.pack()
date.place(relx=0.67, rely=0.21)

file_label = Label(root, text="Enter the text->",
                   font="allerta_stencil", bg='#242124', foreground='white', pady=0)
file_label.place(relx=0.01, rely=0.4567)
bbutto = ttk.Button(root, text="Browse->", command=open_file)
bbutto.pack(pady=0)
bbutto.place(relx=0.24, rely=0.47)
T = Text(root, height=4, width=70, bd=2.3, relief='sunken', bg='#F3F0E0')
T.pack()
T.place(relx=0.37, rely=0.47)


cbutto = tk.Button(root, text="summarize", command="", height=1,
                   width=13, bg='#C7B4F7', bd=4.2, relief='raise', font=("Arial", 12))
cbutto.pack(pady=0)
cbutto.place(relx=0.01, rely=0.53)
dbutto = tk.Button(root, text="summarize pro", command="", height=1,
                   width=13, bg='#C7B4F7', bd=4.2, relief='raise', font=("Arial", 12))
dbutto.pack(pady=0)
dbutto.place(relx=0.2, rely=0.53)
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
T = Text(root, wrap=WORD, height=9,
         width=105, bd=7, relief='raise', bg='#F3F0E0')
scrollbar = Scrollbar(root, command=T.yview)
T.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side=RIGHT, fill=Y)
T.pack(side=LEFT, fill=BOTH, expand=True)
T.insert(END, summary)

T.place(relx=0.07, rely=0.62)
root.geometry("1000x600")
cbutto = tk.Button(root, text="Download the summary", command=save_text, height=1,
                   width=19, bg='#C7B4F7', bd=4.5, relief='raise', font=("Arial", 15))
cbutto.pack(pady=20)
cbutto.place(relx=0.77, rely=0.9)

# create a PhotoImage object from the image file


root.mainloop()
