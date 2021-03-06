class Task:
    name = ""
    reads = []
    writes = []
    run = None


def runT1():
    global X
    X = int(input('Entrez x: '))
    # print("marche")


def runT2():
    global Y
    Y = int(input('Entrez y: '))


def runT3():
    global Z
    Z = int(input('Entrez z: '))


def runTsomme():
    global X, Y, A
    A = X + Y


def runTsoustraction():
    global X, Y, S
    S = X - Y


def runTmultiplication():
    global X, Y, M
    M = X * Y


def getDictPrecedence(listTask, dictPre):  # Recuperer key
    if str(input('Entrez une nouvelle tache ? ((o pour valider) : ')) == 'o':
        key = str(input('Entrez tache: '))
        if verifTask(listTask, key, dictPre):  # verifier entree
            val = entreeVal(listTask, [])  # recuperer sous tache
            # print(val)
            dictPre.setdefault(key, val)  # ajouter key+sous tache
            print(dictPre)
            getDictPrecedence(listTask, dictPre)  # recommencer
        else:
            getDictPrecedence(listTask, dictPre)  # recommencer
    # print(d)
    return dictPre  # retourner le dictionnaire


def verifTask(listTask, key, dictPre):  # verifier les conditions
    if recherche(listTask, key) is None:
        print("Tache inconnue")
    elif key in dictPre:
        print("Tache deja existante")
    else:
        print('bon')
        return True
    return False


def entreeVal(listTask, liste):  # entree les sous taches
    if str(input('Entrez tache precedente ? (o pour valider) : ')) == 'o':
        entree = str(input('Entrez tache: '))
        if verifTask(listTask, entree, liste):  # verifier
            liste.append(entree)
            # print(liste)
            entreeVal(listTask, liste)  # recommencer
        else:
            entreeVal(listTask, liste)
    print('fin')
    return liste


def recherche(liste, nomTache):
    for t in liste:
        if t.name == nomTache:
            return t
    return None


def affiche():
    print(A)
    print(S)
    print(M)


"""
    Retourne la liste des paires de taches non interferentes
    en fonction recursive
"""


def bernstein(liste):
    rs = list()
    ls = liste.copy()
    task1 = ls.pop(0)
    for task2 in ls:
        if set(task1.reads) & set(task2.writes) == set() and set(task1.writes) & set(task2.reads) == set() and \
                set(task1.writes) & set(task2.writes) == set():
            rs.append([task1, task2])
        for a in bernstein(ls):
            y = a in rs
            if not y:
                rs.append(a)
    return rs


class TaskSystem:
    """
    Une classe representant un syst??me de t??ches
    - 'liste' : une liste de Task
    - 'dict' : un dictionaire de (nom de t??che, noms des t??ches pr??c??dences)
    """

    def __init__(self, liste, dictionaire):
        self.liste = liste.copy()
        self.dict = dictionaire

    """
    Retourner la liste de noms des t??ches qui doivent s'ex??cuter avant la t??che 'nomTache'
    en fonction recursive
    """

    def getDependancies(self, nomTache):
        rs = set()  # la liste sans la repetition des elements
        tab = self.dict.get(nomTache)
        for e in tab:
            rs.add(e)
            rs = rs | self.getDependancies(e)  # union 2 liste "set"
        return rs

    def run(self):
        list2 = list()
        for task in self.liste:
            list1 = self.getDependancies(task.name)
            """
            Ajout les elements dans la list1 ?? list2 s'il n'existe pas dans la list2
            """
            for nom in list1:
                ajout = True
                for task in list2:
                    if nom == task.name:
                        ajout = False
                        break
                if ajout:
                    list2.append(recherche(self.liste, nom))
        for task in self.liste:
            ajout = True
            for ele in list2:
                if task.name == ele.name:
                    ajout = False
                    break
            if ajout:
                list2.append(task)
        """inter = bernstein(list2)
        v = inter.pop(0)
        for a in v:
            print(a.name)"""
        while list2:
            t = list2.pop(0)
            t.run()


if __name__ == '__main__':
    X = None
    Y = None
    Z = None
    """addition"""
    A = None
    """soustraction"""
    S = None
    """multiplication"""
    M = None
    t1 = Task()
    t1.name = "T1"
    t1.writes = ["X"]
    t1.run = runT1

    t2 = Task()
    t2.name = "T2"
    t2.writes = ["Y"]
    t2.run = runT2
    """
    t3 = Task()
    t3.name = "T3"
    t3.writes = ["Z"]
    t3.run = runT3
    """
    tSomme = Task()
    tSomme.name = "somme"
    tSomme.reads = ["X", "Y"]
    tSomme.writes = ["A"]
    tSomme.run = runTsomme

    tSoustraction = Task()
    tSoustraction.name = "soustraction"
    tSoustraction.reads = ["X", "Y"]
    tSoustraction.writes = ["S"]
    tSoustraction.run = runTsoustraction

    tMultiplication = Task()
    tMultiplication.name = "multiplication"
    tMultiplication.reads = ["X", "Y"]
    tMultiplication.writes = ["M"]
    tMultiplication.run = runTmultiplication
    """
    t1.run()
    t2.run()
    tSomme.run()
    tSoustraction.run()
    tMultiplication.run()
    print(A)
    print(S)
    print(M)
    """
    d = dict()
    dictionnaire = getDictPrecedence([t1, t2, tSomme, tSoustraction, tMultiplication], d)
    # print(dictionnaire)
    s1 = TaskSystem([t1, t2, tSomme], dictionnaire)
    s1.run()
    print(A)
