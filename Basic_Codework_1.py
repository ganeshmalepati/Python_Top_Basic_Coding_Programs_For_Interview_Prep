"""
    Odd or Even Program
"""

def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter a number: "))
print(even_odd(num))


"""
    Max of three Numbers
"""

def max_three_num(a, b, c):
    if a > b and a > c :
        return f"Max number is {a}"
    elif b > a and b > c:
        return f"Max number is {b}"
    else:
        return f"Max number is {c}"

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
print(max_three_num(a, b, c))
    



"""
    Swap of two numbers
"""
def swap_two_var(var_1, var_2):
    var_1 = var_1 + var_2
    var_2 = var_1 - var_2
    var_1 = var_1 - var_2
    return var_1, var_2

var_1 = int(input("Enter var_1 number: "))
var_2 = int(input("Enter var_1 number: "))
print(swap_two_var(var_1, var_2))



"""
    Palindrome of a string
"""
def check_palindorme_string(s):
    cleaned_string = ''.join(s.split()).lower()
    left, right = 0, len(cleaned_string)-1
    while left < right:
        if cleaned_string[left] != cleaned_string[right]:
            return False
        else:
            left += 1 
            right -= 1
    return True

s = input("Enter a string: ")
print(check_palindorme_string(s))




"""
    Reverse of a string
"""
def reverse_string(s):
    r_string = ""
    for char in s:
        r_string = char + r_string
    return r_string

s = input("Enter some string:")
print(reverse_string(s))



"""
    Counting vowels in a string and and printing vowels
"""
def count_vowels_string(s):
    vowels_elements = {}
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
            vowels_elements[char] = vowels_elements.get(char, 0) + 1
    return count, vowels_elements
    

s = input("Enter some string: ")
print(count_vowels_string(s))




from collections import Counter

def vowels_count(s):
    vowels = set("aeiouAEIOU")
    fileterd = [char for char in s if char in vowels]
    count = Counter(fileterd)
    total = sum(count.values())
    return total, dict(count)

s = input("Enter a string: ")
total, details = vowels_count(s)
for v, c in details.items():
    print(f"V: {v} and C: {c}")



"""
    Factorial of a number
"""
def factorial_num(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial_num(num - 1)

num = int(input("Enter a number: "))
print(factorial_num(num))



def fact_num(number):
    if number < 0:
        return "Factorail is not negative"
    result = 1
    for i in range(1, number+1):
        result *= i
    return result


number = int(input("Enter a number: "))
print(fact_num(number))



"""
    Fibonacci Series
"""

def fibonacci_series(n):
    n1, n2 = 0, 1
    result = []
    for i in range(0, n):
        result.append(n1)
        n1, n2 = n2, n1+n2
    return result

n = int(input("Enter a number: "))
print(fibonacci_series(n))


def fib_generator(n):
    a, b = 0, 1
    for _ in range(0, n):
        yield a
        a, b = b, a+b

n = int(input("Enter a number: "))
print(fibonacci_series(n))




def prime_number(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

n = int(input("Enter a number: "))
print(prime_number(n))
            
    