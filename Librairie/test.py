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
    rs1 = list()
    ls1 = liste.copy()
    task1 = ls1.pop(0)
    for task2 in ls1:
        if set(task1.reads) & set(task2.writes) == set() and set(task1.writes) & set(task2.reads) == set() and set(
                task1.writes) & set(task2.writes) == set():
            rs1.append([task1, task2])
        for a in bernstein(ls1):
            y = a in rs1
            if not y:
                rs1.append(a)
    """rs2 = rs1.copy()
    for i1 in range(len(rs1)-1):
        for i2 in range(1, len(rs1)):
            if memeNiveau(rs1[i1], rs1[i2]):
                new = concatlist(rs1[i1], rs1[i2])
                rs2.remove(rs1[i1])
                rs2.remove(rs1[i2])
                rs2.insert(i1, new)"""
    return rs1


"""Verifier que si 2 listes sont pas interprentes"""


def memeNiveau(ls1, ls2):
    for el1 in ls1:
        for el2 in ls2:
            if el1 == el2:
                return True
    return False


"""concatener 2 listes"""


def concatlist(ls1, ls2):
    rs = ls1.copy()
    for i1 in range(len(ls1) - 1):
        for i2 in range(1, len(ls2)):
            if ls1[i1] != ls2[i2]:
                rs.append(ls2[i2])
    return rs


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
l1 = list([t1, t2, tSomme, tSoustraction, tMultiplication])
v = bernstein(l1)
a = v.pop()
print(a)
print(a.pop().name)

print(set(t1.reads) & set(t2.writes) == set())

print("test 2")
rs = list()
l2 = list([t1, t2, tSomme, tSoustraction])
task1 = l2.pop(0)
for v in l2:
    print(v.name)
    if set(task1.reads) & set(v.writes) == set() and set(task1.writes) & set(v.reads) == set() and set(
            task1.writes) & set(v.writes) == set():
        rs.append([task1.name, v.name])
    task2 = l2.pop(0)
    print(task2.name)

print(rs)

print("test 3")
b = [t1.name, t2.name]
c = [t2.name, tSomme.name]
print(memeNiveau(b,c))
e = concatlist(b,c)
print(e)

print("test 4")
g = [tSomme.name, t1.name]
d = [b, c, g]
f = d.copy()
for i1 in range(len(d) - 1):
    for i2 in range(i1+1, len(d)-1):
        if memeNiveau(d[i1], d[i2]):
            new = concatlist(d[i1], d[i2])
            f.remove(d[i1])
            f.remove(d[i2])
            f.insert(i1, new)
print(range(len(d) - 1))
print(range(1, len(d)-1))
print(f)