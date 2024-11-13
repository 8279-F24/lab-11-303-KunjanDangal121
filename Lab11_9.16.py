# Write a program that gets a list of integers from input, and outputs negative
#  integers in descending order (highest to lowest).




# Get input from user and split it into a list of integers
numbers = list(map(int, input().split()))

# Filter to get only negative numbers and sort them in descending order
negative_numbers = sorted([num for num in numbers if num < 0], reverse=True)

# Print each number followed by a space, without an extra newline at the end
print(*negative_numbers, end=" ")
