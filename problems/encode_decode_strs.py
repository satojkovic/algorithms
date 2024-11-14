def encode(strs):
    return '\n'.join(strs)


def decode(s):
    return s.split('\n')


def test_encode_decode():
    s = encode(["Hello", "World"])
    assert decode(s) == ["Hello", "World"]

    s = encode(["abc", ",de", "f"])
    assert decode(s) == ["abc", ",de", "f"]

    s = encode([""])
    assert decode(s) == [""]
