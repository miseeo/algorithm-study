def sol(n, a, b, c):
    ans = 0
    
    for x in range(n):
        if a[x] <= b:
            ans += 1
        else:
            temp = a[x] - b
            ans += temp//c + 2 if temp % c != 0 else temp//c + 1
            
    print(ans)

if __name__ == "__main__":    
    n = int(input())
    a = list(map(int, input().split()))
    b, c = map(int, input().split())
    
    sol(n, a, b, c)