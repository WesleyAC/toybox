#!/usr/bin/env python3

def dijkstra_pathfind(graph, start, goal):
    dists = {node: (0 if node == start else -1) for node in graph}
    unvisited = list(graph.keys())
    path = []
    current = start
    while current != goal: #TODO(Wesley) termination in no path case
        path.append(current)
        for node,dist in graph[current]:
            dists[node] += dist
        unvisited.remove(current)
        current = min(filter(lambda x: x[0] in unvisited, graph[current]), key=lambda x: dists[x[0]])[0]
    path.append(goal)
    return path

if __name__ == "__main__":
    g = {1:[(3,7),(4,1)],
         2:[(3,1),(7,1)],
         3:[(1,7),(2,1),(6,2)],
         4:[(1,1),(5,3)],
         5:[(4,3),(6,2)],
         6:[(3,2),(5,2),(7,1)],
         7:[(2,1),(6,1)]}
    print(dijkstra_pathfind(g, 1, 7))
