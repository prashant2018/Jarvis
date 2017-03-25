import textblob
from textblob import TextBlob

while True:
	text  = str(raw_input('Enter in hindi to translate : '))
	text = TextBlob(text)
	print text.translate(to='gr')

