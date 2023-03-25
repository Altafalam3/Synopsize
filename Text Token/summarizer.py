#working but not efficient boht chota kr de rha hai and as it is line utha rha
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

# Example input text
input_text = 'Machine learning (ML) is the scientific study of algorithms and statistical models that computer systems use to progressively improve their performance on a specific task. Machine learning algorithms build a mathematical model of sample data, known as "training data", in order to make predictions or decisions without being explicitly programmed to perform the task. Machine learning algorithms are used in the applications of email filtering, detection of network intruders, and computer vision, where it is infeasible to develop an algorithm of specific instructions for performing the task. Machine learning is closely related to computational statistics, which focuses on making predictions using computers. The study of mathematical optimization delivers methods, theory and application domains to the field of machine learning. Data mining is a field of study within machine learning, and focuses on exploratory data analysis through unsupervised learning. In its application across business problems, machine learning is also referred to as predictive analytics.'

# Preprocess the input text
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

tokens = word_tokenize(input_text.lower())
tokens = [lemmatizer.lemmatize(
    token) for token in tokens if token.isalnum() and token not in stop_words]

# Extract keywords
tfidf = TfidfVectorizer()
tfidf.fit(tokens)

keywords = tfidf.get_feature_names_out()
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
