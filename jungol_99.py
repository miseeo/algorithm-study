def sol(s, e):
    t = 1 if s <= e else -1
    
    for k in range(1, 10):
        for n in range(s, e+t, t):
            print(f'{n} * {k} = {str(n*k).rjust(2)}', end='   ')
        print('')
            
if __name__ == "__main__":
    while True:
        s, e = map(int, input().split())
        if 2 <= s <= 9 and 2 <= e <= 9:
            break
        else:
            print("INPUT ERROR!")
    
    sol(s, e)