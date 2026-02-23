year = int(input("enter a year :- "))

if (year % 400 == 0) and (year % 100 == 0):
  print("{0} entered year is leap year".format(year))
elif (year % 4 == 0) and (year % 100 != 0):
  print("{0} entered year is leap year".format(year))
else:
  print("{0} entered year is not leap year".format(year))
