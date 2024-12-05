import sys
from collections import defaultdict, deque
import pyperclip as clipboard

def output_result(result):
    print(result)
    clipboard.copy(result)

# Adjust recursion depth for handling deep recursions
sys.setrecursionlimit(10**6)

# Read the input data from the file
with open("input.txt", "r") as file:
    data = file.read().strip()

# Initialize counters for the results
result1 = 0
result2 = 0

# Dependencies: prerequisites and post-requisites
prerequisites = defaultdict(set)
postrequisites = defaultdict(set)

# Split the input data into dependency rules and page queries
rules, queries = data.split('\n\n')

# Parse dependency rules
for rule in rules.splitlines():
    page_a, page_b = map(int, rule.split('|'))
    prerequisites[page_b].add(page_a)
    postrequisites[page_a].add(page_b)

# Evaluate each page sequence in the queries
for sequence in queries.splitlines():
    pages = list(map(int, sequence.split(',')))
    assert len(pages) % 2 == 1  # Must be odd-length
    
    is_valid = True
    
    # Check if the sequence respects dependency rules
    for i, page_x in enumerate(pages):
        for j, page_y in enumerate(pages):
            if i < j and page_y in prerequisites[page_x]:
                is_valid = False
    
    if is_valid:
        # Add the middle page of the valid sequence to result1
        result1 += pages[len(pages) // 2]
    else:
        # Reorder pages to satisfy dependencies
        sorted_pages = []
        queue = deque()
        dependency_count = {page: len(prerequisites[page] & set(pages)) for page in pages}
        
        # Initialize queue with pages having no unmet prerequisites
        for page in pages:
            if dependency_count[page] == 0:
                queue.append(page)
        
        # Perform a topological sort to find a valid order
        while queue:
            current_page = queue.popleft()
            sorted_pages.append(current_page)
            for dependent_page in postrequisites[current_page]:
                if dependent_page in dependency_count:
                    dependency_count[dependent_page] -= 1
                    if dependency_count[dependent_page] == 0:
                        queue.append(dependent_page)
        
        # Add the middle page of the sorted sequence to result2
        result2 += sorted_pages[len(sorted_pages) // 2]

# Output results and copy to clipboard
output_result(result1)
output_result(result2)
# 4608
# 5723