# Task1
def strmove(s, n):
    return s[n:] + s[:n]

# Task2
#Two ways to do it
def sum_of_multiples(n):
    return n * (n + 1) // 2

print(sum_of_multiples(1000))

def sum_of_multiples(n):
    return sum(x for x in range(n) if x % 3 == 0 or x % 5 == 0)

print(sum_of_multiples(1000))

# Task3

def fibonacci_odd_sum(n):
    a, b = 0, 1
    sum = 0
    while b < n:
        if b % 2 != 0:
            sum += b
        a, b = b, a + b
    return sum

print(fibonacci_odd_sum(4000000))
