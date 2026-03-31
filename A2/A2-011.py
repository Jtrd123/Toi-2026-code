# nums = input().split()
# set_nums = set()
# ans = []

# for num in nums :
#   if num not in set_nums :
#     ans.append(num)
#     set_nums.add(num)

# print(" ".join(ans))

nums = input().split()

unique_nums = list(dict.fromkeys(nums))

print(" ".join(unique_nums))