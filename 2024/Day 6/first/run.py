def load_map(file_path):
    with open(file_path, 'r') as file:
        return [list(line.strip()) for line in file]

def patrol_route(grid):
    movement = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    move_sequence = ['^', '>', 'v', '<']

    # Locate the initial position and orientation of the guard
    for row_idx, row in enumerate(grid):
        for col_idx, cell in enumerate(row):
            if cell in movement:
                current_pos = (row_idx, col_idx)
                current_dir = cell
                break

    traversed = set()
    num_rows, num_cols = len(grid), len(grid[0])

    while 0 <= current_pos[0] < num_rows and 0 <= current_pos[1] < num_cols:
        traversed.add(current_pos)

        row_offset, col_offset = movement[current_dir]
        next_pos = (current_pos[0] + row_offset, current_pos[1] + col_offset)

        if 0 <= next_pos[0] < num_rows and 0 <= next_pos[1] < num_cols and grid[next_pos[0]][next_pos[1]] == '#':
            # Adjust direction by turning 90 degrees clockwise
            current_dir = move_sequence[(move_sequence.index(current_dir) + 1) % 4]
        else:
            # Proceed to the next cell
            current_pos = next_pos

    return traversed

def update_map(grid, traversed):
    for row_idx, col_idx in traversed:
        if grid[row_idx][col_idx] == '.':
            grid[row_idx][col_idx] = 'X'

def process_file(file_path):
    grid = load_map(file_path)
    traversed = patrol_route(grid)
    update_map(grid, traversed)

    # Display the updated grid and traversal count
    for row in grid:
        print(''.join(row))

    print("Unique positions visited:", len(traversed))

if __name__ == "__main__":
    file_path = "input.txt"
    process_file(file_path)
