#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    ct = 0

    for i in range(x):
        try:
            print("{}".format(my_list[i]), end='')
        except Exception:
            break
        else:
            ct += 1

    print()
    return (ct)
