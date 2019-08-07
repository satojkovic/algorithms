# Time complexity: O(n)
#  we iterate over an input string, nums. (length: n)
# Space complexity: O(n)
#  we create new list nums. 
def roman_to_int1(s):
    roman2int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    nums = [roman2int[ch] for ch in s]
    for i in range(0, len(nums) - 1, 1):
        if nums[i] < nums[i+1]:
            nums[i] *= -1
    return sum(nums)

# Time complexity: O(n)
#  we iterate over an input string once (but sum all numbers).
#  append op costs O(1) at average case.
# Space complexity: O(n)
#  we create new list nums.
def roman_to_int2(s):
    roman2int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
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

# Time complexity: O(n)
# Space complexity: O(1)
def roman_to_int3(s):
    roman2int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
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