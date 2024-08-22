function solution(a, b) {
    var answer = 0;
    let i=0;
    if(a<=b){
        i=a;
        for(;i<=b;i++){
            answer+=i;
        }
    }else{
        i=b;
        for(;i<=a;i++){
            answer+=i;
        }
    }
    return answer;
}