# NodesAndEdges

## Contains modules for determining features of graphs

The modules written here are written in `python 3.6.4`. Please make sure that you have this or a later version installed to ensure that they run.

### graph_mod shows a graph that demonstrates modular arithmetic

The user specifies any integer as a base, then specifies a number to increment (i.e. count) by.
A graph is generated that represents the positions of the numbers in that base, just as an analog clock represents numbers in base 12 (or base 60).

Goals: Generate a graph where each node will be connected 
1. To each subsequent node
2. To the node that it jumps to when iterating through values (i.e. counting)

Create labels for the graph that will show
1. Value of node in base specified by user
2. Current running sum of current node and all previous nodes
3. x and y coordinates on graph
4. Angular displacement from first node