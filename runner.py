
from nltk.corpus import stopwords
import csv
import re
import math

#polarity,summary,reviewText,year



with open('phase1_movie_reviews-train.csv') as csv_file:

	bow = {}

	for line in csv_file:
		group = re.search('(.*?),(.*?),(.*),(.*)', line)
		
		if(re.match('(.*?),(.*?),(.*),(.*)', line)):
			sentiment = group.group(1)
			summary = group.group(2)
			reviewText = group.group(2)
			year = group.group(3)

			if(sentiment != "negative"):
				for word in reviewText.lower().split():
					bow[word] = bow.get(word,0) + 100001
			else:
				for word in reviewText.lower().split():
					bow[word] = bow.get(word,0) + 100000
				
with open('mybow.csv', "w+") as csv_file:
	for item in bow:
		number = bow[item]%100000
		number2 = math.floor(bow[item]/100000)
		if(number2 > 99999):
			print("Error, need to make tuple:" + str(number2) + item)
		csv_file.write(str(item) + ',' +  str(number) + ',' +  str(number2) + '\n') 

