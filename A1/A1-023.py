temp = int(input())
unit = input()

if unit == 'c' or unit =='C' :
    new_temp = temp
elif unit == 'f' or unit == 'F' :
    new_temp = (temp-32)/9 * 5

if new_temp < 0 :
    print('solid')
elif new_temp > 100 :
    print('gas')
else :
    print('liquid')
