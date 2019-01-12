# Base, i.e. number of nodes - this will be used as the x in n % x
# base = int(input("Enter an integer to serve as the base:\n"))
# # Incrementor
# steps = int(input("Enter the number of steps that should be incremented:\n"))
# 
import math

base = 10
steps = 3
def print_header(base, steps):
    print(f"\n\tbase = {base}\n")
    print(f"*\tpos\t*\tsum\t*")
    print("*"*33)
    print(f"\n*\t0\t*\t0\t*")
    # Prints the initial position
    print(f"*\t{steps}\t*\t{steps}\t*")
    # Prints the first step and the base

def add_em_up(base, steps):
    positions_hit = []
    running_sums = []

    sum_of_nodes_hit = steps
    nodes_total = 1
    
    while (sum_of_nodes_hit + steps) % base != steps:
        sum_of_nodes_hit += steps
        positions_hit.append(sum_of_nodes_hit % base)
        running_sums.append(sum_of_nodes_hit)
        # positions
        nodes_total += 1    
    journey = [positions_hit, running_sums, sum_of_nodes_hit, nodes_total, base, steps]
    return journey

def graph_journey(journey):
    base = journey[4]
    theta = base/360
    positions_hit = journey[0]
    hit_data = []
    for i in range(len(positions_hit)):
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
    i = 0
    while journey[0][i]:
        print(f"*\t{journey[0][i]}\t*\t{journey[1][i]}\t*")
        i += 1
    
def print_footer(base, steps, journey):
    sum_of_nodes_hit = journey[2]
    nodes_total = journey[3]
    print("*"*33)
    print(f"We have traversed our graph {int(sum_of_nodes_hit / base)} times!")
    print(f"We have landed on {nodes_total} nodes in our journey around the graph!")
    if nodes_total == base:
        print(f"{steps} and {base} are coprime!")
    else:
        print(f"Thanks for asking. Come again.")   


if __name__ == "__main__":
    print_header(base, steps)
    journey = add_em_up(base, steps)    
    # print_journey(journey)
    # print_footer(base, steps, journey)
    hit_data = graph_journey(journey)
    diagnostic(hit_data)
