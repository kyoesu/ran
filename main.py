from func import *

a1=""
a2=""
slash="________________________________________________________________________________"
a=""
h=""
ch=True
end=True
j=0
#z=int(input('введите кол-во глав, которые надо обработать(либо 0, что бы дошло до конца)   '))
z=2
if z==0:
    end=False
elif z!=1:
    z=z-1

while end==False or (j<=z):
    a=conn(ch,h)
    h=href(a)
    a1=a1+gt(search(a))
    a1=a1+slash+"\r \r \r"
    ch=False
    j+=1
    if z==0:
        end=last(a)
    if (j % 50==0):
        print('----------------------------------'+str(j))
        a2=a2+a1
        a1=""

a2=a2+a1
f=open('fin.txt','w+')
f.write(a2)
f.close()
#gt(a)