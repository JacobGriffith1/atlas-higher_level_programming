#!/usr/bin/python3
'''Module contains script to add all args to a Python list,
then save them to a file'''
import sys
import os.path


save = __import__('5-save_to_json_file')
load = __import__('6-load_from_json_file')

list = []
if os.path.exists("add_item.json"):
    list = load("add_item.json")

for arg in sys.argv[1:]:
    list.append(arg)

save(list, "add_item.json")
