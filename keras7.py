# пример использования преобразования к категориям
import numpy as np
from keras.utils import to_categorical

x_train4 = np.array([[100, 100, 100], [20, 20, 20], [50, 50, 50]])
y_train4 = np.array([[10], [20], [50]])

print(y_train4)

nb_classes = 51


# X_train4 = to_categorical(x_train4, nb_classes)
Y_train = to_categorical(y_train4, nb_classes)


print(Y_train)


# categorical_labels = to_categorical(int_labels, num_classes=None)