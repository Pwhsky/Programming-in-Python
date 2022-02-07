#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Uppgift 1.1


# In[ ]:


import math
import cmath
import numpy as np
a = input('Ange talet a: ')
b = input('Ange talet b: ')
c = input('Ange talet c: ')
a=int(a)
b=int(b)
c=int(c)
x1 = (-b + cmath.sqrt(b**2-4*a*c))
x2 = (-b - cmath.sqrt(b**2-4*a*c))
if x1==x2:
    print(f'Röttarna är samma: {x1}')
else:
    print(f'Rötterna är {x1} och {x2}')


# Uppgift 1.2

# In[30]:


a = input('Ange ditt första tal ')
b = input ('Ange ditt andra tal ')
a=int(a)
b=int(b)
x1=hex(a)
x2=hex(b)

print(f'Ditt första tal i hexadecimal form är {x1} och ditt andra tal {x2}')


# In[23]:


a = input('Ange ditt första tal ')
b = input ('Ange ditt andra tal ')
a=float(a)
b=float(b)
x1 = a/b
print(f'Kvoten mellan det första talet {a} och det andra talet {b} är {x1:4.3f}')


# In[2]:


a = input('Ange ditt första tal')
b = input ('Ange ditt andra tal')
a=float(a)
b=float(b)
x1 = a%b
print(f'Resten av divisionen mellan talet {a} och {b} är {x1}')


# In[ ]:


Uppgift 1.1.3


# In[83]:



A=input('Skriv namn: ')
B=input('Skriv Efternamn: ')
C=input('Skriv födelseår: ')
D=input('Skriv namn: ')
E=input('Skriv Efternamn: ')
F=input('Skriv födelseår: ')
G=input('Skriv namn: ')
H=input('Skriv Efternamn: ')
I=input('Skriv födelseår: ')
T='Namn'
Y='Efternamn'
U='Födelseår'
print(f'{T:<15}{Y:<15}{U:<15}\n{A:<15}{B:<15}{C:<15}\n{D:<15}{E:<15}{F:<15}\n{G:<15}{H:<15}{I:<15}')


# In[54]:


Uppgift 1.2.1


# In[4]:


import numpy as np
x=input('Skriv heltal med mellanslag mellan varandra: ')
x=x.split()

v=len(x)
b2=max(x)
b3=min(x)
for i in range(0, len(x)):
    x[i] = int(x[i])
x1=np.sum(x)/v

print(f'Här är strängen {x} med medelvärdet {x1}, största värdet {b2} och minsta värdet {b3}')


# In[ ]:


Uppgift 1.2.2


# In[36]:


A = input("Skriv en mening: ")
d=0
l=0
for c in A:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1

print(f'Antal bokstäver {l}')
print(f'Antal siffror {d}')


# In[ ]:


Uppgift 1.2.3


# In[36]:


string=input('Skriv text som du vill leta efter mönster i ')
pattern=input('Skriv mönstret du är ute efter ')
y=string.find(pattern)
b=y
while y != -1:
    print(b)
    string=string[y+1:]
    y=string.find(pattern)
    b+=y+1


# In[ ]:


Uppgift 1.3.1


# In[55]:


A=input('Skriv ett tal ')
B=complex(A)
if B.imag==0:
    if B-int(B.real) == 0 :
        A=int(A)
        print(f'{A} är ett heltal')
    else:
        print(f'{A} är ett reellttal men inte ett heltal')
elif B.imag!=0:
    print(f'{B} är ett komplextal')


# In[ ]:


Uppgift 1.3.2 KLAR


# In[39]:


A=input('Skriv en vektor med hårdparantes eller siffra.: ')
B=input('Skriv en till vektor med hårdparantes eller en till siffra: ')
C = A is B
if C==True:
    print(f'{A} och {B} pekar på samma objekt')
if C==False:
    T = A==B
    if T==False:
        print(f'{A} har inte samma värde som {B} och de pekar inte mot samma objekt')
    elif T==True:
        print(f'{A} har samma värde som {B} men de pekar inte mot samma objekt')



# In[ ]:


Uppgift 1.3.3 KLAR


# In[40]:


A=input('Skriv något valfritt ')
try:
    b=int(A)
    print('Det du angav innehåller siffror')
except:
    A=list(A)
    c=reversed(A)
    c=list(c)
    if A == c:
        print(f'Det du angav är ett palindrom')
    else:
        print(f'Det du angav är inte ett palindrom eller så innehåller det både siffror och bokstäver')




# In[ ]:


Uppgift 1.4.1 KLAR


# In[24]:


A=input('Skriv namn ')
B=input('Skriv ålder ')
R=1 #Håller koll på vilken iteration
O=1 #"kill switch" låter användaren stoppa while-loopen om användare anger O=0
j=int(B)
q=A
G=int(B)
while O!=0:
    R=R+1 #Motsvarar fortfarande vilken iteration
    Y=input('Skriv ett till namn ')
    E=input('Skriv ålder ')
    C=int(E)
    G=G+C #Adderar alla tidigare samt senaste inputs för att sedan dela på R vilket ger medelvärdet M
    M=G/R
    if C>j:
        q=Y
        j=C
        print(f'{q} är den äldsta personen hittills')
    else:
        print(f'{q} är den äldsta personen hittills')
    print(f'Medelåldern är {M}')
    U=input('Skriv 0 om du är klar, annars skriv 1 ')
    U=int(U)
    if U==0:
        O=0
        print(f'{M} är medelåldern och den äldsta i listan är {q} ')


# In[ ]:


Uppgift 1.4.2 KLAR


# In[147]:


import math
date=input('Skriv ett datum på formatet yyyy-mm-dd ')
year=date[0:4]
month=date[5:7]
day=date[8:11]
months=[1,2,3,4,5,6,7,8,9,10,11,12]
monthdays=[0,31,28,31,30,31,30,31,31,30,31,30,31]
Veckodagar=['Söndag','Måndag', 'Tisdag', 'Onsdag', 'Torsdag', 'Fredag', 'Lördag']
year=int(year)
month=int(month)
day=int(day)
B=(year-1950)#hur många år emellan 1950 och angivna år
B=int(B)
days=B*365 + math.floor(((B-2)/4))
for x in range(0,month):
    days=days+monthdays[x]
days=days+day

Veckodag=days%7
Dag=Veckodagar[Veckodag]
print(f'{Dag}')



# In[ ]:


Uppgift 1.4.3 KLAR


# In[177]:


R=[]
for x in range(1,10):
    B=[]
    for y in range(1,10):

        B.append(x*y)
    R.append(B)

for x in range (0,9):
    for y in range(0,9):
        print(f'{R[x][y]:5}',end='')
    print()


# In[ ]:


Uppgift 1.5.1 KLAR


# In[161]:


Integer=input('Skriv ett heltal: ')
Integer=int(Integer)
for x in range(1,Integer+1):
    if Integer%x==0:
        print(x)


# In[ ]:


Uppgift 1.6.1 KLAR


# In[38]:


a=int(input('Ange ett värde för a, a är det första elementet i listan '))
b=int(input('Ange ett värde för b, b är det sista elementet i listan '))
N=int(input('Ange hur många punkter du vill ha i lista '))
T=(b-a)/(N-1) #Detta ger hur stor mellansteg det skall vara mellan varje element
Y=[]
Y.append(a) #Lägger till första elementet i position 0
for x in range(1,N-1):

    Y.append(a+T)
    a=a+T
Y.append(b) #Lägger till ett sista element som det givna b
u=len(Y) #Antal punkter
print(f'{Y} {u}')


# In[ ]:


Uppgift 1.6.3 KLAR


# In[ ]:


Lista och tupel:[5,4,1,0,10,12,34] (5,10,3,20,2)
1) A[1:3] blir [4,1] samt (10,3)
2) A[3:1:-1] blir [0,1] samt (20,3)
3) A[-1::-1] blir [34,12,10,0,1,4,5] samt (2,20,3,10,5)
4) A[len(A):-1:1] blir en tom vektor då koden går från sista element till sista element [] ()
5) A[1:10] blir [4,1,0,10,12,34] samt (10,3,20,2) (5 och 5 är position 0)
6) A.append(10) lägger till 10 i slutet av listan   [5,4,1,0,10,12,34,10] men ändrar ej en tupel


# In[ ]:


Uppgift 1.7.1 KLAR


# In[42]:


def addmatrix(x1,x2):
    x3=[] # Matris 3 som är resultat av aritmetisk operation
    for x in range(0,len(x1)):
        nyrad=[] #Ny rad som motsvarar resultat av aritmetisk operation mellan rad x
        for y in range(0,len(x1[0])): # Befinner sig i iteration x (rad x) och lägger ihop alla element x1 med motsvarande element i x2
            nyrad.append(x1[x][y]+x2[x][y])
        x3.append(nyrad) # Lägger till denna nya rad x i en matris x3 som returneras och skrivs ut
    return x3
def subtmatrix(x1,x2):
    x3=[] # Matris 3 som är resultat av aritmetisk operation
    for x in range(0,len(x1)):
        nyrad=[]
        for y in range(0,len(x1[0])):
            nyrad.append(x1[x][y]-x2[x][y])
        x3.append(nyrad)
    return x3
def multmatrix(x1,x2):
    x3=[] # Matris 3 som är resultat av aritmetisk operation
    for x in range(0,len(x1)):
        nyrad=[]
        for y in range(0,len(x1[0])):
            nyrad.append(x1[x][y]*x2[x][y])
        x3.append(nyrad)
    return x3
m1=[] #Redskap för konstruera rader
x1=[] #Matris 1 som skall hanteras
x2=[] #Matris 2 som skall hanteras
x3=[] # Matris 3 som är resultat av aritmetisk operation
Breaker=[]
for y in range(1,3):
    V=int(input(f'Hur många rader har matrisen nummer {y} du vill ange? : '))
    Breaker.append(V) # Listan Breaker kontrolleras innan aritmetiska operationer för att se om dimensionerna stämmer.
    for x in range (1,V+1):
        m1=input(f'Skriv ner rad {x} : ')
        m1=m1.split()
        for x in range(0,len(m1)):
            m1[x]=int(m1[x])
        if y==1:
            x1.append(m1)
        elif y==2:
            x2.append(m1)
if Breaker[0]!=Breaker[1]:
    print('Dimensionerna på matriserna går inte ihop')
else:
    x=int(input('Skriv 1 för addition av matris, 2 för subtraktion, 3 för multiplikation : '))
    if x==1:
        b=addmatrix(x1,x2)
        print('\n',b)
    elif x==2:
        b=subtmatrix(x1,x2)
        print('\n',b)
    elif x==3:
        b=multmatrix(x1,x2)
        print('\n',b)


# In[ ]:


Uppgift 1.8.1 KLAR


# In[46]:


import random
Lista1=[]
for x in range(0,100):
    y=random.randrange(1,101,1)
    Lista1.append(y)

L=[i for i in Lista1 if i%7==0 or i%11==0 or i%13==0]
print(L)


#  Uppgift 1.9.3 REDOVISA

# In[112]:


def Primtal(heltal):
    x=[]
    b=1
    for y in range(1,heltal+1):
        if heltal%y==0:
           return False

heltal=int(input('Skriv ett tal : '))
Primtal(heltal)


# In[ ]:


Uppgift 1.10.3 REDOVISA


# In[51]:


def Lista(a,b,N=100):
    Lista=[a+(x*((b-a)/(N-1))) for x in range(0,N)] #i första "iterationen" är a = givna talet, i andra iterationen är a
    # - första talet a + mellansteget, detta görs N-1 gånger (Det är N-1 mellansteg) tills det uppnåda givna sista värdet nås.
    return print(Lista)
Lista(1,10)


# In[ ]:


Uppgift 1.11 REDOVISA


# In[52]:


def Kvadsum(*args):
    A=0
    for x in args:
        A+=x
    A=A**2
    return print(A)
Kvadsum(25,50)
a,b=*(5,3)


# In[ ]:


Uppgift 1.12.2 REDOVISA


# In[173]:


import random
Pm=0 #Håller koll på användarens poäng
Pd=0 #Håller koll på datorns poäng
St=1
Sa=2
På=3
for x in range(3):
    a=int(input('1 = Sten 2 = Sax 3 = Påse : '))
    b=random.randrange(1,4)
    if Pm<4 or Pd<4:
            if a==b:
                print('Du och datorn valde samma, kör igen! : ')
            elif a==St and b==2:
                print('Du fick ett poäng, datorn valde sax.')
                Pm=Pm+1
            elif a==St and b==3:
                print('Datorn fick ett poäng, datorn valde påse.')
                Pd=Pd+1
            elif a==Sa and b==1:
                print('Datorn fick ett poäng, datorn valde sten.')
                Pd=Pd+1
            elif a==Sa and b==3:
                print('Du fick ett poäng, datorn valde påse.')
                Pm=Pm+1
            elif a==På and b==1:
                print('Du fick ett poäng, datorn valde sten.')
                Pm=Pm+1
            elif a==På and b==2:
                print('Datorn fick ett poäng, datorn valde sax')
                Pd=Pd+
            if Pm==3 or Pd==3
print(f'Datorn hade {Pd} poäng och du hade {Pm} poäng')





# In[ ]:


Uppgift 1.13.1 REDOVISA


# In[172]:


f_namn=input('Skriv namnet på textfilen du vill skapa alternativt läsa av')

Option=int(input('1: Skriva ut fil. 2: Lägga till en rad till filen. 3: Skriva över filen. 4: Lämna programmet :'))
if Option==1:
    f=open(f_namn,'r')
    while True:
        o = f.readline()
        if not o:
            break
        print(o,end='')
    f.close()
if Option==2:
    f=open(f_namn,'a')
    while True:
        nyrad=input('Skriv raden du vill lägga till, om du är klar skriv inget och tryck på enter : ')
        if nyrad=='':
            break
        nyrad+='\n'
        f.write(nyrad)
    f.close()
if Option==3:
    f=open(f_namn,'w')
    while True:
        nyrad=input('Skriv raden du vill lägga till, om du är klar skriv inget och tryck på enter ')
        if nyrad=='':
            break
        nyrad+='\n' för radvist istället för kolumnvist
        f.write(nyrad)
    f.close()
else:
    print('Du är klar')









# Uppgift 1.14.2 REDOVISA

# In[ ]:


1)Ger (0,0,0,0)
2)Ger en kolumn med fyra nollor
3)(Broadcastar)Gör Radvektor till 3x3 matris med tre identiska rader (1,2,3) samt gör kolumnvektorn till 3x3 matris med tre identiska kolumner (1,2,3)
4)14
5)14


# In[ ]:


Uppgift 1.15.1 REDOVISA


# In[143]:


import random
import numpy as np
m1=[] #Redskap för konstruera rader
m2=[]
x1=[] #Matris 1 som skall hanteras
x2=[] #Matris 2 som skall hanteras
x3=[] #Matris 3 som är resultat av aritmetisk operation
for y in range(1,3):
    if y==1:
        for i in range(0,4):
            for u in range(0,4):
                P=random.randrange(1,100)
                m1.append(P)
            x1.append(m1)
            m1=[]
    elif y==2:
        for i in range(0,4):
            for u in range(0,4):
                P=random.randrange(1,100)
                m2.append(P)
            x2.append(m2)
            m2=[]



x1=np.array(x1)
x2=np.array(x2)
A=np.block([[x1,x2],[x2,x1]])
B1=np.diag(A)
B=B1.reshape(4,2)
print(A)
print(B1)
print(B)


# In[13]:


Uppgift 1.16.1


# In[57]:


import matplotlib.pyplot as plt

circle1 = plt.Circle((7.5, 6), 1, color='r',fill=False)
circle2 = plt.Circle((3, 6), 1, color='blue',fill=False)
circle3 = plt.Circle((4, 5), 1, color='y',fill=False)
circle4 = plt.Circle((5.25, 6), 1, color='k',fill=False)
circle5 = plt.Circle((6.25, 5), 1, color='g',fill=False)

fig, ax = plt.subplots()
plt.xlim(0,10)
plt.ylim(0,10)
ax.add_artist(circle1)
ax.add_artist(circle2)
ax.add_artist(circle3)
ax.add_artist(circle4)
ax.add_artist(circle5)


# In[ ]:
