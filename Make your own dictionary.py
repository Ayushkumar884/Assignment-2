print("The dictionary of alphabet wuth their Ascii  value \n")
d={}
for i in range (ord('a'),ord('z')+1):
    d[chr(i)]=i
print("Output=",d)