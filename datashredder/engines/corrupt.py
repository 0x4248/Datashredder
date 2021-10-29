import binascii
import random
from tqdm import tqdm
def corrupt(input_file,output_file,chance=1000,data=b"00"):
    """### corrupts a file with a chosen corruption data
    e.g:
    31 32 44 35 36 37 38 39 30 --> 31 FF 44 35 FF 37 FF FF 30

    In this example FF is the chosen corruption data
    Args:
        input_file ([str]): [input file]
        output_file ([str]): [output file]
        chance (int, optional): [This is the chance of the next byte of data being corrupted if i set it to 2 t is 1 in 2 chance of the next byte being corrupted]. Defaults to 1000.
        data (bytes, optional): [Data used to corrupt the image e.g 2B will be changed to 20 if i set this value to 20. this MUST be set is bytes]. Defaults to b"00".
    """
    with open(input_file, 'rb') as f:
        content = f.read()
    file_hex = binascii.hexlify(content)

    n = 2
    split_file_hex = [file_hex[index : index + n] for index in range(0, len(file_hex), n)]

    file = ""
    
    for i in tqdm(split_file_hex):
        if random.randint(1,chance) == 1:
            i = data
        file = file+i.decode()
    f = open(output_file,"wb")
    f.write(binascii.unhexlify(file))
