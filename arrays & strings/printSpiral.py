





def printLayer(mat, layer, lastCol, lastRow):
    
    # single element in layer, print seperately bc other cases wont handle it
    if lastCol == layer and lastRow == layer:
        print(mat[layer][layer])
    
    # top row
    curr = layer
    while curr < lastCol:
        print(mat[layer][curr], end= " ")
        curr += 1
    
    # right column
    curr = layer
    while curr < lastRow:
        print(mat[curr][lastCol], end= " ")
        curr += 1

    # bottom row 
    curr = lastCol
    while curr > layer:
        print(mat[lastRow][curr], end = " ")
        curr -= 1

    # left column
    curr = lastRow
    while curr > layer:
        print(mat[curr][layer], end = " ")
        curr -= 1
        
    

def printSpiral(mat):

    for layer in range(len(mat) // 2):
        printLayer(mat, layer, len(mat[0]) - 1 - layer, len(mat) - 1 - layer)
    
    return mat

printSpiral([[1,2,3], [4,5,6], [7,8,9]])



