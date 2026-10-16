Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#variables
a=2
print(a)
2
b=6
print(b)
6
x=7
print(x)
7
z=5
print(Z)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(Z)
NameError: name 'Z' is not defined. Did you mean: 'z'?
print(z)
5
9=20
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
a9=20
print(a9)
20
9a=45
SyntaxError: invalid decimal literal
a09876=56
print(a09876)
56
name="anjali"
print(name)
anjali
print("name")
name
city="vijayawada"
print(city)
vijayawada
country="india"
print(country)
india
@=9
SyntaxError: invalid syntax
$=8
SyntaxError: invalid syntax
&=5
SyntaxError: invalid syntax
_=78
print(_)
78
__a=89
print(__a)
89
 s=59
 
SyntaxError: unexpected indent
_h=89
print(_h)
89
if=45
SyntaxError: invalid syntax
else=57
SyntaxError: invalid syntax
int=90
print(int)
90
a=5,b=7
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a=8;b=8
print(a,b)
8 8
print(a+b)
16
a,b=5,6
print(a,b)
5 6

print(b-a)
1
a=2,3,4,5,6,7,8,9
print(a)
(2, 3, 4, 5, 6, 7, 8, 9)
a,b,c=3,4,5,6,7,8
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    a,b,c=3,4,5,6,7,8
ValueError: too many values to unpack (expected 3)
a,b,c=(3,6,9)
print(a,b,c)
3 6 9
a=2 3 4 5 6 7
SyntaxError: invalid syntax
first name="anjali"
SyntaxError: invalid syntax
firat_name="anjali"
print*(first_name)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    print*(first_name)
NameError: name 'first_name' is not defined. Did you mean: 'firat_name'?
print(first_name)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    print(first_name)
NameError: name 'first_name' is not defined. Did you mean: 'firat_name'?
print(firat_name)
anjali
fname="anjali"
lname="k"
print(fnamr+lname)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    print(fnamr+lname)
NameError: name 'fnamr' is not defined. Did you mean: 'fname'?
print(fname+lname)
anjalik
print(fname+" "+lname)
anjali k
>>> print(fname,lname)
anjali k
>>> NAME="anjali"
>>> print(NAME)
anjali
>>> Name="anjali"
>>> print(Name)
anjali
>>> name="pandu"
>>> print(name)
pandu
>>> a,b,c=999
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    a,b,c=999
TypeError: cannot unpack non-iterable int object
>>> a=b=c=999
>>> print(a,b,c)
999 999 999
>>> print(a b c)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> a=10
>>> print(a)
10
>>> del a
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined. Did you mean: 'a9'?
