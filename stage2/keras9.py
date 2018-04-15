# пытаемся в инс
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.utils import to_categorical
from keras.optimizers import SGD
# import tokens
# Generate dummy data
import numpy as np

# последовательная модель
model = Sequential()

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

dropout_rate = 0.05
nb_classes = 11
# похуй, пляшем
# 3 на вход, 24 на выходе 
model.add(Dense(25, input_dim=3, activation='tanh'))
# для предотвращения переобучения, как работает хз
model.add(Dropout(dropout_rate))
model.add(Dense(11, activation='tanh'))
model.add(Dropout(dropout_rate))
# для многоклассовой классификации 
model.add(Dense(nb_classes, activation='softplus'))


x_train = np.array([
    [100, 100, 100], 
    [100, 100, 100], 
    [100, 100, 100], 
    [100, 100, 50], 
    [100, 50, 100], 
    [50, 100, 100], 
    [100, 100, 30], 
    [100, 30, 100], 
    [30, 100, 100], 
    [100, 100, 20], 
    [100, 20, 100], 
    [20, 100, 100], 
    [50, 50, 100], 
    [50, 100, 50], 
    [100, 50, 50], 
    [50, 50, 50], 
    [50, 50, 50], 
    [50, 50, 50], 
    [50, 50, 30], 
    [50, 30, 50], 
    [30, 50, 50], 
    [50, 50, 20], 
    [50, 20, 50], 
    [20, 50, 50], 
    [30, 30, 100], 
    [30, 100, 30], 
    [100, 30, 30], 
    [30, 30, 50], 
    [30, 50, 30], 
    [50, 30, 30], 
    [30, 30, 30], 
    [30, 30, 30], 
    [30, 30, 30], 
    [30, 30, 20], 
    [30, 20, 30], 
    [20, 30, 30], 
    [20, 20, 100], 
    [20, 100, 20], 
    [100, 20, 20], 
    [20, 20, 50], 
    [20, 50, 20], 
    [50, 20, 20], 
    [20, 20, 30], 
    [20, 30, 20], 
    [30, 20, 20], 
    [20, 20, 20], 
    [20, 20, 20], 
    [20, 20, 20]
    ])
y_train = np.array([
       [10],
       [10],
       [10],
       [10],
       [10],
       [10],
       [10],
       [10],
       [10],
       [10],
       [10],
       [10],
       [5],
       [5],
       [5],
       [5],
       [5],
       [5],
       [5],
       [5],
       [5],
       [5],
       [5],
       [5],
       [3],
       [3],
       [3],
       [3],
       [3],
       [3],
       [3],
       [3],
       [3],
       [3],
       [3],
       [3],
       [2],
       [2],
       [2],
       [2],
       [2],
       [2],
       [2],
       [2],
       [2],
       [2],
       [2],
       [2]
    ])
# y_test = np.array([[10], [10], [10], [10], [10], [10], [10]])

# переводим в категории

Y_train = to_categorical(y_train, nb_classes)
# Y_test = to_categorical(y_test, nb_classes)



# где то здесь должна быть компиляция и обучение и блэкджек
sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

model.fit(x_train, Y_train,
          epochs=6000,
          batch_size=2000)

# print(model.predict(x_test, batch_size=1))
# print(model.predict_classes(np.array([[100, 100, 20]])))

# print(model.predict_classes(x_test))



# model.fit(x_train, Y_train,
#           epochs=6000,
#           batch_size=150)


# тестовая, для обученной сети
# x_test = np.array([[100, 100, 20], [20, 50, 20], [100, 50, 50], [30, 30, 50]])
# y_test = np.array([[1], [2], [5], [3]])
# x_test = np.array([[100, 100, 20], [100, 100, 30], [100, 100, 50], [20, 100, 100], [30, 100, 100], [50, 100, 100], [100, 100, 100]])
x_test = np.array([[20, 20, 20], [20, 20, 100], [20, 20, 30], [20, 20, 50], [100, 20, 20], [20, 30, 20], [20, 50, 20]])
print(model.predict_classes(x_test))
x_test = np.array([[30, 30, 30], [30, 30, 20], [30, 30, 100], [30, 30, 50], [20, 30, 30], [30, 100, 30], [30, 50, 30]])
print(model.predict_classes(x_test))
x_test = np.array([[50, 50, 50], [50, 50, 20], [50, 50, 30], [50, 50, 100], [20, 50, 50], [50, 30, 50], [50, 100, 50]])
print(model.predict_classes(x_test))
x_test = np.array([[100, 20, 100], [100, 100, 20], [100, 100, 30], [20, 100, 100], [20, 100, 100], [100, 30, 100], [100, 50, 100]])
print(model.predict_classes(x_test))


# x_test = np.array([
#     [ 20,  20,  20],
#     [ 20,  20,  30],
#     [ 20,  20,  50],
#     [ 20,  20, 100],
#     [ 20,  30,  20],
#     [ 20,  30,  30],
#     [ 20,  50,  20],
#     [ 20,  50,  50],
#     [ 20, 100,  20],
#     [ 20, 100, 100],
#     [ 30,  20,  20],
#     [ 30,  20,  30],
#     [ 30,  30,  20],
#     [ 30,  30,  30],
#     [ 30,  30,  50],
#     [ 30,  30, 100],
#     [ 30,  50,  30],
#     [ 30,  50,  50],
#     [ 30, 100,  30],
#     [ 30, 100, 100],
#     [ 50,  20,  20],
#     [ 50,  20,  50],
#     [ 50,  30,  30],
#     [ 50,  30,  50],
#     [ 50,  50,  20],
#     [ 50,  50,  30],
#     [ 50,  50,  50],
#     [ 50,  50, 100],
#     [ 50, 100,  50],
#     [ 50, 100, 100],
#     [100,  20,  20],
#     [100,  20, 100],
#     [100,  30,  30],
#     [100,  30, 100],
#     [100,  50,  50],
#     [100,  50, 100],
#     [100, 100,  20],
#     [100, 100,  30],
#     [100, 100,  50],
#     [100, 100, 100]
#     ])
x_test = np.array([
[100, 100, 100], 
[100, 100, 100], 
[100, 100, 100], 
[100, 100, 50], 
[100, 50, 100], 
[50, 100, 100], 
[100, 100, 30], 
[100, 30, 100], 
[30, 100, 100], 
[100, 100, 20], 
[100, 20, 100], 
[20, 100, 100], 
[50, 50, 100], 
[50, 100, 50], 
[100, 50, 50], 
[50, 50, 50], 
[50, 50, 50], 
[50, 50, 50], 
[50, 50, 30], 
[50, 30, 50], 
[30, 50, 50], 
[50, 50, 20], 
[50, 20, 50], 
[20, 50, 50], 
[30, 30, 100], 
[30, 100, 30], 
[100, 30, 30], 
[30, 30, 50], 
[30, 50, 30], 
[50, 30, 30], 
[30, 30, 30], 
[30, 30, 30], 
[30, 30, 30], 
[30, 30, 20], 
[30, 20, 30], 
[20, 30, 30], 
[20, 20, 100], 
[20, 100, 20], 
[100, 20, 20], 
[20, 20, 50], 
[20, 50, 20], 
[50, 20, 20], 
[20, 20, 30], 
[20, 30, 20], 
[30, 20, 20], 
[20, 20, 20], 
[20, 20, 20], 
[20, 20, 20]
    ])
print()
c = 144/3/4+1
d = 0
print(model.predict_classes(x_test)[0:12])
print(model.predict_classes(x_test)[12:24])
print(model.predict_classes(x_test)[24:36])
print(model.predict_classes(x_test)[36:48])