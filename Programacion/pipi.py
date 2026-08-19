def fibonacci(a):
    if a == 1 or a ==0:
        return a
    else:
        return fibonacci(a-1) + fibonacci(a-2)
    
print(fibonacci(7))