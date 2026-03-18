N,M=map(int, input().split())
NUM_A=set(map(int, input().split()))
NUM_B=set(map(int, input().split()))

UNI=NUM_A.union(NUM_B) - NUM_A.intersection(NUM_B)
print(len(UNI))
