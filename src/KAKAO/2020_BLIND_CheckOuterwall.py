"""
https://programmers.co.kr/learn/courses/30/lessons/60062/
Implementation Problem
"""
#1.My Solution
from itertools import product

def solution(n, weak, dist):
    length = len(dist)
    answer = length + 1

    # dist를 차순으로 정렬
    dist.sort()
    dist.reverse()
    for i in range(len(weak)-1):
        # 최소값을 갱신함
        answer = min(answer, solve(n, weak, dist, len(dist)))
        # weak의 시작점을 n만큼 증가시켜 맨 뒤로 보내기
        weak.append(weak[0]+n)
        del weak[0]

    if answer == length+1:
        return -1
    else:
        return answer

def solve(n, weak, dist, length):

    # weak와 dist 검사
    if not weak:
        return 0
    if weak and not dist:
        return -1

    # node에서 node로 가는 edge의 정보를 담은 list 생성
    edge_list = make_edge_list(weak)

    # num_friends를 하나씩 늘려가며 경우의 수를 찾고, 해답을 찾는 즉시 종료
    for num_friends in range(1, length+2):

        flag = False

        if num_friends == length+1:
            break
        friends_list = dist[0:num_friends]

        # (num_friends - 1) 개의 edge를 제거 -> 사용하지 않아도 되는 edge를 제거
        # 가장 효율적인 경우만 확인하면 됨. 따라서 num_friends - 1개의 edge를 제거
        edge_list_copy = edge_list.copy()

        modified_edge_list = select_delete_edge(num_friends-1, edge_list_copy)

        # breaks if modified_edge_list is empty
        if not modified_edge_list:
            break
        for modified_edge in modified_edge_list:
            start = modified_edge[0][0]
            end = modified_edge[0][1]
            if len(modified_edge)==1:
                sum_list = [end - start]
            else:
                sum_list = []
                for i in range(1, len(modified_edge)):
                    
                    # if edges are connected, friends keep going
                    if end == modified_edge[i][0]:
                        # if edge is last edge
                        if i==len(modified_edge)-1:
                            end = modified_edge[i][1]
                            sum_list.append(end - start)
                        else:
                            end = modified_edge[i][1]
                    # if edges are seperated
                    else:
                        sum_list.append(end - start)
                        start = modified_edge[i][0]
                        end = modified_edge[i][1]
                        # if edge is last edge
                        if i==len(modified_edge)-1:
                            sum_list.append(end - start)

            if not sum_list:
                flag = True
                break
            # if edges are more than friends, it cannot be the answer
            if len(sum_list) > len(dist):
                continue
            flag = True
            # Check each friend can travel the edge
            sum_list.sort()
            sum_list.reverse()
            for k in range(len(sum_list)):
                if sum_list[k] > dist[k]:
                    flag = False
                    break

            if flag:
                break
        if flag:
            break

    return num_friends

def make_edge_list(weak):
    """ 취약 지점에서 취약 지점으로 가는 edge를 tuple 형태로 생성
    """
    edge_list = []
    for i in range(len(weak)-1):
        edge_list.append((weak[i], weak[i+1]))
    return edge_list

def select_delete_edge(num_delete, edge_list):
    """ 지정된 edge를 list에서 제거함
    bit-mask를 이용하여 num_delete 개의 edge가 제거된 list를 원소로 갖는 list 획득
    """
    # Make bit-mask
    masks = list(reversed(list(product((0, 1), repeat=len(edge_list)))))
    # Select bit-mask meets the condition
    masks = [mask for mask in masks if mask.count(0)==num_delete]

    # make edge list to visit
    modified_edge_list = []
    for mask in masks:
        modified_edge = []
        for single_edge, single_mask in zip(edge_list,mask):
            if single_edge * single_mask != tuple():
                modified_edge.append(single_edge * single_mask)
        # returns true if modified_edge has values
        if modified_edge:
            modified_edge_list.append(modified_edge)

    return modified_edge_list
    
n = 12
weak = [1,3,4,9,10]
dist = [1,2,3,4,5,6,7]

solution(n, weak, dist)

#2. Other Solution
from collections import deque


def solution(n, weak, dist):
    dist.sort(reverse=True)
    q = deque([weak])
    visited = set()
    visited.add(tuple(weak))
    for i in range(len(dist)):
        d = dist[i]
        for _ in range(len(q)):
            current = q.popleft()
            for p in current:
                l = p
                r = (p + d) % n
                # l : start node / r : end node
                # temp stores the nodes not visited
                if l < r:
                    temp = tuple(filter(lambda x: x < l or x > r, current))
                else:
                    temp = tuple(filter(lambda x: x < l and x > r, current))
                
                # Check is finished if temp is empty
                if len(temp) == 0:
                    return (i + 1)
                # Not need to use the path already used
                elif temp not in visited:
                    visited.add(temp)
                    q.append(list(temp))
    return -1
