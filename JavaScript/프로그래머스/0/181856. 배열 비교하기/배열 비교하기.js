function solution(arr1, arr2) {
    var answer = 0;
    //1. 배열의 길이 두개 비교하기(배열의 길이 같을때도 고려)
    let arr1_len = arr1.length;
    let arr2_len = arr2.length;
    let arr1sum=0;
    let arr2sum = 0;
    //(1)arr1의 길이가 arr2보다 더 클때
    if(arr1_len>arr2_len){
        answer = 1;
    }else if(arr1_len<arr2_len){
        answer=-1;
    }else if(arr1_len === arr2_len){
        for(i=0;i<arr1_len;i++){
            arr1sum += arr1[i];
            arr2sum += arr2[i];
            if(arr1sum>arr2sum){
                answer=1;
            }else if(arr2sum>arr1sum){
                answer=-1
            }else{
                answer=0;
            }
        }
    }
    return answer;
}