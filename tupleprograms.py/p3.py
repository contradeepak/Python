# Convert list of tuples to dictionary (summing duplicates)

pairs = [("a",2), ("b",3), ("c",4)]

result = {}

for k, v in pairs:
    result[k] = result.get(k,0) + v
    print("Dictionary:", result)