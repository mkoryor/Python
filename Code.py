Selection_sort

arr = [5,2,4,6,1,3]
for j in range(0, len(arr)):
    key = arr[j]
    i = j - 1
    while i >= 0 and arr[i] > key:
        arr[i+1] = arr[i]
        i = i - 1
    arr[i + 1] = key
    


Linear_search(nums, v):
  i = None
  for j in range(len(nums)):
    if nums[j] = v:
      i = j
      return i
  return i
  
  
