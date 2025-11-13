"""
    Reverse of number in two different ways with TC and SC
    1. TC:- O(n) and SC:- O(1)
    2. TC:- O(n) and SC:- O(1)
"""



def reverse_of_num(num):
    rev_num = 0
    while num > 0:
        rev_num = (rev_num * 10) + (num % 10)
        num //= 10
    return rev_num

num = 23456
print(reverse_of_num(num))




def reverse_num(number, rev = 0):
    if number == 0:
        return rev
    return reverse_num(number // 10, rev = (rev*10) + (number%10))

number = 34567
print(reverse_num(number))


"""
    Fibonacci Series of a nth number series in different ways
    1. Using the Recursive method 
    2. Using Generator approach 
    3. Iterative Approach

"""

def fibonocci_series(num):
    if num <= 1:
        return num
    return fibonocci_series(num-1) + fibonocci_series(num-2)

num = 9
sequenc_fib = [fibonocci_series(i) for i in range(num)]
print(sequenc_fib)



def fibanocci_num_series(n):
    n1, n2 = 0, 1
    for _ in range(n):
        yield n1
        n1, n2 = n2, n1+n2

n = 8
print(list(fibanocci_num_series(n)))


def series_for_fibanocci(n):
    n1, n2 = 0, 1
    sequence_series = []
    for _ in range(n):
        sequence_series.append(n1)
        n1, n2 = n2, n1+n2
    return sequence_series

n = 7
print(series_for_fibanocci(n))



"""
    Checking whether two strings are Anagram or not 
    Anagram:- “listen” → “eilnst”  “silent” → “eilnst”
    Both are the same, so “listen” and “silent” are anagrams.
    1. Using Dictionary and Loop 
    2. Counting Using Dictionary
"""


def check_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False
    freq = {}

    for char in s1:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    
    for char in s2:
        if char not in freq:
            return False
        freq[char] -= 1
        if freq[char] < 0:
            return False
    return True

s1 = "silent"
s2 = "listen"

print(check_anagrams(s1, s2))


def anagram_check_dict_count(s1, s2):
    if len(s1) != len(s2):
        return False
    anagram_count = {}
    for char in s1:
        anagram_count[char] = anagram_count.get(char, 0) + 1
    for char in s2:
        if char not in anagram_count or anagram_count[char] == 0:
            return False
        anagram_count[char] -= 1
    return True

s1 = "bat"
s2 = "tab"
print(anagram_check_dict_count(s1, s2))




"""
    Palindrome Code snippet 
    1. Two-Pointer Technique with TC:- O(n) and SC:- O(1) for string
    Here left start with 0 index and right start with len(s)-1 and incresing the left length and decresing the right length.

"""

def check_palindrome_of_string(s):
    left, right = 0, len(s)-1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

s = "madam"
print(check_palindrome_of_string(s))


def check_palindrome_of_number(s):
    num = str(s)
    left, right = 0, len(num)-1
    while left < right:
        if num[left] != num[right]:
            return False
        left += 1
        right -= 1
    return True

s = 12321
print(check_palindrome_of_number(s))

 
"""
    Frequency of character in String or Occurence of a each char in a given String
    Using Dictionary with For Loop
"""

def frequency_of_char_string(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

s = "Ganesh Malepati"
print(frequency_of_char_string(s))


def Occurence_String(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

s = "Run this code in docker and jenkins"
print(Occurence_String(s))


"""
    To Check whether it's a leap year or not

"""

def Leap_or_not_leap_year(year):
    if year % 400 == 0:
        return True
    elif (year%4 == 0) and (year%100 != 0):
        return True
    else:
        return False

year = 2025
print(Leap_or_not_leap_year(year))




"""
    Non-repeating Character in a given String

"""

def Non_repeat_char_string(s):
    new_s = {}
    for char in s:
        new_s[char] = new_s.get(char, 0) + 1
    return [char for char in s if new_s[char] == 1]
        
s = "swiss bank"
print(Non_repeat_char_string(s))



"""
    Replace the old sub-string with new sub-string using split and join case
"""


def replace_substring_string(s, old, new):
    parts = s.split(old)
    return new.join(parts, )


s = "Hey Ganesh, I'm steve from stranger things!"
old = "steve"
new = "Lucas"
print(replace_substring_string(s, old, new))


def even_odd_num(num):
    if num % 2 == 0:
        return True
    else:
        return False

num = 798934351
print(even_odd_num(num))



def Max_Three_Num(a, b, c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

a = 2345262
b = 2452676
c = 2636373
print("Max Number among three numbers is: {}".format(Max_Three_Num(a, b, c)))




def Swap_two_num(num1, num2):
    num1 = num1 + num2
    num2 = num1 - num2
    num1 = num1 - num2
    return num1, num2

num1 = 23426
num2 = 57375
print("After swaping two numbers are: {}".format(Swap_two_num(num1, num2))
