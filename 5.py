f=open("text.txt")
data=f.read()

list=data.split(" ")

unique={}
list1=[]
for i in list:
    if i not in unique:
        unique.update({i:1})
    else:
        unique[i]+=1
i=0
for w in sorted(unique, key=unique.get, reverse=True):
    if i<10:
        print(w," : ", unique[w])
        list1.append(len(w))
        i+=1
print(list1)

print(sum(list1)/len(list1))