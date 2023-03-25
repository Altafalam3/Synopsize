# just eliminating lines directly not efficient moderate chota kr rha
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from collections import Counter
from heapq import nlargest

doc = """Machine learning (ML) is the scientific study of algorithms and statistical models that computer systems use to progressively improve their performance on a specific task. Machine learning algorithms build a mathematical model of sample data, known as "training data", in order to make predictions or decisions without being explicitly programmed to perform the task. Machine learning algorithms are used in the applications of email filtering, detection of network intruders, and computer vision, where it is infeasible to develop an algorithm of specific instructions for performing the task. Machine learning is closely related to computational statistics, which focuses on making predictions using computers. The study of mathematical optimization delivers methods, theory and application domains to the field of machine learning. Data mining is a field of study within machine learning, and focuses on exploratory data analysis through unsupervised learning. In its application across business problems, machine learning is also referred to as predictive analytics."""

nlp = spacy.load('en_core_web_sm')
doc = nlp(doc)

# Use set() to eliminate duplicates
stop_word  = list(STOP_WORDS) 
punctuation = list(punctuation)

stopwords = set(stop_word+punctuation)

# Use list comprehension for efficiency
keyword = [token.text for token in doc if token.text.lower() not in stopwords and token.pos_ in ['PROPN', 'ADJ', 'NOUN', 'VERB']]

freq_word = Counter(keyword)

# Use variable instead of repeating function call
max_freq = freq_word.most_common(1)[0][1]

# Use dictionary comprehension for efficiency
freq_word = {word: freq / max_freq for word, freq in freq_word.items()}

sent_strength = {}
for sent in doc.sents:
    for word in sent:
        if word.text in freq_word:
            sent_strength[sent] = sent_strength.get(sent, 0) + freq_word[word.text]

summarized_sentences = nlargest(3, sent_strength, key=sent_strength.get)

final_sentences = [str(sentence) for sentence in summarized_sentences]
summary = ' '.join(final_sentences)
print(summary)
