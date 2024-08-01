import java.util.HashMap;

public class Solution {
    public String solution(String[] participant, String[] completion) {
        // HashMap을 사용하여 참가자들의 이름과 개수를 저장
        HashMap<String, Integer> map = new HashMap<>();
        
        // 참가자 배열을 순회하며 HashMap에 이름과 개수를 저장
        for (String name : participant) {
            map.put(name, map.getOrDefault(name, 0) + 1);
        }
        
        // 완주자 배열을 순회하며 HashMap에서 개수를 감소
        for (String name : completion) {
            map.put(name, map.get(name) - 1);
        }
        
        // HashMap에서 개수가 1인 이름을 찾아 반환
        for (String name : map.keySet()) {
            if (map.get(name) > 0) {
                return name;
            }
        }
        
        return ""; // 이 줄은 실제로 도달하지 않아야 합니다.
    }
}
