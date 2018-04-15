import gensim
import pymorphy2

model = gensim.models.KeyedVectors.load_word2vec_format("ruscorpora_upos_skipgram_300_10_2017.bin.gz", binary=True, encoding='utf-8')
model.init_sims(replace=True)

morph = pymorphy2.MorphAnalyzer()