list=[1,3,4,4,5,5,5,6,7,7,8,9,9]
print(list)
newlist=[]
for i in list:
    if i not in newlist:
        newlist.append(i)
print(newlist)
newnewlist=[]
for i in newlist:
    if i%2==0:
        newnewlist.append(i)
print(newnewlist)
newnewlist.reverse()
print(newnewlist)
f=open("text.txt")
data=f.read()
print(data.split(" "))
newnewnewlist={}
for i in data.split(" "):
    if i not in newnewnewlist:
        newnewnewlist.update({i:1})
    else:
        newnewnewlist[i]+=1
print(newnewnewlist)