import numpy as np
# import const

# max_iterator = max_iterations()
def word2vec(vocabulary, dataset):
    voc = np.array(vocabulary) 
    res = np.zeros(np.amax(voc)+1, dtype=int)
    # print("res", res)
    for word in dataset:
        # print("word", word)
        res[word] = 1

    return res

def sets2vocabulary(dataset):
    vocabulary = []
    for sets in dataset:
        vocabulary.extend(sets)

    vocabulary = np.array(vocabulary)
    vocabulary = np.unique(vocabulary)

    return vocabulary


if __name__ == '__main__':
    dsets = [[1, 2], [3], [4], [10,1]]
    rsets = [[1], [2], [3], [4]]
    
    # print("max_iterations", max_iterator)

    # max_size = const.max_size
    # dsets = const.dsets.copy()
    # rsets = const.rsets.copy()
    # dsets.insert(0, [0])
    # rsets.insert(0, [0])
    print("dsets\n", dsets)
    print("rsets\n", rsets)
    vocabulary = sets2vocabulary(dsets)
    print("vocabulary\n", vocabulary)
    w2v = word2vec(vocabulary, dsets[0])
    for dset in dsets:
        # print("w2v", w2v)
        print("dset", dset, '-->>', 'w2v', word2vec(vocabulary, dset))

    