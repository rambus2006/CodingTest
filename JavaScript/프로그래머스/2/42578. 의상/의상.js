function solution(clothes) {
    // 의상의 종류와 개수를 저장할 객체
    const map = new Map();
    
    // 의상 배열을 순회하며 각 의상의 종류별 개수 계산
    clothes.forEach(([_, type]) => {
        map.set(type, (map.get(type) || 0) + 1);
    });
    
    // 각 종류별로 가능한 조합의 수를 계산
    let answer = 1;
    map.forEach(count => {
        answer *= (count + 1); // 선택하지 않는 경우도 포함
    });
    
    // 최소 하나의 의상은 착용해야 하므로, 1을 빼줍니다
    return answer - 1;
}
