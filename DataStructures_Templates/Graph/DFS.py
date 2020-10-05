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


clock = 1
pre = {}
post = {}
def dfs(source,graph):
    seen = set([source])
    def previsit(source):
        global clock
        pre[source] = clock
        clock+=1
    def postvisit(source):
        global clock
        post[source] = clock
        clock+=1
    def explore(source):
        previsit(source)
        for i in graph[source]:
            if i not in seen:
                seen.add(i)
                explore(i)
        postvisit(source)
    explore(source)
    print({i:(pre[i],post[i]) for i in pre})

dfs(0,graph)

'''
Applications:
> Compute a graph's minimum spanning Tree
> Detect and find cycles in a graph
> Check if a graph is bipartite
> Find strongly connected components
> Topologically Sort the nodes of a graph
> Find Bridges and articulation points
> Find augmenting paths in a flow network
> Generate Mazes
'''