Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #list[]
>>> a=[2,4.5,"python",8+9j,True,False]
>>> print(a)
[2, 4.5, 'python', (8+9j), True, False]
>>> type(a)
<class 'list'>
>>> b=4.6
>>> type(b)
<class 'float'>
>>> c=4.6
>>> type(c)
<class 'float'>
>>> c=[4.6]
>>> type(c)
<class 'list'>
>>> a=["python","java","c","c++"]
>>> a.append("ai")
>>> a
['python', 'java', 'c', 'c++', 'ai']
>>> a.append("ml","dsa")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a.append("ml","dsa")
TypeError: list.append() takes exactly one argument (2 given)
>>> a.append(["ml","dsa"])
>>> a
['python', 'java', 'c', 'c++', 'ai', ['ml', 'dsa']]
>>> #extend()
>>> a=["dsa","ai","ml"]
>>> a.extend(["python","java"])
a
['dsa', 'ai', 'ml', 'python', 'java']
#insert()
b=["black","white"]
b.insert(1,"red")
b
['black', 'red', 'white']
#index()
a=["apple","mango","kiwi"]
a.index("mango")
1
#copy()
a.copy()
['apple', 'mango', 'kiwi']
b=a.copy()
b
['apple', 'mango', 'kiwi']
#pop
a=["vja","vzg","hyd"]
a.pop()
'hyd'
a
['vja', 'vzg']
a.pop(1)
'vzg'
a
['vja']
a.pop("vja")
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a.pop("vja")
TypeError: 'str' object cannot be interpreted as an integer
a
['vja']
a.pop(0)
'vja'
a
[]
#remove
a=["hii","hello","how"]
a.remove("how")
a
['hii', 'hello']
a.remove(1)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    a.remove(1)
ValueError: list.remove(x): x not in list
#clear
a=["java","ai","ml"]
a.clear()
a
[]
b=[]
a.append("anjali")
b.append("anjali")
b
['anjali']
['anjali']
['anjali']
#sort()
a=["banana","grapes","apple","mango"]
a.sort()
a
['apple', 'banana', 'grapes', 'mango']
b=[7,4,8,2,9,0]
b.sort()
b
[0, 2, 4, 7, 8, 9]
c=[5+8j,2+4j,6+7j]
c.sort()
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    c.sort()
TypeError: '<' not supported between instances of 'complex' and 'complex'
d=[6,8.9,"anjali","hello",6+9j]
d.sort()
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    d.sort()
TypeError: '<' not supported between instances of 'str' and 'float'
c=[4.5,8.9,7.6]
c.sort()
c
[4.5, 7.6, 8.9]
d=["True","False","True"]
d.sort()
d
['False', 'True', 'True']
e=[7,8,9,3.5,4.6]
e.sort()
e
[3.5, 4.6, 7, 8, 9]
#reverse
a=["black","red","white"]
a.reverse()
a
['white', 'red', 'black']
b=[5,7,9,2,3]
b.reverse()
b
[3, 2, 9, 7, 5]
#len
a=["java","ai","ml"]
len(a)
3
b="java"
len(b)
4
c=["java"]
len(c)
1
#count
a=["java","ai","ml"]
a.count("ai")
1
a.count("a")
0
b=["java","ai","a","ml"]
b.count("a")
1
