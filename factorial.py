def factorial_rekur(number):
    if number>1:
        return number*factorial_rekur(number-1)
    else:
        return 1


print(factorial_rekur(5))


def factorial_itter(number):
    i=1
    fact=1
    while number>i:
        fact*=number
        number-=1
    else:
        return fact
    
print(factorial_itter(5))
