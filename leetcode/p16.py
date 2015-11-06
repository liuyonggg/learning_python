'''
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:
'''

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
    def __str__(self):
        return self.__repr__()
    def __repr__(self):
        r = 'label: %s\n' % self.label
        r += 'neighbors:'
        for x in self.neighbors:
            r += ' %s'  % x.label
        r += '\n'
        return r

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        #1. clone all nodes
        visited = set()
        que = []
        m = {}
        x = node
        while x:
            y = None if len(que) == 0 else que.pop()
            if x in visited:
                x = y
                continue
            visited.add(x)
            m[x] = UndirectedGraphNode(x.label)
            que += x.neighbors
            x = y if y else None if len(que)==0 else que.pop()
        assert (len(que) == 0)
        r = m[node]
        x = node
        visited.clear()
        while x:
            y = None if len(que) == 0 else que.pop()
            if x in visited:
                x = y
                continue
            visited.add(x)
            que += x.neighbors
            for y in x.neighbors:
                m[x].neighbors.append(m[y])
            x = y if y else None if len(que)==0 else que.pop()
        assert (len(que) == 0)
        #2. clone the edges
        return r 
    def cloneBFSGraph2(self, node):
        assert (node)
        queue = [node]
        newHead = UndirectedGraphNode(node.label)
        visited = {node:newHead}
        while queue:
            x = queue.pop()
            for n in x.neighbors:
                if n in visited:
                    visited[x].neighbors.append(visited[n])
                else:
                    yn = UndirectedGraphNode(n.label)
                    visited[n] = yn
                    visited[x].neighbors.append(yn)
                    queue.append(n)
        return newHead
        
    def cloneDFSGraph(self, node, visited):
        assert (node)
        if node in visited:
            return visited[node]
        y = UndirectedGraphNode(node.label)
        visited[node] = y
        for n in node.neighbors:
            yn = self.cloneDFSGraph(n, visited)
            visited[node].neighbors.append(yn)
        return y

def generateGraph():
    g1 = UndirectedGraphNode(1)   
    g0 = UndirectedGraphNode(0)   
    g2 = UndirectedGraphNode(2)   
    g1.neighbors.append(g0)
    g1.neighbors.append(g2)
    g0.neighbors.append(g1)
    g0.neighbors.append(g2)
    g2.neighbors.append(g2)
    return g1

def printGraph(g):
    que = [g]
    visited = set()
    x = g
    while len(que):
        x = que.pop()
        if x in visited:
            continue
        visited.add(x)
        que += x.neighbors
        print x
    assert (len(que) == 0)

if __name__ == '__main__':
    g = generateGraph()
    printGraph(g)
    g2 = Solution().cloneGraph(g)
    printGraph(g2)
    g3 = Solution().cloneBFSGraph2(g)
    printGraph(g3)

    visited = {}
    g4 = Solution().cloneDFSGraph(g, visited)
    printGraph(g4)
        
