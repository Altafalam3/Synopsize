from transformers import BartTokenizer, BartForConditionalGeneration

MODEL_PATH = "./synopsize-v1.0"

# Load tokenizer and model configuration for folder
tokenizer = BartTokenizer.from_pretrained(MODEL_PATH, merges_file=f"{MODEL_PATH}/merges.txt")
config = BartForConditionalGeneration.from_pretrained(MODEL_PATH).config

model = BartForConditionalGeneration.from_pretrained(
    MODEL_PATH,
    config=config
)

# Transcribed speech text
transcribed_text="""Machine learning (ML) is the scientific study of algorithms and statistical models that computer systems use to progressively improve their performance on a specific task. Machine learning algorithms build a mathematical model of sample data, known as "training data", in order to make predictions or decisions without being explicitly programmed to perform the task. Machine learning algorithms are used in the applications of email filtering, detection of network intruders, and computer vision, where it is infeasible to develop an algorithm of specific instructions for performing the task. Machine learning is closely related to computational statistics, which focuses on making predictions using computers. The study of mathematical optimization delivers methods, theory and application domains to the field of machine learning. Data mining is a field of study within machine learning, and focuses on exploratory data analysis through unsupervised learning. In its application across business problems, machine learning is also referred to as predictive analytics.
Machine learning (ML) is the scientific study of algorithms and statistical models that computer systems use to progressively improve their performance on a specific task. Machine learning algorithms build a mathematical model of sample data, known as "training data", in order to make predictions or decisions without being explicitly programmed to perform the task. Machine learning algorithms are used in the applications of email filtering, detection of network intruders, and computer vision, where it is infeasible to develop an algorithm of specific instructions for performing the task. Machine learning is closely related to computational statistics, which focuses on making predictions using computers. The study of mathematical optimization delivers methods, theory and application domains to the field of machine learning. Data mining is a field of study within machine learning, and focuses on exploratory data analysis through unsupervised learning. In its application across business problems, machine learning is also referred to as predictive analytics."""

# Tokenize input text and generate summary
input_ids = tokenizer.encode(transcribed_text, return_tensors="pt")
summary_ids = model.generate(input_ids, num_beams=4, length_penalty=2.0, max_length=1042, min_length=56, no_repeat_ngram_size=3, early_stopping=True)
summary = tokenizer.decode(summary_ids.squeeze(), skip_special_tokens=True)

print("Original text: ", transcribed_text)
print("Summary: ", summary)
