# Helper Functions ====================
def DFS1(nodeNo, graph, visited):
    visited[nodeNo] = True
    for edge in graph[nodeNo]:
        if visited[edge] != True:
            DFS1(edge, graph, visited)

def DFS2(nodeNo, parentNodeNo, graph, visited):
    visited[nodeNo] = True
    for edge in graph[nodeNo]:
        if edge == parentNodeNo:
            continue;
        if visited[edge]:
            return True
        if DFS2(edge, nodeNo, graph, visited):
            return True
    return False

def proceed(graph, path, position):
    if position == len(graph):
        if path[position-1] in graph[0]:
            return True
        return False
    
    for node in graph.keys():
        if node != 0:
            if (path[position-1] in graph[node]) and not (node in path):
                path[position] = node
                if proceed(graph, path, position+1):
                    return True
                path[position] = -1
    
    return False


# Question-1 (1 mark) =================
def isConnected(graph, visited):
    connected = True
    DFS1(0, graph, visited)
    for bool in visited:
        if not bool:
            connected = False
    return connected

# Question-2 (2 marks) ================
def containsCycle(nodeNo, graph, visited):
    for n in graph.keys():
        if visited[n]:
            continue
        if DFS2(n, -1, graph, visited):
            return True

    return False

# Question-3 (4 marks) ================
def containsHamiltonian(nodeNo, graph, visited):
    path = [0]
    for i in range(1, len(graph)):
        path.append(-1)
    if not proceed(graph, path, 1):
        return False
    return True
        


# ============= Main Code =============
graph = {}
visitedForConnected = []
visitedForCycle = []
visitedForHamiltonian = []

# Reading graph from SNAP-generated text
with open("test.txt", "r") as f:
    for line in f:
        if line[0] == "#":
            continue
        if int(line[0]) not in graph.keys():
            graph[int(line[0])] = []
        if int(line[2]) not in graph.keys():
            graph[int(line[2])] = []
        graph[int(line[0])].append(int(line[2]))
        graph[int(line[2])].append(int(line[0]))

# Testing code
for node in graph:
    visitedForConnected.append(False)
    visitedForCycle.append(False)
    visitedForHamiltonian.append(False)

connected = isConnected(graph, visitedForConnected)
cycle = containsCycle(0, graph, visitedForCycle)

print("Is the graph connected?                     " + str(connected))
print("Does the graph contain a cycle?             " + str(cycle))
if connected and cycle:
    print("Does the graph contain a Hamiltonian cycle? " + str(containsHamiltonian(0, graph, visitedForHamiltonian)))
if not connected:
    print("Can't check for Hamiltonian cycle as graph is not connected.")
if not cycle:
    print("Can't check for Hamiltonian cycle as graph is not cyclic.")

# Reading peterson.txt
print("\n(Q4) Showing all stats again for Peterson Graph")
graph = {}
visitedForConnected = []
visitedForCycle = []
visitedForHamiltonian = []
with open("peterson.txt", "r") as f:
    for line in f:
        if line[0] == "#":
            continue
        if int(line[0]) not in graph.keys():
            graph[int(line[0])] = []
        if int(line[2]) not in graph.keys():
            graph[int(line[2])] = []
        graph[int(line[0])].append(int(line[2]))
        graph[int(line[2])].append(int(line[0]))

# Testing code
for node in graph:
    visitedForConnected.append(False)
    visitedForCycle.append(False)
    visitedForHamiltonian.append(False)

connected = isConnected(graph, visitedForConnected)
cycle = containsCycle(0, graph, visitedForCycle)

print("Is the graph connected?                     " + str(connected))
print("Does the graph contain a cycle?             " + str(cycle))
if connected and cycle:
    print("Does the graph contain a Hamiltonian cycle? " + str(containsHamiltonian(0, graph, visitedForHamiltonian)))

print("\nAs we can see, the program successfully proves that Petersen graph does not contain a Hamiltonian cycle.")

    
