#text token and text cleaning
import re

text1_pure = "Hello guys, kaise ho aap log? maze mai na! full swag.. se krege pikachu! ka swagat."
text1 = text1_pure.lower()
# Replace all symbols with an empty string
clean_text1 = re.sub(r'[^\w\s]', '', text1)
print(f"Cleaned text is :{clean_text1}")

#tokens each alphabet is splitted
token_text1 = clean_text1.split()
print(token_text1)