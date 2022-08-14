def removeDuplicated(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)-1):
            if arr[i] == arr[j]:
                del arr[j]
    return arr


def mergeSortedArrays(arr1,arr2,m,n):
    new_arr = []
    i = 0
    j = 0
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            new_arr.append(arr1[i])
            i += 1
        else:
            new_arr.append(arr2[j])
            j += 1
    while i < m:
        new_arr.append(arr1[i])
        i += 1
    while j < n:
        new_arr.append(arr2[j])
        j += 1
    return new_arr

def isDuplicate(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[i] == arr[j]:
                return True
            return False


def findSingle(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)-1):
            if arr[i] == arr[j]:
                del arr[j]
    return arr

print(findSingle([1,2,2,1,5]))


def missingNumber(nums):
    n = len(nums)
    sum = 0
    for i in range(n):
        sum += i
    for i in range(n):
        sum -= nums[i]
    return sum


def findMaxConsecutiveOnes(nums):
    max = 0
    count = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
            if count > max:
                max = count
        else:
            count = 0
    return max


def findMaxSum(nums):
    max = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] > max:
                max = nums[i] + nums[j]
    return max

def largestPrimeFactor(n):
    i = 2
    while i * i <= n:
        while n % i == 0:
            n = n / i
        i += 1
    return n


def isPalindrome(n):
    for i in range(1000, 9999):
        n = str(n)
        if n == n[::-1]:
            return True
        else:
            return False


def isEvenlyDivisible(n):
    for i in range(1, 21):
        if n % i != 0:
            return False
    return True



def sumOfSquares(n):
    sum = 0
    for i in range(1, n+1):
        sum += i**2
    return sum



def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True