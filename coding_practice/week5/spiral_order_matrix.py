"""
Spiral Matrix - LeetCode #54
"""
def spiralOrder(matrix):
    res = []
    while matrix:
        res += matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix: res.append(row.pop())
        if matrix: res += matrix.pop()[::-1]
        if matrix and matrix[0]:
            for row in matrix[::-1]: res.append(row.pop(0))
    return res

# Test
mat = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder(mat))  # [1,2,3,6,9,8,7,4,5]
