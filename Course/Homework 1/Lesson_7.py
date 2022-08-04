# Task #1 
# arr = [10, 20, 30]

# def binarySearch(arr, arr_len, length, value):
#     if length >= arr_len:
#         mid = arr_len + (length - arr_len) // 2
#         if arr[mid] == value:
#             return mid
#         elif arr[mid] > value:
#             return binarySearch(arr, l, mid - 1, value)
#         else:
#             return binarySearch(arr, mid + 1, length, value)
#     else:
#         return -1


# print(binarySearch(arr, 0, len(arr) - 1, 20))




# def fibonacci_rec(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)

def fibonacci_iter(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

print(fibonacci_iter(10))

n = int(input('Enter n: '))
cache = []*n
cache[0] = 0
cache[1] = 1
def fibonachi_cache(n):
    if n <= 1:
        return cache[n]
    if cache[n] == 0:
        return fibonachi_cache(n - 1) + fibonachi_cache(n - 2)

    return cache[n]

print(fibonachi_cache(10))