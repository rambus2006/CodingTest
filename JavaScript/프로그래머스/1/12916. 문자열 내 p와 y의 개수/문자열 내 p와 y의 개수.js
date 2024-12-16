function solution(s){
    var answer = true;
    let s_lower = s.toLowerCase();
    let s_array = s.split();
    let pnum=0; ynum=0;
    //p의 개수와 y개수 세기
    //1.p만 세보기 
    for(let i=0;i<s.length;i++){
        if(s_lower[i]=='p')
            pnum++;
        else if(s_lower[i]=='y')
            ynum++;
    }
    if(pnum != ynum){
        answer = false;
    }else{
        answer = true;
    }
    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    // console.log(ynum)

    return answer;
}