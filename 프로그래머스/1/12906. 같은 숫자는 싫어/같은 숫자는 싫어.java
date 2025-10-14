import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        ArrayList<Integer> answerList = new ArrayList<>();
        int prev = -1; // arr 값은 0~9, 안전하게 초기화
        
        for(int num : arr){
            if(num != prev){
                answerList.add(num);
                prev = num;
            }
        }
        
        int[] answer = new int[answerList.size()];
        for(int i = 0; i < answerList.size(); i++){
            answer[i] = answerList.get(i);
        }
        return answer;
    }
}
