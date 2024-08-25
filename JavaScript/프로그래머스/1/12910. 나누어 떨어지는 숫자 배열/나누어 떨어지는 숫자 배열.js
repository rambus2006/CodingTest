function solution(arr, divisor) {
    var answer = [];
    
    for(let i = 0; i < arr.length; i++){
        if(arr[i] % divisor === 0){
            answer.push(arr[i]);
        }
    }
    
    if (answer.length === 0) {
        answer.push(-1);
    } else {
        answer.sort((a, b) => a - b); // 오름차순 정렬
    }
    
    return answer;
}
