import random, copy
data = open("mincut.txt","r")
G = {}
for line in data:
    lst = [int(s) for s in line.split()]
    G[lst[0]] = lst[1:]

def choose_random_key(g):

    # get first vertex
    u = random.choice(list(g.keys()))
    # get second vertex
    v = random.choice(list(g[u]))
    return u, v

def karger(G):
    """
    get a min cut of 1 / n choose 2 probability

    """
    # while still two vertexes, keep on contracting
    cuts = 0
    while len(G) > 2:
        # get two random vertexes
        v1, v2 = choose_random_key(G)
        # connect v1 to all of v2's endpoints
        G[v1].extend(G[v2])
        # connect endpoints
        for x in G[v2]:
            G[x].remove(v2)
            G[x].append(v1)
        # delete loops
        while v1 in G[v1]:
            G[v1].remove(v1)
        # delete intermediate
        del G[v2]

    # get number of cuts
    for key in G.keys():
        cuts = len(G[key])
    return cuts

def operation(n):
    """
    1/n choose 2 chances to get best min cut , so get the min by repeated trials
    """
    i = 0
    count = 10000
    while i < n:
        data = copy.deepcopy(G)
        min_cut = karger(data)
        if min_cut < count:
            count = min_cut
        i = i + 1
    return count

print operation(100)