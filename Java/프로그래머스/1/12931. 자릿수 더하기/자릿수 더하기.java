import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;

        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        //문자열로 바꿔서 저장 
        String num = String.valueOf(n);
        int len=num.length();
        
        char[] charArr = num.toCharArray();
        
        
        //결과 출력 
        for(char c:charArr){
            answer+= c-'0';
        }
        return answer;
    }
}