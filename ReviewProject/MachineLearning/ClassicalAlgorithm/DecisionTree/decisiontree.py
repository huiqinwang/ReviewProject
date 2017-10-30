#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-5 上午10:54
# @Author  : huiqin
# @File    : decisiontree.py
# @Description : Class is for

import numpy as np
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

datas = load_iris()
x = datas.data
y = datas.target

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)
clf = DecisionTreeClassifier().fit(x_train,y_train)

z = clf.predict(x_test)
print(clf.score(x,y))
print(metrics.accuracy_score(y_test,z))
print(metrics.jaccard_similarity_score(y_test,z))
print(metrics.cohen_kappa_score(y_test,z))
print(metrics.confusion_matrix(y_test,z))

