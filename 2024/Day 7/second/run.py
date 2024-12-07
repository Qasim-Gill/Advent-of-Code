from itertools import product

def compute_result(numbers, operators):
    """
    Evaluates the expression formed by inserting the given operators into the numbers.
    """
    result = str(numbers[0])
    for i in range(len(operators)):
        if operators[i] == '+':
            result = str(int(result) + numbers[i + 1])
        elif operators[i] == '*':
            result = str(int(result) * numbers[i + 1])
        elif operators[i] == '||':
            result += str(numbers[i + 1])
    return int(result)

def process_input_data(file_path):
    """
    Parses the input file to extract test values and number lists.
    """
    equations = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            target_value, numbers_str = line.split(':')
            target_value = int(target_value)
            numbers = [int(num) for num in numbers_str.split()]
            equations.append((target_value, numbers))
    return equations

def find_matching_expressions(equations):
    """
    Determines which equations can be solved with the given operators.
    """
    total_calibration = 0
    for target_value, numbers in equations:
        num_positions = len(numbers) - 1
        for operator_combo in product(['+', '*', '||'], repeat=num_positions):
            try:
                result = compute_result(numbers, operator_combo)
                if result == target_value:
                    total_calibration += target_value
                    break
            except ValueError:
                pass  # Handle potential errors in string-to-int conversion
    return total_calibration

def main(file_path):
    """
    Main function to process the input file and calculate the total calibration value.
    """
    equations = process_input_data(file_path)
    total_calibration = find_matching_expressions(equations)
    print(f"Total Calibration Value: {total_calibration}")

if __name__ == "__main__":
    file_path = "input.txt"
    main(file_path)