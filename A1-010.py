age = int(input())
status = input()

if (age < 18) or (status == 's' or status == 'S'):
  print('20')
else:
  print('50')