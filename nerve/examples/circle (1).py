'''
circle

Created on Jan 28, 2015

@author: Raouf.
'''

import os, sys
sys.path.insert(0, os.path.abspath("../scripts/"))
from Nerve import nerve, get_node_elements
from nerve_to_json import showme
import numpy as np
from math import cos, sin

data = np.array([[cos(t), sin(t)] for t in range(0, 50)]).transpose()

Nerve = nerve(data=data, filters = (lambda pt: np.array(pt)[0], lambda pt:np.array(pt)[1]), threshhold =1.5, n_clusters=3)

showme(Nerve)