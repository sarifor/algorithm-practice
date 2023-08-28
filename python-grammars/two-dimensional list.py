# 1. Creating a two-dimensional list
a = [[10, 20], [30, 40], [50, 60]] # row, column
print(a) # [[10, 20], [30, 40], [50, 60]]


# 2. Accessing elements
print(a[0][1]) # 20(Access a row first, then a column)


# 3. Accessing elements using for-statement

# 3.1 Using nested for-statements
a = [[10, 20], [30, 40], [50, 60]]
for i in a:
    for j in i:
        print(j, end=' ')
    print()

# 3.2 Using for-statement and range
b = [[101, 102], [103, 104], [105, 106]]
for i in range(len(b)):
    for j in range(len(b[i])):
        print(b[i][j], end=' ')
    print()