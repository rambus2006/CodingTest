function solution(n)
{
    var answer = 0;

    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    let nstring = n+""; //123 문자열 
    for(let i=0;i<nstring.length;i++){
        answer +=parseInt(nstring[i]);
    }

    return answer;
}