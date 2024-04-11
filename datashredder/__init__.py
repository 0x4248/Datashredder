"""
DataShredder Main module 
Owner: 0x4248
A simple corruption engine made in python
Github:https://github.com/0x4248/Datashredder

Run the demo using demo()
"""
from .corrupt import corrupt
from .random_corrupt import random_data_corrupt
from .swap_corrupt import swap_corrupt

import sys


def demo():
    """This is the demo script to run it use `datashredder.demo`
    """
    print("Welcome to Datashredder Demo")
    print("Please chose a corruption method")
    print("Type 1 to use basic corrupt")
    print("Type 2 to use random basic corrupt")
    print("Type 3 to use swap corrupt")
    while True:
        choice = input("Enter a number>")
        if choice == "1":
            break
        if choice == "2":
            break
        if choice == "3":
            break
        print("Enter a choice:1,2 or 3 not",choice)
    file_in = input("Enter input file location>")
    file_out = input("Enter output file location>")
    if file_in == file_out:
        print("Warning: Datashredder will rewrite "+file_in+". Do you want to contine?")
        while True:
            consent = input("Yes or No>")
            if consent.upper() == "NO":
                print("OK, quitting no changes were made")
                sys.exit()
            if consent.upper() == "YES":
                break
            print("Enter a choice: Yes or No")
    if choice == "1":
        chance = input("chance of corruption>")
        if chance == "":
            chance == "1000"
        chance = int(chance)

    if choice == "2":
        chance = input("chance of corruption>")
        if chance == "":
            chance == "1000"
        chance = int(chance) 

    if choice == "1":
        data = input("corruption data>").encode()
        if data == "":
            data == "00"  

    print("{\n    input file:'"+file_in+"',\n    "+"output file:'"+file_out+"'\n}")    
    print("starting corruption:")

    if choice == "1":
        corrupt(input_file=file_in,output_file=file_out,chance=chance,data=data)
    if choice == "2":
        random_data_corrupt(input_file=file_in,output_file=file_out,chance=chance)
    if choice == "3":
        swap_corrupt(input_file=file_in,output_file=file_out)

    print("Corrupted the file go have a look at your result at: "+file_in)
