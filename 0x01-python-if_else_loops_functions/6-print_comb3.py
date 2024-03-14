#!/usr/bin/python3
for i in range(0, 9):
    for j in range(1, 10):
        if i != j and i < j:
            print(f"{i}", end="")
            if i == 8 and j == 9:
                print(f"{j}", end="\n")
            else:
                print(f"{j}", end=", ")
