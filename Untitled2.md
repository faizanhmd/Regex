```python
#using search function;    here, '?' means pattern may be present 0 or 1 time 

import re

any_string = '''hello, my name is faizan. These are my contact numbers: +91-1234567899 and 9876543211.
feel free to call me at working hours not 247.
'''
numberRegex = re.compile(r"((\+\d\d-)?\d\d\d\d\d\d\d\d\d\d)")
print(numberRegex.search(any_string))
```

    <re.Match object; span=(56, 70), match='+91-1234567899'>
    


```python
#using findall function

import re

any_string = '''hello, my name is faizan. These are my contact numbers: +91-1234567899 and 9876543211.
feel free to call me at working hours not 247.
'''
numberRegex = re.compile(r"((\+\d\d-)?\d\d\d\d\d\d\d\d\d\d)")
print(numberRegex.findall(any_string))
```

    [('+91-1234567899', '+91-'), ('9876543211', '')]
    


```python
#to find how many sentences are there in the string ==> can use no of full stops

import re

any_string = '''hello, my name is faizan. These are my contact numbers: +91-1234567899 and 9876543211.
feel free to call me at working hours not 247.
'''
numberRegex = re.compile(r"(\.)")
print(numberRegex.findall(any_string))
```

    ['.', '.', '.']
    


```python
import re

any_string = '''On the 12th day of Christmas my true love gave to me
12 chocolate cookies, 11 shoppers fighting, 10 cars a honking,
9 broken presents, 8 bags a missing, 7 Christmas parties,
6 crazy in-laws, 5 EXTRA POUNDS, 4 credit cards, 3 crying babies,
2 bras, and a dry brown Christmas tree.
'''

wordRegex = re.compile(r"(\d\d\s\w)")
print(wordRegex.findall(any_string))
```

    ['12 c', '11 s', '10 c']
    


```python
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
```

    ['12 chocolate', '11 shoppers', '10 cars', '9 broken', '8 bags', '7 Christmas', '6 crazy', '5 EXTRA', '4 credit', '3 crying', '2 bras']
    


```python
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
```

    ['O', 'e', 'a', 'o', 'i', 'a', 'u', 'e', 'o', 'e', 'a', 'e', 'o', 'e', 'o', 'o', 'a', 'e', 'o', 'o', 'i', 'e', 'o', 'e', 'i', 'i', 'a', 'a', 'o', 'i', 'o', 'e', 'e', 'e', 'a', 'a', 'i', 'i', 'i', 'a', 'a', 'i', 'e', 'a', 'i', 'a', 'E', 'A', 'O', 'U', 'e', 'i', 'a', 'i', 'a', 'i', 'e', 'a', 'a', 'a', 'o', 'i', 'a', 'e', 'e']
    


```python
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
```

    ['ue', 'oo', 'ie', 'ie', 'OU', 'ie', 'ee']
    


```python
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
```

    ['n', 't', 'h', 't', 'h', 'd', 'y', 'f', 'C', 'h', 'r', 's', 't', 'm', 's', 'm', 'y', 't', 'r', 'l', 'v', 'g', 'v', 't', 'm', 'c', 'h', 'c', 'l', 't', 'c', 'k', 's', 's', 'h', 'p', 'p', 'r', 's', 'f', 'g', 'h', 't', 'n', 'g', 'c', 'r', 's', 'h', 'n', 'k', 'n', 'g', 'b', 'r', 'k', 'n', 'p', 'r', 's', 'n', 't', 's', 'b', 'g', 's', 'm', 's', 's', 'n', 'g', 'C', 'h', 'r', 's', 't', 'm', 's', 'p', 'r', 't', 's', 'c', 'r', 'z', 'y', 'n', 'l', 'w', 's', 'X', 'T', 'R', 'P', 'N', 'D', 'S', 'c', 'r', 'd', 't', 'c', 'r', 'd', 's', 'c', 'r', 'y', 'n', 'g', 'b', 'b', 's', 'b', 'r', 's', 'n', 'd', 'd', 'r', 'y', 'b', 'r', 'w', 'n', 'C', 'h', 'r', 's', 't', 'm', 's', 't', 'r']
    


```python

```
