# Global variable to store the total difference
total_difference = 0

def process_file(file_path):
    global total_difference
    left = []
    right = []

    # Read the file and populate the lists
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():  # Skip empty lines
                l, r = map(int, line.split())
                left.append(l)
                right.append(r)

    # Sort both lists
    left.sort()
    right.sort()

    

    # Calculate the total difference
    for l, r in zip(left, right):
        total_difference += abs(l - r)

    return total_difference

# Call the function with the input file
file_path = 'input.txt'  # Replace with your file path
result = process_file(file_path)
print("Total difference:", result)
