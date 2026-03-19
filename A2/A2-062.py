text = input().lower()
vowels = ['a', 'e', 'i', 'o', 'u']
count = [0, 0, 0, 0, 0]

for char in text :
  if char in vowels:
    index = vowels.index(char)
    count[index] += 1

for i in range(5) :
  if count[i] > 0 :
    print(f"{vowels[i]}: {count[i]}")