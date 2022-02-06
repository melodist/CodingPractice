/**
 * https://programmers.co.kr/learn/courses/30/lessons/12901
 */
//1. Simple Solution
class Solution {
    public String solution(int a, int b) {
        String answer = "";
        Integer[] dayOfMonth = { 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
        String[] dayOfWeek = { "SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT" };
        int days = -1;

        for (int i = 0; i < a - 1; i++) {
            days += dayOfMonth[i];
        }
        days += b;
        answer = dayOfWeek[(days + 5) % 7];

        return answer;
    }
}

//2. Solution using LocalDate
import java.time.LocalDate;
import java.time.format.TextStyle;
import java.util.Locale;


class Solution {
    public String solution(int a, int b) {
        return LocalDate.of(2016, a, b)
            .getDayOfWeek()
            .getDisplayName(TextStyle.SHORT, Locale.ENGLISH)
            .toUpperCase();
    }
}
