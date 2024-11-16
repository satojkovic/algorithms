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


def encode_with_len(strs):
    # エンコード後の文字列
    encoded_str = ""
    # リストに含まれる文字列について、規則に従って文字数とdelimiterを追加した文字列を作成
    for s in strs:
        encoded_str += str(len(s)) + "#" + s
    return encoded_str

def decode_with_len(s):
    # デコード後の文字列のリスト
    decoded_strs = []
    # 文字列のデコード位置
    i = 0
    # sの文字列を走査
    while i < len(s):
        # オリジナル文字列のスタート位置を決める
        j = i
        while s[j] != "#":
            j += 1
        # jは最初に見つかったdelimiterの位置となるので、オリジナルの文字列開始位置はj + 1
        # またdelimiterの位置までの数値が文字列長となる
        str_len = int(s[i:j])
        decoded_strs.append(s[j + 1 : j + 1 + str_len])
        # 次の文字列の文字列長の位置に更新
        i = j + 1 + str_len
    return decoded_strs


def test_encode_decode_with_len():
    s = encode_with_len(["Hello", "World"])
    assert decode_with_len(s) == ["Hello", "World"]

    s = encode_with_len(["abc", ",de", "f"])
    assert decode_with_len(s) == ["abc", ",de", "f"]

    s = encode_with_len([""])
    assert decode_with_len(s) == [""]

    s = encode_with_len(["He6llo", "#World"])
    assert decode_with_len(s) == ["He6llo", "#World"]
