#!/usr/bin/python3
def number_keys(a_dictionary):
    total = 0
    keyList = list(a_dictionary.keys())

    for i in keyList:
        total += 1

    return (total)
