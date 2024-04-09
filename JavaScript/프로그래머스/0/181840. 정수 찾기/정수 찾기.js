function solution(num_list, n) {
    var answer = 0;
    for(i=0;i<num_list.length;i++){
         if(num_list.includes(n)) answer=1;
         else answer=0;
    }
   
    return answer;
}