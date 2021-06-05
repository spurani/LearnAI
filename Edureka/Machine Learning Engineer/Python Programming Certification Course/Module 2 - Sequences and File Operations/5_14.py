#5

s=input("Enter String like H1e2l3l4o5w6o7r8l9d means alphanumeric string which wil contain alternate alphabates and numbers")
s = s[::2]
print(s)

#6
s=input("Enter string which you want to reverse")
s = s[::-1]
print(s)

#7
dic = {}
s=input('Enter string')
for s in s:
    dic[s] = dic.get(s,0)+1
print('\n'.join(['%s,%s' % (k, v) for k, v in dic.items()]))

#8
set1={1,3,6,78,35,55}
set2={12,24,35,24,88,120,155}
set1 &= set2
li=list(set1)
print(li)

#9
def removeDuplicate( li ):
    newli=[]
    seen = set()
    for item in li:
        if item not in seen:
            seen.add( item )
            newli.append(item)
    return newli
li=[12,24,35,24,88,120,155,88,120,155]
print(removeDuplicate(li))

#10
li = [12,24,35,24,88,120,155]
li = [x for x in li if x!=24]
print(li)

#11
li = [12,24,35,70,88,120,155]
li = [x for (i,x) in enumerate(li) if i not in (0,4,5)]
print(li)


#12
li = [12,24,35,70,88,120,155]
li = [x for x in li if x%5!=0 and x%7!=0]
print(li)

#13
import random
print(random.sample([i for i in range(1,1001) if i%5==0 and i%7==0], 5))


#14
n=int(input("Enter a number"))
sum=0.0
for i in range(1,n+1):
    sum += float(float(i)/(i+1))
print(sum)




