function solution(seoul) {
    var answer = '';
    let loc = 0; 
    for(let i=0;i<seoul.length;i++){
        if(seoul[i]=='Kim'){
            loc = i;
        }
    }
    answer = "김서방은 " + loc + "에 있다"
    console.log(loc);
    return answer;
}