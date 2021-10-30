"""
DataShredder - By awesomelewis2007
A simple corruption engine made in python
Github:https://github.com/awesomelewis2007/Datashredder
"""
import configparser
import binascii
import random 
from tqdm import tqdm

from engines import corrupt as basic_corrupt
from engines import random_corrupt as rand_corrupt
from engines import swap_corrupt as swp_corrupt

VERSION = "0.1.6"

def corrupt(input_file,output_file,chance=1000,data=b"00"):
    basic_corrupt.corrupt(input_file,output_file,chance,data)
def random_corrupt(input_file,output_file,chance=1000):
    rand_corrupt.random_data_corrupt(input_file,output_file,chance)
def swap_corrupt(input_file,output_file):
    swp_corrupt.swap_corrupt(input_file,output_file)


config = configparser.ConfigParser()
config.read('settings.ini')

language_config = configparser.ConfigParser()
language_config.read('languages/language.ini')

language = config['general']['language']

class print_language:
    welcome= language_config[language]['welcome']
    version= language_config[language]['version']
    choice_message_line_1= language_config[language]['choice_message_line_1']
    choice_message_line_2= language_config[language]['choice_message_line_2']
    choice_message_line_3= language_config[language]['choice_message_line_3']
    choice_message_line_4= language_config[language]['choice_message_line_4']
    choice_input= language_config[language]['choice_input']
    choice_input_error= language_config[language]['choice_input_error']
    file_in_input=language_config[language]['file_in_input']
    file_out_input=language_config[language]['file_out_input']
    chance_input=language_config[language]['chance_input']
    data_input=language_config[language]['data_input']
    done_message=language_config[language]['done_message']
if __name__ == "__main__":
    print(print_language.welcome)
    print(print_language.version+VERSION)
    print("")
    print(print_language.choice_message_line_1)
    print(print_language.choice_message_line_2)
    print(print_language.choice_message_line_3)
    print(print_language.choice_message_line_4)
    while True:
        choice = input(print_language.choice_input)
        if choice == "1":
            break
        if choice == "2":
            break
        if choice == "3":
            break
        print(print_language.choice_input_error,choice)

    file_in = input(print_language.file_in_input)
    file_out = input(print_language.file_out_input)

    if choice == "1":
        chance = input(print_language.chance_input)
        if chance == "":
            chance == "1000"
        chance = int(chance)

    if choice == "2":
        chance = input(print_language.chance_input)
        if chance == "":
            chance == "1000"
        chance = int(chance) 

    if choice == "1":
        data = input(print_language.data_input).encode()
        if data == "":
            data == "00"       
    if choice == "1":
        corrupt(input_file=file_in,output_file=file_out,chance=chance,data=data)
    if choice == "2":
        random_corrupt(input_file=file_in,output_file=file_out,chance=chance)
    if choice == "3":
        swap_corrupt(input_file=file_in,output_file=file_out)
    print(print_language.done_message+file_in)