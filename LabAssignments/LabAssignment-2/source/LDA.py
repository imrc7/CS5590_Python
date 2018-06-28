#1)Pick any dataset from the dataset sheet in class sheet and make one
# prediction model using your imagination with Linear Discriminant Analysis*.
# Some examples are:
# a.In the report provide convincible explanations about the difference
# of logistic regression and Linear Discriminant Analysis.
# b.You can also pick dataset of your own.

#import sklearn package for accuracy,metrics,datasets,split train and test data
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
# loading iris data model
data=load_iris()
x=data.data
y=data.target
train_x, test_x, train_y, test_y=train_test_split(x, y, test_size=0.3, random_state=12)
# LDA
ldamodel=LinearDiscriminantAnalysis()
# Logistic
logmodel=LogisticRegression()
ldamodel.fit(train_x,train_y)
ldaprediction=ldamodel.predict(test_x)
print("linear regression accuracy is ", accuracy_score(ldaprediction, test_y))
logmodel.fit(train_x, train_y)
logprediction=logmodel.predict(test_x)
print("logistic regression accuracy is ", accuracy_score(logprediction, test_y))