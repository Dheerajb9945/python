def fibonacci(n, a=0, b=1):
    counter = 0
    while counter < n:
        a, b = b, a + b
        print(a, end=' ')
        counter = counter + 1

fibonacci(10)   # ✅ outside the function