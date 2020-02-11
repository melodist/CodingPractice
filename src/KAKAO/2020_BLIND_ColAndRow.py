def delete(build, result):
    temp = result.copy()
    print(f'Delete {build[:3]}')
    temp.pop(temp.index(build[:3]))
    if not check(temp):
        print('Cannot Delete Element')
        temp = result
    return temp

def construct(build, result):
    temp = result.copy()
    print(f'Construct {build[:3]}')
    temp.append(build[:3])
    if not check(temp):
        print('Cannot Create Element')
        temp = result
    return temp

def check(result):
    """
    기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
    보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.

    각 원소에 대하여 조건을 만족하는 조합을 만들고 그 조합이 result 내에 있는지 확인
    """
    for i, el in enumerate(result):
        x = el[0]
        y = el[1]
        a = el[2]

        if len(result) == 0:
            return True
        elif len(result) == 1:
            if x == 0 and a == 0:
                return True
            else:
                return False
        
        # i번째 원소가 기둥인 경우
        if a == 0:  
            # 바닥에 있는 경우
            if y == 0:
                continue
            else:
                # el = [x, y, 0] -> [x, y-1, 0] or [x-1, y, 1] or [x, y, 1]
                if not ([x, y-1, 0] in result or [x-1, y, 1] in result or [x, y, 1] in result):
                        print("1")
                        return False
        # i번째 원소가 보인 경우
        else:
            # el = [x, y, 1] -> [x, y-1, 0] or [x+1, y-1, 0] or [x-1, y, 1] and [x+1, y, 1]
            if not ([x, y-1, 0] in result or [x+1, y-1, 0] in result or \
                    ([x-1, y, 1] in result and [x+1, y, 1] in result)):
                print("3")
                return False

    return True
    
def solution(n, build_frame):
    answer = []
    for build in build_frame:
        if build[3] == 0:
            answer = delete(build, answer)
        else:
            answer = construct(build, answer)
    answer.sort()
    return answer

n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
# result = [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]

result = solution(n, build_frame)
print(result)
  
