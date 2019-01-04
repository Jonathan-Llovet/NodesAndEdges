def find_all_edges(nodes):
    '''Finds the number of edges within a graph with the specified number of nodes,
    where there is a single connection between every pair of nodes.
    An example application of this is to determine how many distinct pairs are in a group.'''
    try:
        if type(nodes) != int:
            message = "You must enter a positive integer indicating the number of nodes."
            return message
        if nodes < 1:
            message = "You must enter a positive integer indicating the number of nodes."
            return message
        elif nodes <= 2:
            total_edges = nodes - 1
            return total_edges
        else:
            peripheral_edges = nodes
            inner_edges = find_inner_edges(nodes)
            total_edges = inner_edges + peripheral_edges
            return total_edges
    except:
        message = "You must enter a positive integer indicating the number of nodes."
        return message


def find_inner_edges(nodes):
    '''Returns the number of inner edges in graph containing specified number of nodes, 
    where there is a single connection between every pair of nodes.
    Inner edges here are the edges connecting non-adjacent nodes in a polygon. 
    For a simple geometrical case, the diagonals of a quadrilateral are inner edges.'''
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