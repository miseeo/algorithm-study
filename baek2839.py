def sol(n):
    answer = 0
    temp = n
    
    if n % 5 == 0:
        return n//5
    
    while temp > 3:
        temp -= 3
        answer += 1
        if temp%5 == 0:
            answer += temp//5
            return answer

    if n % 3 == 0:
        return n//3
    
    return -1
    

if __name__ == "__main__":
    n = int(input())
    
    print(sol(n))