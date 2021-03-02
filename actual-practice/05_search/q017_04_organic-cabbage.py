# 문제명 : 유기농 배추
# url : https://www.acmicpc.net/problem/1012

# 직접 풀이 (3) - 성공
#  - process() 함수 활용

import sys
sys.setrecursionlimit(10000)

T = int(input())
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
field, visited = [], []
M, N = 0, 0

def dfs(x, y):
    global field, visited, M, N
    visited[x][y] = True
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if nx >= 0 and nx < N and ny >= 0 and ny < M:
            if field[nx][ny] and not visited[nx][ny]:
                dfs(nx, ny)

def process():
    global field, visited, M, N
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    
    for _ in range(K):
        y, x = map(int, input().split())
        field[x][y] = 1

    bugCnt = 0
    for x in range(N):
        for y in range(M):
            if field[x][y] and not visited[x][y]:
                dfs(x, y)
                bugCnt += 1
    
    print(bugCnt)

for _ in range(T):
    process()
    
    