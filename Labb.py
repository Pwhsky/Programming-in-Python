# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 19:42:31 2022

@author: 
"""
# In[1]:
# 1.1.1,
import cmath as cm
import numpy as np

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
# In[2]:
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

print(f'{T:<15}{Y:<15}{U:<15}\n{A:<15}{B:<15}{C:<15}')

# In[2]:
#1.2.1
A = input('Enter a series of numbers ')
output = []

for i in A.split():
    output.append(float(i));

 
avg = sum(output)/len(output)

print ('Mean value is: ' + str(avg))
print ('The first element is: ' + str(output[0]))
print ('The last element is: ' + str(output[-1]) ) 

# In[]:
#1.2.2
A = input('Feed me gibberish ' )
num = sum(i.isdigit() for i in A)
letters = sum(i.isdigit() for i in A)
space = sum(i.isdigit() for i in A)

sumchar = num + letters

print('The sum of characters is: ' + str(sumchar))


# In[]:
    #1.2.3
    
A = input('Specify your gibberish: ')
B = input('What are you looking for? ')

Count = A.count(B)

print('Found ' + str(Count) + ' count(s) of ' + str(B) + ' in ' + str(A))

# In[]:
    
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
    
# In[]:
    
#1.3.3 Palindrome
  alecmoegme






    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    




