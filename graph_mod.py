import math
import matplotlib.pyplot as plt

# -----------------------------------------------------------------
# User input section
# Base, i.e. number of nodes - this will be used as the x in n % x
base = int(input("Enter an integer to serve as the base:\n"))
# Incrementor
steps_to_increment = int(input("Enter the number of steps that should be incremented:\n"))

# -----------------------------------------------------------------

# Textual summary section

def print_header(base, steps_to_increment):
    print(f"\n\tbase = {base}\n")
    print(f"*\tpos\t*\tsum\t*")
    print("*"*33)

def print_journey(journey):
    for i in range(len(journey[0])):
        print(f"*\t{str(journey[0][i])}\t*\t{str(journey[1][i])}\t*")
    
def print_footer(base, steps_to_increment, journey):
    sum_of_nodes_hit = journey[2]
    nodes_total = journey[3]
    print("*"*33)
    print(f"We have traversed our graph {int(sum_of_nodes_hit / base)} times!")
    print(f"We have landed on {nodes_total} nodes in our journey around the graph!")
    if nodes_total == base:
        print(f"{steps_to_increment} and {base} are coprime!")
    else:
        print(f"Thanks for asking. Come again.") 

def print_section(base, steps_to_increment, journey):
    print_header(base, steps_to_increment)
    print_journey(journey)
    print_footer(base, steps_to_increment, journey)

# -----------------------------------------------------------------

# Main modular arithmetic calculation section

def calculate_journey(base, steps_to_increment):
    clockface_values_of_nodes = [0]
    running_sum_of_node_values_in_base_10 = [0]
    # Initialize to include starting position, i.e., position 0
    
    sum_of_nodes_hit = 0 + steps_to_increment
    nodes_total = 1
    # Initialize to include first node hit

    while (sum_of_nodes_hit) % base != 0:
        clockface_values_of_nodes.append(sum_of_nodes_hit % base)
        # Add the proverbial "clockface" value of current node to list
        running_sum_of_node_values_in_base_10.append(sum_of_nodes_hit)
        # Add the sum of current and all preceding nodes to list
        sum_of_nodes_hit += steps_to_increment
        nodes_total += 1
    
    clockface_values_of_nodes.append(sum_of_nodes_hit % base)
    running_sum_of_node_values_in_base_10.append(sum_of_nodes_hit)
    # Save values for final node (return to original position)
    
    journey = [clockface_values_of_nodes, 
                running_sum_of_node_values_in_base_10, 
                sum_of_nodes_hit, 
                nodes_total]
    # Save data into a list to be accessed by other functions
    return journey

# -----------------------------------------------------------------

# Helper trigonometric functions

def get_cosine_from_degrees(x):
    cosine = math.degrees(math.cos(math.radians(x)))
    return cosine

def get_sine_from_degrees(y):
    sine = math.degrees(math.sin(math.radians(y)))
    return sine

# Converter for graph data

def calculate_graph_coordinates(base, journey):
    theta = 360/base
    clockface_values_of_nodes = journey[0]
    hit_data = []
    for i in range(len(clockface_values_of_nodes)):
        node_theta = theta*clockface_values_of_nodes[i]
        hit = {
            "angle": node_theta,
            "x": get_cosine_from_degrees(node_theta),
            "y": get_sine_from_degrees(node_theta)
        }
        hit_data.append(hit)
    return hit_data

# Graphing helper function
def connectpoints(x,y,p1,p2):
    '''Credit to https://stackoverflow.com/users/588071/tmdavison on the question here: 
    https://stackoverflow.com/questions/35363444/plotting-lines-connecting-points'''
    x1, x2 = x[p1], x[p2]
    y1, y2 = y[p1], y[p2]
    plt.plot([x1,x2],[y1,y2],'k-')


def draw_graph(hit_data):
    xs = []
    ys = []
    for hit in hit_data:
        xs.append(hit.get("x"))
        ys.append(hit.get("y"))
    plt.scatter(xs, ys, c='red')
    i = 0
    j = 1
    while j < len(xs):
        connectpoints(xs, ys, i, j)
        i += 1
        j += 1
    connectpoints(xs, ys, len(xs)-1, 0)
    plt.ylabel('some numbers')
    plt.axis('equal')
    plt.show()

# -----------------------------------------------------------------    

# Troubleshooting functions

def diagnostic(hit_data):
    for h in range(len(hit_data)):
        print(f"angle: {hit_data[h].get('angle')}")
        print(f"x: {hit_data[h].get('y')}")
        print(f"y: {hit_data[h].get('x')}")

# -----------------------------------------------------------------

# Checks for main

if __name__ == "__main__":
    journey = calculate_journey(base, steps_to_increment)    
    print_section(base, steps_to_increment, journey)
    hit_data = calculate_graph_coordinates(base, journey)
    draw_graph(hit_data)
    # diagnostic(hit_data)
