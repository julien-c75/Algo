from numpy import append

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
    V = []
    E = []

def explorer(G, u):
    P = Pile()
    P.empiler(u)
    temps = 0
    while not P.vide():
        temps = temps + 1
        u = P.depiler()
        #print(u.marque)
        if(not u.marque and u.pre == -1):
            print(u.name)
            u.pre = temps
            P.empiler(u)
            for e in G.E:
                if(e[0] == u and not e[1].marque):
                    P.empiler(e[1])
        elif(u.marque):
            u.post = temps

def DFS(G):
    for u in G.V:
        if not u.marque:
            explorer(G, u)
    return

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
g = Node(7)
h = Node(8)

G = Graphe()
G.V = [a,b,c,d,e,f,g,h]
G.E = [[a,b],[b,a],[a,c],[c,a]]


DFS(G)

""""
P2 = Pile()
print(P2.l)
P2.empiler(1)
P2.empiler(2)
P2.empiler(3)
print(P2.depiler())
print(P2.depiler())
print(P2.depiler())
print(P2.l)"""