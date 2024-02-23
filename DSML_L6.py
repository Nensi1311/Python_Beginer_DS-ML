#!/usr/bin/env python
# coding: utf-8

#  <h1> Programming Fundamentals - 1 : Intro to Python

# In[7]:


print("Hello World")
print("Welcome to begginer Python")


# In[8]:


print('Hello World')
print('Welcome to begginer Python')


# In[14]:


print('Hii 27 !@#$%^&*')


# In[1]:


print(10)


# In[3]:


print(5 + 2)


# In[3]:


print(2.4 + 5.9)


# In[4]:


print(10 - 2 + 6)


# In[5]:


print(8943751089374589364895619845918 + 398457982374598136458913549861980645871608735610986)


# In[6]:


print(5 * 5)


# In[9]:


print(10 - 5)


# In[12]:


print(3/2)


# In[13]:


print(3//2)


# In[6]:


5+2


# In[15]:


print('10+10')


# In[16]:


# Capital P does not work
Print('10+10')


# In[18]:


# Escape character
print('It\'s a nice day')


# In[19]:


# \\ to print \
print("Hello \\ World")


# <h2> Example - Simple Interest   

# In[7]:


p = 100
r = 5
t = 2


# In[8]:


si = (p*r*t)/100
print("Simple Interest is : ",si)


# <h2> Input
# <h3>Take the name of the user as input. And say hello to them

# In[10]:


name = input()


# In[11]:


print("Hello", name)


# In[12]:


print("Hello", input())


# In[13]:


print("Hello\'s")


# <h2> Comments
#   <h4>  
# -> Comments are the statements that are written inside the code but they are ignored by the interpreter. These are written to make the code understable and readable.
# 
#       
#     
#     
# -> Comments start with #
#     
#     
# 

# In[16]:


print("Good evening")
# This is a good evening statements
print("Hello")


# <h2> Data Types

# <h3> Integer - int <br> Floating point numbers - float <br> Strings - str <br> Boolean Type - bool <br> NoneType

# In[17]:


a = 100


# In[18]:


print(type(a))


# In[19]:


b = 10.987654


# In[20]:


print(type(b))


# In[21]:


c = "Hello"


# In[22]:


print(type(c))


# In[23]:


d ='N'


# In[24]:


print(type(d))


# In[1]:


print(.2)


# In[2]:


x = .2
print(type(x))


# In[27]:


e = True
f = False


# In[28]:


print(type(e))
print(type(f))


# In[29]:


print(e,f)


# In[31]:


g = None
# denotes NULL value


# In[32]:


print(type(g))


# # <h2> Declaration of Variable
# #  <h4> 
#     1. The variable name should either begin with an Uppercase(A to Z) or Lowercase(a to z) character or an underscore(_).
#     
#     2. One should always remember to use a meaningful name for variables in Python. For example – no_of_chocolates makes more sense than noc.
#     
#     3.  If a variable has multiple words, it is advised to separate them with an underscore.
#     
#     4. One should ensure that a variable name should not be similar to keywords of the programming language.
#     
#     5. One should also remember that even variable names are case-sensitive.
#     
#     6. A variable should not begin with a digit or contain any white spaces or special characters such as #,@,&.
#     
#     7. No limit on variable name length
#     
#     8. Cannot assign to True, False and None 
#     
#     9. Variable name can only contain alphanumeric characters and underscore
#     
#     10. Cannot assign to operator
#     
#     11. Variable names must start with a letter it can't start with a digit
#     
#     12. Special characters (except underscore) are not allowed
#    

# In[35]:


# variable name must always begin with a character 
# variables name are case sensitive
# special characters are not allowed in naming variables (underscore is an exceptio)
name1
name-1 # not allowed


# In[36]:


_name = 10


# In[37]:


print(_name)


# <h2> Typecasting

# In[38]:


f = 7.4


# In[40]:


i = int(f)
print(i)


# In[41]:


i2 = int(10.9)
print(i2)


# In[42]:


i3 = int(-5.8)
print(i3)


# In[43]:


print(type(i))


# In[44]:


x = int(7.91)
print(x)


# In[45]:


a = 10
b = float(a)


# In[47]:


print(b)
print(type(b))


# <h2> String to int

# In[49]:


i = int("537")


# In[51]:


print(i, type(i))


# In[54]:


i2 = int("abc")


# <h2> Convert int to string

# In[57]:


x = 1.2
b = str(x)
print(b)


# <h2> Convert float to str

# In[58]:


s2 = str(8.2384)


# In[59]:


s2


# <h3> Python doesn't have any range on its numbers

# <h2> Operators
# <h4>
#    
#     Addition +
#     
#     Subtraction -
#     
#     Multiplication *
#     
#     Division / (Always gets float result)
#     
#     Floor Division // (Always gets int result)
#     
#     Exponent ** (Power)
#     
#     Modulo % (Reminder)
#     

# In[60]:


a = 5 +2
a


# In[61]:


a = 5-2
a


# In[62]:


a = 5*2
a


# In[63]:


a = 5/2
a


# In[64]:


a = 5**2
a


# In[65]:


a = 5%2
a


# In[66]:


a = 5/2
a


# In[67]:


2 or 2.5


# In[68]:


a = 5//2
a


# In[69]:


10 ** (1/2)


# # <h2> Operator Predence Rules
# 
# B - Brackets
#         
# E - Exponentiation
#         
# D - Division (both divisions)
#         
# M - Multiplication, Modulo
#         
# A - Addition
#         
# S - Subtraction
#     
#  In case there are two operations with the same precedence in an expression, they are evaluated left-to-right    

# In[5]:


print(10 - 4 * 2 + 5 - 6 / 2)


# # <h2> Relational Operators
#     <
#     >
#     <=
#     >=
#     ==
#     !=

# In[6]:


print(1>2)


# In[7]:


print(1<2)


# In[9]:


print(10<=10)


# In[10]:


print(1==1.0)


# In[11]:


print(5!=10)


# In[3]:


import keyword
keyword.kwlist


# In[ ]:




