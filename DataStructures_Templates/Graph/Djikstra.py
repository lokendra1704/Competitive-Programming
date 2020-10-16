graph = {
    0: {1:4,2:1},
    1: {3:1},
    2: {1:2,3:5},
    3: {4:3},
    4: dict(),
}
from heapq import heapify,heappush,heappop
def djikstra(graph,start):
    dist = [float("inf")]*len(graph)
    vis = [False]*len(graph)
    prev = [None]*len(graph)
    dist[start] = 0
    heap = [(0,start)]
    while heap:
        curDistance,curNode = heappop(heap)
        if curDistance > dist[curNode]:
            continue
        for neighbour,weight in graph[curNode].items():
            if vis[neighbour]==True:
                continue
            best_distance = dist[curNode] + weight
            if best_distance < dist[neighbour]:
                prev[neighbour] = curNode
                dist[neighbour] = best_distance
                heappush(heap,(best_distance,neighbour))
        vis[curNode] = True
    return (dist,prev)

def findShortestPath(graph,start,end):
    dist,prev = djikstra(graph,start)
    path = []
    ptr = end
    while ptr!=None:
        path.append(str(ptr))
        ptr = prev[ptr]
    path.reverse()
    return '->'.join(path)

print(findShortestPath(graph,0,4))
