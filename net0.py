import pymorphy2
def get_normal_form(word):
    morph_analyzer = pymorphy2.MorphAnalyzer()

    # word = input('input something: ')
    forms = morph_analyzer.parse(word.lower())
    # print(forms[0].normal_form)
    return forms[0].normal_form

def get_association(word):
    pass