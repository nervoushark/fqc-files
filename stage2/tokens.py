import pymorphy2
from keras.preprocessing.text import Tokenizer
import numpy as np 
import re

def get_normal_forms(words_sequence, size = 3):
    words_normilized = np.array([])
    morph_analyzer = pymorphy2.MorphAnalyzer()
    words = np.array(re.split('\W+', words_sequence))
    for word in words:
        forms = morph_analyzer.parse(word.lower())
        tag = forms[0].tag.POS if(forms[0].tag.POS) else ""
        words_normilized = np.append(words_normilized, forms[0].normal_form+tag)
    wn_count = words_normilized.size
    for i in range(size - wn_count):
        words_normilized = np.append(words_normilized, "0")
    # words_normilized = np.resize(words_normilized, size)
    print("wn: ", words_normilized)
    print("size: ", words_normilized.size, "size//2: ", words_normilized.size//3)
    words_normilized = np.reshape(words_normilized, (words_normilized.size//3, -1))
    return words_normilized




def make_tokens(words_arr):
    # создаем единый словарь (слово -> число) для преобразования
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(words_arr.tolist())
    text_sequences = tokenizer.texts_to_sequences(words_arr.tolist())
    print("text_sequences: ", text_sequences)
    return text_sequences

def get_association(word):
    pass

def gen_train_sets(tokens, categories, size=3):
    x_train = []
    y_train = []

    for token in tokens:
        x_train.append()


# def get_normal_forms(words_sequence, size = 3):
#     words_normilized = np.array([])
#     morph_analyzer = pymorphy2.MorphAnalyzer()
#     words = np.array(re.split('\W+', words_sequence))

#     for word in words:
#         forms = morph_analyzer.parse(word.lower())
#         tag = forms[0].tag.POS if(forms[0].tag.POS) else ""
#         words_normilized = np.append(words_normilized, forms[0].normal_form+tag)

#     wn_count = words_normilized.size
#     for i in range(size - wn_count):
#         words_normilized = np.append(words_normilized, "")

#     words_normilized = np.resize(words_normilized, size)
#     return words_normilized

if __name__ == '__main__':
    descriptions = ["привет, hi", "успехов gl", "ремонтами plz", "успехов gl2"]
    nf = np.array([])
    for descr in descriptions:
        nf = np.append(nf, get_normal_forms(descr))
    # nf = get_normal_forms(descriptions)
    # nf = np.reshape(nf, (nf.size//3,-1))
    print(nf)
    tok = make_tokens(nf)
    print("tok: ", tok)

    tok2 = [0 if val == "" else val for val in tok]
    print("tok:2 ", tok2)
    
    tok = np.reshape(tok, -1)
    # tok = np.reshape(tok, (,-1))
    print("tok reshape: ", tok)

    tok = np.reshape(tok, (nf.size//3, -1))
    # tok = np.reshape(tok, (,-1))
    print("tok reshape:\n", tok)
    print("tok reshape:\n", tok[0].take([1,2,0]))
    tok3.insert(0, tok3.pop())
    # descriptions = np.append(descriptions, "asdasd");
    # descriptions = np.delete(descriptions, np.where(descriptions == "привет, gj"));

    











    # print("descriptions.tolist(): ", descriptions.tolist())

    # Преобразуем все описания в числовые последовательности, заменяя слова на числа по словарю.

    # print("textSequences: ", textSequences)