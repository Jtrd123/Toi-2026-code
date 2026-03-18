f_name = input()
l_name = input()
age = int(input())

if len(f_name) > 5 and len(l_name) > 5 :
  print(f'{f_name[:2]}{l_name[-1]}{str(age)[-1]}')
else:
  print(f'{f_name[0]}{age}{l_name[-1]}')
