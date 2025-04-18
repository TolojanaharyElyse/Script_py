

def Dyck(n):
    """Fonction  de calcul des mots de Dyck de longueur n:pair"""
    if n % 2 != 0:
        raise ValueError("n doit être pair")
    if n == 2:
        return ["md"] # m:monter ,d:descendre

    result = []
    S = Dyck(n - 2)
    for s in S:
        for i in range(1,len(s) + 1):
            tmp = s[:i] + "md" + s[i:]  # inserer md dans le i-ème position de s
            if not tmp in result:  #Pour eviter le répétion des chémin dans le resultat
                result.append(tmp)

    return result

print(Dyck(8)) #output: ['mmdmdmdd', 'mmmddmdd', 'mmdmmddd', 'mmdmddmd', 'mmmdmddd', 'mmmmdddd', 'mmmdddmd', 'mmddmdmd', 'mmddmmdd', 'mdmdmdmd', 'mdmmddmd', 'mdmdmmdd', 'mdmmdmdd', 'mdmmmddd']