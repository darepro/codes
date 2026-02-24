def binary_search(arr,low,high,target):
    if low>high:
     return -1
  
    mid = (high + low) // 2 
    if arr[mid] == target :
      return mid
    elif arr[mid] > target :
     return binary_search(arr,low,mid-1,target)
    else:
     return binary_search(arr,mid+1,high,target)


arr = [10,20,30,40,50,60,70,80]
result = binary_search(arr,0,len(arr)-1,80)
print(result)