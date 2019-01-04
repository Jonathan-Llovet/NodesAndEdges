def find_all_edges(nodes):
    '''Finds the number of edges within a graph with the specified number of nodes,
    where there is a single connection between every node.
    An example application of this is to determine how many distinct pairs are in a group.'''
    if nodes < 1:
        message = "You must enter a positive number of nodes"
        return message
    elif nodes == 1:
        total_edges = 0
        return total_edges
    elif nodes == 2:
        total_edges = 1
        return total_edges
    else:
        peripheral_edges = nodes
        inner_edges = find_inner_edges(nodes)
        total_edges = inner_edges + peripheral_edges
        return total_edges

def find_inner_edges(nodes):
    if nodes < 3:
        inner_edges = 0
        return inner_edges
    elif nodes == 4:
        inner_edges = 2
        return inner_edges
    else:
        m = nodes - 3
        inner_edges = m
        while m > 0:
            inner_edges += m
            m -= 1
        return inner_edges
    
if __name__ == "__main__":
    graphs = []    
    for i in range(1,11):
        graphs.append(find_all_edges(i))
    for graph in graphs:
        print(graph)