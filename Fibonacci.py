def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

x = int(input("Geben Sie eine positive Ganzzahl ein: "))
print("Die entsprechende Fibonacci-Zahl ist:", fibonacci(x))

