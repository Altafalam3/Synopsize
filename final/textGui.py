#enter text ,get text summary direct
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation as punc
from collections import Counter
from heapq import nlargest
import tkinter as tk

def summarize_text():
    # get the user input from the GUI
    user_input = user_input_text.get("1.0", "end-1c")

    nlp = spacy.load('en_core_web_sm')
    doc = nlp(user_input)

    # Use set() to eliminate duplicates
    stop_word  = list(STOP_WORDS)
    punctuation_list = list(punc)

    stopwords = set(stop_word+punctuation_list)

    # Use list comprehension for efficiency
    keyword = [token.text for token in doc if token.text.lower() not in stopwords and token.pos_ in ['PROPN', 'ADJ', 'NOUN', 'VERB']]

    freq_word = Counter(keyword)

    # Use variable instead of repeating function call
    max_freq = freq_word.most_common(1)[0][1]

    # Use dictionary comprehension for efficiency
    freq_word = {word: freq / max_freq for word, freq in freq_word.items()}

    # compute the summary length based on the input message length and the summary percentage
    SUMMARY_PERCENTAGE = 0.25
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

    # display the summary in the GUI
    summary_text.delete("1.0", "end")
    summary_text.insert("1.0", summary)

# create the GUI
root = tk.Tk()

user_input_label = tk.Label(root, text="Enter text to summarize:")
user_input_label.pack()

user_input_text = tk.Text(root, height=10)
user_input_text.pack()

summarize_button = tk.Button(root, text="Summarize", command=summarize_text)
summarize_button.pack()

summary_label = tk.Label(root, text="Summary:")
summary_label.pack()

summary_text = tk.Text(root, height=10)
summary_text.pack()

root.mainloop()
