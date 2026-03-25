width, height, n = map(int, input().split())
cost = int(input())

length = ((width + height) * 2) * n
total_cost = length * cost

print(length)
print(total_cost)
