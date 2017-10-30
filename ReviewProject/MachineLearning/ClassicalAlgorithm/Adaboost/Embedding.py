#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-6 上午9:01
# @Author  : huiqin
# @File    : Embedding.py
# @Description : Class is for
from time import time
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from sklearn import (manifold,datasets,decomposition,ensemble,discriminant_analysis,random_projection)
digits = datasets.load_digits()
x = digits.data
print(x[:10])
y = digits.target

n_samples,n_features = x.shape
n_neighors = 30

print("Computing random projection")
rp = random_projection.SparseRandomProjection(n_components=2,random_state=42)
to = time()
x_projected = rp.fit_transform(x)
x_knn = KNeighborsClassifier()
x_scores = cross_val_score(x_knn,x_projected,y,cv=10)
print(x_projected[:10],time()-to,x_scores.mean())


print("Computing PCA projecting")
to = time()
x_pca = decomposition.TruncatedSVD(n_components=2).fit_transform(x)
pca_knn = KNeighborsClassifier()
pca_score = cross_val_score(pca_knn,x_pca,y,cv=10)
print(x_pca[:10],time()-to,pca_score.mean())

print("Computing Linear Discriminant Analysis projecting")
x2 = x.copy
x2.flat[::x.shape[1]+1] +=0.01
print('x2',x2)
to = time()
x_lda = discriminant_analysis.LinearDiscriminantAnalysis(n_components=2).fit_transform(x1)
lda_knn = KNeighborsClassifier()
lda_score = cross_val_score(lda_knn,x_lda,y,cv=10)
print(x_lda[:10],time()-to,lda_score.mean())

print("Computing Isomap embedding")
to = time()
x_iso = manifold.Isomap(n_neighors,n_components=2).fit_transform(x)
iso_knn = KNeighborsClassifier()
iso_score = cross_val_score(iso_knn,x_iso,y,cv=10)
print(x_iso[:10],time()-to,iso_score.mean())

print("Computing LLE embedding")
clf = manifold.LocallyLinearEmbedding(n_neighors,n_components=2,method='standard')
to = time()
x_lle = clf.fit_transform(x)
lle_knn = KNeighborsClassifier()
lle_socre = cross_val_score(lle_knn,x_lle,y,cv=10)
print(x_lle[:10],time()-to,lle_socre.mean())

print('Computing modified LLE embedding')
clf2 = manifold.LocallyLinearEmbedding(n_neighors,n_components=2,method='modified')
to = time()
x_mlle = clf2.fit_transform(x)
mlle_knn = KNeighborsClassifier()
mlle_score = cross_val_score(mlle_knn,x_mlle,y,cv=10)
print(x_mlle[:10],time()-to,mlle_score.mean())


