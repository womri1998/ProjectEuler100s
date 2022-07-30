import re


def get_edges(graph):
    edges = []
    length = int(len(graph) ** 0.5)
    for i in range(len(graph)):
        if graph[i] != "-":
            edges.append([graph[i], i // length, i % length])
    for x in edges:
        if [x[0], x[2], x[1]] in edges:
            edges.remove([x[0], x[2], x[1]])
    return edges


def network(graph):
    saved = 0
    edges = get_edges(graph)
    edges.sort(key = lambda x: x[0])
    length = int(len(graph) ** 0.5)
    components = {i: [i] for i in range(length)}
    for e in edges:
        if components[e[1]] == components[e[2]]:
            saved += e[0]
        else:
            components[e[1]] += components[e[2]]
            for x in components[e[1]]:
                components[x] = components[e[1]]
    return saved


if __name__ == "__main__":
    txt = open("p107_network.txt", "r").read()
    graph = re.split(',|\n', txt)
    while '' in graph:
        graph.remove('')
    for i in range(len(graph)):
        if graph[i] != "-":
            graph[i] = int(graph[i])
    print(graph)
    print(network(graph))
