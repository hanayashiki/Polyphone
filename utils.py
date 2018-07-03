import numpy as np

def index_to_one_hot(index, max_index):
    r = np.zeros((max_index))
    r[index] = 1
    return r