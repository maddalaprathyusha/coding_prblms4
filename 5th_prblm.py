def findSingleElement(A):
    result = 0
    for num in A:
        result ^= num
    return result

# Example usage:
input_1 = [1, 2, 2, 3, 1]
input_2 = [1, 2, 2]

output_1 = findSingleElement(input_1)
output_2 = findSingleElement(input_2)

print("Output 1:", output_1)
print("Output 2:", output_2)
