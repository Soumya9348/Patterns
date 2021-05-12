n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(i-1),(str(chr(65+n-i))+" ")*(n+1-i))
    
#output
# E E E E E 
#  D D D D 
#   C C C 
#    B B 
#     A 
