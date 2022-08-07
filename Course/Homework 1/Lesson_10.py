import urllib.request

# Task 1
def findSum():
    sum = 0
    for i in range(100):
        sum += i
    return sum

def findSquares():
    sum = 0
    for i in range(100):
        sum += i**2
    return sum

def final_ans():
    return findSquares() - findSum()

# Task 2

lines = urllib.request.urlopen('https://projecteuler.net/project/resources/p022_names.txt');


for line in lines:
    line = line.capitalize()
    print(line)

with open('output.txt', 'w') as output_file:
    for line in lines:
        output_file.write(line)

# Task 3

def isDigitPalindrome(number):
    number = str(number)
    if number == number[::-1]:
        return True
    else:
        return False