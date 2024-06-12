def longest_alternating_subsequence(X):
    if not X:
        return 0
    
    length = 1  # Start with the first element in the subsequence
    for i in range(1, len(X)):
        if X[i] != X[i-1]:
            length += 1
            
    return length

# Example usage
X1 = [0, 1, 0, 1, 0]
print(longest_alternating_subsequence(X1))  # Output: 5

X2 = [0]
print(longest_alternating_subsequence(X2))  # Output: 1
