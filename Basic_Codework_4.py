"""
    Print numbers from 1 to 100 without using loop
    1. Using Generators concept
    2. Directly printing the elements
"""

def numbers_without_loop(start, end):
    if start > end:
        return 
    yield start

    yield from numbers_without_loop(start + 1, end)

print(*numbers_without_loop(1, 100), sep="\n")


def numbers_without_loop(n, i = 1):
    if i > n:
        return 
    print(i)
    numbers_without_loop(n, i + 1)

print(numbers_without_loop(10), sep="\n")



"""
    Sum of n natural numbers
    1. Without recursion
    2. With recursion
"""

def sum_of_n_numbers(n):
    sum_num = 0
    for i in range(1, n+1):
        sum_num += i
        i += 1
    return sum_num

n = int(input("Enter a number: "))
print(sum_of_n_numbers(n))


def sum_of_n_numbers_recursion(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return n + sum_of_n_numbers_recursion(n-1)

n = int(input("Enter a number: "))
print(sum_of_n_numbers_recursion(n))



"""
    An Armstrong number (a.k.a. narcissistic number) is a number that equals the sum of its digits each raised to the power of the number of digits.

    Example: 153 has 3 digits → 1^3 + 5^3 + 3^3 = 153 → ✔️ Armstrong
    Edge cases: Typically non-negative integers only. 0 is Armstrong (0^1 = 0).
"""

def armstrong_number(n):
    if n < 0:
         return False
    if n == 0:
        k = 1
    else:
        temp = n
        k = 0
        while temp > 0:
            temp //= 10
            k += 1
    total = 0
    temp = n
    while temp > 0:
        digit = temp % 10 
        total += digit ** k
        temp //= 10
    return total == n

n = 153
print(armstrong_number(n))


def armstrong_number_2(num):
    order = len(str(num)) # number of digits
    total = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        total += digit ** order
        temp //= 10
    return total == num, f"{num} is an Armstrong number"

num = int(input("Enter a number: "))
print(armstrong_number_2(num))



"""
    Print prime numbers in a range
    Choose the second case for better understanding
"""

def is_prime_number(n):
    if n < 0:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
        return True

def prime_range(start, end):
    start = max(2, start)
    if start > end:
        start, end = end, start
    for i in range(start, end+1):
        if is_prime_number(i):
            print(i)

n = int(input("Enter a number: "))
start = int(input("Enter a start number: "))
end = int(input("Enter a end number: "))

print(prime_range(start, end))



def prime_recognization(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

start = int(input("Enter start number: "))
end = int(input("Enter end number: "))
for i in range(start, end+1):
    if prime_recognization(i):
        print(i)


def prime_number_range(start, end):
    for num in range(start, end+1):
        if num > 1:
            for i in range(2, int(num**0.5)+1):
                if num % i == 0:
                    break
            else:
                print(num)

start = int(input("Enter start number: "))
end = int(input("Enter end number: "))
print(prime_number_range(start, end))



"""
    Sum of digits of a number
    1. Without Recursion
    2. With Recursion
"""

def sum_of_digits_num(num):
    sum_num = 0
    while num > 0:
        sum_num += num % 10
        num //= 10
    return sum_num

num = int(input("Enter a number: "))
print(sum_of_digits_num(num))



def sum_of_digits_rec(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits_rec(n // 10)

n = int(input("Enter a number: "))
print(sum_of_digits_num(n))



"""
    Count number of digits in a number
    1. Without recursion
    2. With recursion
"""

def count_num_digit(num):
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count

num = int(input("Enter a number: "))
print(count_num_digit(num))


def count_num_digit_recursion(n):
    if n == 0:
        return 0
    return 1 + count_num_digit_recursion(n // 10)

num = int(input("Enter a number: "))
print(count_num_digit(num))




"""
    Using Recursion for Basic Programs 
"""

def factorial_number(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_number(n-1)
    
n = int(input("Enter a number: "))
print(factorial_number(n))


def fibanocci_series_recursion(n):
    if n <= 1:
        return n
    else:
        return fibanocci_series_recursion(n-1) + fibanocci_series_recursion(n-2)

n = int(input("Enter a number: "))
sequence_fib = [fibanocci_series_recursion(i) for i in range(n)]
print(sequence_fib)


def palindrome_check_recursion(n, rev=0, original=None):
    if original == None:
        original = n
    if n == 0:
        return original == rev
    return palindrome_check_recursion(n // 10, (rev * 10 + n % 10), original)

n = int(input("Enter a number: "))
print(palindrome_check_recursion(n))



def sum_of_digits(n, count = 0):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)

n = int(input("Enter a number: "))
print(sum_of_digits(n))





def recursion_binary_search(arr, target, low, high):
    if low > high:
        return -1
    
    mid = low + (high - low) // 2
    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return recursion_binary_search(arr, target, low, mid - 1)
    else:
        return recursion_binary_search(arr, target, mid + 1, high)
    
my_list = [23, 53, 63, 75, 73, 846, 435, 856, 9679, 3453, 858, 9678, 456, 145, 857]
x = 846
result = recursion_binary_search(my_list, x, 0, len(my_list) - 1)
print(result)



def binary_search_recursive(arr, target, low, high):
    # Base case: range is empty, target not found
    if low > high:
        return -1

    # Find middle index
    mid = low + (high - low) // 2

    # Check the middle element
    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        # Search in the left half
        return binary_search_recursive(arr, target, low, mid - 1)
    else:
        # Search in the right half
        return binary_search_recursive(arr, target, mid + 1, high)


# Example usage
data = [1, 3, 4, 7, 9, 12, 15]
x = 9
index = binary_search_recursive(data, x, 0, len(data) - 1)
print(index)  # prints 4





"""
    lambda arguments : expression
    Short and concise code
    No need to define a function using def
    Commonly used with map(), filter(), reduce()
    Useful for one-time operations
"""

numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)


numbers = [10, 15, 20, 25, 30]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)


from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)


check_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check_even(7))  # Odd


add = lambda x, y: {"sum": x + y, "product": x * y}
print(add(4, 5))
