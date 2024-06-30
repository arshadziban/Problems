# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Sample value of n is 5
# Expected Result : 615

def value():
    n = input("Enter an integer: ")
    nn = n + n
    nnn = n + n + n
    print(int(n) + int(nn) + int(nnn))

value()