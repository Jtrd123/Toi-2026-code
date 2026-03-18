cal = [0, 100, 120, 200, 60]
total_cal = 0

while True :
    orders = int(input())

    if orders == 5:
        break
    
    total_cal += cal[orders]

print('Bye Bye')
print(f'Total Calories: {total_cal}')
