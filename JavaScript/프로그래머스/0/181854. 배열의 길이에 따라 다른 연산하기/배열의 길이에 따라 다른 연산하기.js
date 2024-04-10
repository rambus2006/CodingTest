function solution(arr, n) {
    var answer = [];
    //1. arr의 길이를 구해서 짝수인지 홀수인지 판별한다. 
    //2. arr안의 인덱스가 짝수인지 홀수인지 판별한다. 
    //3. 그에 따른 n 을 더한다. 
    var len = arr.length;
    if(len%2==0){
        for(i=0;i<len;i++){
            if(i%2==1) answer[i]=(arr[i]+n);
            else answer[i]=arr[i];
                
        }
    }else{
        for(i=0;i<len;i++){
            if(i%2==0) answer[i]=(arr[i]+n);
            else answer[i]=arr[i];
                
        }
    }
    
    
        
        
    return answer;
}