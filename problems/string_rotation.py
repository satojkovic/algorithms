def string_rotation(s1, s2):
    s1_s1 = s1 + s1
    if len(s1) == len(s2) and len(s1) > 0:
        return s2 in s1_s1
    else:
        return False

if __name__ == "__main__":
    print(string_rotation('erbottlewat', 'waterbottle'))
    print(string_rotation('waterbottle', 'bottlewater'))
    print(string_rotation('waterbottle', 'waterbottle'))
    print(string_rotation('waterb', 'ottlew'))
    print(string_rotation('wat', 'er'))