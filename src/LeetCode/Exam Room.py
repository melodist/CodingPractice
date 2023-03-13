"""
https://leetcode.com/problems/exam-room
Using priority queue
"""
#1. My Solution (171ms)
class ExamRoom:

    def __init__(self, n: int):
        self.intervals = collections.defaultdict(set)
        self.pq = [(0, 0, n - 1)]
        self.intervals[0].add((0, n - 1))
        self.n = n
        self.zeroDeleted = True
        self.nDeleted = True

    def seat(self) -> int:

        while self.pq:
            dist, i, j = heapq.heappop(self.pq)
            if (i, j) not in self.intervals[i]:
                continue
            break

        if self.zeroDeleted and i == 0:
            self.zeroDeleted = False
            mid = 0
            self.putrigh(mid, j)
        elif self.nDeleted and j == self.n - 1:
            self.nDeleted = False
            mid = self.n - 1
            self.putleft(i, mid)
        else:
            mid = (i + j) // 2
            self.putleft(i, mid)
            self.putrigh(mid, j)

        return mid

    def putleft(self, i, mid):
        heapq.heappush(self.pq, (-((mid - i) // 2), i, mid))
        self.cleanupleft(i, mid)
        self.cleanupright(i, mid)

    def putrigh(self, mid, j):
        heapq.heappush(self.pq, (-((j - mid) // 2), mid, j))
        self.cleanupleft(mid, j)
        self.cleanupright(mid, j)

    def cleanupleft(self, key, y):
        to_evict = set([(i, j) for i, j in self.intervals[key] if i == key])
        self.intervals[key] = self.intervals[key].difference(to_evict)
        self.intervals[key].add((key, y))

    def cleanupright(self, x, key):
        to_evict = set([(i, j) for i, j in self.intervals[key] if j == key])
        self.intervals[key] = self.intervals[key].difference(to_evict)
        self.intervals[key].add((x, key))

    def leave(self, p: int) -> None:
        vals = sorted(self.intervals[p])
        l = vals[0][0]
        r = vals[0][1]
        if p == 0:
            self.zeroDeleted = True
            heapq.heappush(self.pq, (-(r - l), l, r))
            self.cleanupright(p, r)
            self.cleanupleft(p, r)
        elif p == self.n - 1:
            self.nDeleted = True
            heapq.heappush(self.pq, (-(r - l), l, r))
            self.cleanupright(l, p)
            self.cleanupleft(l, p)
        else:
            l = vals[0][0]
            r = vals[1][1]
            self.cleanupleft(l, r)
            self.cleanupright(l, r)
            if (self.zeroDeleted and l == 0) or (self.nDeleted and r == self.n - 1):
                heapq.heappush(self.pq, (-(r - l), l, r))
            else:
                heapq.heappush(self.pq, (-((r - l) // 2), l, r))
            self.intervals.pop(p)
        
# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)

#2. Other Solution using bisect.insort
class ExamRoom:

    def __init__(self, n: int):
        self.n, self.room = n, []


    def seat(self) -> int:
        if not self.room: ans = 0                           # sit at 0 if empty room 

        else:
            dist, prev, ans = self.room[0], self.room[0], 0 # set best between door and first student   

            for curr in self.room[1:]:                      # check between all pairs of students  
                d = (curr - prev)//2                        # to improve on current best

                if dist < d: dist, ans = d, (curr + prev)//2
                prev = curr

            if dist < self.n - prev-1: ans = self.n - 1     # finally, check whether last seat is best

        insort(self.room, ans)                              # sit down in best seat

        return ans
