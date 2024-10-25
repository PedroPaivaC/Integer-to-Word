def zerosGrouping(integer):

    integer = list(str(integer))

    grouped_list = []

    for index, element in enumerate(integer):

        grouped_list_aux = []

        if element == '0':
            grouped_list_aux.append(grouped_list[-1])
            grouped_list_aux.append(element)
            grouped_list.pop(-1)
            grouped_list.append(''.join(grouped_list_aux))

        else:
            grouped_list.append(element)

    print(grouped_list)


integer = 100000000000250
zerosGrouping(integer)