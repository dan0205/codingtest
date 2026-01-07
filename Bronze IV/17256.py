li_a = list(map(int, input().split()))
li_c = list(map(int, input().split()))

"""
li_a[2] + li_b[0] == li_c[0]
li_a[1] * li_b[1] == li_c[1]
li_a[0] + li_b[2] == li_c[2]
"""

print(li_c[0]-li_a[2], li_c[1]//li_a[1], li_c[2]-li_a[0])

