l=[]
n=int(input("how many tuple set you have entered"))
print("Entered the tuple set without using brackets and space in between")
for i in range(0,n):
    t=tuple(input())
    l.append(t)
print("Unsorted list=",l)
for j in range(0,n):
    for k in range(0,n-1-j):
        if (l[k][-1]>l[k+1][-1]):
            u=l[k]
            l[k]=l[k+1]
            l[k+1]=u
            
print("The sorted list=",l)