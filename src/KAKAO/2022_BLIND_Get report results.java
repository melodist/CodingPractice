/**
 * https://programmers.co.kr/learn/courses/30/lessons/92334?language=java
 * Implementation Problem
 */
import java.util.*;

class Solution {
    private Map<String, ReportIdsSet> reportIdsSetMap;
    private Map<String, Integer> reportedCountMap;

    private Map<String, ReportIdsSet> initializeReportIdsSetMap(String[] id_list, String[] report) {
        Map<String, ReportIdsSet> reportIdsSetMap = new HashMap<>();

        for (int i = 0; i< id_list.length; i++) {
            reportIdsSetMap.put(id_list[i], new ReportIdsSet());
        }

        for (int j = 0; j< report.length; j++) {
            StringTokenizer tokenizer = new StringTokenizer(report[j], " ");
            String reporter = tokenizer.nextToken();
            String reported = tokenizer.nextToken();
            reportIdsSetMap.get(reporter).add(reported);
        }

        return reportIdsSetMap;
    }

    private Map<String, Integer> getStringIntegerMap(Collection<ReportIdsSet> reportIdsSets) {
        Map<String, Integer> reportMap = new HashMap<>();
        for (ReportIdsSet reportIdsSet: reportIdsSets) {
            for (String reportedId: reportIdsSet.getReportedIds()) {
                reportMap.put(reportedId, reportMap.getOrDefault(reportedId, 0) + 1);
            }
        }
        return reportMap;
    }

    private int[] getBannedUserCounts(String[] id_list, int k) {
        int n = id_list.length;
        int[] answer = new int[n];
        for (int i = 0; i< id_list.length; i++) {
            Set<String> reportedIdsSet = reportIdsSetMap.get(id_list[i]).getReportedIds();
            answer[i] = calculateBannedUserCount(k, reportedIdsSet);
        }

        return answer;
    }

    private int calculateBannedUserCount(int k, Set<String> reportedIdsSet) {
        int bannedUserCount = 0;
        for (String reported: reportedIdsSet) {
            if (reportedCountMap.get(reported) >= k) bannedUserCount = bannedUserCount + 1;
        }
        return bannedUserCount;
    }

    public int[] solution(String[] id_list, String[] report, int k) {
        // 신고한 유저 리스트 초기화
        reportIdsSetMap = initializeReportIdsSetMap(id_list, report);

        // 신고 횟수 계산
        reportedCountMap = getStringIntegerMap(reportIdsSetMap.values());

        // 정지된 유저 수 계산
        return getBannedUserCounts(id_list, k);
    }

    class ReportIdsSet {
        private Set<String> reportedIds;
        public ReportIdsSet() {
            this.reportedIds = new HashSet<>();
        }

        public void add(String id) {
            reportedIds.add(id);
        }

        public Set<String> getReportedIds() {
            return reportedIds;
        }
    }
}
