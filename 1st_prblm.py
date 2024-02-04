def removeDuplicates(A):
    n = len(A)
    
    if n <= 1:
        return n
    
    index = 1  # Initialize the index for the answer array
    
    for i in range(1, n):
        if A[i] != A[i-1]:
            A[index] = A[i]
            index += 1
    
    return index

# Example usage:
input_1 = [1, 1, 2]
input_2 = [1, 2, 2, 3, 3]

output_1 = removeDuplicates(input_1)
output_2 = removeDuplicates(input_2)

print("Output 1:", output_1)
print("Output 2:", output_2)
