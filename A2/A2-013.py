pearl, count_pearl = input().split()

if pearl == "H" :
  pearl = 5
elif pearl == "O" :
  pearl = 3
elif pearl == "J" :
  pearl = 2

energy = {
  ("R", "1"): 12, ("R", "2"): 18, ("R", "3"): 25,
  ("T", "1"): 15, ("T", "2"): 20, ("T", "3"): 30,
  ("M", "1"): 10, ("M", "2"): 15, ("M", "3"): 20,
}

type_tea = input().split()

total_energy = (pearl * int(count_pearl)) + ( energy[(type_tea[0], type_tea[1])] * int(type_tea[2]) )
print(total_energy)