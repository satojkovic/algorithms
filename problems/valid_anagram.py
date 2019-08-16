# Time complexity: O(n + m)
#  length of the input s and t is n and m respectively.
#  iterate over s once, and also iterate over t once, array insertion is O(1).
#  sum of the array is O(1) because of the length of the array is fixed.
# Space complexity: O(1)
def valid_anagram1(s, t):
    used = 256 * [0]
    for ch in s:
        used[ord(ch)] += 1
    for ch in t:
        if used[ord(ch)] == 0:
            return False
        else:
            used[ord(ch)] -= 1
    return True if sum(used) == 0 else False