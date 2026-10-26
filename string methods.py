Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#string methods
#len()
a="python"
len(a)
6
b="python course"
len(b)
13
c=""
len(c)
0
d=" "
len(d)
1
#count()
a="twinkle twinkle little star"
count(a)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
a.count("twinkle")
2
a.count("t")
5
a.count("a")
1
a.count(" ")
3
a="1234"
a.count("3")
1
a=1,2,3,4,5,6
a.count(3)
1
b=3,4,5,,6,3,6,7
SyntaxError: invalid syntax
b=3,4,5,6,3,6,7
b.count(6)
2
#find a string
a="code"
a[2]
'd'
a.find("d")
2
b="hello"
b.find("l")
2
b[2:4]
'll'
b("k")
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    b("k")
TypeError: 'str' object is not callable
>>> b.find("k")
-1
>>> #escape sequences
>>> #\n->new line
>>> #\t->tab space
>>> a="name\nmobileno\tmailid\ncollege\tbranch"
>>> print(a)
name
mobileno	mailid
college	branch
>>> a="name:anjali\nmobileno:8978675698\tmailid:anjali@gmail.com\ncollege:MLEWC\tbranch:CSE
SyntaxError: incomplete input
>>> a="name:anjali\nmobileno:8978675698\tmailid:anjali@gmail.com\ncollege:MLEWC\tbranch:CSE"
>>> print(a)
name:anjali
mobileno:8978675698	mailid:anjali@gmail.com
college:MLEWC	branch:CSE
>>> #replace()
>>> a="wait until you succeed"
>>> a.replace("java","DSA")
'wait until you succeed'
>>> a.replace("wait","work")
'work until you succeed'
>>> a="python,java")
SyntaxError: unmatched ')'
>>> a="python,java"
>>> a.replace("java","DSA")
'python,DSA'
>>> a="hii"
>>> a.replace("h","a")
'aii'
