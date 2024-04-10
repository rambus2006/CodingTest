function solution(arr, delete_list) {
    var answer = [];
    answer = arr.filter(a=>!delete_list.includes(a))
    return answer;
}