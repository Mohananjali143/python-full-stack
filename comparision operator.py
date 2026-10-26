Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#comparision operator
a=5
b=15
a<b
True
a>b
False
b>a
True
a<=b
True
b>=a
True
b<a
False
a!=b
True
a==b
False
a=20
b=15
a<b
False
b>a
False
a<=b
False
b>=a
False
a>b
True
b<a
True
>>> a!=b
True
>>> a==b
False
>>> a=20
>>> b=40
>>> a<b
True
>>> b>a
True
>>> a<=b
True
>>> B>=a
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    B>=a
NameError: name 'B' is not defined. Did you mean: 'b'?
>>> b>=a
True
>>> a>b
False
>>> b<a
False
>>> a!=b
True
>>> a==b
False
>>> b!=a
True
>>> b==a
False
