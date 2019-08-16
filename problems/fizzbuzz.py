def fizzbuzz(n):
    res = []
    for i in range(1, n + 1):
        if int(i) % 3 == 0 and int(i) % 5 == 0:
            res.append('FizzBuzz')
        elif int(i) % 3 == 0:
            res.append('Fizz')
        elif int(i) % 5 == 0:
            res.append('Buzz')
        else:
            res.append(str(i))
    return res