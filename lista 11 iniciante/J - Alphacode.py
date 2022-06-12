def dpTemp(tam, k, memo):
    if k == 0:
        return 1
    s = len(tam) - k
    if tam[s] == '0':
        return 0
    if memo[k] != -1:
        return memo[k]
    result = dpTemp(tam, k - 1, memo)
    if k >= 2 and int(tam[s:s+2]) <= 26:
        result += dpTemp(tam, k - 2, memo)
    memo[k] = result
    return memo[k]

def conta(s):
    old = new = 1
    for i in range(len(s)-1):
        if int(s[i:i+2]) > 26: old = 0 
        if int(s[i+1]) == 0: new = 0 
        (old, new) = (new, old + new)
    return new

band = True
while band:
    num = str(input())
    if num == '0':
        band = False
        break
    else:
        print(conta(num))