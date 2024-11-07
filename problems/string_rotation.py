def string_rotation(s1, s2):
    s1_s1 = s1 + s1
    if len(s1) == len(s2) and len(s1) > 0:
        return s2 in s1_s1
    else:
        return False

def test_string_rotation():
    assert string_rotation('erbottlewat', 'waterbottle')
    assert string_rotation('waterbottle', 'bottlewater')
    assert string_rotation('waterbottle', 'waterbottle')
    assert not string_rotation('waterb', 'ottlew')
    assert not string_rotation('wat', 'er')

def rotate_string(s, goal):
    concat_s = ''.join([s, s])
    len_s = len(s)
    for i in range(len_s):
        if concat_s[i:i+len_s] == goal:
            return True
    return False

def test_rotate_string():
    assert rotate_string("abcde", "cdeab")
    assert not rotate_string("abcde", "abced")
    assert rotate_string("a", "a")
    assert not rotate_string("abcde", "cab")

def rotate_string2(s, goal):
	concat_s = ''.join([s, s])
	if len(s) != len(goal):
		return False
	return goal in concat_s

def test_rotate_string2():
    assert rotate_string2("abcde", "cdeab")
    assert not rotate_string2("abcde", "abced")
    assert rotate_string2("a", "a")
    assert not rotate_string2("abcde", "cab")
