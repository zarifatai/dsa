graph = {}
costs = {}
parents = {}

graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

infinity = float("inf")
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None

    for node, cost in costs.items():
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors:
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

def get_path(parents, final_node="fin", start_node="start"):
    if parents[final_node]:
        path = [final_node]
        node_name = parents[final_node]
        for x in range (len(parents) - 1):
            path.append(node_name)
            node_name = parents[node_name]
        path.append(start_node)
    path.reverse() 
    return path

print(get_path(parents))