def linear_search(arr, target):
  l = len(arr)
  print(l)
  for i in range(l):
    if arr[i] == target:
      return i
  return -1

arr = [5,4,3,2,1,5]
target = 5


result = linear_search(arr,target)

if result != -1:
  print("element found on index",result)

else:
  print("element not found")