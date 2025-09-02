# Empty tuple

t1 = ()
print(t1)

# Tuple with elements

t2 = (1,2,3)
print(t2)


# Tuple with mixed data types
t3 = ("apple", 10, True, 3.14)
print(t3)


# Tuple without parenthesis (packing)
t4 = 1,2,3,4
print(t4)

# Tuple methods

numbers = (1,2,3,2,4,2)
print(numbers.count(2))
print(numbers.count(4))


# What happens if write a single-element tuple like this

t = (5)
print(type(t))

# Can you use a tuple as a dictionary key

d = { (1, 2): "point" }
print(d)

# Memory efficiency

t = (1, 2, 3, 4, 5)
l = [1, 2, 3, 4, 5]

print("Tuple size:", t.__sizeof__())
print("List size:", l.__sizeof__())

