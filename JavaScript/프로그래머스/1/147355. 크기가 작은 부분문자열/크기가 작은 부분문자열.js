function solution(t, p) {
    var answer = 0;
    let numslice3 = 0;
    
    for(let i=0;i<=t.length-p.length;i++){
            numslice3 = parseInt(t.substr(i,p.length))
        
            if(parseInt(numslice3)<=parseInt(p))
                answer+=1;
            
    }
    return answer;
}