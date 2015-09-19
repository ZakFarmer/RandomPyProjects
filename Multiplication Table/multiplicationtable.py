def table(columns, rows = None):
    if not rows:
        rows = columns

    width = len(str(rows * columns)) + 2

    print(' ' * width + '|', end = '')
    for num in range(1, columns + 1):
        print('{0:>{1}}'.format(num, width), end = '')
    print('\n' + '-' * ((columns + 1) * width + 1))

    for row in range(1, rows + 1):
        print('{0:>{1}} |'.format(row, width - 1), end = '')
        for column in range(1, columns + 1):
            print('{0:>{1}}'.format(row * column, width), end = '')
        print()

columns = int(input("Columns: "))
table(columns)
