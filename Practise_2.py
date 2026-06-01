# def remove_duplicate(data):
#     seen = set()
#     result = []
#     for i in data:
#         if i not in seen:
#             seen.add(i)
#             result.append(i)
#     return result

# data = [1,2,3,4,1,3,2,4]
# print(remove_duplicate(data))


# def string_only_numbers(data):
#     for char in data:
#         if not char.isdigit():
#             return False
#     return True

# data = "12408735"
# print(string_only_numbers(data))


# def longest_prefix(data):
#     if not data:
#         return ""
#     data.sort()
#     first = data[0]
#     last = data[-1]
#     i = 0

#     while i < len(first) and i < len(last) and first[i] == last[i]:
#         i += 1
#     return first[:i]

# data = ["interview", "interval", "intermission", "inter"]
# print(longest_prefix(data))



# def caseinsensitive_palindrome_check(data):
#     s = ''.join(char.lower() for char in data if char.isalnum())
#     left = 0
#     right = len(s)-1
#     while left < right:
#         if s[left] != s[right]:
#             return False
#         left += 1
#         right -= 1
#     return True

# data = "123 A man, a plan, a canal: Panama 321"
# print(caseinsensitive_palindrome_check(data))



def reverse_string(data):
    rev_str = ""
    for char in data:
        rev_str = char + rev_str
    return rev_str

data = "Ganesh"
print(reverse_string(data))


def check_palindrome_string(str):
    left = 0
    right = len(str)-1
    while left < right:
        if str[left] != str[right]:
            return False
        left += 1
        right -= 1
    return True

str = "malayalam"
name = "Ganesh"
print(check_palindrome_string(str))
print(check_palindrome_string(name))


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

s1 = "listen"
s2 = "silent"
print(check_anagrams(s1, s2))


def count_vowels_consonants(data):
    vowels = "AEIOUaeiou"
    seen = set()
    v_count = 0
    c_count = 0
    for char in data:
        if char.isalpha():
            if char in vowels:
                v_count += 1
                seen.add(char)
            else:
                c_count += 1

    return v_count, c_count, seen

data = "Ganesh"
print(count_vowels_consonants(data))


def remove_dupliacates(data):
    seen = set()
    result = ""
    for char in data:
        if char not in seen:
            seen.add(char)
            result += char
    return result

data = "programming"
print(remove_dupliacates(data))


def first_non_repeat_char(data):
    freq = {}
    for char in data:
        freq[char] = freq.get(char, 0) + 1
    
    for char in freq:
        if freq[char] == 1:
            return char

data = "swiss"
print(first_non_repeat_char(data))


from collections import OrderedDict

def first_non_repeating(s):
    freq = OrderedDict()

    for char in s:
        freq[char] = freq.get(char, 0) + 1

    for char, count in freq.items():
        if count == 1:
            return char

    return None



def longest_substring_without_repeat_chars(data):
    char_set = set()
    left = 0
    max_length = 0
    for right in range(len(data)):
        while data[right] in char_set:
            char_set.remove(data[left])
            left += 1
        
        char_set.add(data[right])

        max_length = max(max_length, right - left + 1)
    
    return max_length

data = "abcabcbbac"
print(longest_substring_without_repeat_chars(data))


def find_missing_num(data):
    n = max(data)
    actual = sum(data)
    expected = n * (n+1) // 2
    return expected -actual

data = [1,2,4,5,6]
print(find_missing_num(data))

def moves_zeros_to_end(data):
    zero_pos = 0
    for i in range(len(data)):
        if data[i] != 0:
            data[zero_pos], data[i] = data[i], data[zero_pos]
            zero_pos += 1
    return data

data = [2, 0, 4, 5, 0, 0, 8, 0, 24, 0, 9, 0, 10]
print(moves_zeros_to_end(data))



def second_largest_number(data):
    
    first = second = float('-inf')
    for i in data:
        if i > first:
            second = first
            first = i
        elif first > i > second:
            second = i
    return second

my_list = [10, 20, 4, 50, 5, 15, 23, 123, 56, 70]
print(second_largest_number(my_list))




    
