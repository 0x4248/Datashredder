import binascii
import random
from tqdm import tqdm
def random_data_corrupt(input_file,output_file,chance=1000):
    """corrupts a file with random data
    e.g:
    31 32 44 35 36 37 38 39 30 --> 31 0A 44 35 F0 37 00 FA 30

    In this example FF is the chosen corruption data
    Args:
        input_file ([str]): [input file]
        output_file ([str]): [output file]
        chance (int, optional): [This is the chance of the next byte of data being corrupted if i set it to 2 t is 1 in 2 chance of the next byte being corrupted]. Defaults to 1000.
    """
    with open(input_file, 'rb') as f:
        content = f.read()
    file_hex = binascii.hexlify(content)

    n = 2
    split_file_hex = [file_hex[index : index + n] for index in range(0, len(file_hex), n)]

    file = ""
    corruption_times = 0
    
    for i in tqdm(split_file_hex):
        if random.randint(1,chance) == 1:
            a = random.choice(["1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"])
            b = random.choice(["1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"])
            c = a+b
            i = c.encode()
            corruption_times = corruption_times + 1
        file = file+i.decode()
    f = open(output_file,"wb")
    f.write(binascii.unhexlify(file))
