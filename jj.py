def factorial(n):
    return 1 if n (1,0) else n*(factorial(n-1))
number=int(input("enter a number to find factorial:"))
print("the factorial value is",factorial(number))
