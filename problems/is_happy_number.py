def is_happy_number1(n):
    seen = set()
    while True:
        nums = []
        while True:
            a = n % 10
            b = n // 10
            nums.append(a)
            if b == 0:
                break
            elif b < 10:
                nums.append(b)
                break
            n = b
        ret = sum([i ** 2 for i in nums])
        if ret == 1:
            return True
        elif ret in seen:
            return False
        else:
            seen.add(ret)
            n = ret

def is_happy_number2(n):
    seen = set()
    while n != 1:
        n = sum([int(i) ** 2 for i in str(n)])
        if n in seen:
            return False
        seen.add(n)
    return True

def is_happy_number3(n):
    seen = set()
    return _is_happy_number3(n, seen)

def _is_happy_number3(n, seen):
    n = sum([int(c) ** 2 for c in str(n)])
    if n == 1:
        return True
    if n in seen:
        return False
    seen.add(n)
    return _is_happy_number3(n, seen)

def is_happy_number4(n):
    seen = set()
    while n != 1 and not n in seen:
        seen.add(n)
        n = next_number(n)
    return n == 1

def next_number(n):
    total = 0
    while n > 0:
        n, digit = divmod(n, 10)
        total += digit ** 2
    return total