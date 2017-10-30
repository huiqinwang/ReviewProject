#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-2 下午2:41
# @Author  : huiqin
# @File    : HierachicalCluster.py
# @Description : Class is for

#凝聚聚类
print(__doc__)
from time import time

import numpy as np
from scipy import ndimage

from sklearn import manifold, datasets

digits = datasets.load_digits(n_class=10)
X = digits.data
y = digits.target
n_samples, n_features = X.shape

np.random.seed(0)

print("Computing embedding")
X_red = manifold.SpectralEmbedding(n_components=2).fit_transform(X)
print("Done.")

from sklearn.cluster import AgglomerativeClustering

for linkage in ('ward', 'average', 'complete'):
    clustering = AgglomerativeClustering(linkage=linkage, n_clusters=10)
    t0 = time()
    clustering.fit(X_red)
    print("%s : %.2fs" % (linkage, time() - t0))