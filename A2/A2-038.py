n = int(input())

total_fire = 0
total_water = 0
total_earth = 0

for _ in range(n) :
    F1, W1, E1, F2, W2, E2 = map(int, input().split())

    sum1 = F1 + W1 + E1
    sum2 = F2 + W2 + E2

    if sum1 >= sum2 :
        total_fire += F1
        total_water += W1
        total_earth += E1
    elif sum1 < sum2 :
        total_fire += F2
        total_water += W2
        total_earth += E2

total_score = total_fire + total_water + total_earth

print(total_score)
print(f'{total_fire} {total_water} {total_earth}')

if total_fire > total_water + total_earth :
    print('YES')
else:
    print('NO')