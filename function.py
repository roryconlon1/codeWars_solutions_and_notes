def spin_words(sentence):

    split_sentence = sentence.split(' ')
    results = []

    for word in split_sentence:
        if len(word) >= 4:
            results.append(word[::-1])
        else:
            results.append(word)

    return ' '.join(results)

import math

print(spin_words('Welcome all to python3'))


def is_square(n):
    if n >= 0:
        if math.sqrt(n).is_integer():
            return True
        else:
            return False
    else:
        return False


print(is_square(25))


def bool_to_word(boolean):
    if boolean == True:
        return 'Yes'
    return 'No'

print(bool_to_word(True))
