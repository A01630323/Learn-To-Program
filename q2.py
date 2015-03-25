#Rubén Barajas Curiel
#A01630323
def complete():
	elements=int(input("Number of elements: "))
	list=[0]*elements
	n=0
	while(n<elements):
		list[n]=int(input("Number to store in the list: "))
		n=n+1
	return list
#
def find_threes(a):
    add=0
    for x in a:
        if (x%3==0):
          add=add+x
    return add
#
numbers=complete()
print ("The result is: ",find_threes(numbers))