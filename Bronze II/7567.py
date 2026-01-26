input_str = input()
stack = []
res_sum=0

for i in range(len(input_str)):
    if not stack:
        stack.append(input_str[i])
        res_sum += 10
    else:
        if(stack.pop() == input_str[i]):
            res_sum += 5
            stack.append(input_str[i])
        else:
            res_sum += 10
            stack.append(input_str[i])

print(res_sum)