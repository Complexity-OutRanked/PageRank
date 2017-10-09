from collections import deque
import numpy as np
import networkx as nx


def Brandes(G):
    A = G.nodes()
    C = dict((node,0) for node in A)
    for node in A:
        S = []
        P = dict((w,[]) for w in A)
        O = dict((t,0) for t in A)
        O[node] = 1
        D = dict((t,-1) for t in A)
        D[node] = 0
        Q = deque([])
        Q.append(node)
        while Q:
            a = Q.popleft()
            S.append(a)
            for i in G.neighbors(a):
                if D[i] < 0:
                    Q.append(i)
                    D[i] = D[a] + 1
                if D[i] == D[a] + 1:
                    O[i] = O[i] + O[a]
                    P[i].append(a)
    I = dict((v,0) for v in A)
    while S:
        w = S.pop()
        for v in P[w]:
            I[v] = I[v] + ((O[v] / O[w]) * (1+I[w]))
            if w != node:
                C[w] = C[w] + I[w]
    return C


G = nx.Graph()
G.add_edge(1, 0)
G.add_edge(2, 0)
G.add_edge(3,0)

Brandes(G)
