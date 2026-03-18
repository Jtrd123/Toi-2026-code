num_str = input()
operator = input()

reversed_str = num_str[::-1]

num1 = int(num_str)
num2 = int(reversed_str)

if operator == "+":
  result = num1 + num2
else:
  result = num1 * num2

print(f'{num1} {operator} {num2} = {result}')