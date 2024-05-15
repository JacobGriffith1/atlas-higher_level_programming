#!/usr/bin/python3
def subtract(numList):
    sub = 0
    maxList = max(numList)

    for n in numList:
        if maxList > n:
            sub += n

    return (maxList - sub)


def roman_to_int(roman_string):
    if not roman_string:
        return (0)
    if not isinstance(roman_string, str):
        return (0)

    romNum = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    keyList = list(romNum.keys())

    num = 0
    last = 0
    numList = [0]
    for ch in roman_string:
        for r in keyList:
            if r == ch:
                if romNum.get(ch) <= last:
                    num += subtract(numList)
                    numList = [romNum.get(ch)]
                else:
                    numList.append(romNum.get(ch))

                last = romNum.get(ch)

    num += subtract(numList)

    return (num)
