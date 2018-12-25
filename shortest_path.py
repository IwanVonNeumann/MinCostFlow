from math import inf


def choose_next_node(L, unvisited):
    L_unvisited = {v: d for v, d in L.items() if v in unvisited}
    return min(L_unvisited, key=L_unvisited.get)


def not_empty(S):
    return len(S) > 0


def build_shortest_path_tree(D, v_0=0):
    n, _ = D.shape
    V = range(n)

    L = {v: 0 if v == v_0 else inf for v in V}
    T = {}
    unvisited = set(V)

    while not_empty(unvisited):

        i = choose_next_node(L, unvisited)

        for j in V:
            if L[j] > L[i] + D[i, j]:
                L[j] = L[i] + D[i, j]
                T[j] = i

        unvisited.remove(i)

    return T


def as_edges(path):
    return list(zip(path[:-1], path[1:]))


def find_shortest_path(D, source, target):
    T = build_shortest_path_tree(D, v_0=source)

    path = [target]
    current = target

    while T.get(current) is not None:
        current = T[current]
        path = [current] + path

    if path[0] != source:
        return None

    return as_edges(path)
