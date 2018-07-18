Insertion sort

arr = [5,2,4,6,1,3]
for j in range(0, len(arr)):
    key = arr[j]
    i = j - 1
    while i >= 0 and arr[i] > key:
        arr[i+1] = arr[i]
        i = i - 1
    arr[i + 1] = key
#[1,2,3,4,5,6]


Linear_search(nums, v):
  i = None
  for j in range(len(nums)):
    if nums[j] = v:
      i = j
      return i
  return i

print(Linear_search([1,2,4,3], 5))
print(Linear_search([1,2,3,4], 4))
# None
# 3

  

Selection_sort
numbers = [2,3,5,2,8]

for i in range(len(numbers) - 1):
    min = i 
    for j in range(i + 1, len(numbers)):
        if numbers[j] < numbers[min]:
            min = j
    numbers[min] = numbers[i]
    
#[2,2,3,5,8]

