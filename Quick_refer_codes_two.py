def first_non_repear_char(s):
    freq = {}
    for i in s:
        freq[i] = freq.get(i, 0) + 1
    
    for char in freq:
        if freq[char] == 1:
            return char
    
s = "malayalam"
print(first_non_repear_char(s))


def count_vowels_in_string(s):
    vowels = "AEIOUaeiou"
    count = 0
    result = []
    for char in s:
        if char in vowels:
            count += 1
            result.append(char)
    return count, result

s = "Ganesh Malepati"
print(count_vowels_in_string(s))


def remove_duplicates_from_string(s):
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return result

s = "Pineapple"
print(remove_duplicates_from_string(s))


def longest_word_in_sentence(sent):
    sent = sent.split()
    longest = ""
    for word in sent:
        if len(word) > len(longest):
            longest = word
    return longest

sent = "This photosynthesis laptop has been provided by the company notqualified"
print(longest_word_in_sentence(sent))


def check_string_contains_only_nums(s):
    for i in s:
        if not i.isdigit():
            return False
        return True
    
s = "12345F"
print(check_string_contains_only_nums(s))


def smallest_and_largest_element(my_list):
    small = my_list[0]
    large = my_list[1]
    for i in my_list:
        if i > large:
            large = i
        if i < small:
            small = i
    return small, large

my_list = [23, 53, 65, 7, 435, 3435, 76, 342, 54, 6454, 342, 23, 535, 4,45,35]
print(smallest_and_largest_element(my_list))


def common_elements(l1, l2):
    result = []
    for i in l1:
        if i in l2:
            result.append(i)
    return result

l1 = [34, 46, 76, 86, 89, 46, 64]
l2 = [33, 64, 64, 87, 34, 76]
print(common_elements(l1, l2))

def find_missing_number(data):
    n = max(data)
    actual = sum(data)
    expected_data = (n * (n+1)) // 2
    return expected_data - actual

data = [1,2,3,4,5,7]
print(find_missing_number(data))



def conver_two_list_dict(l1, l2):
    return dict(zip(l1, l2))

l1 = ["a", "b", "c", "d"]
l2 = [23, 45, 67, 89]
print(conver_two_list_dict(l1, l2))


def longest_prefix_in_given_data(data):
    if not data:
        return ""
    
    prefix = data[0]

    for i in range(1, len(data)):
        j = 0
        while j < len(prefix) and j < len(data[i]) and prefix[j] == data[i][j]:
            j += 1
        prefix = prefix[:j]

        if prefix == "":
            return ""
    return prefix

data = ["interview", "interval", "intermission", "inter"]
print(longest_prefix_in_given_data(data))



def reverse_num(num):
    temp = 0
    while num > 0:
        temp = temp * 10 + num % 10
        num = num//10
    return temp

num = 435362
print(reverse_num(num))



def group_anagrams_by_word(data):
    group_dict = {}
    for word in data:
        key = ''.join(sorted(word))
        if key in group_dict:
            group_dict[key].append(word)
        else:
            group_dict[key] = [word]
    return group_dict

words = ["eat", "ate", "tan", "tea", "nat", "bat", "listen", "silent", "tab", "bat", "fan"]
print(group_anagrams_by_word(words))





def fibonacci_series(num):
    n1, n2 = 0, 1
    result = []
    for _ in range(0, num):
        result.append(n1)
        n1, n2 = n2, n1+n2
    return result

num = 8
print(fibonacci_series(num))



def print_number_1_100(n, i=1):
    if i > n:
        return
    
    print(i)
    print_number_1_100(n, i+1)

print(print_number_1_100(100), sep="\n")



def compress_string(s):
    if not s:
        return ""
    
    result = ""
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result += s[i-1] + str(count)
            count = 1
        
    result += s[-1] + str(count)

    return result

s = "aaaaaaaabbccddddddeeeefgg"
print(compress_string(s))




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

s = "aaaaaaaabbccddddddeeeefgg"
print(compress_string_approach_2(s))


def word_occurance_sentence(s):
    s = s.split()
    freq = {}

    for word in s:
        freq[word] = freq.get(word, 0) + 1
    
    return freq

s = "hello world hello python"
print(word_occurance_sentence(s))
