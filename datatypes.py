Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#data type
a=10
type(a)
<class 'int'>
b=5.8
type(b)
<class 'float'>
c='python'
type(c)
<class 'str'>
d="course"
type(d)
<class 'str'>
e='''codegnan'''
type(e)
<class 'str'>
>>> f=6+7j
>>> type(g)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    type(g)
NameError: name 'g' is not defined
>>> type(f)
<class 'complex'>
>>> g=45+8j
>>> type(g)
<class 'complex'>
>>> z=5j+9
>>> type(z)
<class 'complex'>
>>> x=4+8j
>>> type(x)
<class 'complex'>
>>> v=j
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    v=j
NameError: name 'j' is not defined
>>> d=4+8i
SyntaxError: invalid decimal literal
>>> c=True
>>> type(c)
<class 'bool'>
>>> b=False
>>> type(b)
<class 'bool'>
