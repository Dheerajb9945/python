def swap(a, b):
    a, b = b, a
    print("After swapping:")
    print("a =", a)
    print("b =", b)

# calling function
x = 5
y = 10

print("Before swapping:")
print("x =", x)
print("y =", y)

swap(x, y)