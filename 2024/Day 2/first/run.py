def calculate_similarity(file_path):

    count = 0

    # Read the file and populate the lists
    with open(file_path, 'r') as file:
        for line in file:
            li = line.split()
            # print(li)
            first = int(li[0])
            last = int(li[-1])
            res = []
            if first > last: # decreasing
                for i in range(len(li)-1, 0, -1):
                    if 1 <= int(li[i-1])-int(li[i]) <= 3:
                        res.append(1)
                    else:
                        break
            else: # increasing
                for i in range(len(li)-1):
                    if 1 <= int(li[i+1])-int(li[i]) <= 3:
                        res.append(1)
                    else:
                        break

            if len(res) == len(li)-1:
                count += 1

    return count

# Call the function with the input file
file_path = 'input.txt'  # Replace with your file path
result = calculate_similarity(file_path)
print("Total similarity score:", result)

