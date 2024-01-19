from aoc_graph import Graph, Vertex
from itertools import permutations
import re 

# This function will read a text file format it and retrun an array of the remaining elements. 
def read_file_return_list(file):
    with open(file) as data:
        text = re.sub(r'to|=', '', data.read())
        lines_array = [line.split() for line in text.split('\n')]

        return lines_array
   
# Create a graph for the Traveling Salesperson Problem.
def build_graph(array):
    destinations_graph = Graph(directed=False)
    unique_locations = set()
    
    for line in array:
        unique_locations.update([line[0], line[1]])
        
    for location in unique_locations:
        destinations_graph.add_vertex(Vertex(location))

    for line in array:
        from_vertex = destinations_graph.graph_dict[line[0]]
        to_vertex = destinations_graph.graph_dict[line[1]]
        weight = int(line[2])
        destinations_graph.add_edge(from_vertex, to_vertex, weight)

    return destinations_graph

# This function will visit each vertex in the graph once, and retrun the shortest distance it  can travel to achieve this.
def get_route(graph, greater=False):
    vertex_objects = list(graph.graph_dict.values()) 
    
    if greater: 
        shortest_distance = 0
    else:
        shortest_distance = float('inf')

    for perm in permutations(vertex_objects):
        current_distance = 0
        feasible = True

        for i in range(len(perm) -1):
            current_vertex = perm[i]
            next_vertex = perm[i+1]

            if next_vertex in current_vertex.edges:
                current_distance += current_vertex.edges[next_vertex]
            else:
                feasible = False
                break

        if greater: 
            if feasible and current_distance > shortest_distance:
                shortest_distance = current_distance
           
        else:
            if feasible and current_distance < shortest_distance:
                shortest_distance = current_distance

    return shortest_distance
  
#________Main Program_________ # 
if __name__ == "__main__":

    puzzle_input = read_file_return_list('text.txt')

    distances_graph = build_graph(puzzle_input)

    # Part one: 
    shortest_distance = get_route(distances_graph)
    print(f'The answer to part one is: {shortest_distance}')

    # Part two:
    longest_distance = get_route(distances_graph, True)
    print(f'The answer to part two is: {longest_distance}')