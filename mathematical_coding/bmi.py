def bmi(height,weight):
  return round((weight/height**2),2)


h = float(input("enter the height in meters :- "))
w = float(input("enter the weight in kg :- "))

bodymassindex = bmi(h,w)

print("your BMI is ",bodymassindex)

if bodymassindex <= 18.5:
  print("you are underweight.")
elif 18.5 < bodymassindex <= 24.9:
  print("your weight is normal.")
elif 24.9 < bodymassindex <= 29.29:
  print("you are overweight.")
else:
  print("you are obese.")