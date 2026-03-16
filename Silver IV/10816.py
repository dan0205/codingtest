""" 입력으로 주어진 수 -> 몇 개 갖고 있을까?
입력으로 10이 주어진다
10이 몇 개 인지 찾는다 -> 매우 빠르게 진행되어야 한다. 숫자 리스트가 있을때 매우 빠르게 숫자가 몇개인지 체크하기

몇 개인지 출력한다
 """

from collections import Counter
import sys

input=sys.stdin.readline
N=int(input())
NUM=list(map(int, input().split()))
M=int(input())
NUM2=list(map(int, input().split()))

counts = Counter(NUM)

for i in range(M):
    print(counts[NUM2[i]], end=' ')