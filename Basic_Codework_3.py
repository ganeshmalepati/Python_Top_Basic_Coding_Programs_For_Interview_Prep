"""
    Dictionary and Set Operations
    Count character frequency in a string using dictionary
"""


def count_char_string(s):
    freq_char = {}
    for char in s:
        freq_char[char] = freq_char.get(char, 0) + 1
    return freq_char

s = "Ganesh Malepati"
print(count_char_string(s))



"""
    Merge two dictionaries
"""

def merge_2_dict(d1, d2):
    return d1 | d2

d1 = {"name": "Ganesh", "company": "Capgemini", "Project": "NCM_IAM"}
d2 = {"salary": 27000, "Experience": 1.9}
print(merge_2_dict(d1, d2))



from collections import ChainMap
def merge_2_dict(d1, d2):
    cm = ChainMap(d2, d1)
    return dict(cm)

d1 = {"name": "Ganesh", "company": "Capgemini", "Project": "NCM_IAM"}
d2 = {"salary": 27000, "Experience": 1.9}
print(merge_2_dict(d1, d2))



"""
    Sort dictionary by values
"""


def sort_values_dict(dict_1):
    key_sorted_values = sorted(dict_1, key=dict_1.get)
    return key_sorted_values

dict_1 = {"banana": 14, "a": 23, "CTC": 4} 
print(sort_values_dict(dict_1))




"""
    Check if two strings are anagrams
"""

def string_anagrams(s1, s2):
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

s1 = input("Enter a string s1: ")
s2 = input("Enter a string s2: ")
print(string_anagrams(s1, s2))



def anagrams_check(s1, s2):
    if len(s1) != len(s2):
        return False
    freq_count = {}
    for char in s1:
        if char in freq_count:
            freq_count[char] += 1
        else:
            freq_count[char] = 1
    for char in s2:
        if char not in freq_count:
            return False
        freq_count[char] -= 1
        if freq_count[char] < 0:
            return False
    return True

s1 = input("Enter the string s1: ")
s2 = input("Enter the string s2: ")
print(anagrams_check(s1, s2))



def anagrams_check_2(s1, s2):
    if len(s1) != len(s2):
        return False
    freq = {}
    for char in s1:
        freq[char] = freq.get(char, 0) + 1
    for char in s2:
        if char not in freq:
            return False
        freq[char] -= 1
        if freq[char] < 0:
            return False
    return True

s1 = input("Enter the string s1: ")
s2 = input("Enter the string s2: ")
print(anagrams_check_2(s1, s2))



"""
    Remove duplicates using set
"""

def remove_duplicate_set(my_set):
    seen = set()
    for i in my_set:
        if i not in seen:
            seen.add(i)
    return seen

my_set = [2, 4, 6, 3, 3, 5, 3, 6, 2, 7, 5, 7, 3, 9, 8, 4, 3, 6, 7985, 3246, 623, 734, 7985, 2452, 9, 90]
print(remove_duplicate_set(my_set))


def remove_duplicate_set_list(my_list):
    unique_set = {item for item in my_list}
    return unique_set
my_list = [2, 4, 6, 3, 3, 5, 3, 6, 2, 7, 5, 7, 9, 6, 3, 2, 10, 345, 6]
print(remove_duplicate_set_list(my_list))




"""
    Convert list to dictionary
"""

def convert_list_dict(my_list):
    d = {i: v for i, v in enumerate(my_list)}
    return d    

my_list = ["items", "apple", "mango"]
print(convert_list_dict(my_list))


def convert_dict_list(my_list):
    return dict(my_list)

my_list = [("a", 1), ("b", 2), ("c", 4), ("e", 9)]
print(convert_dict_list(my_list))



"""
    Find keys with maximum values in dictionary
"""

def keys_max_value_dict(my_dict):
    return max(my_dict, key=my_dict.get)

my_dict = {"Amount_1": 2352152, "amount_2": 34626536, "amount_3": 6846847, "amount_4": 4763567, "amount_5": 84665365, "amount_6": 84665365}
print(keys_max_value_dict(my_dict))


def keys_max_value(dict_1):
    has_any = False
    current_max = None
    max_keys = []
    for k in dict_1:
        v = dict_1[k]
        if not has_any:
            has_any = True
            current_max = v
            max_keys = [k]
        else:
            if v > current_max:
                current_max = v
                max_keys = [k]
            elif v == current_max:
                max_keys.append(v)
    return max_keys

dict_1 = {"Amount_1": 2352152, "amount_2": 34626536, "amount_3": 6846847, "amount_4": 4763567, "amount_5": 84665365, "amount_6": 84665365}
print(keys_max_value(dict_1))



def key_with_max_value(d):
    has_any = False
    max_key = None
    max_val = None

    for k in d:
        v = d[k]
        if not has_any:
            has_any = True
            max_key = k
            max_val = v
        else:
            if v > max_val:
                max_val = v
                max_key = k
            # if equal, keep the first encountered (do nothing)

    return max_key  # returns None for empty dict

# Demo
data = {"a": 10, "b": 25, "c": 25, "d": 15}
print(key_with_max_value(data))  # 'b'



"""
    Group words with same characters (anagram groups)
"""
from collections import defaultdict

def anagrams_groups(words):
    groups = defaultdict(list)
    for w in words:
        key = ''.join(sorted(w))
        groups[key].append(w)
    return list(groups.values())


words = ["eat", "ate", "tan", "tea", "nat", "bat"]
print(anagrams_groups(words))

def anagram_group_by_dict(words):
    group = {}
    for w in words:
        key = ''.join(sorted(w))
        if key in group:
            group[key].append(w)
        else:
            group[key] = [w]
    return list(group.values())

words = ["eat", "ate", "tan", "tea", "nat", "bat", "listen", "silent", "tab", "bat"]
print(anagram_group_by_dict(words))



"""

"""

def check_key_dict(dict_1, key):
    return key in dict_1

dict_1 = {"Amount_1": 2352152, "amount_2": 34626536, "amount_3": 6846847, "amount_4": 4763567, "amount_5": 84665365, "amount_6": 84665365}
key = input("Enter the key: ")
print(check_key_dict(dict_1, key))



