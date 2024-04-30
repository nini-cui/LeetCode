def calculate_factorial(n:int):
    print(f"n = {n}")
    if n == 1:
        return 1
    else:
        return n * calculate_factorial(n - 1)
    
print(calculate_factorial(3))
