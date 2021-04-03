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

def bernstein(self, liste):
    rs = list()
    ls = liste.copy()
    task1 = ls.pop()
    for task2 in ls:
        if set(task1.reads) & set(task2.writes) is None and set(task1.writes) & set(task2.reads) is None and set(
                task1.writes) & set(task2.writes) is None:
            rs.append([task1, task2])
        rs = rs + self.bernstein(ls)
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