def read_grid_from_file(file_name):
    """
    Reads the grid from the given file and returns it as a list of strings.
    """
    with open(file_name, "r") as file:
        return [line.strip() for line in file.readlines()]

def count_x_pattern(grid):
    """
    Counts the occurrences of a specific "X" pattern in the grid.
    """
    num_rows = len(grid)
    num_cols = len(grid[0])
    pattern_count = 0

    # Check if a position forms the desired "X" pattern
    def matches_pattern(row, col):
        # Ensure the position is within the valid range
        if row - 1 < 0 or row + 1 >= num_rows or col - 1 < 0 or col + 1 >= num_cols:
            return False

        # Define the diagonal elements
        primary_diag = [grid[row - 1][col - 1], grid[row][col], grid[row + 1][col + 1]]
        secondary_diag = [grid[row - 1][col + 1], grid[row][col], grid[row + 1][col - 1]]

        # Valid configurations for the diagonals
        valid_config = {"MAS", "SAM"}
        return ''.join(primary_diag) in valid_config and ''.join(secondary_diag) in valid_config

    # Loop through the grid to find all pattern matches
    for row in range(num_rows):
        for col in range(num_cols):
            if matches_pattern(row, col):
                pattern_count += 1

    return pattern_count

# Main program
if __name__ == "__main__":
    input_file = "input.txt"  # Replace with your file name
    grid = read_grid_from_file(input_file)
    result = count_x_pattern(grid)
    print(f"The X pattern appears {result} times in the grid.")
