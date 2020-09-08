import array
class BitArray:
    def __init__(self, bit_size):
        int_size = bit_size >> 5 # number of 32 bit integers
        if bit_size & 31:
            int_size += 1
        self.bit_array = array.array('L') # unsigned 32 bit integer
        self.bit_array.extend((0,) * int_size)

    # Set an integer with the bit at 'bit_num' to 1
    def set(self, bit_num):
        record = bit_num >> 5
        offset = bit_num & 31
        mask = 1 << offset
        self.bit_array[record] |= mask

    # Returns non-zero result if the bit at 'bit_num' is set to 1
    def get(self, bit_num):
        record = bit_num >> 5
        offset = bit_num & 31
        mask = 1 << offset
        return self.bit_array[record] & mask
