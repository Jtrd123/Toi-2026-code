num = int(input())

start = (num // 10) * 10

print(*(range(start, -1, -10)))