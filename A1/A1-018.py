num = int(input())
roman_numerals = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

if num < 0 :
  print('Error : Please input positive number')
elif num == 0 or num > 9 :
  print("Error : Out of range")
else:
  print(roman_numerals[num-1])
