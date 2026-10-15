
import heapq

def astar(graph, heuristic, start, goal):
    queue = [(heuristic[start], 0, start, [start])]
    visited = set()

    while queue:
        f, cost, node, path = heapq.heappop(queue)

        if node == goal:
            print("Shortest Path:", " -> ".join(path))
            print("Total Cost:", cost)
            return

        if node in visited:
            continue

        visited.add(node)

        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                new_cost = cost + weight
                new_f = new_cost + heuristic[neighbor]

                heapq.heappush(
                    queue,
                    (new_f, new_cost, neighbor, path + [neighbor])
                )

    print("No path found")

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

heuristic = {
    'A': 3,
    'B': 2,
    'C': 1,
    'D': 0
}

astar(graph, heuristic, 'A', 'D')
