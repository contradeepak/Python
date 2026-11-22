# Create and print a tuple

t = (1,2,3,4,5)
print("Tuple:", t)


# Access elements

print("First element:", t[0])
print("Second element:", t[1])


# Length of tuple

print("Length of tuple:", len(t))


# Concatenate two tuples

t1=(1,2,3)
t2=(4,5,6)
t3 = t1+t2
print("Concatenated tuple:", t3)


# Repeat a tuple

t = (7,6)
print("Repeated tuple:", t*3)
#(t*3  ye dikhayega ki kitne baar repeat hoga)


# Check if elements exist

t=(10,20,30,40)
print("Is 20 in tuple?", 20 in t)

# Iterate though tuple

for item in t:
     print("Item:", item)


# Find index of an element

t = (1,2,2,3,4,2)
print("Count of 2:", t.count(2))     


# Convert list to a tuple

lst = [1,2,3]
t = tuple(lst)
print("Tuple from list:", t)