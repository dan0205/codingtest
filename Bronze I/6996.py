T=int(input())

for i in range(T):
    str_a, str_b = input().split()
    
    if sorted(str_a)==sorted(str_b):
        print(f"{str_a} & {str_b} are anagrams.")
    else:
        print(f"{str_a} & {str_b} are NOT anagrams.")

