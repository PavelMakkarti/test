


test_matrix = [
        [1, 2, 3],
        [7, -1, 2],
        [123, 2, -1]
]
b = []
for row in test_matrix:
    max_value = row[0]
    for column_index in range(len(row)):
        if max_value < row[column_index]:
            max_value = row[column_index]
    b.append(max_value)
print(max(b))






