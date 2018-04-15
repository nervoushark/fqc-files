import numpy as np

max_size = 6
dsets = [
    [1,2], 
    [1,3], 
    [4,5], 
    [6,7,8], 
    [9]
]
rsets = [
    [1], 
    [2], 
    [3], 
    [5], 
    [6]
]

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


# генерим данные, тупо для трени харкдодом забиваем потом в текст проги
xsets, ysets = get_unmarked_pairs(dsets, rsets)
    
xtrue, ytrue = get_main_pairs(dsets, rsets)

xtrue_copy = []
for xt in xtrue:
    xtrue_copy.append(fill_zeros(xt))
xtrue = xtrue_copy.copy()

xtrain, ytrain = mark_data(xsets, ysets, xtrue, ytrue)
print('Mark data complete')
x_train = np.array(xtrain)
y_train = np.array(ytrain)
print(x_train)
# print("train X:\n", xtrain)
# print("train Y:\n", ytrain)
# for x, y in zip(xtrain, ytrain):
#     print(y, "train:", x)

# for x in xtrain:
    # print(x)
####################################################################################################################################################################
# пытаемся в инс
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.utils import to_categorical
from keras.optimizers import SGD
# import tokens
# Generate dummy data
# import numpy as np

# последовательная модель
model = Sequential()

####################################################################################################################################################################
# Dense реализует операцию:  output = activation(dot(input, kernel) + bias)
# Форма ввода: Произвольное. Используйте аргумент ключевого слова input_shape (кортеж целых чисел, не включает ось выборки) при использовании этого слоя в качестве первого слоя в модели.
# Форма вывода: Такая же форма, как и вход.
# Dense(
#     units,                                    положительное целое число, размерность выходного пространства.
#     activation=None,                          функцию активации
#     use_bias=True,                            Boolean, использует ли слой вектор смещения.
#     kernel_initializer='glorot_uniform',      Инициализатор для kernelматрицы весов
#     bias_initializer='zeros',
#     kernel_regularizer=None,
#     bias_regularizer=None,
#     activity_regularizer=None,
#     kernel_constraint=None,
#     bias_constraint=None)
# ex:
# model = Sequential()
# model.add(Dense(12, input_dim=8, init='uniform', activation='relu'))
# model.add(Dense(8, init='uniform', activation='relu'))
# model.add(Dense(1, init='uniform', activation='sigmoid'))
####################################################################################################################################################################

dropout_rate = 0.5
nb_classes = 7
# похуй, пляшем
# 3 на вход, 24 на выходе 
model.add(Dense(20, input_dim=max_size, activation='tanh'))
# для предотвращения переобучения, как работает хз
model.add(Dropout(dropout_rate))
model.add(Dense(25, activation='tanh'))
model.add(Dropout(dropout_rate))
# для многоклассовой классификации 
model.add(Dense(nb_classes, activation='softplus'))



# переводим в категории

Y_train = to_categorical(y_train, nb_classes)
# Y_test = to_categorical(y_test, nb_classes)



# где то здесь должна быть компиляция и обучение и блэкджек
sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

model.fit(x_train, Y_train,
          epochs=6,
          batch_size=20000)

x_test = np.array([[6,7,8,0,0,0], [0,0,0,0,0,0], [1,2,0,0,0,0], [1,3,0,0,0,0], [4,5,0,0,0,0]])
print("prediction: ", model.predict_classes(x_test))