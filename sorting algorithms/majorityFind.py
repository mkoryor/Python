



def majorityFind(arr):

    candidate = arr[0]
    count = 1

    for i in range(len(arr)):
        if arr[i] == candidate:
            count += 1

        elif count > 0:
            count -= 1
        
        else:
            candidate = arr[i]
            count = 1   

    # check arr, verify candidate is majority
    count = 0
    for i in range(len(arr)):
        if arr[i] == candidate:
            count += 1
    
    return candidate if count > len(arr) // 2 else None

print(majorityFind([1,2,4,1,1]))
  


