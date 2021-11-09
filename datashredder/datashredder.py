"""
DataShredder - By awesomelewis2007
A simple corruption engine made in python
Github:https://github.com/awesomelewis2007/Datashredder
"""
from engines import corrupt as basic_corrupt
from engines import random_corrupt as rand_corrupt
from engines import swap_corrupt as swp_corrupt

import sys

VERSION = "0.2.7"

def corrupt(input_file,output_file,chance=1000,data=b"00"):
    """corrupts a file with a chosen corruption data
    e.g:
    31 32 44 35 36 37 38 39 30 --> 31 FF 44 35 FF 37 FF FF 30

    In this example FF is the chosen corruption data
    Args:
        input_file ([str]): [input file]
        output_file ([str]): [output file]
        chance (int, optional): [This is the chance of the next byte of data being corrupted if i set it to 2 t is 1 in 2 chance of the next byte being corrupted]. Defaults to 1000.
        data (bytes, optional): [Data used to corrupt the image e.g 2B will be changed to 20 if i set this value to 20. this MUST be set is bytes]. Defaults to b"00".
    """
    basic_corrupt.corrupt(input_file,output_file,chance,data)
def random_corrupt(input_file,output_file,chance=1000):
    """corrupts a file with random data
    e.g:
    31 32 44 35 36 37 38 39 30 --> 31 0A 44 35 F0 37 00 FA 30

    In this example FF is the chosen corruption data
    Args:
        input_file ([str]): [input file]
        output_file ([str]): [output file]
        chance (int, optional): [This is the chance of the next byte of data being corrupted if i set it to 2 t is 1 in 2 chance of the next byte being corrupted]. Defaults to 1000.
    """
    rand_corrupt.random_data_corrupt(input_file,output_file,chance)
def swap_corrupt(input_file,output_file):
    """corrupts a file with swapping the next piece of data 
    e.g:
    31 32 44 35 36 37 38 39 30 --> 32 44 35 36 37 38 39 30 

    This will corrupt the entire file
    Args:
        input_file ([str]): [input file]
        output_file ([str]): [output file]
    """
    swp_corrupt.swap_corrupt(input_file,output_file)

if __name__ == "__main__":
    for i in sys.argv:
        if i.upper() == "-V":
            print(VERSION)
            sys.exit()
    print("Welcome to Datashredder Demo")
    print("Version:"+VERSION)
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
    file_in = input("Input File>")
    file_out = input("Output File>")
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
    print("--------------------") 

    if choice == "1":
        corrupt(input_file=file_in,output_file=file_out,chance=chance,data=data)
    if choice == "2":
        random_corrupt(input_file=file_in,output_file=file_out,chance=chance)
    if choice == "3":
        swap_corrupt(input_file=file_in,output_file=file_out)

    print("Corrupted go have a look at your result at: "+file_in)
