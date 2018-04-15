import numpy as np


def gen():
    vals = [100, 50, 30, 20]
    results = [1, 5, 3, 2]
    x_train = []
    y_train = []
    cnt = 0
    for val in vals:
        for addval in vals:
            x_set = []
            y_set = []
            x_set.append(val)
            x_set.append(val)
            x_set.append(addval)        
            y_set.append(results[cnt])
            # print(x_set)
            # print(y_set)
            # x_set.append(x_set)
            x_train.append(x_set)
            y_train.append(y_set)

            x_set = []
            y_set = []
            x_set.append(val)
            x_set.append(addval)        
            x_set.append(val)
            y_set.append(results[cnt])
            # print(x_set)
            # print(y_set)
            # x_set.append(x_set)
            x_train.append(x_set)
            y_train.append(y_set)

            x_set = []
            y_set = []
            x_set.append(addval)        
            x_set.append(val)
            x_set.append(val)
            y_set.append(results[cnt])
            # print(x_set)
            # print(y_set)
            # x_set.append(x_set)
            x_train.append(x_set)
            y_train.append(y_set)
        cnt+=1
    # x_train = np.unique(np.array(x_train), axis = 0)
    # y_train = np.array(y_train)
    return x_train, y_train

def gen2():
    vals = [100, 50, 0]
    results = [1, 5, 0]
    x_train = []
    y_train = []
    # cnt = 0
    for val in vals:
        for addval in vals:
            for count in range(len(vals)):
                if(count!=0 and val == addval):
                    continue

                x_set = [val]*len(vals) # массив из повторяющихся элементов
                # y_set = [val]*len(vals)

                x_set[count] = addval
                x_train.append(x_set)
                if(x_set.count(0) or x_set.count(val) <= x_set.count(addval)):
                    y_train.append([0])
                elif(x_set.count(val) <= x_set.count(addval)):
                    y_train.append([results[count]])
            
                print(x_set, y_train[-1])
        print('len: ', len(x_train), '\n')
        # cnt+=1
    # x_train = np.unique(np.array(x_train), axis = 0)
    # y_train = np.array(y_train)
    return x_train, y_train

# def gen3():
#     dsets = [[0, 1, 10, 100], [0, 2, 20, 200]]
#     results = [0, 5, 10]
#     x_train = []
#     y_train = []
#     # cnt = 0
#     # for dset in dsets: # по массивам
#     #     for el in dset: # по элементам 
#     #         for addset in dsets: # по доп массивам
#     #             for addel in addset: # по элементам доп массива
#     #                 # for count in range(len(dsets)):
#     #                 x_set = [el]
#     #                 x_set = [0]*(len(dset)-1)
#     #                 x_set.insert(0, el)
#     #                 # x_set.insert()

#     #                 x_train.append(x_set)
#     #                 print(x_set)
#     #         print()

#     count = len(dsets[0])

#     for dset in dsets:
#         for count1 in range(count):
#             x_set = [0]*count
#             x_set.pop(count1)
#             xset = x_set.insert(count1-1, dset[count1])

#             for addset in dsets:
#                 for count2 in range(count):
#                     x_set.pop(count2)
#                     xset = x_set.insert(count2-1, addset[count2])

#                     for count3 in range(count):
#                         x_set.pop(count3)
#                         xset = x_set.insert(count3-1, addset[count3])
#                         x_train.extend(x_set)
#                         print("xs:", x_set)
#                 print()

#     xnp = np.unique(np.array(x_train), axis = 0)
#     print("x:", x_train)
#     print("xnp:", np.unique(np.array(x_train).reshape((-1, 4)), axis = 0))
#     return x_train, y_train

# # print(gen3()[0])
# gen3()
# print("end")


# def gen4():
dsets = [[1, 10, 100], [2, 20, 200]]
x_train = []
dset = []
for i in dsets:
    dset.extend(dsets)

count = len(dset)

res = []
for i in range(count):
    res.append(i)





for dset in dsets:


xnp = np.unique(np.array(x_train), axis = 0)
print("x:", x_train)
print("xnp:", np.unique(np.array(x_train).reshape((-1, 4)), axis = 0))
return x_train, y_train


# gen4()
# print("end")



# import numpy as np


# # dsets = [[0], [1, 2, 3], [4, 5, 6]]
# dsets = [[0], [1, 2, 3]]
# dset = []
# for i in dsets:
#     dset.extend(i)

# count = len(dset)

# res = []
# xset = []

# for j in dset:
#     for i in dset:
#         res.append(i)
#         xset.append()
#     dset.insert(0, dset.pop())

# print("dset:", dset, '\n')
# print("res:", res, '\n')
# print("np.array(res).reshape((-1, len(dset))):\n", np.array(res).reshape((-1, len(dset))))
# # print("np.array(res).reshape((-1, len(dsets[0]))):\n", np.array(res).reshape((-1, len(dsets[-1]))))

