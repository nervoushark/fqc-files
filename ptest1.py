

import numpy as np


max_size = 3
dsets = [[0], [1, 2, 3]]
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

for filled_dset in filled_dsets:
    for n1 in filled_dset:
        xset0.append(n1)
        for n2 in filled_dset:
            if(n1 == n2):
                continue
            xset0.append(n2)
            for n3 in filled_dset:
                if(n1 == n3 or n2 == n3):
                    continue
                xset0.append(n3)
                xtrue.append(xset0)
                ytrue.append(rsets[index])
                print(xset0, ytrue[-1])
                xset0.pop()
            xset0.pop()
        xset0.pop()
    index+=1

# for filled_dset in filled_dsets:
#     for n1 in filled_dset:
#         xset0.append(n1)
#         for n2 in filled_dset:
#             if(n1 == n2):
#                 continue
#             xset0.append(n2)
#             for n3 in filled_dset:
#                 if(n1 == n3 or n2 == n3):
#                     continue
#                 xset0.append(n3)
#                 for n4 in filled_dset:
#                     if(n1 == n4 or n2 == n4 or n3 == n4):
#                         continue
#                     xset0.append(n4)
#                     for n5 in filled_dset:
#                         if(n1 == n5 or n2 == n5 or n3 == n5 or n4 == n5):
#                             continue
#                         xset0.append(n5)
#                         for n6 in filled_dset:
#                             if(n1 == n6 or n2 == n6 or n3 == n6 or n4 == n6 or n5 == n6):
#                                 continue
#                             xset0.append(n6)
#                             xtrue.append(xset0)
#                             ytrue.append(rsets[index])
#                             print(xset0, ytrue[-1])
#                             xset0.pop()
#                         xset0.pop()
#                     xset0.pop()
#                 xset0.pop()
#             xset0.pop()
#         xset0.pop()
#     index+=1


dset = []
for i in dsets:
    dset.extend(i)

count = len(dset)

res = []
xset = []
yset = []
xset1 = []


# for n1 in dset:
#     xset1.append(n1)
#     for n2 in dset:
#         xset1.append(n2)
#         for n3 in dset:
#             xset1.append(n3)
#             for n4 in dset:
#                 xset1.append(n4)
#                 for n5 in dset:
#                     xset1.append(n5)
#                     for n6 in dset:
#                         xset1.append(n6)
#                         xset.append(xset1)
#                         yset.append([0])
#                         print(xset1, [0])
#                         xset1.pop()
#                     xset1.pop()
#                 xset1.pop()
#             xset1.pop()
#         xset1.pop()
#     xset1.pop()



# for j in dset:
#     for i in dset:
#         res.append(i)
#         xset.append()
#     dset.insert(0, dset.pop())

# print("dset:", dset, '\n')
# print("res:", res, '\n')
# print("np.array(res).reshape((-1, len(dset))):\n", np.array(res).reshape((-1, len(dset))))
# print("np.array(res).reshape((-1, len(dsets[0]))):\n", np.array(res).reshape((-1, len(dsets[-1]))))



# print("np.array(res).reshape((-1, len(dset))):\n", np.array(res).reshape((-1, len(dset))))

# prin