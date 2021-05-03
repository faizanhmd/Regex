#!/usr/bin/env python
# coding: utf-8

# In[24]:


#using search function;    here, '?' means pattern may be present 0 or 1 time 

import re

any_string = '''hello, my name is faizan. These are my contact numbers: +91-1234567899 and 9876543211.
feel free to call me at working hours not 247.
'''
numberRegex = re.compile(r"((\+\d\d-)?\d\d\d\d\d\d\d\d\d\d)")
print(numberRegex.search(any_string))


# In[25]:


#using findall function

import re

any_string = '''hello, my name is faizan. These are my contact numbers: +91-1234567899 and 9876543211.
feel free to call me at working hours not 247.
'''
numberRegex = re.compile(r"((\+\d\d-)?\d\d\d\d\d\d\d\d\d\d)")
print(numberRegex.findall(any_string))


# In[28]:


#to find how many sentences are there in the string ==> can use no of full stops

import re

any_string = '''hello, my name is faizan. These are my contact numbers: +91-1234567899 and 9876543211.
feel free to call me at working hours not 247.
'''
numberRegex = re.compile(r"(\.)")
print(numberRegex.findall(any_string))


# In[29]:


import re

any_string = '''On the 12th day of Christmas my true love gave to me
12 chocolate cookies, 11 shoppers fighting, 10 cars a honking,
9 broken presents, 8 bags a missing, 7 Christmas parties,
6 crazy in-laws, 5 EXTRA POUNDS, 4 credit cards, 3 crying babies,
2 bras, and a dry brown Christmas tree.
'''

wordRegex = re.compile(r"(\d\d\s\w)")
print(wordRegex.findall(any_string))


# In[30]:


# '+' ==> 1 or more so same shortcut format works until any other character format appears in string

import re

any_string = '''On the 12th day of Christmas my true love gave to me
12 chocolate cookies, 11 shoppers fighting, 10 cars a honking,
9 broken presents, 8 bags a missing, 7 Christmas parties,
6 crazy in-laws, 5 EXTRA POUNDS, 4 credit cards, 3 crying babies,
2 bras, and a dry brown Christmas tree.
'''

wordRegex = re.compile(r"(\d+\s\w+)")
print(wordRegex.findall(any_string))


# In[32]:


#making your own character class
#finding vowels in string

import re

any_string = '''On the 12th day of Christmas my true love gave to me
12 chocolate cookies, 11 shoppers fighting, 10 cars a honking,
9 broken presents, 8 bags a missing, 7 Christmas parties,
6 crazy in-laws, 5 EXTRA POUNDS, 4 credit cards, 3 crying babies,
2 bras, and a dry brown Christmas tree.
'''

vowelRegex = re.compile(r"[aeiouAEIOU]")   #it is same as (r"a|e|i|o|u|A|E|I|O|U")
print(vowelRegex.findall(any_string))


# In[34]:


# finding 2 vowels in continuation in above exp

import re

any_string = '''On the 12th day of Christmas my true love gave to me
12 chocolate cookies, 11 shoppers fighting, 10 cars a honking,
9 broken presents, 8 bags a missing, 7 Christmas parties,
6 crazy in-laws, 5 EXTRA POUNDS, 4 credit cards, 3 crying babies,
2 bras, and a dry brown Christmas tree.
'''
vowelregex = re.compile(r"[aeiouAEIOU]{2}")
print(vowelregex.findall(any_string))


# In[40]:


# finding consonants in string using negative character class(caret symbol'^') with the help of vowels

import re

any_string = '''On the 12th day of Christmas my true love gave to me
12 chocolate cookies, 11 shoppers fighting, 10 cars a honking,
9 broken presents, 8 bags a missing, 7 Christmas parties,
6 crazy in-laws, 5 EXTRA POUNDS, 4 credit cards, 3 crying babies,
2 bras, and a dry brown Christmas tree.
'''
consonantregex = re.compile(r"[^aeiouAEIOU\s\,\.\d\-]")
print(consonantregex.findall(any_string))


# In[ ]:




