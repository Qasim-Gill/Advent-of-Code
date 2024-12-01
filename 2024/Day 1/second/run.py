from collections import Counter

def calculate_similarity(file_path):
    left = []
    right = []

    # Read the file and populate the lists
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():  # Skip empty lines
                l, r = map(int, line.split())
                left.append(l)
                right.append(r)

    # Count occurrences in the right list
    right_counts = Counter(right)

    # Calculate the similarity score
    similarity_score = sum(l * right_counts.get(l, 0) for l in left)

    return similarity_score

# Call the function with the input file
file_path = 'input.txt'  # Replace with your file path
result = calculate_similarity(file_path)
print("Total similarity score:", result)

