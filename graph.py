V=[ "a","b","c","d","e","f"]
E=[["a","e"],["a","b"],["a","d"],["b","c"],["c","b"],["d","e"],["d","f"]]
test=[["v","r"],["s","r"],["s","w"],["w","t"],["w","x"],["u","t"],["x","t"],["x","u"],["x","y"],["y","u"]]
tree=[["a","b"],["a","c"],["c","i"],["c","j"],["j","h"],["i","d"],["j","g"],["i","e"],["f","i"],["g","m"],["n","g"],["g","o"],["n","o"]]


# dicte={x:adjacent(E,x) for x in V}

Q=[]
out={}
i=2
marque=[]

# liste d'adjacence à chaque sommet
def adjacent(Arrets,Sommet):
    listeAdj=[]
    for arret in Arrets:
        if arret[0]==Sommet:
            listeAdj.append(arret[1])
    return listeAdj


# parcour en largeur
def BFS(E,debut):
    Q=[debut]
    out={}
    mark=[]
    out[Q[0]]=0
    mark.append(Q[0])
    while Q:
        list_adj=adjacent(E,Q[0])
        tmp=Q[0]
        Q.remove(Q[0])
        for sommet in list_adj:
            if not sommet in mark:
                out[sommet]=out[tmp] + 1
                mark.append(sommet)
                Q.append(sommet)
    return out
# fonction reccursive
def rec(tree,s): 
    global i,marque
    for adj in adjacent(tree,s):
        if adj not in marque:
            marque.append(adj)
            out[adj]=[i]
            i=i +1
            if adjacent(tree,adj):
                rec(tree,adj)
            out[adj].append(i)
            i=i+1
    return out
# parcour en profodeur avec un seule source
def FDS(tree,s):
    global i,Q,out,marque
    Q.append(s)
    marque.append(s)
    out[s]=[1]
    rec(tree,s)
    out[s].append(i)
    return out


# parcour en profondeur en tous les sommets
def BFS_ALL(arrets,sommets):
    for sommet in sommets:
        print(BFS(arrets,sommet))


# Algorthme de Kruskal
def Kruskal(sommet,weight):
    out=[{i} for i in sommet]
    Marque=set()
    dic_new=dict(sorted(weight.items(),key=lambda item: item[1]))
    A=[]
    liste=list(dic_new.keys())
    for arret in liste: 
        if Marque == sommet:
            break
        else:       
            P1=set()
            P2=set()
            tmp=20
            tmp1=20
            for i  in out:
                if arret[0] in i:
                    P1=i
                    tmp=out.index(i)
                    break
            for j  in out:
                if  arret[1] in j:
                    P2=j
                    tmp1=out.index(j)
                    break
            if  P1 and P2 and P1 !=P2:  
                Marque.add(arret[0])
                Marque.add(arret[1])
                out[tmp]=P1.union(P2)
                A.append(arret)
                out.remove(out[tmp1])
                print(out)
                print("")
    return A

# exercice 1)a
exo1=[["1","2"],["2","1"],["1","5"],["5","1"],["5","2"],["2","5"],["5","4"],["4","5"],["2","4"],["4","2"],["3","4"],["4","3"],["2","3"],["3","2"]]
# print(BFS("exercice 1)a) : ",exo1,"1"))
# exercice 1)b
devoi=[["1","4"],["1","2"],["2","5"],["5","4"],["4","2"],["3","5"],["3","6"],["6","6"]]
# print(BFS("exercice 1)b) : ",devoi,"1"))


# resultat exo 2
sommet_exo2=["r","s","t","u","y","x","z","q","v","w"]
exo2=[["r","u"],["r","y"],["u","y"],["y","q"],["q","t"],["t","y"],["t","x"],["x","z"],["z","x"],["q","w"],["q","s"],["w","s"],["s","v"],["v","w"]]
# print("exercice 2 :")
# BFS_ALL(exo2,sommet_exo2)


#Algorithme de Bellman_Ford

E=[["a","b"],["b","c"],["a","d"],["a","c"],["e","a"],["e","d"],["d","c"],["c","f"],["f","d"],["d","e"]]
weight={("a","b"):9,("b","c"):8,("a","c"):10,("a","d"):3,("e","a"):2,("e","d"):4,("d","e"):5,("d","c"):6,("c","f"):7,("f","d"):5}
V={"a","b","c","d","e","f"}
def Relaxe(u,v,weight,sommet_weit,predecesseur):
    if weight[(u,v)] + sommet_weit[u] < sommet_weit[v]:
        sommet_weit[v] = weight[(u,v)] + sommet_weit[u]
        predecesseur[v]= u
def Bellman_Ford(weight,E,V,s):
    somme=sum(weight.values())
    sommet_weit = { sommet : somme +1  for sommet in V }
    predecesseur = {}
    sommet_weit[s]=0
    for _ in range(len(V)):
        for arret in E:
            Relaxe(arret[0],arret[1],weight,sommet_weit,predecesseur)
    return sommet_weit ,predecesseur
print(Bellman_Ford(weight,E,V,"a"))
    
#Exercice_5
V_exo={"u","z","v","y","x"}
E_exo=[["z","u"],["z","x"],["u","x"],["v","u"],["u","v"],["x","v"],["x","y"],["y","z"],["u","y"],["y","v"]]
weight_exo={("z","u"):6,("z","x"):7,("u","x"):8,("v","u"):-3,("u","v"):5,("x","v"):-3,("x","y"):9,("y","z"):2,("u","y"):-5,("y","v"):7}
# print(Bellman_Ford(weight_exo,E_exo,V_exo,"z"))

