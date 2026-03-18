num = int(input())

start = (num // 10) * 10

# for i in range(start, -1, -10):
#     print(i, end=" ")
# print()

print(*(range(start, -1, -10)))