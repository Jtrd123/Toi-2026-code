safe_f = input()
safe_l = input()

if safe_f == "H" and safe_l == "4567" :
  print("safe unlocked")
elif safe_f == "H":
  print("safe locked - change digit")
elif safe_l == "4567":  
  print("safe locked - change char")
else:
  print("safe locked")