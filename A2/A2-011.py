nums = input().split()

unique_nums = list(dict.fromkeys(nums))

print(" ".join(unique_nums))