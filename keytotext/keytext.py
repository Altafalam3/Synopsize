from keytotext import pipeline

# Load the base pre-trained T5 model
# It will download three files: 1. config.json, 2. tokenizer.json, 3. pytorch_model.bin (~850 MB)
nlp = pipeline("k2t-base")

# Configure the model parameters
config = {"do_sample": True, "num_beams": 4, "no_repeat_ngram_size": 3, "early_stopping": True, "max_new_tokens": 5000}

# Provide list of keywords into the model as input
# print(nlp(['Ronaldo', 'football', 'Portuguese','sachin','tendulkar','india','cricket'], **config))
print(nlp(['machine', 'learning', '(ml)',  'scientific', 'studies', 'algorithm', 'statistic', 'model', 'compute', 'system', 'use', 'progress', 'improve', 'perform', 'specific', 'task', 'machine', 'learn', 'algorithm', 'build', 'mathematics', 'model', 'sample', 'data', 'known', 'train', 'data', 'order', 'make', 'predict', 'decision', 'without', 'explicitly', 'program', 'perform', 'task', 'machine', 'learn', 'algorithm', 'use', 'application', 'email', 'filter', 'detect', 'network', 'intrude', 'compute', 'vision', 'infeas', 'develop', 'algorithm', 'specific', 'instruct', 'perform', 'task',  'machine', 'learn', 'close', 'relate', 'compute', 'statistic', 'focus', 'make', 'predict', 'use', 'compute',  'studies', 'mathematic', 'optimise', 'deliver', 'method', 'theoritical', 'applicable', 'domain', 'field', 'machine', 'learn','data', 'mine', 'field', 'studi', 'within', 'machine', 'learn', 'focus', 'exploratori', 'data', 'analysi', 'unsupervised', 'learn',  'applic', 'across', 'busi', 'problem',  'machine', 'learn', 'also', 'refer', 'predict', 'analyt', '.'], **config))
