/**
* https://school.programmers.co.kr/learn/courses/30/lessons/150370
* Implementation Problem
*/
//1. My Solution
function solution(today, terms, privacies) {
    const dateToDay = date => {
        const [year, month, day] = date.split('.').map(n => parseInt(n));
        return year * 28 * 12 + month * 28 + day;
    }
    
    const todayDay = dateToDay(today);
    const termsMap = terms.reduce((termsMap, term) => {
        const [label, length] = term.split(' ');
        termsMap[label] = length;
        return termsMap;
    }, {})

    const answer = [];
    privacies.forEach((privacy, i) => {
        const [date, label] = privacy.split(' ');
        const expireDay = dateToDay(date) + termsMap[label] * 28 - 1;
        
        if (todayDay > expireDay) {
            answer.push(i+1);
        }
    })
    
    return answer;
}
