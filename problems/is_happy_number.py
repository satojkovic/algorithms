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
