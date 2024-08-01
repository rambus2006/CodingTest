import java.util.Arrays;
import java.util.HashMap;

public class Solution {
    public boolean solution(String[] phone_book) {
        // 전화번호를 정렬합니다.
        Arrays.sort(phone_book);
        
        // 정렬된 전화번호 배열을 순회하면서 접두어 검사
        for (int i = 0; i < phone_book.length - 1; i++) {
            // 현재 번호와 다음 번호를 비교
            if (phone_book[i + 1].startsWith(phone_book[i])) {
                return false; // 현재 번호가 다음 번호의 접두어인 경우
            }
        }
        
        return true; // 접두어인 경우가 없는 경우
    }
}
