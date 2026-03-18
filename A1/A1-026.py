count_even = 0
count_odd = 0

for i in range(3):
    num = int(input())

    if num % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

print(f'even {count_even}')
print(f'odd {count_odd}')
