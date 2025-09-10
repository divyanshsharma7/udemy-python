def factorial(n):
    if n in [0,1]:
        return 1  
    else:
        return n* factorial(n-1)      

print(factorial(5)) #it will show the factorail of 5 = 120
