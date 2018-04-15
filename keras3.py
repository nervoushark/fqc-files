from keras.preprocessing.text import Tokenizer
import numpy as np

# descriptions = np.array(["привет", "успех", "ремонт"])

# # создаем единый словарь (слово -> число) для преобразования
# tokenizer = Tokenizer()
# tokenizer.fit_on_texts(descriptions.tolist())

# # Преобразуем все описания в числовые последовательности, заменяя слова на числа по словарю.
# textSequences = tokenizer.texts_to_sequences(descriptions.tolist())

# print("textSequences: ", textSequences)

# # tokenize text



from keras.datasets import imdb 

# Keras Data Sets
(x_train4, y_train4), (x_test4, y_test4) = imdb.load_data(num_words = 20)
# print(x_train4.length)

from keras.preprocessing import sequence
x_train4 = sequence.pad_sequences(x_train4,maxlen=80)
x_test4 = sequence.pad_sequences(x_test4,maxlen=80)
print(x_train4)
print(y_train4)


# from keras.models import Sequential
# from keras.layers import Embedding, LSTM, Dense, Activation

# # Model Architecture
# model3 = Sequential()
# model3.add(Embedding(200,64))
# model3.add(LSTM(64,dropout=0.2,recurrent_dropout=0.2))
# model3.add(Dense(1,activation='sigmoid'))


# print("model3.output_shape", model3.output_shape)
# print("model3.output_shape", model3.summary())
# print("model3.output_shape", model3.get_config())
# print("model3.output_shape", model3.get_weights())

# #  Compile Model
# model3.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy']) 
# # Model Training
# model3.fit(x_train4, y_train4, batch_size=32, epochs=5, verbose=1, validation_data=(x_test4,y_test4)) 

# score = model3.evaluate(x_test4, y_test4, batch_size=32)


# model3.predict(x_test4, batch_size=32)
# model3.predict_classes(x_test4,batch_size=32) 