import math


def spin_words(sentence):

    split_sentence = sentence.split(' ')
    results = []

    for word in split_sentence:
        if len(word) >= 4:
            results.append(word[::-1])
        else:
            results.append(word)

    return ' '.join(results)


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


def greet(name):
    return "Hello, " + name + " how are you doing today?"

# dictionary of numbers and get number as argument and get the written version by its key


def switch_it_up(number):
    list_of_nums = {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }
    return list_of_nums.get(number)


print(switch_it_up(1))

# take 2 argument and return first multiples of n multiples of x
def count_by(x, n):
    new_list = []
    for i in range(n):
        new_list.append((i+1) * x)
    return new_list


print(count_by(2, 5))
