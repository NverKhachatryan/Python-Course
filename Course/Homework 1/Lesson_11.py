# Task 1
def build_target_array(target, n):
    result = []
    for i in range(n):
        result.append("Push")
        result.append("Pop")
    return result

# Task 2

def find_intersection(arr1, arr2):
    result = []
    for i in arr1:
        if i in arr2:
            result.append(i)
    return result

# Task 3

def find_shortest_subarray(arr, target):
    result = []
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if sum(arr[i:j+1]) == target:
                result.append(j-i+1)
    return min(result)


# Task 4

def sortArrayByParity(nums):
    result = []
    for i in range(len(nums)):
        if i % 2 == 0:
            result.append(nums[i])
    for i in range(len(nums)):
        if i % 2 == 1:
            result.append(nums[i])
    return result


# Task 5

def sumOfUniques(arr):
    result = []
    for i in range(len(arr)):
        if arr[i] not in result:
            result.append(arr[i])
    return sum(result)

print(sumOfUniques([1,2,3,4,5]))

# Task 6

def strStr(haystack, needle):
    if needle in haystack:
        return haystack.index(needle)
    else:
        return -1

# Task 7

def lengthOfLastWord(s):
    s = s.split()
    if len(s) == 0:
        return 0
    else:
        return len(s[-1])

print(lengthOfLastWord("Hello World"))

# Task 8

def isPalindrome(s):
    s = s.lower()
    s = s.replace(" ", "")
    if s == s[::-1]:
        return True
    else:
        return False

# Task 9

def numUniqueEmails(emails):
    result = []
    for i in emails:
        i = i.split("@")
        i[0] = i[0].replace(".", "")
        i[0] = i[0].split("+")[0]
        result.append(i[0] + i[1])
    return len(set(result))

# Task 10

def searchRange(nums, target):
    result = []
    for i in range(len(nums)):
        if nums[i] == target:
            result.append(i)
    if len(result) == 0:
        return [-1, -1]
    else:
        return [result[0], result[-1]]