import numpy as np

max_size = 6
# dsets = [[2]]
# rsets = [[2]]

dsets = [[1, 2], [3]]
rsets = [[1], [2]]


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

def max_iterations():
    max_iterator = 1

    # vocabulary = []
    # for dset in dsets:
    #     vocabulary.extend(i)

    # vocabulary = np.unique(np.array(vocabulary))


    for i in range(max_size):
        max_iterator *= (i+1)
    return max_iterator

max_iterator = max_iterations()
# fill_zeros(dsets, max_size)

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


                            if(category != [additional_class]):
                                xres.append(data_set.copy())
                                yres.append(category.copy())
                                # print("y:", yres[-1], "x:", xres[-1])

                            # if(category == [additional_class]):
                            #     additional_count-=1
                            #     additional_class = additional_count // max_iterator
                            # print("xres:", xres[-1], "yres:", yres[-1])
                            # print("\tcategory", category, '\n')
                            # print("i'm ok")
                            ############################
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

    # for key in vocabulary:

    # for x in vocabulary:
        # print(x)
    # print(vocabulary)

    return xres, yres



    
dsets.insert(0, [0])
rsets.insert(0, [0])

dsets_copy = dsets.copy()
dsets.clear()
for dset in dsets_copy:
    dsets.append(fill_negative(dset))
    # dsets.append(fill_zeros(dset))


x_train, y_train = get_data(dsets, rsets)

xt = []
data_set = []
for x in x_train:
    xt = [t if t > 0 else 0 for t in x]
    data_set.append(xt)
# categories = np.unique(np.array(y_train))
# for category in categories:
#     print(category, y_train.count(category))

x_train = data_set.copy()





x_train = np.array(x_train)
y_train = np.array(y_train)

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

dropout_rate = 0.05
nb_classes = len(rsets)+1
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
          epochs=100,
          batch_size=2000)

x_test = np.array([[5,0,0,0,0,0]])
print("prediction: ", model.predict_classes(x_test))