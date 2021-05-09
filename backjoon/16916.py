s = input()
p = input()

def getPI(pattern):
    pi = [0] * len(p)
    j = 0
    
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j-1]
        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j
    
    return pi

def kmp(s, pattern):
    pi = getPI(pattern)
    j = 0
    
    for i in range(len(s)):
        while j > 0 and s[i] != pattern[j]:
            j = pi[j-1]
        if s[i] == pattern[j]:
            if j == len(pattern) - 1:
                return True
            else: 
                j += 1
    
    return False

if kmp(s, p):
    print(1)
else:
    print(0)