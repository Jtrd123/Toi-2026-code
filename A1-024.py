year = int(input())
size = int(input())
price = [1250, 1400, 2000, 1100, 1300, 1700, 1000, 1200, 1500]

if year <= 1990 :
    if size <= 1500:
        print(price[0])
    elif size > 2000:
        print(price[2])
    else:
        print(price[1])
elif year > 1990 and year < 2000 :
    if size <= 1500:
        print(price[3])
    elif size > 2000:
        print(price[5])
    else:
        print(price[4])
elif year >= 2000:
    if size <= 1500:
        print(price[6])
    elif size > 2000:
        print(price[8])
    else:
        print(price[7])
