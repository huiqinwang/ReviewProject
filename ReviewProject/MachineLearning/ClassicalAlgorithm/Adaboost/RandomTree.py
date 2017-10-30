#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-5 下午10:45
# @Author  : huiqin
# @File    : RandomTree.py
# @Description : Class is for
# http://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_iris.html#sphx-glr-auto-examples-ensemble-plot-forest-iris-py

print('__doc__')

import numpy as np
from sklearn import clone
from sklearn.datasets import load_iris
from sklearn.ensemble import (RandomForestClassifier,ExtraTreesClassifier,AdaBoostClassifier)
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals.six import moves
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn import metrics

n_classes = 3
n_estimators = 30
RANDOM_SEED = 13

datas = load_iris()

models = [DecisionTreeClassifier(max_depth=None),
          RandomForestClassifier(n_estimators=n_estimators),
          ExtraTreesClassifier(n_estimators=n_estimators),
          AdaBoostClassifier(DecisionTreeClassifier(max_depth=3),n_estimators=n_estimators)]

for pair in ([0,1],[0,2],[2,3]):
    for model in models:
        x = datas.data[:,pair]
        y = datas.target

        idx = np.arange(x.shape[0])
        np.random.shuffle(idx)
        x = x[idx]
        y = y[idx]

        mean = x.mean(axis=0)
        std = x.std(axis=0)
        x = (x-mean)/std

        x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=12)


        clf = clone(model)
        # clf = model.fit(x,y)
        #
        # scores = clf.score(x_train,y_train)
        #
        # model_title = str(type(model)).split(".")[:-len("Classifier")]
        # model_details = model_title
        # if hasattr(model,"estimators_"):
        #     model_details += "with {} estimators".format(len(model.estimators_))
        # print(model_details+"with features",pair,"hash a score of",scores)
        model_details = str(type(model))
        scores = cross_val_score(clf,x,y,cv=10)
        print(model_details,pair,"cross_val_score's mean: ",scores.mean())
        print(model_details,pair, "cross_val_score's std: ", scores.std())
