"""
DataShredder corrupt module 
Owner: 0x4248
Github:https://github.com/0x4248/Datashredder
"""
import binascii
import random
def corrupt(input_file,output_file,chance=1000,data=b"00"):
    with open(input_file, 'rb') as f:
        content = f.read()
    file_hex = binascii.hexlify(content)

    n = 2
    split_file_hex = [file_hex[index : index + n] for index in range(0, len(file_hex), n)]

    file = ""
    
    for i in split_file_hex:
        if random.randint(1,chance) == 1:
            i = data
        file = file+i.decode()
    f = open(output_file,"wb")
    f.write(binascii.unhexlify(file))
