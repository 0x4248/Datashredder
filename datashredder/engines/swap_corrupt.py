import binascii
import random
from tqdm import tqdm
def swap_corrupt(input_file,output_file):
    """corrupts a file with swapping the next piece of data 
    e.g:
    31 32 44 35 36 37 38 39 30 --> 32 44 35 36 37 38 39 30 

    This will corrupt the entire file
    Args:
        input_file ([str]): [input file]
        output_file ([str]): [output file]
    """
    with open(input_file, 'rb') as f:
        content = f.read()
    file_hex = binascii.hexlify(content)

    n = 2
    split_file_hex = [file_hex[index : index + n] for index in range(0, len(file_hex), n)]

    file = ""
    

    for i, ele in enumerate(split_file_hex[:-1]):
    
        file = file+split_file_hex[i + 1].decode()
    f = open(output_file,"wb")
    f.write(binascii.unhexlify(file))