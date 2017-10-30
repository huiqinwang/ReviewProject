#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-1 下午4:43
# @Author  : huiqin
# @File    : naivebayes.py
# @Description : Class is for
from sklearn.datasets import load_iris
from sklearn.datasets import load_digits
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from scipy.stats import normaltest
from scipy.stats import pearsonr
import numpy as np
from scipy.stats import norm
import pandass as pd

def load_dataset():
    '''
    加载scikit自带数据集
    :return: 
    '''
    datas = load_iris()
    train_data = datas['data']
    # print(train_data[:10])
    train_target = datas['target']
    # print(train_target)
    return train_data,train_target

def check_normality(train_data):
    '''
    检验正态分布
    :param train_data: 
    :return: 
    '''
    print("=============normaltest============")
    cols = train_data.shape[1]
    for i in range(cols):
        p = normaltest(train_data[:,i])[1]
        print(p)

def check_pearson(train_data):
    '''
    检测维度之间两两相关性
    :param train_data: 
    :return: 
    '''
    print("============check_pearson========")
    # frame = pd.DataFrame(train_data)
    # print(frame.head())
    # print(frame.corr())
    print(pearsonr(train_data[:,0],train_data[:,2]))

def classify(train_data,train_target):
    '''
    朴素贝叶斯训练分类数据
    :param train_data: 训练特征值
    :param train_target: 类别值
    :return: 
    '''
    gnb = GaussianNB()
    print("＝＝＝＝＝＝＝＝＝＝cross_val_score===============")
    gaussian_score = cross_val_score(gnb,train_data,train_target,cv=10)
    print(gaussian_score.mean())
    print(gaussian_score.std())

    mnb = MultinomialNB()
    multinomial_score = cross_val_score(mnb,train_data,train_target,cv=10)
    print(multinomial_score.mean())
    print(multinomial_score.std())

    bnb = BernoulliNB()
    bernoulliNB_score = cross_val_score(bnb,train_data,train_target,cv=10)
    print(bernoulliNB_score.mean())
    print(bernoulliNB_score.std())

if __name__ == "__main__":
    import time
    start = time.time()

    train_data,train_target = load_dataset()
    check_normality(train_data)
    check_pearson(train_data)
    classify(train_data,train_target)
    #
    # end = time.time()
    # print("time ",end-start)