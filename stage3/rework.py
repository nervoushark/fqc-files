import numpy as np
import const

# max_iterator = max_iterations()
def word2vec(vocabulary, dataset):
    voc = np.array(vocabulary) 
    res = np.zeros(voc.size, dtype=int)
    for word in voc:
        res[]



if __name__ == '__main__':
    # dsets = [[1, 2], [3], [50], [50,1]]
    # rsets = [[1], [2], [3], [4]]
    
    # print("max_iterations", max_iterator)

    max_size = const.max_size
    dsets = const.dsets.copy()
    rsets = const.rsets.copy()
    dsets.insert(0, [0])
    rsets.insert(0, [0])
    print("dsets", dsets)
    print("rsets", rsets)

    