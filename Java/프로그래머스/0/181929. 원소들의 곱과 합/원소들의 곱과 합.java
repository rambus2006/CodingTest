class Solution {
    public int solution(int[] num_list) {

        int answer = 0;
        int numplus=0;
        int numproduct=1;
        int numplussq=0;
        for(int i=0;i<num_list.length;i++){
            numplus +=num_list[i]; //결과값 15
            numproduct *=num_list[i]; //결과값 120
        }
        // answer = numproduct;
        numplussq =(int)Math.pow(numplus,2);
        
        if(numproduct<numplussq)
            answer=1;
        else if(numproduct>numplussq)
            answer=0;

        return answer;
    }
}