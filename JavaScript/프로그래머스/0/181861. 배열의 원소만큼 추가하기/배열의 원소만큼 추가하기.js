function solution(arr) {
    var answer = [];
    let n =0;
    for(let i=0;i<arr.length;i++)
    {
        n=parseInt(arr[i]);
        for(let j=0;j<n;j++){
            answer.push(n)
        }
    }
    return answer;
}