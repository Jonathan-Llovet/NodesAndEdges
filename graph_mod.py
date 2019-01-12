# Base, i.e. number of nodes - this will be used as the x in n % x
# base = int(input("Enter an integer to serve as the base:\n"))
# # Incrementor
# steps_to_increment = int(input("Enter the number of steps that should be incremented:\n"))
# 
import math

base = 10
steps_to_increment = 3
def print_header(base, steps_to_increment):
    print(f"\n\tbase = {base}\n")
    print(f"*\tpos\t*\tsum\t*")
    print("*"*33)
    print(f"\n*\t0\t*\t0\t*")
    # Prints the initial position
    print(f"*\t{steps_to_increment}\t*\t{steps_to_increment}\t*")
    # Prints the first step and the base

def add_em_up(base, steps_to_increment):
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
                nodes_total, 
                base, 
                steps_to_increment]
    # Save data into a list to be accessed by other functions
    return journey

def graph_journey(journey):
    base = journey[4]
    theta = base/360
    clockface_values_of_nodes = journey[0]
    hit_data = []
    for i in range(len(clockface_values_of_nodes)):
        node_theta = theta*i
        hit = {
            "angle": node_theta,
            "x": math.cos(node_theta),
            "y": math.sin(node_theta)
        }
        hit_data.append(hit)
    return hit_data

def diagnostic(hit_data):
    for h in range(len(hit_data)):
        print(f"angle: {hit_data[h].get('angle')}")
        print(f"x: {hit_data[h].get('y')}")
        print(f"y: {hit_data[h].get('x')}")
    





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


if __name__ == "__main__":
    # print_header(base, steps_to_increment)
    journey = add_em_up(base, steps_to_increment)    
    print_journey(journey)
    # print_footer(base, steps_to_increment, journey)
    # hit_data = graph_journey(journey)
    # diagnostic(hit_data)
