'''
Creating a hecadecimal look-up table.

Table will represent every possible hexadecimal digit (0-9, A-F) and its binary equivalent.

Example:
    0: 0000
    1: 0001
    2: 0010
    ...
    A: 1010
    B: 1011
    ...
    F: 1111
'''

'''

def create_hex_table():
    hex_table = {}
    for i in range(16):
        hex_table[hex(i)[2:].upper()] = bin(i)[2:].zfill(4)
    return hex_table

'''

# let's create a list of all possible hexadecimal digits instead

def create_hex_list():
    '''
    Creates a list of all possible hexadecimal digits.
    '''
    hex_list = []
    for i in range(16):
        #print("Hex i:", hex(i))
        #print("Hex i[2:]:", hex(i)[2:])
        #print("Hex i[2:].upper()", hex(i)[2:].upper())
        hex_list.append(hex(i)[2:].upper())
        #hex_list.append(hex(i)[2:])

    return hex_list


def create_hex_to_binary_list() -> list:
    '''
    Creates a list of binary values for each hexadecimal digit.

    Input: None

    Output: List of binary values for each hexadecimal digit.
    [0000, 0001, 0010, ..., 1110, 1111]
    (0, 1, 2, ..., E, F)
    '''
    hex_table = create_hex_list()
    hex_to_binary_list = []
    for hex_digit in hex_table:
        hex_to_binary_list.append(bin(int(hex_digit, 16))[2:].zfill(4))
        print("Hex:", hex_digit)
        print(bin(int(hex_digit, 16))[2:].zfill(4))
    return hex_to_binary_list