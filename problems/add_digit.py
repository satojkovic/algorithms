def add_digits(num):
    def add(num):
        result = 0
        while num >= 10 or (num % 10) != 0:
            d = num % 10
            num = num // 10
            result += d
        return result

    result = add(num)
    while result >= 10:
        result = add(result)
    return result


def test_add_digits():
    assert add_digits(123) == 6
    assert add_digits(10) == 1
    assert add_digits(0) == 0
    assert add_digits(19) == 1
