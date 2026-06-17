print("Hello")


def even_odd(n):
    if n % 2 == 0:
        return "Even Number"
    else:
        return "Odd Number"
n = 24
print(even_odd(n))


def max_three_number(a, b, c):
    if a>b and a>c:
        return "a is max number"
    elif b>a and b>c:
        return "b is max number"
    else: 
        return "c is max number"
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))
print(max_three_number(a, b, c))


def swap_two_var_without_var(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
print(swap_two_var_without_var(a, b))


def palindorme_string(s):
    left , right = 0, len(s)-1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
s = "madam"
print(palindorme_string(s))


def reverse_string(s):
    rev_str = ""
    for char in s:
        rev_str = char + rev_str
    return rev_str
s = "Ganesh"
print(reverse_string(s))


def count_vowels_in_string(s):
    vowels = "AEIOUaeiou"
    count = 0
    vow_char = []
    for char in s:
        if char in vowels:
            count += 1
            vow_char.append(char)
    return count, vow_char
s = "Ganesh Malepati"
print(count_vowels_in_string(s))



def fact_num(n):
    if n < 0:
        return "Number must be positive"
    ini_num = 1
    for i in range(1, n+1):
        ini_num *= i
    return ini_num
n = 5
print(fact_num(n))





def fibnocci_series(n):
    a, b = 0, 1
    for _ in range(0, n):
        yield a
        a, b = b, a + b
n = 8
print(fibnocci_series(n))


def fibnocci_series(n):
    n1, n2 = 0, 1
    result = []
    for i in range(0, n):
        result.append(n1)
        n1, n2 = n2, n1+n2
    return result
n = 8
print(fibnocci_series(n))



def check_prime_num(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

strt = 5
end = 55
print(check_prime_num(n))
for i in range(strt, end):
    if check_prime_num(i):
        print(i)



def concat_list(n1, n2):
    for i in n2:
        n1.append(i)
    return n1
    
n1 = [1, 2, 4, 5, 6]
n2 = [2, 3, 7, 8, 9]
print(concat_list(n1, n2))

def concat_list_2(n1, n2):
    result = n1 + n2
    return result

n1 = [1, 2, 4, 5, 6]
n2 = [3, 6, 7, 8]
print(concat_list_2(n1, n2))


def remove_duplicate(n):
    seen = set()
    # result = []
    for i in n:
        if i not in seen:
            seen.add(i)
            # result.append(i)
    return list(seen)

n = [1, 2, 3, 2, 2, 3, 4, 5, 3, 5, 4, 4, 4, 4, 7, 8, 5, 8, 9, 5, 5, 1, 7, 7, 0, 0, 0, 0, 11, 23, 22, 22, 11, 23]
print(remove_duplicate(n))


def second_largest_element(n):
    first_large = second_large = float('-inf')
    for i in n:
        if i > first_large:
            second_large, first_large = first_large, i
        elif first_large > i > second_large:
            second_large = i
    return second_large

n = [233, 534, 23, 124, 346, 634, 62, 755, 478, 354, 956, 234, 335, 100]
print(second_largest_element(n))



def common_ele_list(n1, n2):
    seen = set(n2)
    result = []
    for i in n1:
        if i in seen:
            result.append(i)
    return result

n1 = [1, 2, 4, 5, 6]
n2 = [3, 6, 7, 8]
print(common_ele_list(n1, n2))
            
def common_elements(n1, n2):
    common = [x for x in n1 if x in n2]
    return common
n1 = [1, 2, 4, 5, 6]
n2 = [3, 6, 7, 8]
print(common_elements(n1, n2))



def freq_count_list(my_list):
    freq_cont = {}
    for i in my_list:
        freq_cont[i] = freq_cont.get(i, 0) + 1
    return freq_cont
    

n = ['g', 'a', 'n', 'e', 's', 'h', 'm', 'a', 'l', 'e', 'p', 'a', 't', 'i']
list_2 = ['o', 'l', 'l', 'm', 'a']
print(freq_count_list(list_2))
print(freq_count_list(n))



def reverse_list(my_list):
    return my_list[::-1]

my_list = [233, 534, 23, 124, 346, 634, 62, 755, 478, 354, 956, 234, 335, 100]
print(reverse_list(my_list))


def reverse_list_2(mylist):
    left, right = 0, len(my_list)-1
    while left < right:
        my_list[left], my_list[right] = my_list[right], my_list[left]
        left += 1
        right -= 1
    return my_list
    
my_list = [233, 534, 23, 124, 346, 634, 62, 755, 478, 354, 956, 234, 335, 100]
print(reverse_list_2(my_list))


def capitalize_first_letter(s):
    return s.title()
        

s = "hey ganesh how are you! are you doing well?"
print(capitalize_first_letter(s))

import string
def cap_letter(s):
    return string.capwords(s)
s = "hey ganesh how are you! are you doing well?"
print(cap_letter(s))


def largest_word_sentence(s):
    longest = ""
    words = s.split()
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

s = "hey ganesh how are you! are you doing well?"
print(largest_word_sentence(s))



def freq_count_string(s):
    freq_dict = {}
    for char in s:
        freq_dict[char] = freq_dict.get(char, 0) + 1
    return freq_dict
s = "ganeshmalepati"
print(freq_count_string(s))


def merge_two_dict(d1, d2):
    dict_merge = d1 | d2
    return dict_merge

d1 = {"name": "Ganesh", "Age": 24}
d2 = {"Sex": "Male", "Occupation": "IT_Employee"}
print(merge_two_dict(d1, d2))


def sort_dict_values(d):
    sort_values = sorted(d, key=d.get)
    return sort_values

d = {"banana": 14, "a": 23, "CTC": 4, "ganesh": 10} 
print(sort_dict_values(d))



def check_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False
    freq_count = {}
    for char in s1:
        freq_count[char] = freq_count.get(char, 0) + 1
    for char in s2:
        if char not in freq_count and freq_count[char] == 0:
            return False
        freq_count[char] -= 1
    return True

s1 = "silent"
s2 = "listen"

data1 = "bat"
data2 = "tab"

print(check_anagrams(s1, s2))
print(check_anagrams(data1, data2))
        



def conver_list_to_dict(my_list):
    result = {i: v for i, v, in enumerate(my_list)}
    return result

my_list = ["items", "apple", "mango"]
print(conver_list_to_dict(my_list))


def group_anagrams_by_dict(words):
    group = {}
    for w in words:
        key = ''.join(sorted(w))
        if key in group:
            group[key].append(w)
        else:
            group[key] = [w]
    return list(group.values())

words = ["eat", "ate", "tan", "tea", "nat", "bat", "listen", "silent", "tab", "bat"]
print(group_anagrams_by_dict(words))





def number_1_100(num, i = 1):
    if i > num:
        return 
    print(i)
    number_1_100(num, i+1)

num = 100
print(number_1_100(num))


def multi_table(n):
    for i in range(1, 11):
        result = n * i
        print(f"Muliply of 8: {n} * {i} = {result}")
        i += 1
n = 8
multi_table(n)



def sum_of_digits(n):
    sum_dig = 0
    while n > 0:
        sum_dig += n % 10
        n = n//10
    return sum_dig

n = 1234
print(sum_of_digits(n))



def armstrong_num(n):
    order = len(str(n))
    a_num = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        a_num +=  digit ** order
        temp //= 10
    return a_num, f"{a_num} is an armstrong number"

n = int(input("Enter a number:- "))
print(armstrong_num(n))



def count_no_digits(n):


    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

n = 24235325
print(f"Number of digits in a given number is:- {count_no_digits(n)}")


def leap_or_not_leap_year(n):
    if n % 400 == 0:
        return "It's Leap year"
    elif n % 100 != 0 and n % 4 == 0:
        return "It's leap year"
    return False
n = 2024
print(leap_or_not_leap_year(n))


def fibanocci_series_recursion(n):
    if n <= 1:
        return n
    else:
        return fibanocci_series_recursion(n-1) + fibanocci_series_recursion(n-2)

n = int(input("Enter a number: "))
sequence_fib = [fibanocci_series_recursion(i) for i in range(n)]
print(sequence_fib)




def fibonacci_series(n):
    n1, n2 = 0, 1
    result = []
    for i in range(0, n):
        result.append(n1)
        n1, n2 = n2, n1+n2
    return result

n = 8
print(fibonacci_series(n))    


# def prime_number(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n%i == 0:
#             return False
#     return True

def remove_duplicates(n):
    seen = set()
    result = []
    for i in n:
        if i not in seen:
            seen.add(i)
            result.append(i)
    return  seen

n = [2,3,4,2,3,5,6,7,3,4,5,7,8,9,5,78,9,8,6,53,2]
print(remove_duplicates(n))


def common_elem(l1,l2):
    seen = set(l2)
    return [i for i in l1 if i in seen]

l1 = [23, 46, 375, 62, 65, 865, 864, 854]
l2 = [67, 86, 84, 456, 865, 375, 23, 854]
print(common_elem(l1, l2))



s = ""
longest = ""
words = s.split()
for word in words:
    if len(word) > len(longest):
        longest = word
return longest

def str_len(s):
    count = 0
    for _ in s:
        count += 1
    return count

def longest_word(s):
    words = s.split()
    longest = ""
    for word in words:
        if str_len(word) > str_len(longest):
            longest = word
    return longest

s = "This is the longest word in the presentation of proggraming simultaneously"
print(longest_word(s))


from collections import ChainMap
def merge_2_dict(d1, d2):
    cm = ChainMap(d2, d1)
    return dict(cm)

d1 = {"name": "Ganesh", "company": "Capgemini", "Project": "NCM_IAM"}
d2 = {"salary": 27000, "Experience": 1.9}
print(merge_2_dict(d1, d2))



def two_string_anagram_check(s1, s2):
    if len(s1) != len(s2):
        return False
    anagram_check = {}
    for char in s1:
        anagram_check[char] = anagram_check.get(char, 0) + 1
    for char in s2:
        if char not in anagram_check or anagram_check[char] == 0:
            return False
        anagram_check[char] -= 1
    return True

s1 = "listen"
s2 = "silent"
a1 = 'bat'
a2 = 'tal'
print(two_string_anagram_check(s1, s2))
print(two_string_anagram_check(a1, a2))


def remove_duplicate_set(my_set):
    seen = set()
    for i in my_set:
        if i not in seen:
            seen.add(i)
    return seen

my_set = [2, 4, 6, 3, 3, 5, 3, 6, 2, 7, 5, 7, 3, 9, 8, 4, 3, 6, 7985, 3246, 623, 734, 7985, 2452, 9, 90]
print(remove_duplicate_set(my_set))



def convert_list_dict(my_list):
    my_dict = {key: value for key, value in enumerate(my_list)}
    return my_dict

my_list = ['Ganesh', 'Jhon', 'Abraham']
print(convert_list_dict(my_list))



def key_with_max_value(my_dict):
    has_any = False
    max_key = None
    max_value = None

    for k in my_dict:
        v = my_dict[k]
        if not has_any:
            has_any = True
            max_key = k
            max_value = v
        else:
            if v > max_value:
                max_value = v
                max_key = k
    return max_key

data = {"a": 10, "b": 25, "c": 54, "d": 15}
print(key_with_max_value(data))



def anagrams_group(my_list):
    group = {}
    for word in my_list:
        key = ''.join(sorted(word))
        if key in group:
            group[key].append(word)
        else:
            group[key] = [word]

    return list(group.values())

my_list = ["eat", "ate", "tan", "tea", "nat", "bat", "listen", "silent", "tab", "bat"]
print(anagrams_group(my_list))


def print_num_1_to_100(n, i=1):
    if i > n:
        return
    print(i)
    print_num_1_to_100(n, i+1)
n = 100
print(print_num_1_to_100(n))


def num_1_to_1oo(start, end):
    if start > end:
        return
    yield start
    yield from num_1_to_1oo(start+1, end)
print(*num_1_to_1oo(1, 100))



def sum_of_n_numbers(n):
    sum_num = 0
    for i in range(1, n+1):
        sum_num += i
        i += 1
    return sum_num

n = int(input("Enter a number: "))
print(sum_of_n_numbers(n))


def armstrong(num):
    order = len(str(num))
    total = 0
    temp = num
    while temp > 0:
        digit = temp%10
        total += digit ** order
        temp //= 10
    return total == num, f"{num} is an armstrong number"

num = 153
print(armstrong(num))


    

def is_prime_or_not(n):
    if n < 2:
        return False
    if n in (2,3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    d = 5
    while d * d <= n:
        if n % d == 0 or n % (d + 2) == 0:
            return False
        d += 6
    return True

num = 23
print(is_prime_or_not(num))


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


def sum_of_digits_num(num):
    sum_num = 0
    while num > 0:
        sum_num += num % 10
        num //= 10
    return sum_num

num = int(input("Enter a number: "))
print(sum_of_digits_num(num))



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


def reverse_number(num):
    rev_num = 0
    while num > 0:
        rev_num = rev_num * 10 + num % 10
        num //= 10
    return rev_num

num = 1234
print(reverse_number(num))


def reverse_num(num, rev = 0):
    if num == 0:
        return rev
    return reverse_num(num//10, rev = rev * 10 + num % 10)

num = 123456
print(reverse_number(num))



def occurence_of_char(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] = char_count.get(char, 0) + 1
        else:
            char_count[char] = 1
    return char_count

s = "malepatiganesh"
print(occurence_of_char(s))


def occurence_of_char(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

s = "malepatiganesh"
print(occurence_of_char(s))


def Occurence_String(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

s = "Run this code in docker and jenkins"
print(Occurence_String(s))
        

def non_repeat_char(s):
    freq_char = {}
    for char in s:
        freq_char[char] = freq_char.get(char, 0) + 1
    non_rep_ch = [char for char in s if freq_char[char] == 1]
    return non_rep_ch
s = 'swiss bank'
print(non_repeat_char(s))



def Non_repeat_char_string(s):
    new_s = {}
    for char in s:
        new_s[char] = new_s.get(char, 0) + 1
    return [char for char in s if new_s[char] == 1]
        
s = "swiss bank"
print(Non_repeat_char_string(s))

def repeat_char_string(s):
    new_s = {}
    for char in s:
        new_s[char] = new_s.get(char, 0) + 1
    return [char for char in s if new_s[char] != 1]
        
s = "swiss bank"
print(repeat_char_string(s))





def sort_without_builtin_func(list_num):
    if len(list_num) <= 1:
        return list_num
    mid = len(list_num)//2
    left = sort_without_builtin_func(list_num[:mid])
    right = sort_without_builtin_func(list_num[mid:])
    return merge(left, right)

def merge(left, right):
    i = j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

num_list = [38, 56, 29, 76, 27, 43, 3, 9, 82, 10, 1, 66, 7]
print(sort_without_builtin_func(num_list))



def first_non_repeat_char_in_string_using_comprehension(s):
    freq = {}

    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    for char in s:
        if freq[char] == 1:
            return char
    return None

s = "malayalam"
name = "Ganesh"
print(first_non_repeat_char_in_string_using_comprehension(s))
print(first_non_repeat_char_in_string_using_comprehension(name))


def reverse_num(num):
    rev_num = 0
    while num > 0:
        rev_num = rev_num * 10 + (num % 10)
        num //= 10
    return rev_num
num = 1234
print(reverse_num(num))



def reverse_string(s):
    rev_str = ""
    for char in s:
        rev_str = char + rev_str
    return rev_str

s = "ganesh"
print(reverse_string(s))




def group_anagram(my_list):
    group = {}
    for word in my_list:
        key = ''.join(sorted(word))
        if key in group:
            group[key].append(word)
        else:
            group[key] = [word]
    return group

words = ["eat", "ate", "tan", "tea", "nat", "bat", "listen", "silent", "tab", "bat"]
print(group_anagram(words))




def arm_strong_num(num):
    order = len(str(num))
    temp = 0
    a_num = num
    while a_num > 0:
        digit = a_num % 10
        temp += digit ** order
        a_num //= 10
    return temp == num

num = 153
print(arm_strong_num(num))



def prime_number(num):
    if num == 0 or num == 1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or (num % i + 2) == 0:
            return False
        i += 6
    return True
        

num = 23
n = 31
print(prime_number(n))
print(prime_number(num))




def reverse_a_string(s):
    rev = ""
    for char in s:
        rev = char + rev
    return rev
s = "Ganesh"
print(reverse_a_string(s))


def first_non_repeat_char(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    for char in s:
        if freq[char] == 1:
            return char
    return None

s = "Ganesh"
print(first_non_repeat_char(s))


def check_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False
    freq = {}
    for char in s1:
        freq[char] = freq.get(char, 0) + 1
    for char in s2:
        if char not in freq or freq[char] == 0:
            return False
        freq[char] -= 1
    return True

s1 = "silent"
s2 = "listen"
t1 = "bat"
t2 = "hat"
print(check_anagrams(s1, s2))
print(check_anagrams(t1, t2))
    


def find_missing_num(data):
    n = max(data)
    actual_sum = sum(data)
    expected_sum = n * (n+1)//2
    result = expected_sum - actual_sum
    return result

data = [1, 2, 3, 5, 6, 7]
print(find_missing_num(data))


def remove_duplicate_from_list(data):
    seen = set()
    result = []
    for i in data:
        if i not in seen:
            seen.add(i)
            result.append(i)
    return result

data = [2,2,3,4,5,3,4,5,6,7,1,1,3,5,7,9,7,8,6,8,6,8,4,1,4,6,8]
print(remove_duplicate_from_list(data))


def second_largest_element(data):
    first_largest = second_largest = float('-inf')
    for i in data:
        if i > first_largest:
            second_largest = first_largest
            first_largest = i
        elif first_largest > i > second_largest:
            second_largest = i
    return second_largest

data = [23443, 55353, 6432, 63546, 7436, 57474, 85466, 4564, 8568, 4564]
data_2 = [2, 3, 4, 5, 6, 7]
print(second_largest_element(data_2))
print(second_largest_element(data))


def char_freq(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

s = "Ganesh malepati"
print(char_freq(s))

def count_vowels_in_string(s):
    vowels = "AEIOUaeiou"
    count = 0
    result = []
    for char in s:
        if char in vowels:
            count += 1
            result.append(char)
    return count, result

s = "Ganesh malepati"
s_2 = "Hey! Good Morning"
print(count_vowels_in_string(s))
print(count_vowels_in_string(s_2))

def longest_word_in_sentence(s):
    s = s.split()
    longest = ""
    for word in s:
        if len(word) > len(longest):
            longest = word
    return longest

s = "These room belong bedroom to our friends"
print(longest_word_in_sentence(s))


def check_string_contains_onlynum(s):
    for char in s:
        if not char.isdigit():
            return False
    return True

s = "1234"
s_1 = "Gani123"
print(check_string_contains_onlynum(s))
print(check_string_contains_onlynum(s_1))


def sort_list_without_using_built_sort(data):
    if len(data) <= 1:
        return data
    mid = len(data)//2
    left = sort_list_without_using_built_sort(data[:mid])
    right = sort_list_without_using_built_sort(data[mid:])
    return merge (left, right)

def merge(left, right):
    i = j = 0
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
print(sort_list_without_using_built_sort(data))


def longest_prefix(data):
    if not data:
        return ''
    data.sort()
    first, last = data[0], data[-1]
    i = 0
    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1
    return first[:i]

my_list = ["interview","internet","internal"]
print(longest_prefix(my_list))
