"""
    Concatenate two lists
"""

def concat_list(l1, l2):
    new_list = l1 + l2
    return new_list

l1 = [4, 67, 784, 9658, 48456]
l2 = [7, 83, 975, 9456, 84568]
print(concat_list(l1, l2))


def concat_list(l1, l2):
    l1.extend(l2)
    return l1

l1 = [4, 67, 784, 9658, 48456]
l2 = [7, 83, 975, 9456, 84568]
print(concat_list(l1, l2))


def concat_list(l1, l2):
    for i in l2:
        l1.append(i)
    return l1

l1 = [4, 67, 784, 9658, 48456]
l2 = [7, 83, 975, 9456, 84568]
print(concat_list(l1, l2))


"""
    Remove duplicates from a list
"""

def remove_duplicate_list(list_1):
    seen = set()
    # result = []
    for i in list_1:
        if i not in seen:
            seen.add(i)
            # result.append(i)
    return list(seen)

list_1 = [3,5,6,7,8,3,8,4,7,2,8,5,2,8,35,85,26,87,26,35]
print(remove_duplicate_list(list_1))


def remove_duplicate_list(list_1):
    return list(dict.fromkeys(list_1))

list_1 = [3,5,6,7,8,3,8,4,7,2,8,5,2,8,35,85,26,87,26,35]
print(remove_duplicate_list(list_1))


"""
    Find the second largest number in a list
"""

def second_largest_num(my_list):
    if len(my_list) < 2:
        raise ValueError("Alteast two numbers are required")
    first = second = float('-inf')
    for i in my_list:
        if i > first:
            second, first = first, i
        elif first > i > second:
            second = i
    return second

my_list = [23545, 35636, 6423623, 6346748, 86587457, 8634743]
print(second_largest_num(my_list))



"""
    Sort a list without using built-in sort
"""

def sort_list_no_built(num_list):
    if len(num_list) <= 1:
        return num_list
    
    mid = len(num_list) // 2
    left = sort_list_no_built(num_list[:mid])
    right = sort_list_no_built(num_list[mid:])

    return merge(left, right)

def merge(left, right):
    i = j = 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


num_list = [38, 56, 29, 76, 27, 43, 3, 9, 82, 10, 1, 66, 7]
print(sort_list_no_built(num_list))



def bubble_sort(num_list):
    n = len(num_list)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
                swapped = True
        if not swapped:
            break
    return num_list

num_list = [38, 56, 29, 76, 27, 43, 3, 9, 82, 10, 1, 66, 7]
print(bubble_sort(num_list))



"""
    Find common elements in two lists

"""

def Common_elements(l1, l2):
    common_ele = []
    seen = set(l2)
    for i in l1:
        if i in seen:
            common_ele.append(i)
    return common_ele


l1 = [23, 46, 375, 62, 65, 865, 864, 854]
l2 = [67, 86, 84, 456, 865, 375, 23, 854]
print(Common_elements(l1, l2))



def list_common_elements(l1, l2):
    common = [x for x in l1 if x in l2]
    return common

l1 = [23, 46, 86, 62, 65, 865, 864, 854]
l2 = [67, 86, 84, 456, 865, 375, 23, 854]
print(list_common_elements(l1, l2))




"""
    Count frequency of elements in a list
"""

def freq_count_list(l1):
    freq_ele = {}
    for i in l1:
        freq_ele[i] = freq_ele.get(i, 0) + 1
    return freq_ele

l1 = ['g', 'a', 'n', 'e', 's', 'h', 'm', 'a', 'l', 'e', 'h']
print(freq_count_list(l1))




from collections import Counter

def freq_count_collection_counter(l1):
    return freq_count_collection_counter(Counter(l1))

l1 = ['g', 'a', 'n', 'e', 's', 'h', 'm', 'a', 'l', 'e', 'h']
print(freq_count_list(l1))


"""
    Reverse a List
    1. Using Slice operator
    2. Using pop and append
    3. Append
    4. Two pointer Technique
"""

def reveres_list(l1):
    return l1[::-1]

l1 = [32, 454, 643, 6423, 7346, 7345, 6353, 3246]
print(reveres_list(l1))



my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)  # [5, 4, 3, 2, 1]



def reveres_list_without_slice(l1):
    r_list = []
    for i in range(len(l1)):
        r_list.append(l1.pop())
    return r_list

l1 = [32, 454, 643, 6423, 7346, 7345, 6353, 3246]
print(reveres_list_without_slice(l1))



def reveres_list_without_slice(l1):
    r_list = []
    for i in range(len(l1) - 1, -1, -1):
        r_list.append(l1[i])
    return r_list

l1 = [32, 454, 643, 6423, 7346, 7345, 6353, 3246]
print(reveres_list_without_slice(l1))


def reverse_list_2_pointer(l1):
    left, right = 0, len(l1)-1
    while left < right:
        l1[left], l1[right] = l1[right], l1[left]
        left += 1
        right -= 1
    return l1
l1 = [32, 454, 643, 6423, 7346, 325464, 7345, 6353, 3246]
print(reverse_list_2_pointer(l1))



"""
    Find the longest word in a sentence
"""

def longest_word_sens(s):
    words = s.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

s = "This is the longest word in the presentation of proggraming simultaneously"
print(longest_word_sens(s))


def capitalize_first_letter(s):
    return s.title()

s = "hey ganesh how are you"
print(capitalize_first_letter(s))

import string

def capitalize_first_letter(s):
    return string.capwords(s)

s = "hey ganesh how are you"
print(capitalize_first_letter(s))


