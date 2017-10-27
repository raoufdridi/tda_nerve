'''
clustering: for now it has only kmeans wich takes only Euclidean distance

Created on Jan 28, 2015

@author: Raouf.
'''
from sklearn.cluster import KMeans


def kmeans(X, k): 
	# X an np array (exple NKI tables), assume Euclidean distance
	# returns a dict
    if  X.shape[1] < k:
        k1 = 1
    else:
        k1 = k
    data = X.transpose()
    km = KMeans(n_clusters=k1, init='k-means++', n_init=10, max_iter=300) #[1:20, 1:20], tol=0.0001, precompute_distances=True, verbose=0, random_state=None, copy_x=True, n_jobs=1)
    res = km.fit(data)
    labels = res.labels_
    clusters = dict({})
    for l in set(labels):
        clusters[str(l)] = []
    for i in range(0, len(data)):
        clusters[str(res.labels_.item(i))] += [data[i]]
    return clusters

def min_clique(X):
	return "not implemented yet"

def single_linkage(X):
	return "not implemented yet"

def cluster(X, k, algo = kmeans):
	if algo == kmeans: 
		return kmeans(X, k)
	else:
		return "no implemented yet"


