cost = int(input())

c10 = cost // 10 #หารเอาเฉพาะจำนวนเต็ม
rem = cost % 10 #หารเอาเศษที่เหลือจากการหารด้วย 10

c5 = rem // 5
rem = rem % 5

c2 = rem // 2
rem = rem % 2

c1 = rem // 1

print(f'10 = {c10}')
print(f'5 = {c5}')
print(f'2 = {c2}')
print(f'1 = {c1}')
