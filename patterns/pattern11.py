"""
        5
      5 4
    5 4 3
  5 4 3 2
5 4 3 2 1          

"""
n = int(input("enter a number"))
for i in range(1,n+1):
    for s in range(1,(n+1)-i):
        print(" " , end=" ")
    for j in range(n,n-i,-1):
        print(j,end=" ")   
    print()     