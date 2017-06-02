string1 = input('Строка 1: ')
string2 = input('Строка 2: ')


def string_compare(string1, string2):

    if string1 == string2:
        return 1
    elif string1 != string2 and len(string1) > len(string2):
        return 2
    elif string1 != string2 and string2 == 'learn':
        return 3

print(string_compare(string1, string2))
