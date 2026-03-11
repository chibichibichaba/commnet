import numpy as np
import random as rnd
from project0 import dijkstra 
import time
import matplotlib.pyplot as plt


#Functions                                

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
            # Nodes are unidirectional so any copy can be removed
            if check_edge_connection in edge_list:
                continue
            
            edge_list.append(edge_connection)


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
        print(f"Done with iteration {i}")

    print(average_list)

    plt.semilogy(range(N_start, N_stop+1), average_list, color = "black")    
    plt.ylabel("Average Time (s)")
    plt.xlabel("Exponent N (Network Size 2^N)")
    plt.title("Time to Network Size 2^N")
    plt.show()

## Testing ##                                

#N = 2**5
k_av = 20
m = 20

#print(average_graph_time(graph_generation(N, k_av), N, m))

N_start = 5
N_stop = 6

time_to_nodesize_plot(k_av, m, N_start, N_stop)

