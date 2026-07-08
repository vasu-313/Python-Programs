def are_anagrams(s1, s2):
    
    # create a hashmap to store character frequenceies
    char_count = {}
    
    # count frequencey of each character in string s1
    for char in s1:
        char_count[char] = char_count.get(char, 0) + 1

    # count frequency of each character in string s2 
    for char in s2:
        char_count[char] = char_count.get(char, 0) - 1 
        
    # check if all frequencies are zero
    for value in char_count.values():
        if value != 0:
            return False
        
    return True
    
s1 = "listen"
s2 = "silent"    
print(are_anagrams(s1, s2))


























# str1 = "vasu"
# str2 = "usav"

# str1 = str1.lower()
# str2 = str2.lower()

# list1 = list(str1)
# list2 = list(str2)

# list1.sort()
# list2.sort()

# if list1 == list2:
#     print("Anagram")
# else:
#     print("not Anagram")    