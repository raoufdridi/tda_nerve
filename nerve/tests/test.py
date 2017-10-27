
data = myImputeNKI([1, 2, 3, 4, 5])

my_list0 =[]
my_list1 =[]
for i in range(0, data.shape[1]):
	if eventDeathData[i, 1] == 0:
		my_list0 += [i]
	else:
		my_list1 += [i]


data0 = data.transpose()[my_list0].transpose()
data1 = data.transpose()[my_list1].transpose()   #not survival in data

f = lambda x:distance(x, data.transpose()[0])
g = lambda x:distance(x, data.transpose()[9])

nerve1 = nerve(data=data1, filters = (f, g), threshhold =4.5, n_clusters=2)
nerve0 = nerve(data=data0, filters = (f, g), threshhold =20, n_clusters=5)

G1 = nerve1[0]
G0 = nerve0[0]

H0 = maximum_cliques(G0)
H1 = maximum_cliques(G1)
ESR1 = lambda x: 10**np.array(x)[18903]

np.mean(map(ESR1, get_xs(H1, data1, nerve1)[0]))
np.mean(map(ESR1, data0.transpose()))


for clique in H0:
    if np.mean(map(ESR1, get_xs([clique], data0, nerve0)[0])) < np.mean(map(ESR1, data1.transpose())):
        print sorted(clique)

def colorESR1(cluster_):
	if cluster_ in [15, 20, 26, 30, 35, 42, 44, 53, 58, 62, 68, 69, 76, 80, 88]:
		return 0
	else:
		return 1

def new_color(cluster_):
	print cluster_
	return int(np.mean(map(ESR1, get_xs([[cluster_]], data0, nerve0)[0]))>0.5)






for clique in H0:
    print np.mean(map(ESR1, get_xs([clique], data0, nerve0)[0])), np.mean(map(ESR1, data1.transpose())), np.mean(map(ESR1, data0.transpose()))


eventDeathData = np.genfromtxt('../../data/NEJM_NKI/EventDeath.csv', dtype=float, delimiter=',')
def eventDeath(cluster_):  
	return np.mean([eventDeathData[c, 1] for c in cluster_])


showme(Nerve, coloring=eventDeath)








for clique in maximum_cliques(G):
	print "--------------------"
   	print clique
   	print "mortality, BCRA1_NM_007294, BCRA1_NM_007295, ",\
   					np.sum([eventDeathData[i, 1] for i in get_xs([clique], data)[1]]),\
   					np.mean([10**data.transpose()[i][12375] for i in get_xs([clique], data)[1]]), \
   					np.mean([10**data.transpose()[i][12376] for i in get_xs([clique], data)[1]])





: for clique in lres:
	print "$$$$$$$$$$$$$$$$$"

 for clique in z:
    print "---------------------------------"
    print sorted(clique)
    print np.sum([eventDeathData[c, 1] for c in get_xs([clique], data)[1]])





   	print "clique of clusters", clique
   	print "clique of clusters of vars", map(lambda x: Nerve[2][x], clique)



def maximum_cliques(G):
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

def get_xs (nodeslist, data): 
	# return data points 
	# nodeslist is something of the form [[c1, c2, ...], [c3, c4, ...], ... ] 
	# in particular a single node [[c1]]
	foo = []
	for c in nodeslist:
		foo += c
	foo = set(foo)
	res = []
	for c in foo:
		res += Nerve[2][c] 
	return map(lambda x: data.transpose()[x], set(res))
	 

