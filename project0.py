import numpy as np

# Create edge list (start_node, end_node, weight)
# This example edge list is from week 4 discussion 1 slides pdf page 6
# where A = 0, B = 1 ..... S = 8
edge_list = [
    (0, 1, 1),
    (0, 5, 5),
    (1, 3, 2),
    (1, 7, 1),
    (2, 0, 2),
    (3, 2, 3),
    (4, 2, 1),
    (5, 6, 1),
    (5, 7, 3),
    (6, 4, 1),
    (7, 6, 1),
    (8, 3, 8),
    (8, 4, 1)
]

def dijkstra(edge_list, origin_node, destination_node):
    # Maximum node number (nodes can be only outgoing or incoming so need to check both)
    max_node_outgoing = max(edge_list[i][0] for i in range(len(edge_list)))
    max_node_incoming = max(edge_list[i][1] for i in range(len(edge_list)))
    max_node = max(max_node_outgoing, max_node_incoming)

    # Create predecessor and distance from origin node list
    predecessor_distance = [(None, np.inf)] * (max_node + 1)
    predecessor_distance[origin_node] = (None, 0)

    # Create visited record
    visited = [False] * (max_node + 1)

    current_node = origin_node
    while False in visited:
        # Compute distances to neighboring nodes if smaller than current known distance
        for i in edge_list:
            if (i[0] == current_node):
                if (predecessor_distance[current_node][1] + i[2] < predecessor_distance[i[1]][1]):
                    predecessor_distance[i[1]] = (current_node, predecessor_distance[current_node][1] + i[2])
        # Set current node as visited            
        visited[current_node] = True

        # Exit loop it destination node is reached
        if current_node == destination_node:
            break

        # Find the unvisited node with the smallest distance to origin node
        minimum_distance = np.inf
        for j in range(len(predecessor_distance)):
            if (visited[j] == False):
                if (predecessor_distance[j][1] < minimum_distance):
                    minimum_distance = predecessor_distance[j][1]
                    current_node = j
        
    # Trace smallest path from destination node to origin node
    path = []
    current_node = destination_node
    while current_node != None:
        path.append(current_node)
        current_node = predecessor_distance[current_node][0]

    # Reverse path to obtain path from origin node to destination node
    return path[::-1]

# Find shortest path from S to H
print(f"Shortest path: {dijkstra(edge_list, 8, 7)}")