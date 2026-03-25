size, soup_type = input().split()

prices = {
  ('S', 'R'): 60, ('S', 'T'): 80,
  ('M', 'R'): 80, ('M', 'T'): 100,
  ('L', 'R'): 100, ('L', 'T'): 120
}

total_price = prices[(size, soup_type)]


topping_info = input().split()

if topping_info[0] == "P" :
  total_price += 15 * int(topping_info[1])
elif topping_info[0] == "E" :
  total_price += 10 * int(topping_info[1])

print(total_price)