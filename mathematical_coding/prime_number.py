num=int(input("enter a number a :- "))

flag = False 

if num == 1:
  print(f"{num} is not a prime number")
elif num>1:
  for i in range(2,num):
    if(num%i==0):
      flag=True
      break

if flag == True:
  print("the entered number is not prime.")

else:
  print("the entered number is prime number ")