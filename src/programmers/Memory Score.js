/**
* https://school.programmers.co.kr/learn/courses/30/lessons/176963
* Implementation Problem
*/
//1. My Solution
function solution(name, yearning, photo) {
    const map = {}
    name.forEach((n, i) => map[n] = yearning[i])
    return photo.map(p => p.reduce((a, b) => a + (map[b] || 0), 0));
}

//2. Other Solution
function solution(name, yearning, photo) {
    return photo.map((v)=> v.reduce((a, c)=> a += yearning[name.indexOf(c)] ?? 0, 0))
}
