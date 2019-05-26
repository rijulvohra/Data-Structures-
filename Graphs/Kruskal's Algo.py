class Edge:
    def __init__(self,src,dest,wt):
        self.src = src
        self.dest = dest
        self.wt = wt

def getParent(v, parent):
    if (v == parent[v]):
        return v
    return getParent(parent[v],parent)

def kruskal(in_array,nVertices):
    parent = [i for i in range(nVertices)]
    edges = sorted(in_array,key=lambda edge: edge.wt)
    output = []
    count = 0
    i = 0
    while(count < nVertices-1):
        currentEdge = edges[i]
        srcParent = getParent(currentEdge.src,parent)
        desParent = getParent(currentEdge.dest,parent)
        if srcParent != desParent:
            output.append(currentEdge)
            count+=1
            parent[srcParent] = desParent
        i+=1
    return output
        
l = [int(i) for i in input().strip().split()]
v,e = l[0],l[1]

in_array = []
for i in range(e):
    r = [int(j) for j in input().strip().split()]
    v1,v2,w = r[0],r[1],r[2]
    in_array.append(Edge(v1,v2,w))
output = kruskal(in_array,v)
for i in range(len(output)):
    ce = output[i]
    if (ce.src < ce.dest):
        print(str(ce.src)+" "+str(ce.dest)+" "+str(ce.wt))
    else:
        print(str(ce.dest)+" "+str(ce.src)+" "+str(ce.wt))
        
    
    
