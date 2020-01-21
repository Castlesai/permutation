a = int(input("Enter no:")) #no of elements
ar = []
#compare the string and substring
for i in range(a):
    b = input("Enter string:")  #first string
    c = input("Enter string:")  #second string
    d=b[::-1]
    #logic for finding substring and reveres string 
    if (b in c) or (d in c):
        ar.append("YES") 
    else:
        ar.append("NO")
for i in ar:
    print(i)