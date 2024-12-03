import re

def parse_mul_instructions(corrupted_memory):
    """Parses corrupted memory for valid 'mul' instructions and calculates their sum.

    Args:
        corrupted_memory: A string containing the corrupted memory dump.

    Returns:
        The sum of the results of all valid 'mul' instructions.
    """

    mul_pattern = r"mul\s*\(([0-9]+),\s*([0-9]+)\)"
    total_sum = 0

    for match in re.finditer(mul_pattern, corrupted_memory):
        x, y = int(match.group(1)), int(match.group(2))
        total_sum += x * y

    return total_sum

# Read the corrupted memory from input.txt
with open("input.txt", "r") as f:
    corrupted_memory = f.read()

# Calculate and print the sum of valid 'mul' instructions
result = parse_mul_instructions(corrupted_memory)
print(result)