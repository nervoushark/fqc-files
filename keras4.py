from keras.preprocessing.text import one_hot
from keras.preprocessing.text import text_to_word_sequence
# define the document
text = 'The quick brown fox jumped over the lazy dog.'
# estimate the size of the vocabulary
words = set(text_to_word_sequence(text)) #{'brown', 'over', 'the', 'lazy', 'jumped', 'fox', 'dog', 'quick'}
vocab_size = len(words)
print(vocab_size)
# integer encode the document
result = one_hot(text, round(vocab_size*1.3))
print(result)

print()

# from keras.preprocessing.text import Tokenizer
# # define 5 documents
docs = ['Well done!',
        'Good work',
        'Great effort',
        'nice work',
        'Excellent!']
# # create the tokenizer
# t = Tokenizer()
# # fit the tokenizer on the documents
# t.fit_on_texts(docs)

# # print(t)
# # summarize what was learned
# print('counts: ', t.word_counts)
# print('document_count: ', t.document_count)
# print('word_index: ', t.word_index)
# print('word_docs: ', t.word_docs)




# 
# one_hot(str(docs), 20)
# docs = [[10, 1], [19, 1], [2, 10], [9, 14], [2, 18], [19, 0]]
# resDocs = [[1], [2], [3], [4], [5], [6]]
