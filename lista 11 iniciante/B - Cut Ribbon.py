import sys 
sys.setrecursionlimit(500000000) 
def cut(n): 
    if n in memo.keys(): 
        return memo[n] 
    
    resp = float("-inf") 
    if n == 0: 
        return 0 
    for tamanho in entrada: 
        if n >= tamanho: 
            resp = max(resp, 1 + cut(n - tamanho)) 
    memo[n] = resp 
    return resp 
     
memo = dict() 
 
entrada = list(map(int, input().split())) 
n, entrada = entrada[0], entrada[1:] 
print(cut(n)) 