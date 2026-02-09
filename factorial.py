num=int(input("enter a number number :- ")) 

factorial = 1 

if num<0:
  print("Factorial doesn't exists for the negative number.")

elif num == 0:
  print("Factorial of the 0 is 1.")

else:
  for i in range(1,num+1):
    factorial=factorial*i
  print(f"factorial of the {num} is {factorial}")
