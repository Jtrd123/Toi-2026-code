N = int(input())
cave = list(map(int, input().split()))
S = input()

pos = cave.index(1)

for char in S :
  next_pos = pos

  if char == 'R' :
    next_pos += 1
  elif char == 'L' :
    next_pos -= 1
  
  if 0 <= next_pos < N :

    if cave[next_pos] == 2 :
      cave[pos] = 0
      pos = next_pos
      cave[pos] = 1
      break

    else :
      cave[pos] = 0
      pos = next_pos
      cave[pos] = 1

print(" ".join(map(str, cave)))
