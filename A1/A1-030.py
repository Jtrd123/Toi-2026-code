n = int(input())
nums = list(map(int, input().split()))

max_vals = []
total_sum = 0

for i in range(0, n*2, 2):
    max_num = max(nums[i], nums[i+1])
    max_vals.append(max_num)
    total_sum += max_num

if n == 1 :
    print(max_vals[0])
else:
    equation = " + ".join(map(str, max_vals))
    print(f'{equation} = {total_sum}')