def calculate_similarity(file_path):
    count = 0

    # Read the file and process each line
    with open(file_path, 'r') as file:
        for line in file:
            levels = list(map(int, line.split()))
            n = len(levels)
            safe = False

            # Function to check if a report is safe
            def is_safe(levels):
                res = []
                if levels[0] > levels[-1]:  # Decreasing
                    for i in range(len(levels) - 1, 0, -1):
                        if 1 <= levels[i - 1] - levels[i] <= 3:
                            res.append(1)
                        else:
                            break
                else:  # Increasing
                    for i in range(len(levels) - 1):
                        if 1 <= levels[i + 1] - levels[i] <= 3:
                            res.append(1)
                        else:
                            break
                return len(res) == len(levels) - 1

            # Check if the current report is already safe
            if is_safe(levels):
                safe = True
            else:
                # Try removing each level and check if the report becomes safe
                for i in range(n):
                    modified_levels = levels[:i] + levels[i + 1:]
                    if is_safe(modified_levels):
                        safe = True
                        break

            if safe:
                count += 1

    return count

# Call the function with the input file
file_path = 'input.txt'  # Replace with your file path
result = calculate_similarity(file_path)
print("Total similarity score:", result)
