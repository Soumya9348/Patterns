n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
  for j in range(1,n+2-i):
    print(chr(65+n-j),end=" ")
  print()
  
 #output
#J I H G F E D C B A
#J I H G F E D C B
#J I H G F E D C
#J I H G F E D
#J I H G F E
#J I H G F
#J I H G
#J I H
#J I
#J
