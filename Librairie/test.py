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
            x = [task1.name, task2.name] in rs
            if not x:
                rs.append([task1.name, task2.name])
        rs = rs + bernstein(ls)
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

l = list([t1, t2, tSomme, tSoustraction])
v = bernstein(l)
print(v)

print(set(t1.reads) & set(t2.writes) == set())

rs = list()
l = list([t1, t2, tSomme, tSoustraction])
task1 = l.pop(0)
for v in l:
    print(v.name)
if set(t1.reads) & set(t2.writes) == set() and set(t1.writes) & set(t2.reads) == set() and set(
        t1.writes) & set(t2.writes) == set():
    rs.append([t1.name, t2.name])
print(rs)
a = ["T1", "T2"] in rs
print(a)