str1 = "vasu"
str2 = "usav"

str1 = str1.lower()
str2 = str2.lower()

list1 = list(str1)
list2 = list(str2)

list1.sort()
list2.sort()

if list1 == list2:
    print("Anagram")
else:
    print("not Anagram")    