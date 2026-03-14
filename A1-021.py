year = int(input())

if year <= 1582:
    if year % 4 == 0:
        print("yes")
    else:
        print("no")
else:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("yes")
    else:
        print("no")