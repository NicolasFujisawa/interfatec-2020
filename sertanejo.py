def graph_input():
    duplas = int(input())
    grafo = {}
    for i in range(0, duplas):
        [primeiro, segundo] = [value.rstrip()
                               for value in input().split(" e ")]
        if primeiro in grafo:
            grafo[primeiro].append(segundo)
        else:
            grafo[primeiro] = [segundo]

        if segundo in grafo:
            grafo[segundo].append(primeiro)
        else:
            grafo[segundo] = [primeiro]

    return grafo


def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not start in graph:
        return None
    shortest = None

    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest


def format_output(name, path):
    distance = 'infinito' if path == None else len(path) - 1
    return '{name}: {distance}'.format(name=name, distance=distance)


def sort_output(output_string):
    name, distance = output_string.split(': ')
    return(distance, name)


def solution():
    graph = graph_input()
    output_list = []
    for k, v in graph.items():
        if k != 'Saracura':
            output_list.append(format_output(
                k, find_shortest_path(graph, k, 'Saracura')))

    print('\n'.join(sorted(output_list, key=lambda string: sort_output(string))))


solution()
