# 쭉 진행하면서 이전 주유소 값보다 크면 거리만 계속 더하고
# 이전 주유소 값보다 작으면 거기서 마무리하고 새로 시작하자
# 만약 그러다 끝까지 가면 -> 더하기만 하고 안끝날수도 있으니까
# 마지막 단계에서도 마무리를 해야겠다
# 리스트를 하나씩 순서대로 지나가니까 for도 괜찮을꺼같고

import sys
from unittest.loader import VALID_MODULE_NAME

N=int(sys.stdin.readline())
DIS=list(map(int, sys.stdin.readline().strip().split()))
COST=list(map(int, sys.stdin.readline().strip().split()))

distance, cost, result = DIS[0],COST[0],0
for i in range(1, N):
    if i==N-1:
        # 마지막
        result += distance*cost
        break

    if cost < COST[i]:
        # 다음 주유소의 값이 큰 경우 - 계속 진행
        distance += DIS[i]

    else:
        # 다음 주유소의 값이 작은 경우 - 여기서 스탑
        result += distance*cost
        cost=COST[i]
        distance=DIS[i]
    
    

print(result)
