import numpy as np

num = 11
sign = np.sign(num)

if sign==1:
    print("Positive")
elif sign == -1:
    print("Negative")
else:
    print("Zero")