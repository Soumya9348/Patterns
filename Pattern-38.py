n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(2*i-1,0,-1):
        print(j,end=" ")
    print()
 
#output
#     1 
#   3 2 1 
#  5 4 3 2 1 
# 7 6 5 4 3 2 1 
#9 8 7 6 5 4 3 2 1 
