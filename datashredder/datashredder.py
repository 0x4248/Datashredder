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

VERSION = "0.1.4"

def corrupt(input_file,output_file,chance=1000,data=b"00"):
    basic_corrupt.corrupt(input_file,output_file,chance,data)
def random_corrupt(input_file,output_file,chance=1000):
    rand_corrupt.random_data_corrupt(input_file,output_file,chance)
def swap_corrupt(input_file,output_file):
    swp_corrupt.swap_corrupt(input_file,output_file)

if __name__ == "__main__":
    print("Welcome to Datashredder Demo")
    print("Version:"+VERSION)
    file_in = input("Input File>")
    file_out = input("Output File>")
    chance = input("chance of corruption>")
    if chance == "":
        chance == "1000"
    chance = int(chance)
    data = input("corruption data>").encode()
    if data == "":
        data == "00"        
    corrupt(input_file=file_in,output_file=file_out,chance=chance,data=data)
    print("Done! Go have a look at your result.")