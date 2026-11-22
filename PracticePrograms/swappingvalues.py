# Python allows you to swap values directly without Temp Variable

# Python allows swapping values directly.


print("Before swapping")
a=10
b=20
print("a =", a)
print("b =", b)

a,b = b,a # Swap without temp variable

print("After swapping")
print("a =", a)
print("b =", b)