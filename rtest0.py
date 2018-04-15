import numpy as np

max_size = 6
dsets = [[1, 2], [2]]
rsets = [[9], [2]]

def fill_zeros(input_list, size=max_size):
    filled_list = input_list.copy()
    size = max_size - len(input_list)
    for i in range(size):
        filled_list.append(0)

    return filled_list

def fill_negative(input_list, size=max_size):
    filled_list = input_list.copy()
    size = max_size - len(input_list)
    for i in range(size):
        filled_list.append(-i-1)

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
    append_value = []
    additional_class = 0
    additional_count = 0
    for cset in csets:
        for n1 in cset:
            curr = n1
            data_set.append(curr)
            for n2 in cset:
                curr = n2
                data_set.append(curr)
                for n3 in cset:
                    curr = n3
                    data_set.append(curr)
                    for n4 in cset:
                        curr = n4
                        data_set.append(curr)
                        for n5 in cset:
                            curr = n5
                            data_set.append(curr)
                            for n6 in cset:
                                curr = n6
                                data_set.append(curr)
                                xtrue.append(data_set.copy())
                                for x in cset:
                                    if(cset.count(x) == data_set.count(x)):
                                        append_value = ysets[index]
                                    else:
                                        if(additional_count%6 == 0):
                                            additional_class -=1
                                        append_value = [additional_class]
                                        additional_count -= 1
                                        break
                                    ytrue.append(append_value.copy())
                                data_set.pop()
                            data_set.pop()
                        data_set.pop()
                    data_set.pop()
                data_set.pop()
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



rsets.append([0]) # дописываем 0
dsets.append([0]) # дописываем 0
dsets_copy = dsets.copy()
xsets, ysets = get_unmarked_pairs(dsets, rsets) # немаркированные данные 
# dsets.pop()
# rsets.pop(0)
# print('9:', ysets.count([9]))
# print('2:', ysets.count([2]))


dsets.clear()
for dset in dsets_copy:
    dsets.append(fill_negative(dset)) # добываем каждый сет отрицательными числами



xtrue, ytrue = get_main_pairs(dsets, rsets) # получаем правильные данные
for x, y in zip(xtrue, ytrue):
    print(y, 'true', x)
print('9:', ytrue.count([9]))
print('2:', ytrue.count([2]))
print('0:', ytrue.count([0]))

# print('-1:', ytrue.count([-1]))
# xtrue_copy = []
# for xt in xtrue:
#     xtrue_copy.append(fill_zeros(xt))
# xtrue = xtrue_copy.copy()








xtrain, ytrain = mark_data(xsets, ysets, xtrue, ytrue)
for x, y in zip(xtrain, ytrain):
    print(y, 'train', x)
print('9:', ytrain.count([9]))
print('2:', ytrain.count([2]))
print('0:', ytrain.count([0]))
# print('size:', len(ytrain))
# # print()