matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

rows = len(matrix)
columns = len(matrix[0])

transpose = []

for i in range(columns):

    row = []

    for j in range(rows):
        row.append(matrix[j][i])

    transpose.append(row)

for row in transpose:
    print(row)



# Time complexity = O(rows × columns)
# Space complexity = O(rows × columns)
