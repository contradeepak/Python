# Create and print a list

fruits  = ["apple", "banana", "cherry"]
print(fruits)


# Access elements

print(fruits[0])     # apple
print(fruits[-1])    # cherry


# Add items

fruits.append("mango")
print(fruits)

# Insert at specific position

fruits.insert(1, "orange")
print(fruits)


# Remove items

fruits.remove("banana")
print(fruits)


# Loop through the list

for fruit in fruits:
    print(fruit)


# List comprehension

squares = [x**2 for x in range(1, 6)]  
print(squares)  


# Sort List
#( isne jo sort kiya hai wo ascending order me sort kiya hai).
numbers = [5,3,8,1,2]
numbers.sort()
print(numbers)


# Slicing

print(fruits[1:3])


# Length of List

print(len(fruits))