
##graph = {
##    "S" : ["A", "D"],
##    "A" : ["B", "C"],
##    "D" : ["B", "E"],
##    "B" : ["C", "E"],
##    "C" : ["G"],
##    "E" : ["G"],
##    "G" : []
##}
##
##visited = []
##
##queue = []
##
##visited_D = set()
##
##
##def BFS(visited, graph, node):
##    visited.append(node)
##    queue.append(node)
##
##    while queue:
##        m = queue.pop(0)
##        print(m, end=" ")
##
##        for neighbour in graph[m]:
##
##            if neighbour not in visited:
##                visited.append(neighbour)
##                queue.append(neighbour)
##
##
##
##
##
##
##def DFS(visited_D, graph, node):
##
##    if node not in visited_D:
##        print(node, end=" ")
##        visited_D.add(node)
##        for neighbour in graph[node]:
##            DFS(visited_D, graph, neighbour)
##
##
##print("Applying BFS...")
##BFS(visited, graph, "S")
##print()
##print("Applying DFS...")
##DFS(visited_D, graph, "S")





def iterative_deepening_search(graph, start_node, goal_node):
     depth_limit = 0
     while True:
        result = depth_limited_search(graph, start_node, goal_node, depth_limit)
        if result == goal_node:
            return result
        depth_limit += 1

     
def depth_limited_search(graph, node, goal, depth_limit):
    if depth_limit == 0 and node == goal:
         return node
    elif depth_limit > 0:
        if node == goal:
            return node
        elif depth_limit > 0:
            for neighbor in graph[node]:
                result = depth_limited_search(graph, neighbor, goal, depth_limit- 1)
                if result == goal:
                    return result
    return None
 # Example usage:
graph = {
    'S':['A', 'D'],
    'A': ['B', 'C'],
    'B': ['C', 'E'],
    'C': ['G'],
    'D': ['B','E'],
    'E': ['G'],
    'G': []
}
start_node = 'S'
goal_node = 'G'
result = iterative_deepening_search(graph, start_node, goal_node)
if result:
    print(f"Path found from {start_node} to {goal_node}: {result}")
else:
    print(f"No path found from {start_node} to {goal_node}.")


























