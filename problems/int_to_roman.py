def int_to_roman(num):
    res = []
    romans = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 
        100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
    }
    
    for k in romans.keys():
        if num // k == 0:
            continue
        count = num // k
        res.append(romans[k] * count)
        num = num % k
    return ''.join(res)