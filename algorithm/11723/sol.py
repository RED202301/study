import sys
sys.stdin = open("input.txt")

M = int(input())

# 배열 : arr
ZeroArr = list([0 for _ in range(20)])
arr = list([0 for _ in range(2)] for _ in range(M))

for i in range(M):
    arr = input().split()

    # add  => S  + X를 추가한다. / 1과 20사이일 경우 pass
    if arr[0] == 'add':
        if ZeroArr[int(arr[1])-1] == 0:
            ZeroArr[int(arr[1])-1] = 1
        else:
            pass
    # check => S에 X가 있으면 1 / 없으면 0
    elif arr[0] == 'check':
        if ZeroArr[int(arr[1])-1] == 0:
            print(0)
        else:
            print(1)
    # remove => S - X를 뺀다. / 1과 20사이일 경우 pas
    elif arr[0] == 'remove':
        if ZeroArr[int(arr[1])-1] == 0:
            pass
        else:
            ZeroArr[int(arr[1])-1] = 1
    # toggle => S 에 X 있으면 X 제거 / 없으면 X 추가
    elif arr[0] == 'toggle':
        if ZeroArr[int(arr[1])-1] == 0:
            ZeroArr[int(arr[1])-1] = 1
        else:
            ZeroArr[int(arr[1])-1] = 0
    # all => 배열 순회 후 S 를 {1, 2, ..., 20}
    elif arr[0] == 'all':
        for i in range(20):
            ZeroArr[i] = 1
    # empty => S를 공집합
    elif arr[0] == 'empty':
        for i in range(20):
            ZeroArr[i] = 0

            

#  list 형식이기에 메모리 초과 발생
# set형식으로 푸는 걸 추천