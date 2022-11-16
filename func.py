import requests #pip install requests
from googletrans import Translator#pip install googletrans==4.0.0-rc1


def search(a):
    i=0
    i1=0
    i2=0
    #выборка текста
    for i in range(len(a)):
        if a[i:i+29]=="chapter-inner chapter-content":
            i1=i+31
        if i1!=0 and a[i:i+6]=="</div>" and i2==0:
            i2=i
    a=a[i1:i2]

    #поиск тегов и их удаление
    j=0
    for j in range(a.count('<')):
        g=True
        i1=0
        i2=0
        i=0
        while i<len(a) and g==True:
            if a[i]=="<"and i2==0:
                i1=i
            if a[i]==">"and i2==0 and i1!=0:
                i2=i
                g=False
            i+=1
        a=a[:i1]+a[i2+1:]
        
    for j in range(a.count('&nbsp;')):#удаление мусора какого-то
        i=0
        i1=0
        g=True
        while i<len(a) and g==True:
            if a[i:i+6]=="&nbsp;":
                i1=i
                g=False
            i+=1
        a=a[:i1]+a[i1+6:]
    #print (a)
    return a


def href(a):
    #поиск ссылки на след. страницу
    i=0
    i1=0
    i2=0
    g=False
    for i in range(len(a)):
        if a[i:i+4]=="Next" and a[i+30:i+37]=="Chapter":
            i2=i
            g=True
    i=i2
    while g==True:
        if a[i-5:i]=="href=":
            i1=i
            g=False
        i=i-1
    
    h=a[i1+1:i2-2]
    h="https://www.royalroad.com"+h
    return h

def conn(ch,h):
    if ch==True:
        #l=input("введи ссылку(работает только с www.royalroad.com)     ")
        l="https://www.royalroad.com/fiction/16946/azarinth-healer/chapter/1032812/chapter-894-eyes-of-the-world"#пред-пред последняя шлава
        #l="https://www.royalroad.com/fiction/16946/azarinth-healer/chapter/198097/chapter-1-boring-introduction-where-is-the-magic"#1 глава
    else:
        l=h
    response = requests.get(l)
    if response.status_code ==200:
        print("connect sussessful")
    else:
        exit("не коннектится")

    a=response.text
    return a
def last(a):
    end=False
    if a.count('disabled">Next')>0:
        end=True
    return end

def gt(a):
    a1=a.splitlines()
    translator = Translator()
    a2=""
    for i in range(len(a1)-1):
        if a1[i]!='':
            if len(a1[i])>4900:
                j=2000
                a3=a1[i]
                while a3[j]!="."and a3[j]!='!'and a3[j]!='?':
                    j+=1
                a2=a2+translator.translate(str(a3[:j]),src= 'en', dest= 'ru').text
                a2=a2+translator.translate(str(a3[j:]),src= 'en', dest= 'ru').text
                a2=a2+"\r"
            else:
                a2=a2+translator.translate(str(a1[i]),src= 'en', dest= 'ru').text
                a2=a2+"\r"
        
    return a2
    #t = translator.translate(a,src= 'en', dest= 'ru').text
    #print (t)
    #return t
