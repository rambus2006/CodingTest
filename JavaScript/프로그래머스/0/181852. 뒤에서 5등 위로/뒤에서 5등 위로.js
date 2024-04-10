function solution(num_list) {
    var answer = [];
    
    num_list = num_list.sort(function(a,b){
        return a-b;
    });
    
    removenum = num_list.splice(0,5);
    for(i=0;i<num_list.length;i++){
        if(num_list[i]!==removenum)
            answer[i]=num_list[i];
    }
    return answer;
}