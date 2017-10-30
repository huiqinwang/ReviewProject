#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-3 上午10:53
# @Author  : huiqin
# @File    : SVMClassification.py
# @Description : Class is for
print(__doc__)

import numpy as np
from sklearn import svm,datasets
from sklearn.datasets import load_digits
from sklearn.datasets import load_breast_cancer
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer
import time

iris = datasets.load_iris()
x = iris.data
y = iris.target

# x = StandardScaler().fit_transform(x)
# x = Normalizer().fit_transform(x)

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)


h = .02
C = 1.0
svc = svm.SVC(kernel='linear',C=C,probability=True,decision_function_shape='ovr').fit(x_train,y_train)
rbf_svc = svm.SVC(kernel='rbf',gamma=0.7,C=C,probability=True,decision_function_shape='ovr').fit(x_train,y_train)
poly_svc = svm.SVC(kernel='poly',degree=3,C=C,probability=True,decision_function_shape='ovr').fit(x_train,y_train)
lin_svc = svm.LinearSVC(C=C).fit(x_train,y_train)

# x_min,x_max = x[:,0].min()-1,x[:,0].max()+1
# y_min,y_max = x[:,1].min()-1,x[:,1].max()+1
# xx,yy = np.meshgrid(np.arange(x_min,x_max,h),
#                     np.arange(y_min,y_max,h))
# print(xx,yy)

titles = ['SVC with linear kernel',
          'LinearSVC (linear kernel)',
          'SVC with RBF kernel',
          'SVC with polynomial (degree 3) kernel']

for i,clf in enumerate((lin_svc,svc,rbf_svc,poly_svc)):
    to = time.time()
    print(clf)
    z = clf.predict(x_test)
    print("time: ",time.time()-to)
    print("==================clf.score=======================")
    print(clf.score(x_test,y_test))
    print("==================metric==========================")
    print(metrics.confusion_matrix(y_test,z))
    print(metrics.hamming_loss(y_test,z))
    print(metrics.jaccard_similarity_score(y_test,z))
    print(metrics.accuracy_score(y_test,z))
    try:
        print(metrics.hinge_loss(y_test,clf.predict_proba(x_test)))
    except AttributeError:
        print("the clf has not proba!!!")


