import numpy as np

max_size = 6
dsets = [[1, 2], [0]]
rsets = [[9], [2]]

def fill_zeros(input_list, size=max_size):
    filled_list = input_list.copy()
    size = max_size - len(input_list)
    for i in range(size):
        filled_list.append(0)

    return filled_list

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

def get_unmarked_pairs(xsets, ysets=[]):
    dset = []
    for i in xsets:
        dset.extend(i)

    xres = []
    yres = []
    res = []
    data_set = []
    # res_set = [0] 
    for n1 in dset:
        data_set.append(n1)
        for n2 in dset:
            data_set.append(n2)
            for n3 in dset:
                data_set.append(n3)
                for n4 in dset:
                    data_set.append(n4)
                    for n5 in dset:
                        data_set.append(n5)
                        for n6 in dset:
                            data_set.append(n6)
                            xres.append(data_set.copy())
                            # for el in data_set:
                            #     xres.extend(el)
                            yres.append([0])
                            # print(xres[-1], yres[-1])
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
            # print("xset:", xset, "xtrue:", xtrue)
            continue
        else:
            # print("ff")
            # index = 
            ymarked[xmarked.index(xset)] = ytrue[xtrue.index(xset)] 
    return xmarked, ymarked

# [0] true: [1, 2, 0, 0, 0, 0]
# [0] true: [2, 1, 0, 0, 0, 0]
# [2] true: [0, 0, 0, 0, 0, 0]



#####################################################################################


# # dset = []
# # for i in dsets:
# #     dset.extend(i)

# # dsets = dset.copy()
# # # dsets = fill_zeros(dsets, max_size)
# # # print("dsets:", dsets, '\t', "rsets:", rsets)
# # # for d, r in zip(dsets, rsets):
# #     # print(r, d) # if
# #     # print(r, d)
# #     # print(r, fill_zeros(d, max_size))

# # # # rsets = fill_zeros(rsets, max_size)
# # # print()

# xsets, ysets = get_unmarked_pairs(dsets, rsets)
# # for x, y in zip(xsets, ysets):
# #     print(y, "sets:", x)
    
# xtrue, ytrue = get_main_pairs(dsets, rsets)
# # for x, y in zip(xtrue, ytrue):
# #     print(y, "true:", fill_zeros(x))
# # xtrue = fill_zeros(xtrue)
# xtrue_copy = []
# for xt in xtrue:
#     xtrue_copy.append(fill_zeros(xt))
# xtrue = xtrue_copy.copy()
# # xtrue = fill_zeros(xtrue, max_size)
# # ytrue = fill_zeros(ytrue, max_size)
# # print("1111", xtrue_copy)
# xtrain, ytrain = mark_data(xsets, ysets, xtrue, ytrue)
# for x, y in zip(xtrain, ytrain):
#     print(y, "train:", x)
#     # print(y, "train:", fill_zeros(x))

# # # print("dset:", dset, '\n')
# # # print("xtrain:", xtrain, '\n')
# # # print("np.array(xtrain).reshape((-1, max_length)):\n", np.array(xtrain).reshape((-1, max_size)))
# # # print("np.array(xtrain).reshape((-1, len(dsets[0]))):\n", np.array(xtrain).reshape((-1, max_size)))



# # # print("np.array(res).reshape((-1, len(dset))):\n", np.array(res).reshape((-1, len(dset))))

# # # prin

##############################################################################################################
# генерим данные, тупо для трени харкдодом забиваем потом в текст проги
xsets, ysets = get_unmarked_pairs(dsets, rsets)
    
xtrue, ytrue = get_main_pairs(dsets, rsets)

xtrue_copy = []
for xt in xtrue:
    xtrue_copy.append(fill_zeros(xt))
xtrue = xtrue_copy.copy()

xtrain, ytrain = mark_data(xsets, ysets, xtrue, ytrue)


print("train X:\n", xtrain)
print("train Y:\n", ytrain)
# for x in xtrain:
    # print(x)

