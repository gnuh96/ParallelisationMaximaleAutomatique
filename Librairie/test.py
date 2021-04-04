class Task:
    name = ""
    reads = []
    writes = []
    run = None


def runT1():
    global X
    X = 1


def runT2():
    global Y
    Y = 2


def runTsomme():
    global X, Y, Z
    Z = X + Y


def runTsoustraction():
    global X, Y, S
    S = X - Y


def runTmultiplication():
    global X, Y, M
    M = X * Y


def bernstein(liste):
    rs = list()
    ls = liste.copy()
    task1 = ls.pop(0)
    for task2 in ls:
        if set(task1.reads) & set(task2.writes) == set() and set(task1.writes) & set(task2.reads) == set() and set(
                task1.writes) & set(task2.writes) == set():
            rs.append([task1.name, task2.name])
        for a in bernstein(ls):
            y = a in rs
            if not y:
                rs.append(a)
    return rs

"""Verifier que si 2 listes sont pas interprentes"""
def memeNiveau(ls1, ls2):
    for el1 in ls1:
        for el2 in ls2:
            if el1 == el2:
                return True
    return False

"""concatener 2 listes"""
def concatlist(ls1, ls2):
    for el2 in ls2:
        for el1 in ls1:
            if el2 != el1:
                ls1.append(el2)
    return ls1

"""supprimer item dans la liste"""
def removeItem(liste, item):
    None

t1 = Task()
t1.name = "T1"
t1.writes = ["X"]
t1.run = runT1

t2 = Task()
t2.name = "T2"
t2.writes = ["Y"]
t2.run = runT2

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

print("test 1")
l = list([t1, t2, tSomme, tSoustraction, tMultiplication])
v = bernstein(l)
print(v)

print(set(t1.reads) & set(t2.writes) == set())

print("test 2")
rs = list()
l = list([t1, t2, tSomme, tSoustraction])
task1 = l.pop(0)
for v in l:
    print(v.name)
    if set(task1.reads) & set(v.writes) == set() and set(task1.writes) & set(v.reads) == set() and set(
            task1.writes) & set(v.writes) == set():
        rs.append([task1.name, v.name])
    task2 = l.pop(0)
    print(task2.name)

print(rs)

print("test 3")
a = [[1, 2], [3], [1, 2], [4], [1, 2], [3, 5]]

