NETWORK FLOW PROBLEM:
import networkx as nx

# Step 1: Model the Network Flow Problem
G = nx.DiGraph()
G.add_edge('source', 'A', capacity=10)
G.add_edge('source', 'B', capacity=5)
G.add_edge('A', 'C', capacity=9)
G.add_edge('A', 'B', capacity=3)
G.add_edge('B', 'C', capacity=7)
G.add_edge('B', 'sink', capacity=8)
G.add_edge('C', 'sink', capacity=12)

# Step 2: Solve the Network Flow Problem
max_flow_value, flow_dict = nx.maximum_flow(G, 'source', 'sink')
print("NETWORK FLOW PROBLEM:")
print("Maximum Flow Value:", max_flow_value)
print("Flow Dict:", flow_dict)

LINEAR PROGRAMMING PROBLEM:
from scipy.optimize import linprog

# Step 3: Model the Linear Programming Problem
c = [-3, -2]  # Coefficients of the objective function (to minimize)
A = [[1, 1],  # Coefficients of inequality constraints
     [1, 0],
     [0, 1]]
b = [10, 8, 5]  # Right-hand side of inequality constraints
x0_bounds = (0, None)  # Bounds for decision variables
x1_bounds = (0, None)

# Step 4: Solve the Linear Programming Problem
res = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')
print("\nLINEAR PROGRAMMING PROBLEM:")
print("Optimal Solution:", res.x)
print("Optimal Objective Value:", res.fun)

output:

NETWORK FLOW PROBLEM:
Maximum Flow Value: 15
Flow Dict: {'source': {'A': 10, 'B': 5}, 
            'A': {'C': 9, 'B': 1}, 
            'B': {'C': 5, 'sink': 5}, 
            'C': {'sink': 12}, 
            'sink': {}}

LINEAR PROGRAMMING PROBLEM:
Optimal Solution: [4. 1.]
Optimal Objective Value: -14.0
