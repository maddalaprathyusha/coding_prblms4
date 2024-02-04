def reverseBits(A):
    result = 0
    for _ in range(32):
        result = (result << 1) | (A & 1)
        A >>= 1
    return result

# Example usage:
input_1 = 0
input_2 = 3

output_1 = reverseBits(input_1)
output_2 = reverseBits(input_2)

print("Output 1:", output_1)
print("Output 2:", output_2)
