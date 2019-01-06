# Base, i.e. number of nodes - this will be used as the x in n % x
# base = int(input("Enter an integer to serve as the base:\n"))
# # Incrementor
# steps = int(input("Enter the number of steps that should be incremented:\n"))
# 

base = 150
steps = 6
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
    journey = [positions_hit, running_sums, sum_of_nodes_hit, nodes_total]
    return journey

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
    print_journey(journey)
    print_footer(base, steps, journey)
    
