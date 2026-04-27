n = int(input())
score_list = []

for i in range(n):
    score = int(input())
    score_list.append(score)

max_score = max(score_list)
max_idx = score_list.index(max_score)

count = 0
for num in score_list:
    if num == score_list[max_idx]:
        count += 1

print(max_score)
print(count)