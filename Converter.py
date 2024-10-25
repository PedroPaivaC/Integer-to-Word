import math
import copy


class IntegerToWord:

    def __init__(self, integer: int):

        self.integer = list(str(integer))

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

        self.words = ['ten', 'twenty', 'thirty',
                      'forty', 'fifty', 'sixty',
                      'seventy', 'eighty', 'ninety', 'and']

    def zerosGrouping(self):

        grouped_list = []

        for index, element in enumerate(self.integer):

            grouped_list_aux = []

            if element == '0':
                grouped_list_aux.append(grouped_list[-1])
                grouped_list_aux.append(element)
                grouped_list.pop(-1)
                grouped_list.append(''.join(grouped_list_aux))

            else:
                grouped_list.append(element)

        print(grouped_list)

    def integerClassAux(self):

        words_list = []

        if len(self.integer) % 3 == 0:
            pass
        elif len(self.integer) == 2:
            pass
        else:
            pass

    def verifyBasic(self):

        # Verifies for 10, 20, 30, 40, 50, 60, 70, 80, 90
        if len(self.integer) == 2:
            return self.words[int(self.integer[0])-1]

        if len(self.integer) == 3:
            val = self.integer[0]
            self.integer.pop(0)
            if int(''.join(self.integer)) == 0:
                self.integer.insert(0, val)
                return self.numbers[self.integer[0]] + ' hundred'

        if len(self.integer) == 4:
            return self.words[int(self.integer[0])-1]

        match self.integer:
            case 11:
                return 'eleven'
            case 12:
                return 'twelve'
            case 13:
                return 'thirteen'
            case 14:
                return 'fourteen'
            case 15:
                return 'fifteen'
            case 16:
                return 'sixteen'
            case 17:
                return 'seventeen'
            case 18:
                return 'eighteen'
            case 19:
                return 'nineteen'

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

    integer = 100023450070

    ito = IntegerToWord(integer=integer)
    print(ito.zerosGrouping())
