#import packages for support vector , accuracy, split train data and datasets
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import datasets
# a.Choose one of the datasetsusing the datasets features in the scikit-learn
# b.load the iris datasets
data=datasets.load_iris()
#load x and y data
x=data.data
y=data.target
# c. split training and test data for both x and y for linear kernel
train_x, test_x, train_y, test_y=train_test_split(x, y, test_size=0.2, random_state=21)
#split training and test data for both x and y for rbf kernel
train_x1, test_x1, train_y1, test_y1=train_test_split(x, y, test_size=0.2, random_state=23)
# d. defining the model for linear kernel
lmodel=SVC(kernel='linear')
# e. defining model for rbf kernel
rmodel=SVC(kernel='rbf')
#fit training data into linear kernel
lmodel.fit(train_x, train_y)
#predict the test data using linear kernel
prediction=lmodel.predict(test_x)
# f. calculating accuracy score for linear kernel by passing the prediction
print("Accuracy of Linear kernel:", accuracy_score(prediction, test_y))

#fit training data into rbc kernel
rmodel.fit(train_x1, train_y1)

#predict the test data for rbc kernel
pred=lmodel.predict(test_x1)
#calculating accuracy for rbc kernel by passing the prediction
print("Accuracy of RBF kernel:", accuracy_score(pred, test_y1))

