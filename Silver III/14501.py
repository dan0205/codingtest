""" N=int(input())
T=[]
P=[]
for i in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)


def backtrack(day):
    if day==N:
        return 0
    if day>N:
        return -float('inf')

    take = P[day] + backtrack(day+T[day])
    skip = backtrack(day + 1)

    return max(take, skip)

print(backtrack(0))
    


 """






N=7
NUM=[[3,10],[5,20],[1,10],[1,20],[2,15],[4,40],[2,200]]

def backtrack(day):
    # 1. 언제 멈출까? = return
    # 정말 최소한으로 해도 N일 이상으로 결과가 나오니까
    # if day == N 이 최소 보장이다

    if day == N:
        return 0
    
    if day > N:
        return -1 # ?
    
    # 2. 종이에 상태트리 직접 그리기
    # 현재 상태에서 내가 지금 할 수 있는 선택지 개수만큼 가지를 뻗는다
    # 가지 끝에 변한 상태를 적는다

    print(day)
    backtrack(day+2)

    backtrack(day+1)



backtrack(0)














