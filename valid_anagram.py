class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count_s = {}
        count_t = {}

        for i in range(len(s)):
            if s[i] in count_s :
                count_s[s[i]] += 1
            else:
                count_s[s[i]] = 1

        for i in range(len(t)):
            if t[i] in count_t :
                count_t[t[i]] += 1
            else:
                count_t[t[i]] = 1

        return count_s == count_t      


#WE CAN USE GET METHOD AS WELL 

if len(s) != len(t):
    return False

count_s = {}
count_t = {}

for i in range(len(s)):
    count_s[s[i]] =  1 + count_s.get(s[i], 0)

for i in range(len(t)):
    count_t[t[i]] = 1 + count_t.get(t[i], 0)

return count_s == count_t 