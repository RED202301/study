import sys
sys.stdin = open("input.txt")



def dfs():

    if len(st) == N-1:
        ar.append(st[0])
        print(st)
        return
    for i in range(N):
        if i not in st:
            st.append(i)
            dfs()
            st.pop()

T = int(input())
for _ in range(1, T + 1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    st = []
    ar = []
    dfs()
    print(ar)
