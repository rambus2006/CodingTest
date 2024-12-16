function solution(x) {
    var answer = true;
    let i = 0;
    //1. 자릿수의 합 구하기 
    let digitssum = Array.from(x.toString()).map(Number);
    //acc(accumulator): 누산기, 누적되는 값, 최종적으로 출력되는 값
    //cur(current)현재 돌고 있는 요소
    digitssum = digitssum.reduce((acc,cur)=>acc+cur);
    //2. 자릿수로 나누기 
    let test = x/digitssum;
    if(x%digitssum!=0){
        answer = false;
    }
    console.log(test);
    return answer;
}