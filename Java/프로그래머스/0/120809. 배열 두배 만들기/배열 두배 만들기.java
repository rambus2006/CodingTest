class Solution {
    public int[] solution(int[] numbers) {
        //정수 배열 numbers가 매개변수로 주어질 떄 
        // numbers의 각 원소에 두배한 원소를 가진 배열을 return 하도록 하기 
        int[] answer = new int[numbers.length]; //배열 크기 쓰기 
        // int temp=0; //옮길 변수 
        
        for(int i=0;i<numbers.length;i++){
            answer[i] = (numbers[i]*2);
        }
        return answer;
    }
}