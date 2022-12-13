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

# take number n and return array of each number and reverse array


def digitize(n):
    res = list(map(int, str(n)))
    return list(reversed(res))


print(digitize(12345))


def count_sheeps(sheep):
    count = 0
    for s in sheep:
        if s == True:
            count += 1
    return count


array1 = [True,  True,  True,  False,
          True,  True,  True,  True,
          True,  False, True,  False,
          True,  False, False, True,
          True,  True,  True,  True,
          False, False, True,  True]
print(count_sheeps(array1))


def number(lines):
    my_arr = []
    total = 0
    # make total of 0 so that every iteration can add 1 and use it as the number of the element in the list
    for letter in lines:
        total += 1
        my_arr.append(f'{total}: {letter}')
    return my_arr


print(number(["a", "b", "c", "d", "e", "f", "g", "h", "i", "h"]))
