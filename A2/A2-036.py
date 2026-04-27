num, query = map(int, input().split())

diff = [0] * 1442

for _ in range(num) :
    start, stop = map(int, input().split())
    diff[start] += 1
    diff[stop + 1] -= 1

    open_shop = [0] * 1442
    curr_open = 0
    for i in range(1442) :
        curr_open += diff[i]
        open_shop[i] = curr_open

q_time = list(map(int, input().split()))

results = []
for q in q_time :
    results.append(str(open_shop[q]))
    
print(*results)
