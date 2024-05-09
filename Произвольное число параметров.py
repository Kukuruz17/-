def test(*params):
    print(*params)
test(2, 3, 5, 7, 88)

##

def factorial(n):
    if n == 0:
        return 0
    else:
        return n * (n-1)
print(factorial(22))