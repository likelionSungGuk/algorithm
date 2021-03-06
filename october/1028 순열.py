def perm(n, k): #n숫자를 결정할 인덱스, (결정한 개수) k 순열의 길이
    if n == k:
        print(A)
    else:
        for i in range(n, k):
            A[n], A[i] = A[i], A[n] # 현재 숫자 유지부터 오른쪽 끝까지 교환
            perm(n+1, k)            # 다음 자리 결정하러 이동(n) 개 결정
            A[n], A[i] = A[i], A[n] # 교환 전으로 복구

A = [1, 2, 3]
perm(0, 3)
###########################
def perm(n, k, m): #n 숫자를 결정할 자리 인덱스, k 순열의 길이, m 주어진 숫자의 개수
    if n==k:
        print(A[0:3])
    else:
        for i in range(n, m):
            A[n], A[i] = A[i], A[n]
            perm(n+1, k, m)
            A[n], A[i] = A[i], A[n]
A = [1, 2, 3, 4, 5]
perm(0, 3, 5)