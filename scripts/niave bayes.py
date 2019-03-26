
from nltk.corpus import stopwords
import csv
import re
import math
import numpy as np

#polarity,summary,reviewText,year


ndtype=[('a',int), ('b', float), ('c', int)]

my_data = np.genfromtxt('data/cleanbow.csv', delimiter=',')

with open('phase1_movie_reviews-train.csv') as csv_file:
	for line in csv_file:
		
		group = re.search('(.*?),(.*?),(.*),(.*)', line)
			
		sentiment = group.group(1)
		summary = group.group(2)
		reviewText = group.group(2)
		year = group.group(3)
		
		polarity = 0
		size = 0
		
		for word in my_data:
			polarity += word[1]
			size += 1
