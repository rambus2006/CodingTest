function solution(str_list, ex) {
    var answer = '';
    answer = str_list.filter(a=>!a.includes(ex)).join('')
    return answer;
}