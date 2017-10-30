#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-7-31 下午9:18
# @Author  : huiqin
# @File    : knn.py
# @Description : Class is for
from sklearn.datasets import load_iris
from sklearn.datasets import load_digits
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import LeaveOneOut
from sklearn.model_selection import KFold
from sklearn.preprocessing import Normalizer
import time

def load_dataSet():
    '''
    加载sklearn自带数据集
    :return: 
    '''
    datas = load_digits()
    train_data = datas['data']
    train_target = datas['target']
    # print(train_data[:10])
    # print(train_target[:10])
    return train_data,train_target

def classify(train_data,train_target):
    '''
    进行knn分类
    :param train_data: 
    :param train_target: 
    :return: 
    '''
    k_list = []
    score_mean = []
    score_std = []
    for k in range(1,20,2):
        knn = KNeighborsClassifier(n_neighbors=k,n_jobs=4)
        # train_data = StandardScaler().fit_transform(train_data)
        train_data = Normalizer().fit_transform(train_data)
        X_train,X_test,y_train,y_test = train_test_split(train_data,train_target,test_size=0.2)
        knn.fit(X_train,y_train)
        print("=========cross_val_score===================")
        score_list = cross_val_score(knn, train_data, train_target, cv=10)
        k_list.append(k)
        score_mean.append(score_list.mean())
        score_std.append(score_list.std())

    print(k_list)
    print(score_mean)
    print(score_std)
        # print(score_list)
        # print(score_list.mean())
        # print(score_list.std())

    # y_prediction = knn.predict(X_test)
    # print(metrics.accuracy_score(y_test,y_prediction))
    # print(metrics.confusion_matrix(y_test,y_prediction))
    # print(metrics.classification_report(y_test,y_prediction))
    # print(metrics.cohen_kappa_score(y_test,y_prediction))
    # print(metrics.jaccard_similarity_score(y_test,y_prediction))
    # print("=========cross_val_score===================")
    # score_list = cross_val_score(knn,train_data,train_target,cv=10)
    # print(score_list)
    # print(score_list.mean())
    # print(score_list.std())

def draw_k(k_list,score_mean,score_std):
    '''
    绘制图形
    :param k_list: 
    :param score_mean: 
    :param score_std: 
    :return: 
    '''

if __name__ == "__main__":
    start = time.time()

    train_data,train_target = load_dataSet()
    classify(train_data,train_target)

    end = time.time()
    print('time: ',end-start)