# 문제명 : 주사위 네개
# url : https://www.acmicpc.net/problem/2484

# 해설 (1) - 성공

def money():
    lst = sorted(list(map(int, input().split())))
    
    if len(set(lst)) == 1:
        return 50000 + lst[0] * 5000

    if len(set(lst)) == 2:
        if lst[1] == lst[2]:
            return 10000 + lst[1] * 1000
        else:
            return 2000 + (lst[1] + lst[2]) * 500

    for i in range(3):
        if lst[i] == lst[i+1]: # 이웃된 수가 같다 -> (2,1,1) 중 2
            return 1000 + lst[i] * 100

    return lst[-1] * 100 # 서로 모두 다른 경우 -> 최대값(맨 뒤에 있는 값)

N = int(input())

print(max(money() for i in range(N)))