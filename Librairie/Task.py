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
  
def main ():
  t1 = Task()
  t1.name = "T1"
  t1.writes = ["X"]
  t1.run = runT1
  t2 = Task()
  t2.name = "T2"
  t2.writes = ["X"]
  t2.run = runT2
  tSomme = Task()
  tSomme.name = "somme"
  tSomme.reads = ["X", "Y"]
  tSomme.writes = ["Z"]
  tSomme.run = runTsomme
  t1.run()
  t2.run()
  tSomme.run()
  affiche()

  
def affiche():
  print(X)
  print(Y)
  print(Z)

main()