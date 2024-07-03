# Write a Python function to find the maximum and minimum numbers from a sequence of numbers.
#Note: Do not use built-in functions.
def find_max_min(numbers):
    max_num = numbers[0]
    min_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    return max_num, min_num

numbers = [int(x) for x in input("Enter a sequence of numbers separated by spaces: ").split()]
max_num, min_num = find_max_min(numbers)
print("Maximum number:", max_num)
print("Minimum number:", min_num)