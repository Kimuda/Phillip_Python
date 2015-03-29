
def radix(number, r = 16, case = "upper"):
    upper = "0123456789ABCDEF"
    lower = "0123456789abcdef"
    if case == "upper":
        digits = upper
    else:
        digits = lower
    ret = ""
    while number > 0:
        ret = digits[number % r] + ret
        number = number // r
    return ret

print (radix(17))
print (radix(255))
print (radix(17,8))
print (radix(17,2))
