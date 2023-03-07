import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Sample text
text = "Natural Language Processing is the technology used to aid computers to understand human language."

# Convert to lowercase
text = text.lower()

# Tokenize the text
tokens = word_tokenize(text)



# -----------------------------------
# Remove stop words
stop_words = set(stopwords.words('english'))
# print(stop_words)
tokens = [word for word in tokens if not word in stop_words]
# print(tokens)

# Perform stemming
stemmer = nltk.PorterStemmer()
tokens = [stemmer.stem(word) for word in tokens]

# Print the tokens
print(tokens)


# Get word frequency distribution
freq_dist = nltk.FreqDist(tokens)

# Get top 3 most common tokens
top_tokens = freq_dist.most_common(3)

# Reconstruct summary text from top tokens
summary_tokens = [token[0] for token in top_tokens]
summary_text = " ".join(summary_tokens)

# Print the summary text
print(summary_text)


'''
    tokens = [[stemmer.stem(word) for word in token if not word in stop_words] for token in tokens]

    # Create a frequency distribution of the tokens
    freq_dist = nltk.FreqDist([word for token in tokens for word in token])

    # Score each sentence based on the frequency of its tokens
    scores = [(i, sum([freq_dist[word] for word in token])) for i, token in enumerate(tokens)]

    # Sort the sentences by their score in descending order
    ranked_sentences = sorted(scores, key=lambda x: x[1], reverse=True)

    # Get the top N sentences
    top_sentences = sorted([sentence[0] for sentence in ranked_sentences[:num_sentences]])

    # Reconstruct the summary text from the top sentences
    summary = ' '.join([sentences[i] for i in top_sentences])

    return summary
'''

