# пример использования преобразования к категориям
import numpy
from keras.datasets import cifar10
from keras.utils import to_categorical
# Задаем seed для повторяемости результатов
numpy.random.seed(42)

# Загружаем данные
(X_train, y_train), (X_test, y_test) = cifar10.load_data()
# Размер мини-выборки
batch_size = 32
# Количество классов изображений
nb_classes = 10
# Количество эпох для обучения
nb_epoch = 25
# Размер изображений
img_rows, img_cols = 32, 32
# Количество каналов в изображении: RGB
img_channels = 3

# Нормализуем данные
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255

# Преобразуем метки в категории
Y_train = to_categorical(y_train, nb_classes)
Y_test = to_categorical(y_test, nb_classes)

print("y: ", type(y_train))
print("Y: ", Y_train)

# y:  
#  [[6]
#  [9]
#  [9]
#  ...
#  [9]
#  [1]
#  [1]]
# Y:  
#  [[0. 0. 0. ... 0. 0. 0.]
#  [0. 0. 0. ... 0. 0. 1.]
#  [0. 0. 0. ... 0. 0. 1.]
#  ...
#  [0. 0. 0. ... 0. 0. 1.]
#  [0. 1. 0. ... 0. 0. 0.]
#  [0. 1. 0. ... 0. 0. 0.]]
