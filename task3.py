import heapq

def dijkstra(graph, start):
    heap = []
    heapq.heappush(heap, (0, start))  
    shortest_paths = {node: float('inf') for node in graph}
    shortest_paths[start] = 0
    
    while heap:
        current_distance, current_node = heapq.heappop(heap)
        
        if current_distance > shortest_paths[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
    
    return shortest_paths

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
shortest_paths = dijkstra(graph, start_node)

for node, distance in shortest_paths.items():
    print(f"Найкоротший шлях від {start_node} до {node}: {distance}")