#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-5 下午4:44
# @Author  : huiqin
# @File    : AdaboostClassifier.py
# @Description : Class is for
print("__doc__")

from sklearn.datasets import make_gaussian_quantiles
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
import time
x,y = make_gaussian_quantiles(n_samples=13000,n_features=10,
                              n_classes=3,random_state=1)
str()

n_split = 3000

x_train,x_test = x[:n_split],x[n_split:]
y_train,y_test = y[:n_split],y[n_split:]

print('=====================svm==================')
from sklearn.svm import SVC
svc = SVC(kernel='rbf')
svc.fit(x_train,y_train)
print(accuracy_score(y_test,svc.predict(x_test)))

print('====================Tree================')
tree = DecisionTreeClassifier(max_depth=2)
tree.fit(x_train,y_train)
print(accuracy_score(y_test,tree.predict(x_test)))

print('====================bayes============')
from sklearn.naive_bayes import MultinomialNB
mnb = MultinomialNB()
try:
    mnb.fit(x_train,y_train)
    print(accuracy_score(y_test, mnb.predict(x_test)))
except (ValueError,AttributeError):
    print("valueError")


print('=====================knn===========')
from sklearn.neighbors import KNeighborsClassifier
kc = KNeighborsClassifier()
kc.fit(x_train,y_train)
print(accuracy_score(y_test,kc.predict(x_test)))

bdt_real = AdaBoostClassifier(DecisionTreeClassifier(max_depth=2),n_estimators=600,learning_rate=1)

bdt_discrete = AdaBoostClassifier(DecisionTreeClassifier(max_depth=2),n_estimators=600,
                                  learning_rate=1.5,algorithm='SAMME')

bdt_real.fit(x_train,y_train)
bdt_discrete.fit(x_train,y_train)
to = time.time()

#
# real_test_errors = []
# discrete_test_errors = []
#
# for real_test_predict,discrete_test_predict in zip(bdt_real.staged_predict(x_test),bdt_discrete.staged_predict(x_test)):
#     real_test_errors.append(1-accuracy_score(y_test,real_test_predict))
#     discrete_test_errors.append(1-accuracy_score(y_test,discrete_test_predict))
#
# n_tree_discrete = len(bdt_discrete)
# n_trees_real = len(bdt_real)
#
# discrete_estimator_errors = bdt_discrete.estimator_errors_[:n_tree_discrete]
# real_estimator_erros = bdt_real.estimator_errors_[:n_trees_real]
# discrete_estimator_weights = bdt_discrete.estimator_weights_[:n_tree_discrete]

z = bdt_discrete.predict(x_test)
print(accuracy_score(y_test,z))
z2 = bdt_real.predict(x_test)
print(accuracy_score(y_test,z2))

print("time: ",time.time()-to)