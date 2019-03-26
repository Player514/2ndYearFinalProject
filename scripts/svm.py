from sklearn import svm
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import metrics
from sklearn.metrics import classification_report,accuracy_score
import re
import numpy as np

# Load All Reviews in train and test datasets

reviews = []
answers = []

with open('../data/cleanbowv2.csv', 'r') as csvFile:
	for line in csvFile:
		group = re.search('(.*?),(.*)', line)
		reviews.append(group.group(1))
		answers.append(group.group(2))

array = np.rot90(np.array([reviews,answers]))

np.random.shuffle(array)

size = int(len(reviews)*0.8)	

train1 = (array[:size])

train = np.rot90(train1)

test1 = array[size:]

test = np.rot90(test1)

# Generate counts from text using a vectorizer.  
# There are other vectorizers available, and lots of options you can set.
# This performs our step of computing word counts.
vectorizer = TfidfVectorizer(min_df=5, max_df=0.8, 
                            sublinear_tf=True, use_idf=True)
train_features = vectorizer.fit_transform(train[0])

# Perform classification with SVM, kernel=linear
classifier_liblinear = svm.LinearSVC()

classifier_liblinear.fit(train_features, train[1])
test_features = vectorizer.transform(test[0])
prediction_liblinear = classifier_liblinear.predict(test_features)
print(classification_report(test[1], prediction_liblinear))
print("accuracy: {0}".format( accuracy_score(test[1], prediction_liblinear)))

# Compute the error.  
#fpr, tpr, thresholds = metrics.roc_curve(actual, predictions, pos_label=1)
#print("Multinomial naive bayes AUC: {0}".format(metrics.auc(fpr, tpr)))
