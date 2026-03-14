month = int(input())
day = int(input())

# if month == 1 or month == 2:
#   season = "winter"
# elif month == 3:
#   season = "spring" if day >= 21 else "winter"
# elif month == 4 or month == 5:
#   season = "spring"
# elif month == 6:
#   season = "summer" if day >= 21 else "spring"
# elif month == 7 or month == 8:
#   season = "summer"
# elif month == 9:
#   season = "fall" if day >= 23 else "summer"
# elif month == 10 or month == 11:
#   season = "fall"
# elif month == 12:
#   season = "winter" if day >= 22 else "fall"

# print(season)




if month < 12 and month % 3 == 0 and day >= 21:
  month += 1
elif month == 12 and day >= 21:
  month = 1

if month in [1,2,3] :
  season = "winter"
elif month in [4,5,6] :
  season = "spring"
elif month in [7,8,9] :
  season = "summer"
elif month in [10,11,12] :
  season = "fall"

print(season)