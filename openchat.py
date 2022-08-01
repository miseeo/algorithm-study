def solution(record):
    info = {}
    message = ["Enter", "Change"]
    answer = []
    
    for n in record:
        spl = n.split()
        if spl[0] in message:
            info[spl[1]] = spl[2]
    
    for m in record:
        spl = m.split()

        if spl[0] == 'Enter':
            k = info[spl[1]] + "님이 들어왔습니다."
            answer.append(k)
        elif spl[0] == 'Leave':
            k = info[spl[1]] + "님이 나갔습니다."
            answer.append(k)
    
    return answer        
            
if __name__ == "__main__":
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
    t = solution(record)
    print(t)