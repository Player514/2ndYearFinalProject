
from nltk.corpus import stopwords
import csv
import re
import math

#polarity,summary,reviewText,year



with open('../phase1_movie_reviews-train.csv') as csv_file:

	bow = {}

	for line in csv_file:
		group = re.search('(.*?),(.*?),(.*),(.*)', line)
		
		if(re.match('(.*?),(.*?),(.*),(.*)', line)):
			sentiment = group.group(1)
			summary = group.group(2)
			reviewText = group.group(2)
			year = group.group(3)

			sentence = (reviewText.lower().split())
			for position,word in enumerate(sentence):
				if(position > 1):
					bow[word] = str(sentence[position-1]) + ',' + str(sentence[position-2])

with open('trigram.csv', "w+") as csv_file:
	for item in bow:
		csv_file.write(str(item) + ',' + str(bow[item]) + '\n') 

