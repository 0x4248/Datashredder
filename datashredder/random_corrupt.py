"""
DataShredder random corrupt module 
Owner: awesomelewis2007
Github:https://github.com/awesomelewis2007/Datashredder
"""
import binascii
import random
def random_data_corrupt(input_file,output_file,chance=1000):
    with open(input_file, 'rb') as f:
        content = f.read()
    file_hex = binascii.hexlify(content)

    n = 2
    split_file_hex = [file_hex[index : index + n] for index in range(0, len(file_hex), n)]

    file = ""
    
    for i in split_file_hex:
        if random.randint(1,chance) == 1:
            a = random.choice(["1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"])
            b = random.choice(["1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"])
            c = a+b
            i = c.encode()
        file = file+i.decode()
    f = open(output_file,"wb")
    f.write(binascii.unhexlify(file))
