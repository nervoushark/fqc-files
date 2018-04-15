dropout_rate = 0.5
nb_classes = 6
# похуй, пляшем
# 3 на вход, 24 на выходе 
model.add(Dense(24, input_dim=3, activation='tanh'))
# для предотвращения переобучения, как работает хз
model.add(Dropout(dropout_rate))
# model.add(Dense(6, activation='tanh'))
# model.add(Dropout(dropout_rate))
# для многоклассовой классификации 
model.add(Dense(nb_classes, activation='softmax'))








sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

model.fit(x_train, Y_train,
          epochs=7000,
          batch_size=2000)