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

 
    
 
    
 
    
 
    
 
    
 
    
 
    




