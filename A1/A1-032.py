n = int(input())

for i in range(0, 5, 2) :
    if n - i >= 1:
        print("*" * (n - i))