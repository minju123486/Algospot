import sys

input = sys.stdin.readline


def str_calcu(a,b):
    length = min(len(a), len(b))
    l = 0
    j = 0
    cnt = 0
    while j < length:
        if a[len(a)-length+j] == b[cnt]:
            cnt += 1
            j += 1
        else:
            if cnt != 0:
                cnt = 0
            else:
                j += 1 
    return a+b[cnt::]

def direct_dfs(check, idx, lst, dp,count):
    if count == len(lst):
        return lst[idx]
    if check in dp[idx]:
        return dp[idx][check]
    dp[idx][check] = ''
    length = 31212312312313
    tmp = ''
    for i in range(len(lst)):
        tempt = 1 << i
        if((tempt & check) != 0) : continue
        rtr = direct_dfs(check + (1 << i), i, lst, dp, count+1)
        mmm = ''
        if rtr in lst[idx]:
            mmm = lst[idx]
        elif lst[idx] in rtr:
            mmm = rtr
        else:
            mmm = str_calcu(lst[idx], rtr)
        if len(mmm) < length:
            length = len(mmm)
            tmp = mmm
    dp[idx][check] = tmp
    return dp[idx][check]
            

T = int(input())
answer = []
for _ in range(T):
    k = int(input())
    str_lst = [input().strip() for _ in range(k)]
    check = [1 for _ in range(len(str_lst))]
    dp = []
    for _ in range(k):
        dp.append(dict())
    ans = ''
    min_ = 123123123213213
    for i in range(k):
        m = direct_dfs(1 << i, i, str_lst, dp, 1)
        if m in str_lst[i]:
            mmm = str_lst[i]
        elif str_lst[i] in m:
            mmm = m
        else:
            mmm = str_calcu(str_lst[i], m)
        if len(mmm) < min_:
            min_ = len(mmm)
            ans = mmm
    answer.append(ans)
for k in answer:
    print(k)