from func import *

a1=""
slash="________________________________________________________________________________"
a=""
h=""
ch=True
end=True
j=0
z=int(input('введите кол-во глав, которые надо обработать(либо 0, что бы дошло до конца)   '))

if z==0:
    end=False
else:
    z=z-1

while end==False or (j<=z):

    a=conn(ch,h)

    h="https://www.royalroad.com"+href(a)
    a1=a1+search(a)
    a1=a1+slash+"\r \r \r"
    ch=False
    j+=1
    end=last(a)


f=open('fin.txt','w+')
f.write(a1)
f.close()
