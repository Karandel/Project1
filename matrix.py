matrix = [
    [1, 2 ,3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

matrix[1][2] = 20

print(matrix[1][2])

for rows in matrix:
    for item in rows:
        print(item)

coords = [0, 1, 2]
x, y ,z = coords
print(z)