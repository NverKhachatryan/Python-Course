# Task 1
given_file = open('input.txt', 'r')

lines = given_file.readlines()
sum = 0

for line in lines:
    for c in line:
        if c.isdigit() == True:
            sum = sum + int(c)

print(sum)

given_file.close()

# Task 2

given_file = open('input.txt', 'r')

lines = given_file.readlines()

for line in lines:
    line = line.capitalize()
    print(line)

with open('output.txt', 'w') as output_file:
    for line in lines:
        output_file.write(line)


# Task 3

from collections import Counter
numbers = [1, 2, 3, 2, 5, 3, 3, 5, 6, 3, 4, 5, 7]

counts = dict(Counter(numbers))
duplicates = {key:value for key, value in counts.items() if value > 1}

print(duplicates)

# Task 4

given_file = open('input.txt', 'r')

value = given_file.read()

# count symbols in file
count = 0
for c in value:
    if c.isalpha() == True:
        count = count + 1

# Task 5

def removeThirdLetter(string):
    return string[:2] + string[3:]

print(removeThirdLetter('abcdef'))

# Task 6

given_file = open('input.txt', 'r')

value = given_file.read()

count = 0
# count duplicate words in file
for word in value.split():
    if word in value.split():
        count = count + 1


# Task 7

arr = [10, 20, 30]

# find the squrare of the arr elements
for i in range(len(arr)):
    arr[i] = arr[i] ** 2
    new_arr = arr


# Task 8    
def getSum(n):
    
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum
   
# Task 9

def getSumTimesTwo(n):
    sum = 0
    for digit in str(n): 
      sum *= int(digit)
      ans = sum - getSum(n)      
    return ans

# Task 10

def countOdd(n, m):
    count = 0
    for i in range(n, m):
        if i % 2 == 1:
            count += 1
    return count