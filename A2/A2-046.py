T = int(input())

vowels = {'a', 'e', 'i', 'o', 'u'}

for i in range(1, T + 1):
  total_vowels = 0
  curr_consecutive = 0
  max_consecutive = 0

  text = input()

  for char in text :
    if char.lower() in vowels :
      total_vowels += 1
      curr_consecutive += 1

      if curr_consecutive > max_consecutive :
        max_consecutive = curr_consecutive
    else :
      curr_consecutive = 0

  print(f'Line {i}: vowels = {total_vowels}, max_consecutive = {max_consecutive}')
