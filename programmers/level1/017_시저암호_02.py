# 다른 사람 풀이
def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i]) - ord('A') + n)%26 + ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord('a') + n)%26 + ord('a'))
    return ''.join(s)


print(solution('AB'))
print(solution('z'))
print(solution('a B z'))