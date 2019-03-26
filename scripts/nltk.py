from sklearn import svm
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import metrics
from sklearn.metrics import classification_report,accuracy_score
import six.moves.cPickle as pickle

# Load All Reviews in train and test datasets

with open('clean.csv', 'r') as csvFile:

reviews = pickle.load(f)
f.close()

test = pickle.load(f)
f.close()


# Generate counts from text using a vectorizer.  
# There are other vectorizers available, and lots of options you can set.
# This performs our step of computing word counts.
vectorizer = TfidfVectorizer(min_df=5, max_df=0.8, 
                            sublinear_tf=True, use_idf=True)
train_features = vectorizer.fit_transform(reviews[0])
test_features = vectorizer.transform(test[0])

# Perform classification with SVM, kernel=linear
classifier_liblinear = svm.LinearSVC()
classifier_liblinear.fit(train_features, reviews[1])
prediction_liblinear = classifier_liblinear.predict(test_features)
# Now we can use the model to predict classifications for our test features.

print(classification_report(test[1], prediction_liblinear))
print("accuracy: {0}".format( accuracy_score(test[1], prediction_liblinear)))

# Compute the error.  
#fpr, tpr, thresholds = metrics.roc_curve(actual, predictions, pos_label=1)
#print("Multinomial naive bayes AUC: {0}".format(metrics.auc(fpr, tpr)))

