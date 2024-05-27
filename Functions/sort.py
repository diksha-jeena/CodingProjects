def sort_numbers(numbers):
    numbers.sort()
    return numbers

# Main 
nums = []

n = int(input("Enter the number of elements in the list: "))
print("Enter the elements:")

for i in range(n):
    num = float(input())
    nums.append(num)

sorted_nums = sort_numbers(nums)
print("Sorted numbers in ascending order:", sorted_nums)
