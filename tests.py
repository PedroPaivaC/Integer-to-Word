def splittingClasses(integer):

    integer_list = list(str(integer))

    # print(integer_list)

    integer_list.reverse()

    # print(integer_list)

    integer_classes_aux = []
    aux_list = []

    for index in range(len(integer_list)):

        if len(aux_list) == 3:
            aux_list.reverse()
            integer_classes_aux.append(aux_list.copy())
            aux_list.clear()

        if list(integer_list[index]):
            aux_list.append(integer_list[index])

    if aux_list:
        aux_list.reverse()
        integer_classes_aux.append(aux_list.copy())

    integer_classes = []

    for i in range(-1, -len(integer_classes_aux) - 1, -1):
        integer_classes.append(integer_classes_aux[i])

    return integer_classes


def zerosGrouping(integer):

    integer_classes = splittingClasses(integer)

    # print(integer_classes)

    final_grouped_list = []

    for index, class_ in enumerate(integer_classes):

        grouped_list = []

        for index2, element in enumerate(class_):

            grouped_list_aux = []

            if element == '0':

                if (len(grouped_list) > 0 and
                        list(grouped_list[-1])[-1] == '0' and
                        len(list(grouped_list[-1])) <= 2):

                    grouped_list_aux.append(grouped_list[-1])
                    grouped_list_aux.append(element)
                    grouped_list.pop(-1)
                    grouped_list.append(''.join(grouped_list_aux))

                else:
                    grouped_list.append(element)

            else:
                grouped_list.append(element)

        final_grouped_list.append(grouped_list)

    return final_grouped_list


def classSelectionAux(grouped_list: list):

    grouped_list = grouped_list

    greater_classes = None

    if len(grouped_list) % 6 == 0:
        greater_classes = ['quadrillion', 'trillion', 'billion', 'million', 'thousand', 'regular']
    elif len(grouped_list) % 5 == 0:
        greater_classes = ['trillion', 'billion', 'million', 'thousand', 'regular']
    elif len(grouped_list) % 4 == 0:
        greater_classes = ['billion', 'million', 'thousand', 'regular']
    elif len(grouped_list) % 3 == 0:
        greater_classes = ['million', 'thousand', 'regular']
    elif len(grouped_list) % 2 == 0:
        greater_classes = ['thousand', 'regular']

    for index, class_ in enumerate(greater_classes):
        grouped_list[index].append(class_)

    return grouped_list


def individualClassSelectionAux(greater_classes_grouped_list: list):

    numbers = {'1': 'one',
               '2': 'two',
               '3': 'three',
               '4': 'four',
               '5': 'five',
               '6': 'six',
               '7': 'seven',
               '8': 'eight',
               '9': 'nine'}

    digit_numbers = {'2': 'twenty',
                     '3': 'thirty',
                     '4': 'forty',
                     '5': 'fifty',
                     '6': 'sixty',
                     '7': 'seventy',
                     '8': 'eighty',
                     '9': 'ninety'}

    words = ['hundred', 'and']

    nums_list = [str(x) for x in range(1, 10)]

    grouped_list = greater_classes_grouped_list

    # print(grouped_list)

    for index, greater_class in enumerate(grouped_list):

        if greater_class[0] == '000':

            grouped_list.pop(index)

    for index, greater_class in enumerate(grouped_list):

        if greater_class[0] == '00':
            greater_class[0] = words[1]

        if len(greater_class) > 3:

            greater_class.insert(1, words[0])
            greater_class.insert(2, words[1])

            if greater_class[3] != '0':

                greater_class[3] = digit_numbers[greater_class[3]]

                if greater_class[4] != '0':
                    greater_class[4] = numbers[greater_class[4]]

        if greater_class[1] == '00':

            greater_class.insert(1, words[0])
            greater_class.remove('00')

        if greater_class[-2] in nums_list:
            greater_class[-2] = numbers[greater_class[-2]]

        if greater_class[0] in nums_list:
            greater_class[0] = numbers[greater_class[0]]

    for index, class_ in enumerate(grouped_list):
        for index2, element in enumerate(class_):

            if element == '0':
                grouped_list[index].pop(index2)

    return grouped_list


def classesAndWordsSelection(integer):

    grouped_list = zerosGrouping(integer)

    # print(grouped_list)

    greater_classes_grouped_list = classSelectionAux(grouped_list)

    # print(greater_classes_grouped_list)

    all_classes_grouped_list = individualClassSelectionAux(greater_classes_grouped_list)

    # print(all_classes_grouped_list)

    all_classes_grouped_list[-1].pop(-1)

    # print(all_classes_grouped_list)

    final_number = []

    for _ in all_classes_grouped_list:
        for __ in _:
            final_number.append(__)

    final_number = ' '.join(final_number).upper()

    print(final_number)


# integer = 900_123_350_399
# integer = 90_123_350_399
# integer = 7_900_301_350_399
integer = 777_777_777_777_777_777
classesAndWordsSelection(integer)