

# dictionary = {'22': '23',
#                'CNRS': 'CAC40',
#                'sa': 'son',
#                 'Médaille': 'colier',
#                  'or' : 'bronze',
#                   'France': 'Belgique'}

# text = 'Le 22 septembre dernier, le CNRS annonçait que sa Médaille en or, avait été décernée à un chercheur français.'


def substitute_words(dictionary, text):

    for key, value in dictionary.items():
        text = text.replace(key, value)
    return text

# print("Text intial: ", text)
# print("Teste apres remplacement:\n")
# print(substitute_words(dictionary, text))