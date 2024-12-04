import random
import math

def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

  
# Open the output file for writing
output_file = open('output.txt', 'w')

# Open the input file for reading
with open("test.txt", "r") as input_file:
    data = input_file.readlines()
    total_cases = 0
    line_no = 1
    case_no = 0
    for line in data:
        word = line.split()
        prime = 0
        prime_list = list()
        if len(word) == 1 and line_no == 1:
            total_cases = int(word[0])
        elif line_no > 1 and len(word) == 1:
            digit = int(word[0])
            if digit > 2:         
                for i in range (digit, 1, -1):
                    if isPrime(i):
                        prime_list.append(i)
                for i in range(len(prime_list) - 1):
                    if (prime_list[i] - prime_list[i + 1]) in prime_list:
                        prime += 1
                
            case_no += 1
            out = f"Case #{case_no}: {prime}\n"
            print(out)
            output_file.write(out)

        line_no += 1


# Close the output file after writing
output_file.close()


