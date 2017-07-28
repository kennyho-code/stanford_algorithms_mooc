import sys


def get_graph():
    g = {}
    with open("dijkstra_data.txt") as f:
        for l in f:
            nodes = l.strip().split()
            u = nodes[0]
            vs = nodes[1:]
            g[u] = {}
            for v in vs:
                v, d = v.split(',')
                g[u][v] = int(d)
    return g


def dijkstra(g, s):
    q = {}
    dist = {}
    prev = {}
    new_dist = {}

    for v in g:
        dist[v] = sys.maxint
        prev[v] = None
        q[v] = sys.maxint
    dist[s] = 0

    while q:
        u = min(q, key=q.get)
        del q[u]
        for v in g[u]:
            alt = dist[u] + g[u][v]
            if alt < dist[v]:
                q[v] = alt
                dist[v] = alt
                prev[v] = u

    return dist


def run():
    g = get_graph()
    d = dijkstra(g, '1')
    ns = ['7','37','59','82','99','115','133','165','188','197']
    res = [str(d[n]) for n in ns]
    print ','.join(res)


if __name__ == '__main__':
    run()

