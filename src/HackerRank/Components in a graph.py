"""
https://www.hackerrank.com/challenges/components-in-graph/problem
"""
def componentsInGraph(queries):
    def find_set(root: int, array: list) -> int:
        if array[root] == root:
            return root
        else:
            return find_set(array[root], array)
    
    n = len(queries)
    nodes_count = 2*n+1
    root = [0] * nodes_count
    count = [0] * nodes_count

    for i in range(1, nodes_count):
        root[i] = i
        count[i] = 1
    
    for query in queries:
        a, b = query
        
        # find root of a & b
        a_root = find_set(a, root);
        b_root = find_set(b, root)
        if a_root == b_root:
            continue
        
        # union without ranking
        root[b_root] = a_root
        count[a_root] += count[b_root]
        count[b_root] = 0
    
    # find min and max
    smallest, biggest = nodes_count, -1
    for i in range(1, nodes_count):
        if count[i] > biggest:
            biggest = count[i]

        if count[i] > 1 and count[i] < smallest:
            smallest = count[i]
    
    return [smallest, biggest]
