import numpy as np

max_size = 6
def fill_zeros(list1, size):
    filled_dsets = []

dsets = [[0], [1, 2, 3]]
# dsets = [[0], [1,2]]
rsets = [[0], [2]]

# дополняем списки
filled_dsets = []
for dset in dsets:
    diff = max_size - len(dset)
    # print("diff:", diff)
    new_dset = dset.copy()
    new_dset.extend([0]*diff)
    # print("new_dset:", new_dset)
    filled_dsets.append(new_dset)
print("filled_dsets:", filled_dsets)

# генерируем все возможные "правильные" комбо
xset0 = []
xtrue = []
ytrue = []
index = 0
level = 0
skip = 0
curr = 0
csets = dsets.copy()

for cset in csets:
    clen = len(cset)
    if(level >= clen):
        skip = 1
    for n1 in cset:
        curr = n1
        if(skip-1):
            xset0.append(curr)
            # print("insert:", curr, "lvl:", level)
        level+=1
        if(level >= clen):
            skip = 1
        #
        for n2 in cset:
            curr = n2
            if(skip-1):
                xset0.append(curr)
                # print("insert:", curr, "lvl:", level)
            level+=1
            if(level >= clen):
                skip = 1
            #
            for n3 in cset:
                curr = n3
                if(skip-1):
                    xset0.append(curr)
                    # print("insert:", curr, "lvl:", level)
                level+=1
                if(level >= clen):
                    skip = 1
                #
                for n4 in cset:
                    curr = n4
                    if(skip-1):
                        xset0.append(curr)
                        # print("insert:", curr, "lvl:", level)
                    level+=1
                    if(level >= clen):
                        skip = 1
                    #
                    for n5 in cset:
                        curr = n5
                        if(skip-1):
                            xset0.append(curr)
                            # print("insert:", curr, "lvl:", level)
                        level+=1
                        if(level >= clen):
                            skip = 1
                        #
                        for n6 in cset:
                            curr = n6
                            if(skip-1):
                                xset0.append(curr)
                                # print("insert:", curr, "lvl:", level)
                                level+=1
                            skip = 0
                            if(xset0 not in xtrue):
                                for res in xset0:
                                    if(xset0.count(res) == 1):
                                        skip = 0
                                    else:
                                        skip = 1
                                if(skip-1):
                                    xtrue.append(xset0.copy())
                                    ytrue.append(rsets[index])
                                    print(xset0, ytrue[-1])
                            level = 0
                            skip = 0
                            if(len(xset0)>0):
                                xset0.pop()
                        if(len(xset0)>0):
                            xset0.pop()
                    if(len(xset0)>0):
                        xset0.pop()
                if(len(xset0)>0):
                    xset0.pop()
            if(len(xset0)>0):
                xset0.pop()
        if(len(xset0)>0):
            xset0.pop()
    index+=1

print('\n\n\n')
print(xtrue)
print("clen:", clen)
print(csets)
dset = []
for i in dsets:
    dset.extend(i)

count = len(dset)


# тренировочная выборка
res = []
xset = []
yset = []
xset1 = []
xtrain = []
index = 0
# for filled_dset in filled_dsets:
#     for n1 in filled_dset:
#         curr = n1
#         xset0.append(curr)
#         for n2 in filled_dset:
#             curr = n2
#             xset0.append(curr)
#             for n3 in filled_dset:
#                 curr = n3
#                 xset0.append(curr)
#                 for n4 in filled_dset:
#                     curr = n4
#                     xset0.append(curr)
#                     for n5 in filled_dset:
#                         curr = n5
#                         xset0.append(curr)
#                         for n6 in filled_dset:
#                             curr = n6
#                             xset0.append(curr)
#                             xtrain.append(xset0.copy())
#                             ytrue.append(rsets[index])
#                             print(xset0, ytrue[-1])
#                             xset0.pop()
#                         xset0.pop()
#                     xset0.pop()
#                 xset0.pop()
#             xset0.pop()
#         xset0.pop()
#     index+=1


for n1 in dset:
    xset1.append(n1)
    for n2 in dset:
        xset1.append(n2)
        for n3 in dset:
            xset1.append(n3)
            for n4 in dset:
                xset1.append(n4)
                for n5 in dset:
                    xset1.append(n5)
                    for n6 in dset:
                        xset1.append(n6)
                        xtrain.append(xset1.copy())
                        yset.append([0])
                        print(xset1, [0])
                        xset1.pop()
                    xset1.pop()
                xset1.pop()
            xset1.pop()
        xset1.pop()
    xset1.pop()


# print("dset:", dset, '\n')
# print("xtrain:", xtrain, '\n')
# print("np.array(xtrain).reshape((-1, max_length)):\n", np.array(xtrain).reshape((-1, max_size)))
# print("np.array(xtrain).reshape((-1, len(dsets[0]))):\n", np.array(xtrain).reshape((-1, max_size)))



# print("np.array(res).reshape((-1, len(dset))):\n", np.array(res).reshape((-1, len(dset))))

# prin