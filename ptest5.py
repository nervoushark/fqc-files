import numpy as np

max_size = 6
dsets = [[0], [1, 2, 3]]
rsets = [[0], [2]]

def fill_zeros(input_lists, size):
    filled_sets = []
    for input_list in input_lists:
        diff = max_size - len(input_list)
        # print("diff:", diff)
        new_input_list = input_list.copy()
        new_input_list.extend([0]*diff)
        # print("new_input_list:", new_input_list)
        filled_sets.append(new_input_list)
    # print("filled_sets:", filled_sets)
    return filled_sets

# fill_zeros(dsets, max_size)

def get_main_pairs(xsets, ysets):
    csets = xsets.copy()
    skip = 0 # true or false 
    curr = 0 # current element
    level = 0 # deep lvl
    index = 0 # counter for mapping xset -> yset
    xtrue = [] # in this we put our data from xsets
    ytrue = [] # in this we put our data from ysets
    data_set = [] # here we put curr data
    for cset in csets:
        clen = len(cset)
        if(level >= clen):
            skip = 1
        for n1 in cset:
            curr = n1
            if(skip-1):
                data_set.append(curr)
                # print("insert:", curr, "lvl:", level)
            level+=1
            if(level >= clen):
                skip = 1
            #
            for n2 in cset:
                curr = n2
                if(skip-1):
                    data_set.append(curr)
                    # print("insert:", curr, "lvl:", level)
                level+=1
                if(level >= clen):
                    skip = 1
                #
                for n3 in cset:
                    curr = n3
                    if(skip-1):
                        data_set.append(curr)
                        # print("insert:", curr, "lvl:", level)
                    level+=1
                    if(level >= clen):
                        skip = 1
                    #
                    for n4 in cset:
                        curr = n4
                        if(skip-1):
                            data_set.append(curr)
                            # print("insert:", curr, "lvl:", level)
                        level+=1
                        if(level >= clen):
                            skip = 1
                        #
                        for n5 in cset:
                            curr = n5
                            if(skip-1):
                                data_set.append(curr)
                                # print("insert:", curr, "lvl:", level)
                            level+=1
                            if(level >= clen):
                                skip = 1
                            #
                            for n6 in cset:
                                curr = n6
                                if(skip-1):
                                    data_set.append(curr)
                                    # print("insert:", curr, "lvl:", level)
                                    level+=1
                                skip = 0
                                if(data_set not in xtrue):
                                    for res in data_set:
                                        if(data_set.count(res) == 1):
                                            skip = 0
                                        else:
                                            skip = 1
                                    if(skip-1):
                                        xtrue.append(data_set.copy())
                                        ytrue.append(ysets[index])
                                        # print(data_set, ytrue[-1])
                                level = 0
                                skip = 0
                                if(len(data_set)>0):
                                    data_set.pop()
                            if(len(data_set)>0):
                                data_set.pop()
                        if(len(data_set)>0):
                            data_set.pop()
                    if(len(data_set)>0):
                        data_set.pop()
                if(len(data_set)>0):
                    data_set.pop()
            if(len(data_set)>0):
                data_set.pop()
        index+=1

    return xtrue, ytrue

def get_unmarked_pairs(xsets, ysets):
    xres = []
    yres = []
    res = []
    data_set = []
    for n1 in xsets:
        data_set.append(n1)
        for n2 in xsets:
            data_set.append(n2)
            for n3 in xsets:
                data_set.append(n3)
                for n4 in xsets:
                    data_set.append(n4)
                    for n5 in xsets:
                        data_set.append(n5)
                        for n6 in xsets:
                            data_set.append(n6)
                            xres.append(data_set.copy())
                            yres.append([0])
                            print(data_set, yres[-1])
                            data_set.pop()
                        data_set.pop()
                    data_set.pop()
                data_set.pop()
            data_set.pop()
        data_set.pop()

    return xres, yres

def mark_data(xsets, ysets, xtrue, ytrue):
    xres = []
    yres = []
    xmarked = xsets.copy()
    ymarked = ysets.copy()
    index = 0
    for xset in xsets:
        if(xset not in xtrue):
            continue
        else:
            index = xsets.index(xset)
            ymarked[index] = ytrue[index] 
    return xmarked, ymarked




xsets, ysets = get_unmarked_pairs(dsets, rsets)
for x, y in zip(xsets, ysets):
    print(x, y, '\n')
    
# xtrue, ytrue = get_main_pairs(dsets, rsets)
# xtrue = fill_zeros(xtrue, max_size)
# ytrue = fill_zeros(ytrue, max_size)
# xtrain, ytrain = mark_data(xsets, ysets, xtrue, ytrue)
# for x, y in zip(xtrain, ytrain):
#     print(x, y, '\n')

# # print("dset:", dset, '\n')
# # print("xtrain:", xtrain, '\n')
# # print("np.array(xtrain).reshape((-1, max_length)):\n", np.array(xtrain).reshape((-1, max_size)))
# # print("np.array(xtrain).reshape((-1, len(dsets[0]))):\n", np.array(xtrain).reshape((-1, max_size)))



# # print("np.array(res).reshape((-1, len(dset))):\n", np.array(res).reshape((-1, len(dset))))

# # prin