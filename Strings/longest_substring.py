s = "vasuuaewrp"

left = 0
right = 0
max_len = 0
char_set = set()

while right < len(s):
    if s[right] not in char_set:
        char_set.add(s[right])
        max_len = max(max_len, len(char_set))
        right += 1
    else:
        char_set.remove(s[left])
        left += 1
        
        
print(max_len)