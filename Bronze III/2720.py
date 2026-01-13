"""
25, 10, 5, 1 이 배수관계이므로 그리디로 풀린다
"""

T=int(input())
coins = [25,10,5,1]

for i in range(T):
    change = int(input())
    result = []
    for coin in coins:
        count, change = divmod(change, coin)
        result.append(count)

    print(*result)