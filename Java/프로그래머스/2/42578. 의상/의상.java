import java.util.HashMap;

public class Solution {
    public int solution(String[][] clothes) {
        // 의상의 종류와 개수를 저장할 HashMap
        HashMap<String, Integer> map = new HashMap<>();
        
        // 의상 배열을 순회하며 각 의상의 종류별 개수 계산
        for (String[] cloth : clothes) {
            String type = cloth[1];
            map.put(type, map.getOrDefault(type, 0) + 1);
        }
        
        // 각 종류별로 가능한 조합의 수를 계산
        int answer = 1;
        for (int count : map.values()) {
            answer *= (count + 1); // 선택하지 않는 경우도 포함
        }
        
        // 최소 하나의 의상은 착용해야 하므로, 1을 빼줍니다
        return answer - 1;
    }
}
