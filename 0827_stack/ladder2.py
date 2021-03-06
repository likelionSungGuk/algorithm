'''
1. 마지막 행의값이 2인 index를 찾아 아래에서부터 올라온다.
2. 좌/우 중 1이면서 visited에 기록이 없으면 그쪽으로 이동한다.
3. 좌우로 이동할 수 없으면 위로 한 칸 이동한다.
'''
import sys
sys.stdin = open('ladder2.txt','r')
sys.stdin = open('ladder2.txt','r')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    row = []
    max_dist = 9999

    for i in range(100):
        if arr[0][i] == 1:
            row.append(i)

    for i in row:
        x = 0
        y = i

        visited = [[0]*100 for _ in range(100)]

        while x < 99:
            visited[x][y] = 1        #현재 위치 방문표시
            if 1 <= y <= 98:
                if arr[x][y-1] == 1 and visited[x][y-1] != 1:   #좌로 움직일 수 있는가?
                    y -= 1
                elif arr[x][y+1] == 1 and visited[x][y+1] != 1: #좌로 움직일 수 있는가?
                    y += 1
                else:
                    x += 1
            elif y == 0:            #우만 체크
                if arr[x][y+1] == 1 and visited[x][y+1] != 1:
                    y += 1
                else:
                    x += 1
            else:           #좌만 체크
                if arr[x][y-1] == 1 and visited[x][y-1] != 1:
                    y -= 1
                else:
                    x += 1

        #x = 99 일 때, visited의 값과 i값
        total_visit = 0
        for k in range(100):
            for l in range(100):
                if visited[k][l] != 0:
                    total_visit += 1

        if total_visit < max_dist:
            max_dist = total_visit
            result = i
    print('#{} {}'.format(tc,result))