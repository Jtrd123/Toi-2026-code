text = input()
result = ""
count = 1

for i in range(1, len(text)):
  if text[i] == text[i - 1]:
    count += 1
  else:
    result += f'{count}{text[i - 1]}'
    count = 1

result += f'{count}{text[-1]}'
print(result)