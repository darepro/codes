def bubble(arr):
  count = 0
  n = len(arr)
  for i in range (n-1):
    swapped = False
    for j in range(n-1-i):
      if arr[j]>arr[j+1]:
        arr[j+1],arr[j] = arr[j],arr[j+1]
        count = count + 1
        swapped = True
    if not swapped:
      break
  return count
arr = [1,2,3,4,5,7,6]
bubble(arr)
print(arr)