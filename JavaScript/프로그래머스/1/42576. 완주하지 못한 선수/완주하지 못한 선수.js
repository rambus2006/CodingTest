function solution(participant, completion) {
    // 참가자들의 이름과 개수를 저장할 Map 객체 생성
    const map = new Map();
    
    // 참가자 배열을 순회하며 Map에 이름과 개수를 저장
    participant.forEach(name => {
        map.set(name, (map.get(name) || 0) + 1);
    });
    
    // 완주자 배열을 순회하며 Map에서 개수를 감소
    completion.forEach(name => {
        map.set(name, map.get(name) - 1);
    });
    
    // Map에서 개수가 1인 이름을 찾아 반환
    for (const [name, count] of map.entries()) {
        if (count > 0) {
            return name;
        }
    }
    
    return ""; // 이 줄은 실제로 도달하지 않아야 합니다.
}
