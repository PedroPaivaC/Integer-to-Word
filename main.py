import math
import copy

class IntegerToWord:

    def __init__(self, integer: int):
        self.integer = str(integer)

        self.integer_class = None
        self.integer_classes = ['hundred', 'thousand',
                                'million', 'billion',
                                'trillion', 'quadrillion']

        self.numbers = {'1': 'one',
                        '2': 'two',
                        '3': 'three',
                        '4': 'four',
                        '5': 'five',
                        '6': 'six',
                        '7': 'seven',
                        '8': 'eight',
                        '9': 'nine'}

    def integerClassAux(self):

        integer_list = list(self.integer)
        integer_list.reverse()

        integer_classes_aux = []
        aux_list = []

        for index in range(len(integer_list)):

            if len(aux_list) == 3:
                aux_list.reverse()
                integer_classes_aux.append(aux_list.copy())
                aux_list.clear()

            aux_list.append(integer_list[index])

        if aux_list:
            aux_list.reverse()
            integer_classes_aux.append(aux_list.copy())

        integer_classes = []

        for i in range(-1, -len(integer_classes_aux) - 1, -1):
            # classes.remove(classes_aux[i])
            integer_classes.append(integer_classes_aux[i])

        return integer_classes

    def integerClass(self):

        split_int = self.integerClassAux()

        classes_ = []

        for class_ in range(len(split_int)):
            classes_.append(self.integer_classes[class_])

        classes = []

        for i in range(-1, -len(classes_)-1, -1):
            # classes.remove(classes_aux[i])
            classes.append(classes_[i])

        print(classes)

        for index, class_ in enumerate(classes):

            if classes[index] == 'hundred':
                split_int[index].insert(1, classes[index])
            else:
                split_int[index].append(classes[index])

        print(split_int)


if __name__ == '__main__':

    integer = 1234567

    ito = IntegerToWord(integer=integer)
    print(ito.integerClass())
