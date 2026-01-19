s = input()
num_list = [-1]*(ord('z') - ord('a') + 1)

for idx in range(len(s)):
    if (num_list[ord(s[idx]) - ord('a')] == -1):
        num_list[ord(s[idx]) - ord('a')] = idx

print(*num_list)