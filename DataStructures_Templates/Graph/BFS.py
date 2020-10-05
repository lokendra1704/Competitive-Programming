graph = {
    0: [1,9],
    1: [0,8],
    2: [3],
    3: [2,4,5,7],
    4: [3],
    5: [3,6],
    6: [5,7],
    7: [3,6,8,10,11],
    8: [1,7,9],
    9: [0,8],
    10: [7,11],
    11: [7,10],
    12: []
}
from collections import deque
def BFS(source, graph):
    q = deque([source])
    seen = set([source])
    while q:
        for i in range(len(q)):
            node = q.popleft()
            print(node)
            for j in graph[node]:
                if j not in seen:
                    seen.add(j)
                    q.append(j)

BFS(0,graph)
    