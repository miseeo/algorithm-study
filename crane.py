def solution(board, moves):
    answer = 0
    basket = []
    
    for n in moves:
        for x in range(len(board)):
            now = board[x][n-1] # 옮길 인형
            # 그 위치에 인형이 없는 경우
            if now == 0:
                continue
            
            # 인형이 있는 경우
            else:
                # 바구니 맨 위에 있는 인형과 같은 인형일 경우,
                # 바구니에 담을 인형, 맨 위 인형 삭제
                if basket and basket[-1] == now:
                    basket.pop()
                    answer += 2
                
                # 다른 인형일 경우 바구니에 담기
                else: 
                    basket.append(now)
                
                # 해당 위치에 인형이 없음을 표시
                board[x][n-1] = 0
                break
                   
    return answer

if __name__ == "__main__":
    board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    moves = [1,5,3,5,1,2,1,4]
    
    ans = solution(board, moves)
    print(ans)