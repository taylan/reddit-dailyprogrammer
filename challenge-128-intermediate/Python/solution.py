def initialize_grid(lines):
    grid = []
    for line in lines:
        grid.append([cell for cell in line.strip().split(' ')])
    return grid


def all_roads_repaired(grid):
    return sum([len([cell for cell in row if cell == '0' or cell[0] == '-']) for row in grid]) == 0


def repair_column(grid, col):
    print("Column {0} repaired.".format(col))
    for col, row in [(col, x) for x in range(len(grid))]:
        grid[row][col] = 'x'
    pass


def repair_row(grid, row):
    print("Row {0} repaired.".format(row))
    for col, row in [(x, row) for x in range(len(grid))]:
        grid[row][col] = 'x'
    pass


def main():
    with open("input.txt") as input_file:
        grid = initialize_grid(input_file.read().splitlines()[1:])
    col_grid = list(zip(*grid))

    if all_roads_repaired(grid):
        print('No broken roads.')
        exit(0)

    to_repair = dict()

    for row_num, row in enumerate(grid):
        to_repair['r' + str(row_num)] = len([cell for cell in row if cell == '0' or cell.startswith('-')])
        for col_num, col in enumerate(row):
            to_repair['c' + str(col_num)] = len([cell for cell in col_grid[col_num] if cell == '0' or cell.startswith('-')])

    for thingy in sorted(to_repair, key=to_repair.get, reverse=True):
        func = repair_column if thingy.startswith('c') else repair_row
        func(grid, int(thingy[1]))
        if all_roads_repaired(grid):
            break

    print()
    [print(' '.join(line)) for line in grid]

if __name__ == "__main__":
    main()