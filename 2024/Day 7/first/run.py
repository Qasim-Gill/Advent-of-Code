from itertools import product

def calculate_expression(numbers, operators):
    """Calculates the result of an expression with given numbers and operators."""
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i + 1]
        elif operators[i] == '*':
            result *= numbers[i + 1]
    return result

def process_input_file(file_path):
    """Reads the input file and extracts test values and number lists."""
    equations = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            test_value, numbers_str = line.split(':')
            test_value = int(test_value)
            numbers = [int(num) for num in numbers_str.split()]
            equations.append((test_value, numbers))
    return equations

def find_valid_expressions(equations):
    """Determines which equations can be solved with + or * operators."""
    total_calibration = 0
    for target_value, numbers in equations:
        num_positions = len(numbers) - 1
        for operator_combo in product(['+', '*'], repeat=num_positions):
            result = calculate_expression(numbers, operator_combo)
            if result == target_value:
                total_calibration += target_value
                break
    return total_calibration

def main(file_path):
    """Main function to process the input file and calculate the total calibration value."""
    equations = process_input_file(file_path)
    total_calibration = find_valid_expressions(equations)
    print(f"Total Calibration Value: {total_calibration}")

if __name__ == "__main__":
    file_path = "input.txt"
    main(file_path)
# 2299996598890