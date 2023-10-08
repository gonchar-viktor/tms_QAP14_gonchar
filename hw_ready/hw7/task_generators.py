# +
# 1 Напишите генератор, который принимает список
# numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7] и
# возвращает новый список только с положительными
# числами

def f():
    """
    Write a generator that accepts a list and
    returns a new list with only positive numbers
    """
    numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
    n = []
    for i in numbers:
        if i >= 0:
            n.append(i)
    yield n


b = f()

for o in b:
    print(o)


# 2 Необходимо составить список чисел которые
# указывают на длину слов в строке: sentence = " thequick
# brown fox jumps over the lazy dog", но только если слово
# не "the" с обработкой исключений

def f2():
    """
    It is necessary to make a list of numbers that indicate the length of words
    in a string, but only if the word is not "the" with exception handling
    """
    sentence = " thequick brown fox jumps over the lazy dog"
    list_of_numbers = []
    sentence = sentence.split()

    for i in sentence:
        try:
            if "the" in i:
                raise ValueError(f"В слове: '{i}' находится исключение:"
                                 f" 'the' ")
                # aa = 'Исключение: the'
                #  list_of_numbers.append(aa)  #--- эти две строки, если хотим
                #  видеть в списке исключения
            else:
                a = len(i)
                list_of_numbers.append(a)
        except ValueError as e:
            print(e)
    return list_of_numbers


print(f2())
