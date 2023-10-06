# Input: x = 2.00000, n = 10
# Output: 1024.00000

def myPow(x: float, n: int) -> float:
    # when power is negative -> x**n = (1/x)**(-n)
    if n < 0:
        x = 1/x
        n = -n
    
    # when power is positive -> x^(2n) = (x^n) *(x^n)
    power = 1
    current_product = x
    while n > 0:
        if n%2:
            power *= current_product
        # if n is odd, we need to time x one more time'
        current_product *= current_product
        n = n//2
    return power

x = 2.00000
n = 10
print(myPow(x, n))