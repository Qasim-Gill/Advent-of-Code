import re

def count_word_occurrences(puzzle, word):
    """Counts the occurrences of a word in a word search puzzle.

    Args:
        puzzle: A list of strings representing the puzzle.
        word: The word to search for.

    Returns:
        The number of occurrences of the word.
    """

    rows = len(puzzle)
    cols = len(puzzle[0])
    count = 0

    # Check horizontal and vertical occurrences
    for i in range(rows):
        for j in range(cols - len(word) + 1):
            if puzzle[i][j:j+len(word)] == word:
                count += 1

    # Check diagonal occurrences (top-left to bottom-right)
    for i in range(rows - len(word) + 1):
        for j in range(cols - len(word) + 1):
            if all(puzzle[i+k][j+k] == word[k] for k in range(len(word))):
                count += 1

    # Check diagonal occurrences (top-right to bottom-left)
    for i in range(rows - len(word) + 1):
        for j in range(len(word) - 1, cols):
            if all(puzzle[i+k][j-k] == word[k] for k in range(len(word))):
                count += 1

    return count

# Read the puzzle from the input file
with open("input.txt", "r") as f:
    puzzle = f.read().splitlines()

# Count the occurrences of "XMAS"
word = "XMAS"
occurrences = count_word_occurrences(puzzle, word)

print(f"The word '{word}' appears {occurrences} times in the puzzle.")
