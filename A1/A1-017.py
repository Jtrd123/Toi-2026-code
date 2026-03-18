y1 = int(input())
m1 = int(input())
d1 = int(input())
y2 = int(input())
m2 = int(input())
d2 = int(input())

if y1 < y2 :
  print('1')
elif y1 > y2 :
  print('2')
else:
  if m1 < m2 :
    print('1')
  elif m1 > m2 :
    print('2')
  else:
    if d1 < d2 :
      print('1')
    elif d1 > d2 :
      print('2')
    else:
      print('0')