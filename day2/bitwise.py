a = 10
b = 1


# ~ (bitwise NOT): Flips all bits (1's complement)
print("1's complement of b =", ~b)  # Output: -2

# & (bitwise AND): Only 1 where both bits are 1
print("a & b =", a & b)  # Output: 0 → 1010 & 0001 = 0000

# | (bitwise OR): 1 if any one bit is 1
print("a | b =", a | b)  # Output: 11 → 1010 | 0001 = 1011

# >> (right shift): Shifts bits to the right (divides by 2^b)
print("a >> b =", a >> b)  # Output: 5 → 1010 >> 1 = 0101

# << (left shift): Shifts bits to the left (multiplies by 2^b)
print("a << b =", a << b)  # Output: 20 → 1010 << 1 = 10100
