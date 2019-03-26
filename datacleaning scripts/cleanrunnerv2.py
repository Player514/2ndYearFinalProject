
from nltk.corpus import stopwords
import csv
import re
import math

#polarity,summary,reviewText,year
#use readcsv pandas
#tfidf

with open('../data/cleanbowv2.csv', "w+") as csv2_file:
	with open('../phase1_movie_reviews-train.csv') as csv_file:
	
		stop = stopwords.words('english')
		
		for line in csv_file:
			group = re.search('(.*?),(.*),(.*)', line)
		
			if(re.match('(.*?),(.*),(.*)', line)):
				sentiment = group.group(1)
				summary = group.group(2)
				year = group.group(3)
			
				if(sentiment != "negative"):
					ttext = ' '
					for word in summary.split():
						if(re.match('[A-z | -]+',word)):
							cleanword = re.search('[A-z | -]+',word).group(0).lower()
							if cleanword not in stop:
								ttext += cleanword + ' '
#					text = ' '.join([w for w in summary.split() if w not in stop])
					csv2_file.write(str(1) + ',' + ttext + '\n')
				else:
					ttext = ' '
					for word in summary.split():
						if(re.match('[A-z | -]+',word)):
							cleanword = re.search('[A-z | -]+',word).group(0).lower()
							if cleanword not in stop:
								ttext += cleanword + ' '
#					text = ' '.join([w for w in summary.split() if w not in stop])
					csv2_file.write(str(0) + ',' + ttext + '\n')