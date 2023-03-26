import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from collections import Counter
from heapq import nlargest
import tkinter as tk
from tkinter import filedialog, messagebox

# define the summary length as a percentage of the input message
SUMMARY_PERCENTAGE = 0.25

def summarize_text():
    file_path = filedialog.askopenfilename()
    if file_path:
        try:
            with open(file_path, 'r') as f:
                doc = f.read()
        except:
            messagebox.showerror("Error", "Failed to open file.")
            return
    
        nlp = spacy.load('en_core_web_sm')
        doc = nlp(doc)

        # Use set() to eliminate duplicates
        stop_word  = list(STOP_WORDS)
        punctuation_list = list(punctuation)

        stopwords = set(stop_word+punctuation_list)

        # Use list comprehension for efficiency
        keyword = [token.text for token in doc if token.text.lower() not in stopwords and token.pos_ in ['PROPN', 'ADJ', 'NOUN', 'VERB']]

        freq_word = Counter(keyword)

        # Use variable instead of repeating function call
        max_freq = freq_word.most_common(1)[0][1]

        # Use dictionary comprehension for efficiency
        freq_word = {word: freq / max_freq for word, freq in freq_word.items()}

        # compute the summary length based on the input message length and the summary percentage
        summary_length = int(len(list(doc.sents)) * SUMMARY_PERCENTAGE)

        sent_strength = {}
        for sent in doc.sents:
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
        summary = ' '.join(final_sentences)
        messagebox.showinfo("Summary", summary)

        # Update the file name label
        filename_label.configure(text="File: " + file_path)

def clear_filename():
    filename_label.configure(text="")

# Create the GUI
root = tk.Tk()
root.title("Text Summarizer")
root.geometry("500x300")

# Create a button to upload a file
upload_button = tk.Button(root, text="Upload File", command=summarize_text)
upload_button.pack(pady=10)

# Create a label to display the uploaded file name
filename_label = tk.Label(root, text="")
filename_label.pack()

# Create a button to clear the file name label
clear_button = tk.Button(root, text="Clear", command=clear_filename)
clear_button.pack(pady=10)

root.mainloop()
