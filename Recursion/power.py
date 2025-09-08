def power(base, exp):
    assert int(exp)==exp, "The exponent must be integer number only "
    if exp==0:
        return 1
    else:
        return base * power(base,exp-1)
    
print(power(2,5))