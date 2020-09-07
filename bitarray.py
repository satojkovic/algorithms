import array
class BitArray:
    def __init__(self, bit_size):
        int_size = bit_size >> 5 # number of 32 bit integers
        if bit_size & 31:
            int_size += 1
        self.bit_array = array.array('L') # unsigned 32 bit integer
        self.bit_array.extend((0,) * int_size)
