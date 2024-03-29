#
# Note: In this problem, you can assume that the input string is valid.
#

#
# Whether the symbols are ordered from most significant to least.
# If not, subtract the current value from the value immediately after it.
#

def roman_to_int1(s):
    # Time complexity: O(n)
    #  we iterate over an input string, nums. (length: n)
    # Space complexity: O(n)
    #  we create new list nums.
    roman2int = {'I': 1, 'V': 5, 'X': 10,
                 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    nums = [roman2int[ch] for ch in s]
    for i in range(0, len(nums) - 1, 1):
        if nums[i] < nums[i+1]:
            nums[i] *= -1
    return sum(nums)


def roman_to_int2(s):
    # Time complexity: O(n)
    #  we iterate over an input string once (but sum all numbers).
    #  append op costs O(1) at average case.
    # Space complexity: O(n)
    #  we create new list nums.
    roman2int = {'I': 1, 'V': 5, 'X': 10,
                 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    nums = []
    for i, ch in enumerate(s):
        if i == len(s) - 1:
            nums.append(roman2int[ch])
        else:
            if roman2int[ch] < roman2int[s[i+1]]:
                nums.append(roman2int[ch] * -1)
            else:
                nums.append(roman2int[ch])
    return sum(nums)


def roman_to_int3(s):
    # Time complexity: O(n)
    # Space complexity: O(1)
    roman2int = {'I': 1, 'V': 5, 'X': 10,
                 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ret = 0
    for i, ch in enumerate(s):
        if i == len(s) - 1:
            ret += roman2int[ch]
        else:
            if roman2int[ch] < roman2int[s[i+1]]:
                ret += (roman2int[ch] * -1)
            else:
                ret += roman2int[ch]
    return ret


def roman_to_int4(s):
    roman2int = {'I': 1, 'V': 5, 'X': 10,
                 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    i, res = 0, 0
    while i < len(s):
        if i+1 < len(s) and int(roman2int[s[i]]) < int(roman2int[s[i+1]]):
            res += int(roman2int[s[i+1]]) - int(roman2int[s[i]])
            i += 2
        else:
            res += int(roman2int[s[i]])
            i += 1
    return res


def roman_to_int5(s):
    roman2int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    res = roman2int[s[-1]]
    for i in range(len(s) - 2, -1, -1):
        if roman2int[s[i]] < roman2int[s[i + 1]]:
            res -= roman2int[s[i]]
        else:
            res += roman2int[s[i]]
    return res


def roman_to_int6(s):
    roman2int = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900,
    }

    res = 0
    pos = 0
    while pos < len(s):
        if pos < len(s) - 1 and s[pos : pos + 2] in roman2int:
            res += roman2int[s[pos : pos + 2]]
            pos += 2
        else:
            res += roman2int[s[pos]]
            pos += 1
    return res
