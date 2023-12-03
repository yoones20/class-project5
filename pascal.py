def generate_pascal_triangle(row, current_row=[]):
    if row == 0:
        return

    else:
        yield current_row
        next_row = [1] + [current_row[i] + current_row[i + 1] for i in range(len(current_row) - 1)] + [1]
        yield from generate_pascal_triangle(row - 1, next_row)

rows_to_generate = 5

for i, row in enumerate(generate_pascal_triangle(rows_to_generate)):
    print(f"Row {i + 1}: {row}")