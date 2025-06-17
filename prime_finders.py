'''
We will now develop a method of traversing a very large range of numbers, 
in binary, to find all prime numbers within that range.

We will need to build upon the hexadecimal_lookup_table.py modules
to build a list of all possible hexadecimal digits and their binary equivalents,
ranging from 0000.0000.0000.0000.0000.0000 to 1111.1111.1111.1111.1111.1111 [HEX: 000000 to FFFFFF] (6 hex numbers: can represent 16,777,216 decimal numbers)
Indexes from -1 to -24...
'''

def create_txt_digits(filename, possible_digits_list):
    '''
    Creating a txt file of all possible digits from 0 to FFFFFF.
    '''
    text = ''
    with open(filename, "w") as file:
        for i in range(16): # eg. indices for 0001, 0010, etc.
            for j in range(16):
                for k in range(16):
                    for l in range(16):
                        for m in range(16):
                            for n in range(16):
                                text = possible_digits_list[i] + possible_digits_list[j] + possible_digits_list[k] + possible_digits_list[l] + possible_digits_list[m] + possible_digits_list[n]
                                file.write(text + "\n")


# HARD PART: Maybe, go through squares of numbers (similar to sieve of Eratosthenes), look for patterns in binary, or...

# Pattern 1: All numbers ending in 10 are NOT PRIME (divisible by 2)

def flag_mults_of_two(filename, possible_digits_list):
    
    for number in filename.strip():
        ### WIP
        return None


# Pattern 2: Find multiples of 3...
# Pattern 3: Find multiples of 5... etc. etc.
