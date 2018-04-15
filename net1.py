import pymorphy2

def get_normal_form(word):
    morph_analyzer = pymorphy2.MorphAnalyzer()
    forms = morph_analyzer.parse(word.lower())
    return forms[0].normal_form

def get_association(word):
    pass


if __name__ == '__main__':
    word = input('input something: ')
    print(get_normal_form(word))