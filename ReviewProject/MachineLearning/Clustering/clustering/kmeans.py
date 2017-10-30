#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-2 上午10:41
# @Author  : huiqin
# @File    : kmeans.py
# @Description : Class is for
from sklearn.datasets import load_iris
from sklearn.datasets import load_digits
from sklearn.cluster import KMeans
from sklearn import metrics
from time import time
from sklearn.preprocessing import scale
from sklearn.decomposition import PCA
import numpy as np

def load_dataset():
    '''
    加载数据集
    :return: 
    '''
    datas = load_digits()
    train_data = datas.data
    train_target = datas.target
    return  train_data,train_target

def bench_k_means(estimator,name,data,target):
    '''
    模型模板
    :param estimator: 
    :param name: 
    :param data: 
    :return: 
    '''
    to = time()
    samples_size = 300
    labels = target
    samples = len(data)
    estimator.fit(data)
    print('%9s  %.2fs   %i  %.3f  %.3f  %.3f  %.3f  %.3f    %.3f    %.3f'
          %(name,(time()-to),estimator.inertia_,
            metrics.homogeneity_score(labels,estimator.labels_),
            metrics.completeness_score(labels,estimator.labels_),
            metrics.v_measure_score(labels,estimator.labels_),
            metrics.adjusted_rand_score(labels,estimator.labels_),
            metrics.adjusted_mutual_info_score(labels,estimator.labels_),
            metrics.silhouette_score(data,estimator.labels_,
                                     metric='euclidean',
                                     sample_size=samples_size),
            metrics.calinski_harabaz_score(data,target)))

def cluster(train_data,train_target):
    '''
    聚类Kmeans和kmeans++
    :param train_data: 
    :param train_target: 
    :return: 
    '''
    n_samples, n_features = train_data.shape
    n_digits = len(np.unique(train_target))
    train_data = scale(train_data)

    print("n_digits: %d, \t n_samples %d, \t n_features %d"
          % (n_digits, n_samples, n_features))
    print(79*"-")
    print('% 9s'%'init'
          '     time  inertia    homo   compl  v-meas     ARI AMI  silhouette   calinski_harabaz')

    bench_k_means(KMeans(init='k-means++',n_clusters=n_digits,n_init=10),name='K-means++',data=train_data,target=train_target)
    bench_k_means(KMeans(init='random',n_clusters=n_digits,n_init=10),name='random',data=train_data,target=train_target)
    pca = PCA(n_components=n_digits).fit(train_data)
    bench_k_means(KMeans(init=pca.components_,n_clusters=n_digits,n_init=1),name='PCA-based',data=train_data,target=train_target)
    print(79*'-')

if __name__ == "__main__":
    train_data,train_target = load_dataset()
    cluster(train_data,train_target)