def graph_coloring(graph):
    n = len(graph)
    result = [-1] * n
    result[0] = 0

    for u in range(1, n):
        used_colors = set()
        for i in range(n):
            if graph[u][i] == 1 and result[i] != -1:
                used_colors.add(result[i])
            print(used_colors)

        color = 0
        while color in used_colors:
            color += 1
        result[u] = color

    return result