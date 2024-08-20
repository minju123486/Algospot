import sys

input = sys.stdin.readline

def map_func(lst):
    rtr = 0
    for idx, i in enumerate(lst):
        rtr += (2**idx)*i
    return rtr



T = int(input())

for _ in range(T):
    k = int(input())
    str_lst = [input().strip() for _ in range(k)]
    