# Find common elements

t1 = (1,2,3,4)
t2 = (3,4,5,6)


common = tuple(set(t1) and set(t2))
print("Common Elements:", common)