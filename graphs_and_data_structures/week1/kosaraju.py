import sys
import resource
sys.setrecursionlimit(10 ** 6)
resource.setrlimit(resource.RLIMIT_STACK, (2 ** 29, 2**30))

class Graph_Data(object):
    def __init__(self):
        self.current_time = 0
        self.finish_time = {}
        self.seen = set()
        self.current_source = None
        self.leader_nodes = {}


def dfs_loop(g, nodes, graph_data):
    for u in nodes:
        if u not in graph_data.seen:
            graph_data.current_source = u
            dfs(g, u, graph_data)

def dfs(g, u, graph_data):
    graph_data.seen.add(u)
    graph_data.leader_nodes[u] = graph_data.current_source
    for v in g[u]:
        if v not in graph_data.seen:
            dfs(g, v, graph_data)
    graph_data.current_time += 1
    graph_data.finish_time[u] = graph_data.current_time


def create_graph():
    g = {}
    with open("graph.txt") as f:
        for l in f:
            u, v = l.strip().split()
            if u not in g:
                g[u] = set([v])
            else:
                g[u].add(v)

            if v not in g:
                g[v] = set([])
    return g

def reverse_graph(g):
    grev = {}
    for u in g:
        if u not in grev:
            grev[u] = set()
        for v in g[u]:
            if v not in grev:
                grev[v] = set([u])
            else:
                grev[v].add(u)
    return grev

def test_graph():
    g = {'1': set(['2']), '2': set(['3']), '3': set(), '4': set(['5']), '5': set([])}
    return g

from collections import Counter

def kosaraju():
    g = create_graph()

    graph_data = Graph_Data()
    grev = reverse_graph(g.copy())
    nodes = list(grev)
    dfs_loop(grev, nodes, graph_data)
    sorted_nodes = sorted(graph_data.finish_time, key=graph_data.finish_time.get, reverse=True)

    graph_data = Graph_Data()
    dfs_loop(g, sorted_nodes, graph_data)
    leader_count = Counter(graph_data.leader_nodes.values()).items()
    print sorted(leader_count, key=lambda x: x[1], reverse=True)[:5]
kosaraju()



