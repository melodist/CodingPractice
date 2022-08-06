/**
 * https://school.programmers.co.kr/learn/courses/30/lessons/12912
 * Math Problem
 */
//1. My Solution
function solution(a, b) {
    if (a > b) {
        [a, b] = [b, a]
    }
    return b*(b+1)/2 - a*(a-1)/2;
}

//2. Other Solution
function solution(a, b){
    return (a+b)*(Math.abs(b-a)+1)/2;
}
