function solution(n) {
    var answer = [];
    let ntostring = n + "";
    console.log(ntostring)
    ntostring = ntostring.split('').map(Number)
    
    answer = ntostring.reverse();
    return answer;
}