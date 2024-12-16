function solution(s) {
    var answer = 0;
    let sarray = s.split();
    if(sarray[0]=='-'){
        for(let i=1;i<s.length;i++)
            answer = Number(sarray);  
        answer = '-' + answer;
    }else{
        answer = Number(sarray);
    }
    return answer;
}