#!/usr/bin/env python3
# coding: utf-8

import sys
import gensim, logging

# Что вообще происходит?
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


# ----------------------------------------------
# Ниже демонстрируется процесс тренировки модели
# ----------------------------------------------
# на вход модели даём текстовый файл, каждое предложение на отдельной строчке
argument = 'text.txt'

# создаём структуру данных для модели
data = gensim.models.word2vec.LineSentence(argument)

# инициализируем модель (параметры в скобочках: data - данные, size - размер вектора, window -размер окна наблюдения,
#                                               min_count - мин. частотность слова в корпусе, которое мы берем,
#                                               sg - используемый алгоритм обучение (0 - CBOW, 1 - Skip-gram))
model = gensim.models.Word2Vec(data, size=500, window=10, min_count=2, sg=0)
# чтобы модель использовала меньше RAM (но теперь её нельзя менять!)
model.init_sims(replace=True)

# Смотрим, сколько в модели слов
print(len(model.vocab))

# сохраняем
model.save('my.model')

# ---------------------------------------------
# Ниже демонстрируется процесс работы с моделью
# ---------------------------------------------
# берём модель
our_model = 'some.model'

# загружаем модель
if our_model.endswith('.vec.gz'):
    model = gensim.models.Word2Vec.load_word2vec_format(our_model, binary=False)
elif m.endswith('.bin.gz'):
    model = gensim.models.Word2Vec.load_word2vec_format(our_model, binary=True)
else:
    model = gensim.models.Word2Vec.load(our_model)
# Чтобы модель требовала меньше RAM
model.init_sims(replace=True)

# скажем, нам интересны такие слова (пример для русского языка)
words = ['день', 'ночь', 'человек', 'семантика', 'студент']

# играем со словами
for word in words:
    # есть ли слово в модели? Может быть, и нет
    if word in model:
        print(word)
        # смотрим на вектор слова (его размерность 1000, смотрим на первые 10 чисел)
        print(model[word][:10])
        # выдаем 10 ближайших соседей слова:
        for i in model.most_similar(positive=[word], topn=10):
            # слово + коэффициент косинусной близости
            print(i[0], i[1])
        print('\n')
    else:
        # Увы!
        print(word + 'is not present in the model')

# находим косинусную близость пары слов
print(model.similarity('человек', 'обезьяна'))

# найди лишнее!
print(model.doesnt_match('яблоко груша виноград банан лимон картофель'.split()))

# реши пропорцию!
print(model.most_similar(positive=['женщина', 'король'], negative=['мужчина'])[0][0])

# Want to know more? Read API docs!
# http://radimrehurek.com/gensim/models/word2vec.html