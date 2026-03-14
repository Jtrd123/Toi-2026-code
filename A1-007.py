text = input()
vowels = ['a', 'e', 'i', 'o', 'u']

for i in range(len(text)):
  if text[i] in vowels:
    print('yes')
  else:
    print('no')