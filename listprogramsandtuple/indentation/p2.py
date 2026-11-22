for i in range(3):              # outer loop
    for j in range(3):          # inner loop
        print(i, j)             # inside inner loop
    print("End of inner loop")  # inside outer but outside inner
print("Completely outside")     # outside both
