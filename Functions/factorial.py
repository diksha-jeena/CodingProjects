def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

# Main
print(fact(5))  
