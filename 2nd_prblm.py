def countSetBits(A):
    count = 0
    while A > 0:
        count += A % 2
        A //= 2
    return count

input_1 = 11
output_1 = countSetBits(input_1)
print("Output 1:", output_1)
