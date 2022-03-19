
def ackermann(x, y):
    if y == 0:
        return 0
    elif x == 0:
        return 2 * y
    elif y == 1:
        return 2
    else:
        return ackermann(x - 1, ackermann(x, y - 1))


print(ackermann(1, 5))  # -> 32
print(ackermann(2, 4))  # -> 65536
print(ackermann(3, 3))  # -> 65536

"""
Կարճ նկարագրեք, թե ինչ են հաշվում a1, a2, և a3 ֆունկցիաները

>>> def a1(n):
	return ackermann(0, n)
>>> def a2(n):
	return ackermann(1, n)
>>> def a3(n):
	return ackermann(2, n)

Այս ֆունկցիաները հաշվում են ն-ի դեպքում Ակերմանի ֆունկցիան: 

"""
