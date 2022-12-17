/*
* https://school.programmers.co.kr/learn/courses/30/lessons/135808/
* Find minimum for each box using sort
*/
//1. My Solution
function solution(k, m, score) {
    score.sort((a, b) => {return b - a;})
    return score.reduce((acc, cur, ind) => {
        return ((ind + 1) % m) === 0 ? acc + cur * m : acc}, 0)
}

//2. Other Solution
solution = (_, m, s) => s.sort().filter((_, i) => !((s.length - i) % m)).reduce((a, v) => a + v, 0) * m
