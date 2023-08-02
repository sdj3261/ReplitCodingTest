from collections import deque
#connected Component 문제
n,l,r = map(int,input().split())
a = [[] * n  for _ in range(n)]
for i in range(n) :
    data = list(map(int,input().split()))
    for j in range(n) :
        a[i][j] = data[j]
        
def dfs(i, j):
    dq = deque()
    dq.append((i, j))
    visit[i][j] = True
    # 연합된 국가 담기
    union = [(i, j)]
    count = arr[i][j]   # 총 연합된 국가 수 
        # 1. 인접 국가를 탐색하면서 인구차이 l명 이상, r명 이하인 경우 연합 국가에 담기 
    while dq:
        x, y = dq.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visit[nx][ny]:
                continue
            if l <= abs(arr[nx][ny] - arr[x][y]) <= r:  # 인구차이 l명 이상, r명 이하인 경우, 연합 국가에 담기 
                union.append((nx, ny))
                visit[nx][ny] = True
                dq.append((nx, ny))
                count += arr[nx][ny]
    # 2. 연합 국가 간 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수) 가 되도록 계산  
    for x, y in union:
        arr[x][y] = math.floor(count / len(union))

    return len(union)

result = 0    # 인구 이동이 발생하는 일수 
while True:   # 1. 인구 이동이 없을 때까지 반복 
    visit = [[False] * n for _ in range(n)]
    flag = False  # 인구 이동 존재 유무 플래그 
    # 2. 모든 곳을 bfs로 방문하여 연합 진행 
    for i in range(n):
        for j in range(n):
            if not visit[i][j]:
                if dfs(i, j) > 1:
                    flag = True
    if not flag:   # 3. 지금까지 인구 이동이 없는 경우, 그만 
        break
    result += 1