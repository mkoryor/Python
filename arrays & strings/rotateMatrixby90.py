


def rotate(mat, start, end):
    curr = 0

    while curr + start < end:
        temp = mat[start][start + curr] # save top
        mat[start][start + curr] = mat[end - curr][start] # left to top
        mat[end - curr][start] = mat[end][end - curr] # bottom to top
        mat[end][end - curr] = mat[start + curr][end] # right to bottom
        mat[start + curr][end] = temp  # top to right
        curr += 1


def rotateMatrixBy90(mat):

    for layer in range(len(mat) // 2):
        rotate(mat, layer, len(mat) - 1 - layer)
    
    return mat

print(rotateMatrixBy90([[1,2,3], [4,5,6], [7,8,9]]))



