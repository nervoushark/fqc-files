import numpy as np

max_size = 6
dsets = [[1, 2], [2]]
rsets = [[12], [2]]

def fill_zeros(input_list, size=max_size):
    filled_list = input_list.copy()
    size = max_size - len(input_list)
    for i in range(size):
        filled_list.append(0)
    print("filled:", filled_list)
    return filled_list

def fill_negative(input_list, size=max_size):
    filled_list = input_list.copy()
    size = max_size - len(input_list)
    for i in range(size):
        filled_list.append(-i-1)

    return filled_list


# fill_zeros(dsets, max_size)

def get_data(xsets, ysets=[]):
    xres = np.array([], dtype = int)
    yres = np.array([], dtype = int)
    additional_class = 0
    additional_count = 0
    ######################################
    vocabulary = [] # все возможные ключи
    for i in xsets:
        vocabulary.extend(i)

    print("raw voc:", vocabulary)
    vocabulary = np.array(vocabulary)
    print("vocabulary:", np.unique(vocabulary), '\n')
    vocabulary = np.unique(vocabulary)
    ######################################

    data_set = np.array([], dtype = int)
    category = []
    # index = 0
    for n1 in vocabulary:
        curr = n1
        # data_set.append(curr)
        data_set = np.append(data_set, curr)
        for n2 in vocabulary:
            curr = n2
            # data_set.append(curr)
            data_set = np.append(data_set, curr)
            for n3 in vocabulary:
                curr = n3
                # data_set.append(curr)
                data_set = np.append(data_set, curr)
                for n4 in vocabulary:
                    curr = n4
                    # data_set.append(curr)
                    data_set = np.append(data_set, curr)
                    for n5 in vocabulary:
                        curr = n5
                        # data_set.append(curr)
                        data_set = np.append(data_set, curr)
                        for n6 in vocabulary:
                            curr = n6
                            # data_set.append(curr)
                            data_set = np.append(data_set, curr)
                            # print("data_set:", data_set)
                            #############################
                            for xset, yset in zip(xsets, ysets):
                                # print("\txset:", xset)
                                for x in xset:
                                    # print('\t\tx', x, "in xset: ", xset.count(x), "in ds:", data_set.count(x), "???", xset.count(x)==data_set.count(x))
                                    if(np.count_nonzero(xset == x) == np.count_nonzero(data_set == x)):
                                        category = yset
                                    else:
                                        # print("noooooooooooooooooo")
                                        category = [additional_class]
                                        break
                                if(category != [additional_class]):
                                    break
                            xres = np.concatenate((xres, data_set), axis = 0)
                            yres = np.concatenate((yres, np.array(category)), axis = 0)

                            if(category == [additional_class]):
                                additional_count-=1
                                additional_class = additional_count // 720
                                    
                            # print("xres:", xres[-1], "yres:", yres[-1])
                            # print("\tcategory", category, '\n')
                            # print("i'm ok")
                            ############################
                            data_set = np.delete(data_set, -1)
                        data_set = np.delete(data_set, -1)
                    data_set = np.delete(data_set, -1)
                data_set = np.delete(data_set, -1)
            data_set = np.delete(data_set, -1)
        data_set = np.delete(data_set, -1)

    # for key in vocabulary:

    # for x in vocabulary:
        # print(x)
    # print(vocabulary)

    return xres, yres
dsets.insert(0, [0])
rsets.insert(0, [-1])

dsets_copy = dsets.copy()
dsets.clear()
for dset in dsets_copy:
    dsets.append(fill_negative(dset))
    # dsets.append(fill_zeros(dset))


xdata, ydata = get_data(dsets, rsets)

# for category in rsets:
    # print(category, ydata.count(category))
# print("0", ydata.count([0]))

categories = np.unique(np.array(ydata))
for category in categories:
    print(category, np.count_nonzero(ydata == category))
