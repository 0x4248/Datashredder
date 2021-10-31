"""
DataShredder - By awesomelewis2007
A simple corruption engine made in python
Github:https://github.com/awesomelewis2007/Datashredder
"""

import binascii
import random 
from tqdm import tqdm

from engines import corrupt as basic_corrupt
from engines import random_corrupt as rand_corrupt
from engines import swap_corrupt as swp_corrupt

VERSION = "0.1.7"

def corrupt(input_file,output_file,chance=1000,data=b"00"):
    basic_corrupt.corrupt(input_file,output_file,chance,data)
def random_corrupt(input_file,output_file,chance=1000):
    rand_corrupt.random_data_corrupt(input_file,output_file,chance)
def swap_corrupt(input_file,output_file):
    swp_corrupt.swap_corrupt(input_file,output_file)

if __name__ == "__main__":
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
    if choice == "1":
        corrupt(input_file=file_in,output_file=file_out,chance=chance,data=data)
    if choice == "2":
        random_corrupt(input_file=file_in,output_file=file_out,chance=chance)
    if choice == "3":
        swap_corrupt(input_file=file_in,output_file=file_out)
    print("Corrupted go have a look at your result at: "+file_in)