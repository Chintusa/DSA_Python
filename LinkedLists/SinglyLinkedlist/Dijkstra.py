import heapq 
def dijkstra(graph,source):
    dist={node : float('inf') for node in graph }
    dist[source]=0
    minHeap=[(0,source)]

    while minHeap:
        curr_dist,u=heapq.heappop(minHeap)

        for v,w in graph[u].items():
            if (curr_dist+w) < dist[v]:
                dist[v]=curr_dist+w
                heapq.heappush(minHeap,(dist[v],v))
    return dist

# Sample graph
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A':4,'C': 5, 'D': 10},
    'C': {'A':2,'B':5,'E':3},
    'D': {'B':10,'E':4,'F':11},
'E':{'C':3,'D':4},
'F':{'D':11}
}

distances = dijkstra(graph, 'A')

print("Shortest Distances from A:")
for node, distance in distances.items():
    print(f"A → {node}: {distance}")