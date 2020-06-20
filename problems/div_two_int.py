def divide(dividend, divisor):
    def div_iter(dividend, divisor):
        ret = -1
        while dividend >= 0:
            dividend -= divisor
            ret += 1
        return ret
    
    def div(dividend, divisor):
        if dividend < 0:
            return -1
        return div(dividend - divisor, divisor) + 1
    
    sign = 1 if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else -1
    return min(2**31 - 1, max(-2**31, sign * div(abs(dividend), abs(divisor))))