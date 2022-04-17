from collections import deque

graph = {}
graph["you"] = ["bob", "alice", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["claire"] = ["thom", "jonny"]
graph["alice"] = ["peggy"]
graph["thom"] = []
graph["jonny"] = []
graph["anuj"] = []
graph["peggy"] = []


def bfs(graph, name):
    searched = []

    queue = deque()
    queue += graph[name]

    while queue:
        item = queue.popleft()

        if meets_reqs(item):
            print("Node found:", item)
            return True
        else:
            searched.append(item)
            queue += graph[item]
    print("Not found")
    return False


def meets_reqs(item):
    if item[-1] == "m":
        return True
    return False


print(bfs(graph, "you"))
