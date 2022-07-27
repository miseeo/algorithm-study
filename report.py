def solution(id_list, report, k):
    answer = [0 for i in range(len(id_list))]
    id = []
    count = []
    
    # 중복 제거
    report = list(set(report)) 
    
    # 신고 당한 아이디 id 리스트에 저장
    for x in report:
        spl = x.split()
        id.append(spl[1])
    
    # 한 아이디가 신고 당한 횟수 카운트
    # 정지당한 아이디 있으면 count 리스트에 아이디 저장
    for t in range(len(id_list)):
        if id.count(id_list[t]) >= k:
            count.append(id_list[t])
    
    # 정지당한 아이디를 신고한 아이디 찾아서 해당 인덱스 +1
    for n in report:
        spl = n.split()
        if spl[1] in count:
            answer[id_list.index(spl[0])] += 1
        
    return answer

if __name__ == "__main__":
    id_list = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
    k = 2
    
    s = solution(id_list, report, k)
    print(s)