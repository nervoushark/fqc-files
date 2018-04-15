# docs = ['Well done!',
#         'Good work',
#         'Great effort',
#         'nice work',
#         'Excellent lol!']

# res = ['5' , '4' , '3', '2', '1'];


# from keras.preprocessing.text import Tokenizer
# # create the tokenizer
# t = Tokenizer()
# # fit the tokenizer on the documents
# t.fit_on_texts(docs)

import numpy as np
from keras.utils import to_categorical
# docs = np.array([[10, 1], [19, 1], [2, 10], [9, 14], [2, 18], [19, 0]])
# resDocs = np.array([[1], [2], [3], [4], [5], [6]])

# testDocs = np.array([[10, 1],   [19, 1], [2, 10], [9, 14], [2, 18], [19, 0], [10, 2], [19, 0], [1, 10], [8, 14], [3, 17], [17, 2], [10, 0], [18, 2], [2, 11], [9, 11], [2, 19], [19, 0]])
# testResDocs = np.array([[1],    [2], [3], [4], [5], [6], [1], [2], [3], [4], [5], [6], [1], [2], [3], [4], [5], [6]])

x_train4 = np.array([[100, 100, 100], [20, 20, 20], [50, 50, 50]])
y_train4 = np.array([[10], [20], [50]])


x_test4 = np.array([[100, 100, 100], [20, 20, 20], [50, 50, 50], [100, 100, 50]])
y_test4 = np.array([[10], [2], [5], [10]])

# x_train4 = to_categorical(x_train4)
# y_train4 = to_categorical(y_train4)
# x_test4 = to_categorical(x_test4)
# y_test4 = to_categorical(y_test4)


from keras.models import Sequential
from keras.layers import Embedding, LSTM, Dense, Activation


# Model Architecture
model3 = Sequential()
model3.add(Embedding(200,10))
model3.add(LSTM(10,dropout=0.1,recurrent_dropout=0.1))
# model3.add(Dense(1,activation='sigmoid'))
model3.add(Dense(1,activation='linear'))


#  Compile Model
model3.compile(loss='binary_crossentropy', optimizer='nadam', metrics=['accuracy']) 
# Model Training
model3.fit(x_train4, y_train4, batch_size=100, epochs=120, verbose=1, validation_data=(x_test4,y_test4)) 
# model3.fit(testResDocs, testResDocs, batch_size=2, epochs=5, verbose=1, validation_data=(docs,resDocs))

print('one moment...')
print(model3.predict(x_test4, batch_size=1))
print(model3.predict_classes(x_test4, batch_size=1))
print(model3.predict_on_batch(x_test4))


