from cProfile import label
import graphviz as gpz

class Node:
    def __init__(self, name):
        self.name = name
        self.pre = -1
        self.post = -1
        self.marque = False

class Pile:
    def __init__(self):
        self.l = []

    def empiler(self, x):
        self.l.append(x)

    def depiler(self):
        a = self.l[-1]
        del self.l[-1]
        return a

    def vide(self):
        if(len(self.l) > 0):
            return False
        else: 
            return True

class Graphe:
    def __init__(self, V = [], E = []):
        self.V = V
        self.E = E
        self.TE = None
        self.oriente = False

    def print(self):
        if self.V == [] or self.TE == None :
            print("Error print L.38")
            return

        if self.oriente:
            g = gpz.Digraph("Algo/graph", filename="Algo/graph", format="png")
        else:
            g = gpz.Graph("Algo/graph", filename="Algo/graph", format="png")

        for v in self.V:
            g.node(v.name, v.name)
        i = 0
        for e in self.E:
            g.edge(str(e[0].name), str(e[1].name), label = self.TE[i])
            i = i + 1

        g.view()

def typeEdges(G):
    TE = []
    for e in G.E:
        if e[0].pre < e[1].pre < e[1].post < e[0].post:
            TE.append("A")
        elif e[1].pre <= e[0].pre < e[0].post <= e[1].post:
            TE.append("R")
        else:
            TE.append("T")
    G.TE = TE
    return

def explorer(G, u):
    P = Pile()
    P.empiler(u)
    temps = 0
    while not P.vide():
        temps = temps + 1
        u = P.depiler()
        if(not u.marque and u.pre == -1):
            u.pre = temps
            P.empiler(u)
            for e in G.E:
                if(e[0] == u and not e[1].marque):
                    P.empiler(e[1])
        elif(u.post == -1):
            u.post = temps

def DFS(G):
    for u in G.V:
        if not u.marque:
            explorer(G, u)
    typeEdges(G)
    return

def importGraph(link):
    file = open(link, "r")
    V = [] #Nodes
    E = [] #Edges
    C = [] #Edges temp

    #Create Nodes and keep edges for later in C
    for line in file:
        line = ''.join(line.splitlines())
        split = line.split(" ")
        V.append(Node(split[0]))
        if(len(split) > 1):
            C.append([V[-1], split[1:]])
        else:
            C.append([[V[-1]], []])

    #Create Edges
    for node in C:
        for e in node[1]:
            i = 0
            while e != V[i].name and i < len(V) - 1:
                i = i + 1
            if i < len(V):
                E.append([node[0], V[i]])
            else:
                V.append(Node(e))
                E.append([node[0], V[-1]])
    return Graphe(V, E)

G = importGraph("Algo/G1.txt")
G.oriente = True
DFS(G)
for v in G.V:
    print(v.pre, v.post)
G.print()
