import numpy as np
import random as rnd
import time
import matplotlib.pyplot as plt
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
                    # Return 0 if there is no path from origin node to destination node
                    if (predecessor_distance[j][1]>= np.inf):
                        return 0
                    
    # Trace smallest path from destination node to origin node
    path = []
    current_node = destination_node
    while current_node != None:
        path.append(current_node)
        current_node = predecessor_distance[current_node][0]

    # Reverse path to obtain path from origin node to destination node
    return path[::-1]
#----------------------------Functions---------------------------------#


def graph_generation(N,k_av):

    edge_list = []
    p = k_av/N # Using the relationship between the average degree and edge connection probability <k> ~=~ N*p
    
    for current_node in range(N):
        
        for destination_node in range(N):
            
            # We assume nodes dont connect with themselves
            if (current_node == destination_node):
                continue
            
            # Our probability of having an edge with an unique node
            if (rnd.uniform(0.0, 1.0) > p):
                continue

            edge_connection = (current_node, destination_node, 1)
            check_edge_connection = (destination_node, current_node, 1)
            other_edge_connection = (destination_node, current_node, 1)
            # Nodes are unidirectional so any copy can be removed
            if check_edge_connection in edge_list:
                continue
            
            edge_list.append(edge_connection)
            edge_list.append(other_edge_connection)


    return edge_list


def average_graph_time(edge_list, N, iterations):
    time_per_test = []

    i = 0
    while (i < iterations): 
        
        origin_node = rnd.randint(0,N-1)
        destination_node = rnd.randint(0,N-1)

        
        start_time = time.time()
        path = dijkstra(edge_list,origin_node, destination_node)
        total_time = time.time() - start_time
        
        # Redo if no path from origin node to destination node
        if (path == 0):
            continue

        time_per_test.append(total_time)
        i += 1

    return np.average(time_per_test)


def time_to_nodesize_plot(k_av, iterations,N_start, N_stop):

    average_list = []

    for i in range(N_start, N_stop+1):
        
        edge_list = graph_generation(2**i, k_av)
        average_time = average_graph_time(edge_list, 2**i, iterations)
        average_list.append(average_time)
        print(f"Done with N^{i}")

    print(average_list)

    plt.plot(range(N_start, N_stop+1), np.log(average_list), color = "black")
    plt.xticks(range(N_start, N_stop + 1))
    plt.grid() 
    plt.ylabel("log(Average Time (s))")
    plt.xlabel("Exponent N (Network Size = $2^N$)")
    plt.title("Log Average Time vs Network Size $2^N$")
    plt.show()

#---------------------------Testing-----------------------------#

k_av = 20
m = 20

N_start = 3
N_stop = 13

time_to_nodesize_plot(k_av, m, N_start, N_stop)
