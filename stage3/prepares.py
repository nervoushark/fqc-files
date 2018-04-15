import numpy as np
max_size = 4



def fill_zeros(input_list, size=max_size):
    filled_list = input_list.copy()
    size = max_size - len(input_list)
    for i in range(size):
        filled_list.append(0)
    # print("filled:", filled_list)
    return filled_list

def fill_negative(input_list, size=max_size):
    filled_list = input_list.copy()
    size = max_size - len(input_list)
    for i in range(size):
        filled_list.append(-i-1)
    return filled_list

def max_iterations():
    max_iterator = 1
    for i in range(max_size):
        max_iterator *= (i+1)
    return max_iterator

def get_data(xsets, ysets=[]):
    xres = []
    yres = []
    additional_class = -100
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

    data_set = []
    category = []
    # index = 0
    lvl = 0
    for n1 in vocabulary:
        curr = n1
        if(lvl < max_size):
            data_set.append(curr)
        lvl+=1
        for n2 in vocabulary:
            curr = n2
            if(lvl < max_size):
                data_set.append(curr)
            lvl+=1
            for n3 in vocabulary:
                curr = n3
                if(lvl < max_size):
                    data_set.append(curr)
                lvl+=1
                for n4 in vocabulary:
                    curr = n4
                    if(lvl < max_size):
                        data_set.append(curr)
                    lvl+=1
                    for n5 in vocabulary:
                        curr = n5
                        if(lvl < max_size):
                            data_set.append(curr)
                        lvl+=1
                        for n6 in vocabulary:
                            curr = n6
                            if(lvl < max_size):
                                data_set.append(curr)
                            lvl+=1
                            # print("data_set:", data_set)
                            #############################
                            for xset, yset in zip(xsets, ysets):
                                # print("\txset:", xset)
                                for x in xset:
                                    # print('\t\tx', x, "in xset: ", xset.count(x), "in ds:", data_set.count(x), "???", xset.count(x)==data_set.count(x))
                                    if(xset.count(x)==data_set.count(x)):
                                        category = yset
                                    else:
                                        # print("noooooooooooooooooo")
                                        category = [additional_class]
                                        break
                                if(category != [additional_class]):
                                    break


                            if(category == [additional_class]):
                                additional_count-=1
                                additional_class = additional_count // 720
                            xres.append(data_set.copy())
                            yres.append(category.copy())
                            # additional_class
                            lvl-=1
                            if(lvl < max_size):
                                data_set.pop()
                        lvl-=1
                        if(lvl < max_size):
                            data_set.pop()
                    lvl-=1
                    if(lvl < max_size):
                        data_set.pop()
                lvl-=1
                if(lvl < max_size):
                    data_set.pop()
            lvl-=1
            if(lvl < max_size):
                data_set.pop()
        lvl-=1
        if(lvl < max_size):
            data_set.pop()

    return xres, yres

if __name__ == '__main__':
    # dsets = [[1, 2], [3], [50], [50,1]]
    # rsets = [[1], [2], [3], [4]]
    dsets = [[1, 2], [3]]
    rsets = [[1], [2]]
    max_iterator = max_iterations()
    print("max_iterations", max_iterator)

    dsets.insert(0, [0])
    rsets.insert(0, [0])

    dsets_copy = dsets.copy()
    dsets_test = []
    dsets.clear()
    for dset in dsets_copy:
        dsets.append(fill_negative(dset))
        dsets_test.append(fill_zeros(dset))

    x_train, y_train = get_data(dsets, rsets)

    categories = np.unique(np.array(y_train))
    for category in categories:
        print(category, "~", y_train.count(category))


    for x,y in zip(x_train, y_train):
        print(y, "--->", x)