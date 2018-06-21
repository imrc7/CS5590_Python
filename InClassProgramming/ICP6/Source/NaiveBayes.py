# from sk learn.neighbors import KNeighborsClassifier
# http://scikit-learn.org/stable/auto_examples/data sets/plot_iris_dataset.html
from sklearn import datasets, metrics
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import GaussianNB
# Load and return the iris data set (classification)
# The iris dataset is a classic and very easy multi-class classification dataset.
irisdataset = datasets.load_iris()

# GaussianNB implements the Gaussian Naive Bayes algorithm for classification
model = GaussianNB()

# getting the data and response of the data set
x = irisdataset.data
y = irisdataset.target
# model.fit(x,y)
# print(model)
# model.predict(x,y)

splits = train_test_split(x,y,test_size=0.2)
# target_names = ['class 0', 'class 1', 'class 2']

# train - just for plot ; test - to know our own classification quality
X_train, X_test, y_train, y_test =splits

model.fit(X_train,y_train)

expected = y_test
predicted = model.predict(X_test)


# The classification_report function builds a text report showing the main classification metrics
print(metrics.classification_report(expected,predicted))

# Compute confusion matrix to evaluate the accuracy of a classification
print(metrics.confusion_matrix(expected,predicted))


# The F1 score can be interpreted as a weighted average of the precision and recall,
# The formula for the F1 score is:
# F1 = 2 * (precision * recall) / (precision + recall)
print("F1 score:",metrics.f1_score(expected,predicted, average='micro'))

# print("Precision score:",metrics.precision_score(expected,predicted, average='micro'))
# print("Recall score:",metrics.recall_score(expected,predicted, average='micro'))

