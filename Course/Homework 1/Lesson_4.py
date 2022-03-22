"""
Վարժություն 1.11
f ֆունկցիան սահմանվում է հետևայլ կերպ.
f(n) = n, եթե n < 3
f(n) = f(n - 1) + f(n - 2) + f(n - 3), եթե n >= 3
n-ը կարող է լինել միայն 0 և դրական ամբողջ թիվ։ Իրականացրեք լուծումը ռեկուրսիվ,
իտերատիվ և պոչավոր ռեկուրսիվ տարբերակներով։
"""

# ռեկուրսիվ


def rec(n):
    if n in [0, 1, 2, 3]:
        return n
    else:
        return rec(n - 1) + rec(n - 2) + rec(n - 3)


print(rec(4))  # => 6
print(rec(3))  # => 3

# իտերատիվ


def iter(n):
    arr = [0, 1, 2, 3]
    while n <= 3:
        return n
    else:
        tmp = iter(n - 1) + iter(n - 2) + iter(n - 3)
        arr.append(tmp)
        return tmp


print(iter(4))
print(iter(3))

# պոչավոր ռեկուրսիվ


def tail(n):
    a = 0
    b = 1
    c = 2

    if n < 0:
        print("Incorrect input")

    # Check is n is equal
    # to 0
    elif n <= 3:
        return n

    else:
        for i in range(1, n):
            d = a + b + c
            a = b
            b = d
        return b


print(iter(4))
print(iter(3))

"""
Վարժություն 1.12
Եռանկյան կողմերում գտնվող բոլոր թվերը հավասար են 1-ի, իսկ եռանկյան ներսում 
գտնվող թվերից յուրաքանչյուրը հավասար է նրա վերևի երկու թվերի գումարին։ 
Գրեք ռեկուրսիվ ֆունկցիա, որը հաշվում է Պասկալի եռանկյունու անդամի արժեքը։


Պասկալի եռանկյունը եռանկյունու օրինաչափություն է, որը հիմնված է nCr-ի վրա:
Պետք է օգտագործել nCr բանաձեւը, այսինքն՝ n!/(n-r)!r!
"""


def generateNthRow(N):

    # nC0 = 1
    prev = 1
    print(prev, end='')

    for i in range(1, N + 1):

        # nCr = (nCr-1 * (n - r + 1))/r
        curr = (prev * (N - i + 1)) // i
        print(",", curr, end='')
        prev = curr


print(generateNthRow(5))  # => 1, 5, 10, 10, 5, 1
