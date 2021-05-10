#примерный вариант для собеса
    graph = dict(
        A=dict(B=5, C=2),
        B=dict(D=4, E=2),
        C=dict(B=8, E=7),
        D=dict(E=6, F=3),
        E=dict(F=1),
        F=dict()
    )
    start, end = 'A', 'F'
    costs = {v:float('inf') for v in graph if v != start}
    costs.update(graph[start])
    parents = {child:start for child in graph[start]}
    searched = set()
    def find_lowest_cost(costs):
        return min([(cost, v) for v, cost in costs.items() if v not in searched], default=('', None))[1]
    node = find_lowest_cost(costs)
    while node:
        neighbors = graph[node] #можно убрать
        for n, n_cost in neighbors.items():
            new_cost = costs[node] + n_cost
            if new_cost < costs[n]:
                costs[n] = new_cost
                parents[n] = node
        searched.add(node)
        node = find_lowest_cost(costs)
    res = [end, parents[end]]
    while res[-1] != start:
        res += parents[res[-1]]
    res.reverse()
    print(res)
#довольно переусложено на мой взгляд
#хреновое решение сильно усложняющее СД взамен микроскопического упрощения алгоритма
#содержит небольшие ошибки, в основном - имя neighbors переназначется
    #использование констант для улучшения читаемости
    inf, cost,searched,parent,neighbors = float('inf'), 'cost', 'searched', 'parent','neighbors'
    graph = dict(A=dict(neighbors=dict(B={cost: 5}, C={cost: 2}), searched=True),
                 B=dict(neighbors=dict(D={cost: 4}, E={cost: 2}), cost=5, searched=False, parent='A'),
                 C=dict(neighbors=dict(E={cost:7}), cost=2, searched=False, parent='A'),
                 D=dict(neighbors=dict(E={cost:6}, F={cost:3}), cost=inf, searched=False),
                 E=dict(neighbors=dict(F={cost:1}), cost=inf, searched=False),
                 F=dict(neighbors={}, cost=inf, searched=False)
    )
    start, end = 'A', 'F'
    #генерация графа с полями parent, cost, searched из простого
    data = {'A': {'B': 5, 'C': 2}, 'B': {'D': 4, 'E': 2}, 'C': {'E': 7}, 'D': {'E': 6, 'F': 3}, 'E': {'F': 1}, 'F': {}}
    graph = dict.fromkeys(data.keys())
    inf, cost,searched,parent = float('inf'), 'cost', 'searched', 'parent'
    for node, neighbors in data.items():
        #temp = {n: cost   for n, cost in neighbors.items()}
        graph[node] = dict(neighbors=graph[node], cost=inf, searched=False)
    graph[start][searched] = True
    #ДОБАВЛЯЕМ COST PARENT
    for node, v in data[start].items():
        graph[node][cost] = v
        graph[node][parent] = start
    #отрисовка графа для проверки
    import matplotlib.pyplot as plt
    import networkx as nx
    def plotGraph(graph):
        G = nx.DiGraph()
        G.add_nodes_from(graph)
        for node in graph:      #можно использовать items()?
            for neighbor in graph[node][neighbors]:
                G.add_edges_from([(node, neighbor)], weight=graph[node][neighbors][neighbor][cost])
        edge_labels = {(k, v): graph[k][neighbors][v][cost] for k in graph for v in graph[k][neighbors]}
        pos = nx.planar_layout(G)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        nx.draw(G, pos, with_labels=True)
        plt.show()
    plotGraph(graph)
    def find_lowest_cost_node(graph):
        return min([(v[cost],node) for node,v in graph.items() if not v[searched]], default=('', None))[1]
    node = find_lowest_cost_node(graph)
    while node:
        for n, n_cost in graph[node][neighbors].items():
            new_cost = graph[node][cost] + n_cost
            if new_cost < graph[n][cost]:
                graph[n][cost] = new_cost
                graph[n][parent] = node
        graph[node][searched] = True
        node = find_lowest_cost_node(graph)
    res = [end, graph[end][parent]]
    while res[-1] != start:
        res.append(graph[res[-1]][parent])
    res.reverse()
    print(res)
