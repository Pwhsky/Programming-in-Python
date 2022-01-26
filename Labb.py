# -*- coding: utf-8 -*-

# In[1]:
# 1.1.1,
import cmath as cm

a = int(input('Assign coefficient a '))
b = int(input('Assign coefficient b '))
c = int(input('Assign coefficient c '))

x1 = (-b + cm.sqrt(b**2 - 4*a*c))/(2*a)
x2 = (-b - cm.sqrt(b**2 - 4*a*c))/(2*a)
print (x1)
print (x2)
# In[2]:
#1.1.2

A = int(input('feed me a number '))
B = int(input('feed me a second number '))


print(hex(A))
print(hex(B))

A = float(A) 
B = float(B)
print(round(A/B,3))

print ('resten är ' + str(A%B))
# In[3]:
##1.1.3


A=input('Name: ')
B=input('Surname: ')
C=input('Date of birth: ')
T='Namn'
Y='Efternamn'
U='Födelseår'
#There is a character limit of 15
#These strings contain replacement fields, 
#which are expressions delimited by curly braces {}.

print(f'{T:<15}{Y:<15}{U:<15}')
print(f'{A:<15}{B:<15}{C:<15}')

# In[4]:
#1.2.1
A = input('Enter a series of numbers ')
output = []

for i in A.split():
    output.append(float(i));

 
avg = sum(output)/len(output)

print ('Mean value is: ' + str(avg))
print ('The first element is: ' + str(output[0]))
print ('The last element is: ' + str(output[-1]) ) 

# In[5]:
#1.2.2
A = input('Feed me numbers or words ' )
num = sum(i.isdigit() for i in A)
letters = sum(i.isdigit() for i in A)
space = sum(i.isdigit() for i in A)

sumchar = num + letters

print('The sum of characters is: ' + str(sumchar))


# In[6]:
    #1.2.3
    
A = input('Specify your gibberish: ')
B = input('What are you looking for? ')

Count = A.count(B)

print('Found ' + str(Count) + ' count(s) of ' + str(B) + ' in ' + str(A))

# In[7]:
    
#1.3.1
A=input('Feed me a number ')
B=complex(A)
if B.imag==0:
    if B-int(B.real) == 0 :
        A=int(A)
        print(str(A)+ ' is an integer')
    else:
        print(str(A) + ' is real but not an integer')
elif B.imag!=0:
    print(str(B) + ' is complex')
    
    # In[39]: #maybe broken?


    A=input('Write a vector or number, ex: [a,b,c,d...]: ')
    B=input('Do another one: ')
    condition = A is B
if condition==True:
        print(str(A)+ ' and ' +str(B)+ ' are the same ')
if condition==False:
        condition2 = A==B
        if condition2==False:
            print(str(A) +' is not the same value as '+ str(B) +' and they do not point to the same object.')
        elif condition2==True:
            print(str(A) + ' is the same value as ' + str(B) + ' but they do not point to the same object.')


# In[8]:
    
#1.3.3 Palindrome

Candidate = input('Choose your word: ')

try:
   isnumber = float(Candidate)
   print('This is not a word...')
   
except:
    Candidate = list(Candidate)
    rCandidate = list(reversed(Candidate))
    
    
if Candidate == rCandidate:
    
    output = '' # this converts a list back to a string
    for i in Candidate:
        output +=i
    
    
    print(str(output) + ' is a palindrome')
    
else:
    
  print('Your word is not a palindrome.')
# In[9]: 
    #uppgift 1.4.1
    
A=input('Write a name ')
B=input('Write the persons age  ')
i=1 #iteration number
end=0 #stops the input process by writing end = 1

j=int(B)
q=A
G=int(B)
while end!=1:
        i=i+1 #Motsvarar fortfarande vilken iteration
        Y=input('Write another name ')
        E=input('Write another age ')
        C=int(E)
        G=G+C #Adderar alla tidigare samt senaste inputs för att sedan dela på R vilket ger medelvärdet M
        Mean=G/i
        if C>j:
            q=Y
            j=C
            print(str(q) + ' is the oldest person so far')
        else:
            print(str(q) + ' is the oldest person so far')
        print('The average age is ' + str(Mean))
        U=input('Write "0" if you are done, otherwise write "1" ')
        U=int(U)
        if U==0:
            end=1
            print(str(Mean) +' is the mean age and the oldest person in the list is ' + str(q))
            
            

        # In[10]: 
            #uppgift 1.4.3 
            R=[] #R is the main matrix, a list of lists.
            for x in range(1,10):  #x goes from 1 to 9
                B=[]                   #create empty vector B for each x
                
                for y in range(1,10): #y goes from 1 to 9

                    B.append(x*y) #fill B with x*y
                    
                    
                R.append(B) #fill R with the values of B after multiplication

            for x in range (0,9):
                for y in range(0,9):
                    print(f'{R[y][x]:4}',end='') #prints each element of R sequentially

                print('\n') #starts a new row
            
   
    
   # In[11]: 
       #Uppgift 1.5.1 
       
A = int(input('Choose an integer: ' ))

for i in range(1,A+1):
 
    if A % i ==0: #0 modulus = divider
        print(str(i) + ' is a divider of '+ str(A))
       
       # In[12]: 
    
    #uppgift 1.5.2 Geometric series
    
    a = int(input('Enter the starting element value: '))
q = float(input ('Enter a positive floater less than 1: '))
Z = float(0)
for i in range(0,100):
            Z = Z + a*q**i
            
print('The series is calculated to Z = ' + str(Z))
        
        
S = float(a/(1-q))
print('The exact solution is S = ' + str(S))

# In[13]
#Uppgift 1.6.1 
import numpy as np
N = int(input('Input N: '))
a = int(input('Input a: '))
b = int(input('Input b: '))

C= np.linspace(a,b,N) #Using Linspace
print('Using linspace gives: '+str(C))
 #OR
#K = (b-a)/N
#fakelinspace = [i*K for i in range(a,b+1)]
#print('Manual linspace gives: ' + str(fakelinspace))

# In[16]
 #Uppgift 1.6.2
A = input('Enter a sequence of numbers: ')
sequence = []

for i in A.split():
    sequence.append(int(i));


istuple = input('Is your input a tuple or a list? T/L ')

if istuple == 'T':
    sequence = tuple(sequence)
    print('Your input is a tuple')
else:
    print('Your input is a list')

askforsort = input('How do you want the sequence sorted? R/D ')


askfortuple = input('Do you want to make it a tuple or a list? T/L ')
    


if askforsort == 'R':
     
    sequence = list(sequence)
    sequence.sort()
    
else:
    sequence = list(sequence)
    sequence.sort(reverse = True)
 
    
 
    
if askfortuple == 'T':
    sequence = tuple(sequence)
    print('Your tuple is '+ str(sequence))
else:
    sequence = list(sequence)
    print('Your list is ' + str(sequence))

# In[17]:
    #1.7.2
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


    
    
    
    
# In[18]:
    #1.8.1
    import random 

biglist = []
for i in range(1,101):
        n = random.randint(1,100)
        biglist.append(n)
        
        factors=[i for i in biglist if i%7==0 or i%11==0 or i%13==0]
print(factors)

# In[20]:
    #1.8.3
    import numpy as np
size = int(input('Choose the size of your matrix: '))
A = np.zeros((size,size))
    
crossmatrix = [i for i in A ]

    
    

# In[19] #Sets have no repeating elements
# delkapitel 1.9
A = input('Input food separated by comma: ')

B = A.split(",")
C = tuple(set(B))

print(str(C))

# In[20]
#Delkapitel 1.10
#OBS OBS EJ FÄRDIGT




# In[21:
    #uppgift 2.1.2
import numpy as np
def convert(number):
    n = complex(number)
    nreal = float(n.real)
    nimag = float(n.imag)
    angle = round(np.arctan(nimag/nreal) * 57.2957795)
    
    print('Absolute value is: ' + str(abs(n)))
    
    print('Angle is: ' + str(angle) + ' degrees.')
    
    # In[22] #Uppgift 2.2.1
    A = float(input('Enter your starting value: '))
    Q = float(input('Enter your desired base: '))
    N = int(input('Enter your desired element (integers only): '))
    
    
    
    nth = A*Q**(N-1)
    
    print('The ' + str(N) +'th'  ' element is calculated as: ' + str(nth))
    
    
    # In[24]
#Uppgift 2.2.2
x1 = float(input('Input your point for sine approximation: '))
iterations = int(input('Enter number of iterations (accuracy): '))
truesine = math.sin(x1)

for k in range(0,iterations,1):
    taylorsine=((-1)**k)*(x1**(1+2*k))/factorial(1+2*k)

    

print('The Taylor approximation for sin(x) is: ' + str(taylorsine))
error = abs(truesine - taylorsine)
print('The error is: '+ str(error))

x2 = float(input('Input your point for cosine approximation: '))
iterations = int(input('Enter number of iterations (accuracy): '))
truecos = math.cos(x2)

for k in range(0,iterations,1):
    taylorcosine=((-1)**k)*(x2**(1+2*k))/factorial(1+2*k)

    

print('The Taylor approximation for cos(x) is: ' + str(taylorcosine))
error = abs(truesine - taylorcosine)
print('The error is: '+ str(error))




    
# In[25]:
    #uppgift 2.2.3
    def Longlist(a,b,N=100):
        Longlist=[a+(x*((b-a)/(N-1))) for x in range(0,N)] #i första "iterationen" är a = givna talet, i andra iterationen är a
        # - första talet a + mellansteget, detta görs N-1 gånger (Det är N-1 mellansteg) tills det uppnåda givna sista värdet nås.
        return print(Longlist)
    Longlist(1,10)
    
# In[26]:
    #2.3.2
    import cmath as cm
    
    roots = lambda a, b, c: tuple(((-b + cm.sqrt(b**2 - 4*a*c))/(2*a),(-b - cm.sqrt(b**2 - 4*a*c))/(2*a)))
    
    # In[27]:
        #Uppgift 2.4
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
                    Pd=Pd+1
                if Pm==3 or Pd==3:
                    print(f'Datorn hade {Pd} poäng och du hade {Pm} poäng')
                    
print(f'Datorn fick {Pd} poäng och du fick {Pm} poäng')
                    
                    
# In[28]:
    #uppgift 2.5.1
f_namn=input('Skriv namnet på textfilen du vill skapa alternativt läsa av ')

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
        nyrad += '\n' #för radvist istället för kolumnvist
        f.write(nyrad)
    f.close()
else:
    print('Du är klar')
    

# In[29]:
    #delkapitel 3.1
  


# In[30]:
    
    #Uppgift 3.2.1
    import random
    import numpy as np
    m1=[] #Redskap för konstruera rader
    m2=[]
    x1=[] #Matris 1 som skall hanterar, 4x4
    x2=[] #Matris 2 som skall hanteras, 4x4
    x3=[] #Matris 3 som är resultat av aritmetisk operation, 8x8
    
    #Målet är att skapa matris C =  x1 x2 
    #                               x2 x1
    
    
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
    
# In[31]:
  #  Uppgift 3.3.1 (Olympiska ringar)
import matplotlib.pyplot as plt
import numpy as np

circle1 = plt.Circle((7, 6), 1, color='r', fill = False)
circle2 = plt.Circle((4.75, 6), 1, color='black', fill = False)
circle3 = plt.Circle((2.5,6),1,color='blue',fill=False)

circle4 = plt.Circle((5.88, 5), 1, color='green', fill = False)
circle5 = plt.Circle((3.65, 5), 1, color='orange', fill = False)

fig, ax = plt.subplots()


ax.add_patch(circle1)
ax.add_patch(circle2)
ax.add_patch(circle3)
ax.add_patch(circle4)
ax.add_patch(circle5)

plt.xlim(0,11)
plt.ylim(0,11)
plt.axis('off')
plt.legend()

# In[32]:
    #Uppgift 3.3.2: 
        #Plotta sin(x), Cos(x), sin(x)/x, mellan -6pi till 6pi
import numpy as np
import matplotlib.pyplot as plt
decision = input('Choose a plot type: "figure","figures","subplots"  ')

x = np.arange(-6*np.pi,6*np.pi,0.1)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x)/x



#this section puts everything in the same figure
if decision == "figure":
    plt.figure(1)
    plt.plot(x,y1)
    plt.plot(x,y2)
    plt.plot(x,y3)
    
    #This section makes 3 subplots in 1 figure

    
elif decision == "subplots":
    plt.figure(2)
    plt.subplot(311)
    plt.plot(x, y1)
    plt.subplot(312)
    plt.plot(x, y2)
    plt.subplot(313)
    plt.plot(x,y3)


elif decision == "figures": #This section makes 3 figures for each function
        plt.figure(1)
        plt.plot(x,y1)
        plt.figure (2)
        plt.plot(x,y2)
        plt.figure(3)
        plt.plot(x,y3)

# In[33]
#Delkapitel 3.4




