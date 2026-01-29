input_str = input().upper()
alpha_list = [0] * (ord('Z') - ord('A') + 1)
for i in range(len(input_str)):
    alpha_list[ord(input_str[i]) - ord('A')] += 1
max_num = max(alpha_list)

max_idx=-1
for i in range(len(alpha_list)):
    if max_idx==-1 and max_num==alpha_list[i]:
        max_idx = i
    elif max_idx!=-1 and max_num==alpha_list[i]:
        max_idx = -1
        break

print("?" if max_idx==-1 else chr(max_idx + ord('A')))

