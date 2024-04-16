function solution(A, B) {
    var answer = -1;
    A.sort((a,b) => b-a);
    B.sort((a,b)=>b-a);
    
    let j=0; //B를 가리키는 인덱스 
    let ans = 0; //점수 
    for(let i=0;i<A.length;i++){
        if(A[i]<B[j]){
            ans++;
            j++;
        }
    }
    return ans;
}