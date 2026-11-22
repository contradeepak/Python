list1 = ["a","b","c"]
list2 = [1,2,3]

joined = list1+list2
print("Joined List:", joined)

list1.extend(list2)
print("After Extend:", list1)