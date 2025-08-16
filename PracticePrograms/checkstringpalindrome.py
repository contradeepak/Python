# Check String Palindrome


word = input("Enter a word: ")

# reverse the word using slicing
if word == word[::-1]:
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")





# Check Number Palindrome

num = int(input("Enter a number: "))

# convert to string and check

if str(num) == str(num)[::-1]:
    print(f"{num} is a palindrome number")
else:
    print(f"{num} in not a palindrome number")


