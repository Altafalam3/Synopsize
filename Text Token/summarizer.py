import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

# Example input text
input_text = "This is an example text about a meeting. The meeting discussed various topics including Python, natural language processing, and text summarization. The participants in the meeting found the discussion to be informative and engaging."

# Preprocess the input text
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

tokens = word_tokenize(input_text.lower())
tokens = [lemmatizer.lemmatize(
    token) for token in tokens if token.isalnum() and token not in stop_words]

# Extract keywords
tfidf = TfidfVectorizer()
tfidf.fit(tokens)

keywords = tfidf.get_feature_names()
top_keywords = keywords[:3]  # Select the top 3 keywords

# Generate summary
sentences = sent_tokenize(input_text)
scores = [sum(tfidf.transform([sentence.lower()]).toarray()[0][tfidf.vocabulary_[
              keyword]] for keyword in top_keywords) for sentence in sentences]
top_sentences = [sentences[index] for index in sorted(range(len(
    scores)), key=lambda i: scores[i], reverse=True)[:2]]  # Select the top 2 sentences

# Combine sentences and keywords to form a summary
summary = ' '.join(top_sentences) + ' '.join(top_keywords)

print(summary)
