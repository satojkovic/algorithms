def add_strings(num1, num2):
    carry = 0
    i, j = len(num1) - 1, len(num2) - 1
    result = []
    while i >= 0 or j >= 0 or carry != 0:
        n1 = ord(num1[i]) - ord("0") if i >= 0 else 0
        n2 = ord(num2[j]) - ord("0") if j >= 0 else 0
        digit = (n1 + n2 + carry) % 10
        result.append(str(digit))
        carry = (n1 + n2 + carry) // 10
        i -= 1
        j -= 1
    return "".join(result[::-1])


def test_add_strings():
    assert add_strings("11", "123") == "134"
    assert add_strings("345", "15") == "360"
    assert add_strings("1", "9") == "10"
    assert add_strings("0", "0") == "0"
