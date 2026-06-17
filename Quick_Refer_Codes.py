def first_non_repeat_char(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    for char in freq:
        if freq[char] == 1:
            return char

s = "swiss"
print(first_non_repeat_char(s))


def count_vowels(s):
    vowels = "AEIOUaeiou"
    result = []
    count = 0
    for char in s:
        if char in vowels:
            count += 1
            result.append(char)
    return count, result

s = "Ganesh malepati"
print(count_vowels(s))


def remove_duplicates_from_string(s):
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)

s = "Apple"
print(remove_duplicates_from_string(s))



def longest_word_in_sentence(s):
    s = s.split()
    longest = ""
    for word in s:
        if len(word) > len(longest):
            longest = word
    return longest

s = "This laptop has been provided by the Capgemini"
print(longest_word_in_sentence(s))


def check_string_contains_only_num(s):
    for char in s:
        if not char.isdigit():
            return False
    return True
s = "F2345567"
print(check_string_contains_only_num(s))

def find_smallest_largest_element(data):
    # data.sort()
    # small = data[0]
    # large = data[-1]
    small = data[0]
    large = data[1]
    for i in data:
        if i < small:
            small = i
        if i > large:
            large = i
    return small, large



data = [122, 53, 635, 63, 75, 5757, 8, 35, 746, 868, 2424, 54, 5]
print(find_smallest_largest_element(data))


def common_elements_in_list(l1, l2):
    # seen = set(l2)
    result = [i for i in l1 if i in l2]
    # for i in l1:
    #     if i in seen:
    #         seen.add(i)
    return result

l1 = [1, 2, 3, 4, 5]
l2 = [3, 4, 1, 5, 7, 9]
print(common_elements_in_list(l1, l2))


def find_missing_num(data):
    n = max(data)
    expected = sum(data)
    actual = (n * (n + 1)) // 2
    return actual - expected

data = [2,3,4,5]
print(find_missing_num(data))



def sort_list(data):
    if len(data) <= 1:
        return data
    
    mid = len(data)//2
    left = sort_list(data[:mid])
    right = sort_list(data[mid:])
    return merge(left, right)

def merge(left, right):
    i = 0
    j = 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

data = [64, 34, 25, 12, 22, 11, 90]
print(sort_list(data))



def merge_two_dict(d1, d2):
    return d1 | d2
d1 = {"name": "Ganesh", "Age": 24}
d2 = {"Sex": "Male", "Occupation": "IT_Employee"}
print(merge_two_dict(d1, d2))


l1 = [23, 46, 767, 87, "Ganesh"]
result = {k:v for k, v in enumerate(l1)}
print(result)

d2 = {"Sex": "Male", "Occupation": "IT_Employee"}
result = {v:k for k, v in d2.items()}
print(result)


def group_elements_by_freq(data):
    freq = {}
    for i in data:
        freq[i] = freq.get(i, 0) + 1
    return freq

data = ["PASS", "FAIL", "PASS", "FAIL", "PASS", "PASS"]
print(group_elements_by_freq(data))


def longest_prefix_in_given_strings(data):
    if not data:
        return ""
    data.sort()
    first = data[0]
    last = data[-1]
    i = 0
    while i < len(first) and len(last) and first[i] == last[i]:
        i += 1
    return first[:i]

data = ["interview", "interval", "intermission", "inter"]
print(longest_prefix_in_given_strings(data))



def second_largest_element(l):
    first = second = float('-inf')
    for i in l:
        if i > first:
            second = first
            first = i
        elif first > i and i > second:
            second = i
    return second

my_list = [10, 20, 4, 50, 5, 15, 23, 123, 56, 70]
print(second_largest_element(my_list))



def check_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False
    freq = {}
    for i in s1:
        freq[i] = freq.get(i, 0) + 1

    for i in s2:
        if i not in freq or freq[i] == 0:
            return False
        freq[i] -= 1
    return True

s1 = "silent"
s2 = "listen"
b1 = "ball"
b2 = "labb"
print(check_anagrams(s1, s2))
print(check_anagrams(b1, b2))


def reverse_number(num):
    rev_num = 0
    while num > 0:
        rev_num = rev_num * 10 + num % 10
        num //= 10
    return rev_num

num = 34533525
print(reverse_number(num))



def reverse_number_given(num):
    rev_num = 0
    while num > 0:
        rev_num = rev_num * 10 + num % 10
        num //= 10
    return rev_num

num = 746363
print(reverse_number_given(num))


def reverse_string(s):
    rev_str = ""
    for char in s:
        rev_str = char + rev_str
    return rev_str

s = 'Ganesh malepati'
print(reverse_string(s))


def check_prime_number(num):
    if num == 0 or num == 1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or (num + 2 % i) == 0:
            return False
        i += 6
    return True

num = 19
print(check_prime_number(num))


def check_armstrong_number(num):
    order = len(str(num))
    arm_num = num
    temp = 0
    while arm_num > 0:
        digit = arm_num % 10
        temp += digit ** order
        arm_num //= 10
    return temp, f"{temp} is a armstrong number"

num = 153
print(check_armstrong_number(num))


def sum_of_digits(num):
    sum = 0
    while num > 0:
        digit = num % 10
        sum += digit
        num //= 10
    return sum

num = 34216935
print(sum_of_digits(num))


def check_palindrom_string(name):
    left = 0
    right = len(name)-1
    while left < right:
        if name[left] != name[right]:
            return False
        left += 1
        right -= 1
    return True

name = "malayalam"
data = "radar"
s1 = 'ganesh'
print(check_palindrom_string(s1))
print(check_palindrom_string(name))
print(check_palindrom_string(data))



def palindrome_string_caseincensitive(data):
    s = ''.join(char.lower() for char in data if char.isalnum())
    left = 0
    right = len(name)-1
    while left < right:
        if name[left] != name[right]:
            return False
        left += 1
        right -= 1
    return True

data = "12 A man, a plan, a canal: Panama 21"
print(palindrome_string_caseincensitive(data))



def check_fibonacci_series(num):
    n1 = 0
    n2 = 1
    series_fib = []
    for _ in range(num):
        series_fib.append(n1)
        n1, n2 = n2, n1+n2
    return series_fib

num = 9
print(check_fibonacci_series(num))


def factorial_num(num):
    if num == 0:
        return 1
    return num * factorial_num(num - 1)

num = 5
print(factorial_num(num))

def factorial(num):
    i = 1
    for a in range(1, num+1):
        i *= a
    return i

num = 6
print(factorial(num))



def compress_string_approach_2(s):
    if not s:
        return ""
    
    result = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result.append(s[i-1] + str(count))
            count = 1

    result.append(s[-1] + str(count))

    return ''.join(result)

s = "aaaaaaaabbccddddddeeeefggh"
print(compress_string_approach_2(s))

