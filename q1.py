#Rubén Barajas Curiel
#A01630323
def triangles(size):
    for a in range (1,size+1,1):
      for b in range (1,a+1):
          print('T',end='')
      print()
    for a in range (size-1,0,-1):
        for b in range (1,a+1):
            print('T',end='')
        print()
#
number=int(input("Triangles: "))
triangles(number)