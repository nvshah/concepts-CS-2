def validTree1(n, edges, root):
    '''
    (ie alike directed Acyclic Graph)
    when root is known & want to start search from Top -> Bottom 
    :param n: number of vertexes
    :param edges: list of directed (edges)
    :param root: vertex number of root
    '''
    if not n:
        return True 
    
    #1. Define Adjacency Matrix

    adj = {v:[] for v in range(n)}

    # We are treating as Directed Acyclic Graph = Tree
    for v1, v2 in edges:
        adj[v1].append(v2)

    print(adj)

    # TREE = Directed Acyclic Graph

    #2. define dfs
    visited = set()
    def dfs(v):
        if v in visited:
            print(v)
            return True  # Cycle detected

        visited.add(v)

        for neig in adj[v]:
            if dfs(neig):
                return True

    isCycle = dfs(root)
    print(isCycle)
    print(visited)
    allNodesVisted = len(visited) == n
    print(allNodesVisted)
    isTree =(not isCycle) and allNodesVisted

    return isTree

def validTree2(n, edges):
    '''
    (ie alike Undirected acyclic Graph)
    when root is unknown & need to start search from any random vertex 
    :param n: number of vertexes
    :param edges: list of undirected (edges)
    :param root: vertex number of root
    '''
    if not n:
        return True 
    
    #1. Define Adjacency Matrix

    adj = {v:[] for v in range(n)}

    # We are treating as UnDirected Acyclic Graph = Tree So need to add both the way edges
    for v1, v2 in edges:
        adj[v1].append(v2)
        adj[v2].append(v1)

    # TREE = Directed Acyclic Graph

    #2. define dfs
    visited = set()
    def dfs(v, prev):
        '''
        :param v: vertex
        :param prev: prev vertex (ie connected to this vertex v)
        '''
        if v in visited:
            return False  # Cycle/Loop detected

        visited.add(v)

        for neig in adj[v]:
            if prev == neig: # Edge has already been explored earlier (False Positive)
                continue
            if not dfs(neig, v):
                return False
        
        return True

    noLoop = dfs(0, -1)
    allNodesVisted = len(visited) == n
    isTree = noLoop and allNodesVisted

    return isTree