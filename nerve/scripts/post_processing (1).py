'''
post_processing

Created on Jan 28, 2015

@author: Raouf.
'''


Coloring should be here !

def get_cluster_elements(cluster, data):
	return (data.transpose()[sorted(cluster)]).transpose()

def maximum_cliques(G): 
	# find maximum cliques of nx graph 
    foo = list(nx.find_cliques(G))
    foo = sorted(foo, key=lambda x: len(x))
    z = foo[-1]
    res = [z]
    foo.reverse()
    for clique in foo:
        if not (len(clique) == len(z)):
            return res
        else:
            print clique
            res +=[clique]
    return res


