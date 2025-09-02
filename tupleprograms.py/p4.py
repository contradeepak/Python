# Flatten tuple of tuples

def flatten(t):
    flat = []
    for item in t:
        if isinstance(item, tuple):
            flat.extend(flatten(item))
        else:
            flat.append(item)
    return flat

nested = (1, (2, (3, 4)), 5)
print("Flattened:", flatten(nested))