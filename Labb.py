# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 19:42:31 2022

@author: 
"""
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
A = input('Feed me gibberish ' )
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
    
# In[18]:
    #1.8.1
    import random 

biglist = []
for i in range(1,101):
        n = random.randint(1,100)
        biglist.append(n)
        
        factors=[i for i in biglist if i%7==0 or i%11==0 or i%13==0]
print(factors)

# In[19]:
    #uppgift 1.9.2
import numpy as np
def convert(number):
    n = complex(number)
    nreal = float(n.real)
    nimag = float(n.imag)
    angle = round(np.arctan(nimag/nreal) * 57.2957795)
    
    print('Absolute value is: ' + str(abs(n)))
    
    print('Angle is: ' + str(angle) + ' degrees.')
# In[20]:
    #uppgift 1.10.
    def Longlist(a,b,N=100):
        Longlist=[a+(x*((b-a)/(N-1))) for x in range(0,N)] #i första "iterationen" är a = givna talet, i andra iterationen är a
        # - första talet a + mellansteget, detta görs N-1 gånger (Det är N-1 mellansteg) tills det uppnåda givna sista värdet nås.
        return print(Longlist)
    Longlist(1,10)
    
# In[21]:
    #1.11.2
    import cmath as cm
    
    roots = lambda a, b, c: tuple(((-b + cm.sqrt(b**2 - 4*a*c))/(2*a),(-b - cm.sqrt(b**2 - 4*a*c))/(2*a)))
    
    # In[22]:
        #Uppgift 1.12.2
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
                    
                    
# In[23]:
    #uppgift 1.13.1
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
        nyrad += '\n' #för radvist istället för kolumnvist
        f.write(nyrad)
    f.close()
else:
    print('Du är klar')
    

# In[24]:
    #Uppgift 1.14.2
1)Ger (0,0,0,0)
2)Ger en kolumn med fyra nollor
3)(Broadcastar)Gör Radvektor till 3x3 matris med tre identiska rader (1,2,3) samt gör kolumnvektorn till 3x3 matris med tre identiska kolumner (1,2,3)
4)14
5)14

# In[25]:
    
    #Uppgift 1.15.1
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
    
# In[26]:
    Uppgift 1.16.1








