# decimal => binary
decimal_number = 13

binary_number = bin(decimal_number)[2:]
print(binary_number)    # 1101

# << left shift and >> right shift
result = decimal_number << 2
print(result, bin(result))  # 0b_110111

result = decimal_number >> 2
print(result, bin(result))  # 0b_11
