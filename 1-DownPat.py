from math import ceil
from itertools import permutations


def is_pat(data, console=True):
    def split_string(s):
        if len(s) >= 1:
            if len(s) == 2:
                if s[0] > s[1]:
                    return 1
                else:
                    return 0
            elif len(s) == 1:
                return 1

            mid = ceil(len(s) / 2)
            s1 = s[:mid][::-1]
            s2 = s[mid:][::-1]
            return split_string(s1), split_string(s2)

    def calc_pat(string):
        string = split_string(string)

        """Expands the tuple response from split string - this only works to a depth of 6 characters, 
        could use a recursive solution to allow greater depth if I had more time"""
        res = ''
        try:
            for elem in string:
                try:
                    if len(elem) > 1:
                        for i in elem:
                            res += str(i)
                    else:
                        res += str(elem)
                except TypeError:
                    res += str(elem)
        except TypeError:
            res = string

        flag = True
        if len(str(res)) == 1:
            if res == 0:
                flag = False
        else:
            for val in res:
                if val == '0':
                    flag = False

        return flag

    strings = data.split(' ')
    pats = []
    for string in strings:
        pats.append(calc_pat(string))
    pats.append(calc_pat(data.replace(" ", "")))

    if console:
        for pat in pats:
            if pat:
                print('YES')
            else:
                print('NO')

    return pats[0]


def pat_permutations(data, console=True):
    data = list(permutations(data, len(data)))
    print(len(data))

    pats = []
    for i in data:
        temp = ""
        for char in i:
            temp += char
        pats.append(is_pat(temp, console=False))

    count = 0
    for x in range(len(pats)):
        if pats[x]:
            count += 1
            if console:
                print(data[x])
    return count


if __name__ == '__main__':
    # 1a
    data = input('1a: Enter two strings separated by a space')
    is_pat(data)

    # 1b
    print('\n\n1b:')
    pat_permutations("ABCD")

    # 1c
    print('\n\n1c:')
    """Will take too long, calculating 25 factorial permutations"""
    # print(pat_permutations("BCDEFGHIJKLMNOPQRSTUVWXYZ", console=False))
