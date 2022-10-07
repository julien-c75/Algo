import graphviz as gpz


##############################  Class #######################################
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

    ####    Affichage   ####
    
    def graphImg(self):
        if self.V == [] or self.TE == None :
            print("Error print L.38")
            return

        if self.oriente:
            g = gpz.Digraph("graph", filename="graph", format="png")
        else:
            g = gpz.Graph("graph", filename="graph", format="png")

        for v in self.V:
            g.node(v.name, v.name)
        i = 0
        for e in self.E:
            g.edge(str(e[0].name), str(e[1].name), label = self.TE[i])
            i = i + 1

        g.view()
    
    def printResult(self):
        if self.TE == None:
            DFS(self)
        print("pre et post des toutes les Nodes :")
        for v in self.V:
            print("N", v.name, "\tpre", v.pre, "\tpost", v.post)
        print("\nType de chaque arrêtes :")
        i = 0
        if self.oriente:
            for e in self.E:
                print(e[0].name, "-->" , e[1].name, "Type :", self.TE[i])
                i = i + 1

#################################   Type    #######################################

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
    
############################### Importation ######################################

def importGraph(link, oriente):
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
    G = Graphe(V, E)
    G.oriente = oriente
    return G

###################################   DFS   ###########################################

def explorer(G, u, temps):
    P = Pile()
    P.empiler(u)
    while not P.vide():
        u = P.depiler()

        #Si post est initialisé alors le noeud apartient a un arbre déjà visité
        if u.post == -1:
            temps = temps + 1

        if(not u.marque and u.pre == -1):
            u.pre = temps
            P.empiler(u)
            for e in G.E:
                if G.oriente:
                    if(e[0] == u and not e[1].marque):
                        P.empiler(e[1])
                else:
                    if(e[0] == u and not e[1].marque):
                        P.empiler(e[1])
                    elif(e[1] == u and not e[1].marque):
                        P.empiler(e[0])
        elif(u.post == -1):
            u.post = temps
    return temps

def DFS(G):
    temps = 0
    for u in G.V:
        if not u.marque:
            temps = explorer(G, u, temps)
    typeEdges(G)
    return G

##############################################  Main    ##################################

G = importGraph("G1.txt", True)
DFS(G)
G.graphImg()
G.printResult()