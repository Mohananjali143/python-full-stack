Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#sets{}
a={1,2.0,"python",5+7j,True,False}#set is a unordered collection
print(a)
{False, 1, 2.0, 'python', (5+7j)}
#set is a semi mutable and it removes the duplicate values
type(a)
<class 'set'>
b={5,7,8,6,5,3,9,3,}
print(b)
{3, 5, 6, 7, 8, 9}
#add
a={4,5,6,7,8,9}
a.add(10)
a
{4, 5, 6, 7, 8, 9, 10}
#issubset
a={123456}
b={4,5,6};
false
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    false
NameError: name 'false' is not defined. Did you mean: 'False'?
a=(1,2,3,4,5,6}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
a={1,2,3,4,5,6}
b={4,5,6}
b.issubset(a)
True
a.issubset(b)
False
#issuperset
a={2,3,4,56,7,8,9}
b={6,78,9}
b={6,7,8,9}
hhg
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    hhg
NameError: name 'hhg' is not defined
a={2,3,4,5,6,7,8,9}
b={6,7,8,9}
a.issupperset(b)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    a.issupperset(b)
AttributeError: 'set' object has no attribute 'issupperset'. Did you mean: 'issuperset'?
a.issuperset(b)
True
b.issuperset(a)
False
#union()
a={2,4,6,7,9}
b={3,5,7,0}
a.union(b)
{0, 2, 3, 4, 5, 6, 7, 9}
#intersection
a={4,5,6,7,8}
b={7,8,9,2,3}
a.intersection(b)
{8, 7}
b.intersection(a)
{8, 7}
#update
a={1,2,3,4,5,6}
b={4,5,,6,7,8,9}
SyntaxError: invalid syntax
b={4,5,6,7,8,9}
a.update(b)
a
{1, 2, 3, 4, 5, 6, 7, 8, 9}
b.update(a)
a
{1, 2, 3, 4, 5, 6, 7, 8, 9}
b
{1, 2, 3, 4, 5, 6, 7, 8, 9}
#difference
a={3,4,5,6,7,8}
b={8,9,10,11,12,13}
a.difference(b)
{3, 4, 5, 6, 7}
b.difference(a)
{9, 10, 11, 12, 13}
a
{3, 4, 5, 6, 7, 8}
a={1,2,3,4,5}
b={6,7,8,9,10}
a.difference(b)
{1, 2, 3, 4, 5}
b.difference(a)
{6, 7, 8, 9, 10}
#symmetric_difference
a={1,2,3,4,5,6}
b={2,3,4,12,13,14,15}
a.symmetric_difference(b)
{1, 5, 6, 12, 13, 14, 15}
b.symmetric_difference(a)
{1, 5, 6, 12, 13, 14, 15}
#intersection_update
a={8,9,10,11,12}
b{10,11,12,13,14,15}
SyntaxError: invalid syntax
b={10,11,12,13,14,15}
a.intersection_update(b)
a
{10, 11, 12}
a
{10, 11, 12}
b.intersection_update(a)
b
{10, 11, 12}
b
{10, 11, 12}
#difference_update
a={5,6,7,8,9,10}
b={30,40,50,60,70}
a.difference_update(b)
a
{5, 6, 7, 8, 9, 10}
b.difference_update(a)
b
{50, 70, 40, 60, 30}
a={10,20,30,40}
b={30,40,50,60}
a.difference_update(b)
a
{20, 10}
b.difference_update(a)
b
{40, 50, 60, 30}
#symmetric_difference_update()
a={2,3,4,5,6,7,8,9}
b={7,8,9,10,2,9}
a.symmetric_difference_update(b)
a
{3, 4, 5, 6, 10}
a
{3, 4, 5, 6, 10}
b.symmetric_difference_update(a)
b
{2, 3, 4, 5, 6, 7, 8, 9}
b
{2, 3, 4, 5, 6, 7, 8, 9}
#pop
a={2,3,4,5,6}
a.pop()
2
#pop is used to delete the first value in the set
#remove
a
{3, 4, 5, 6}
a.remove(5)
a
{3, 4, 6}
#remove is used to delete a perticular value in the set
#discard
a.discard(4)
a
{3, 6}
#discard is same as remove
#copy
{10,11,1213,14,15}
{10, 11, 1213, 14, 15}
a={10,11,12,13,14,15}
a.copy()
{10, 11, 12, 13, 14, 15}
b=a.copy()
b
{10, 11, 12, 13, 14, 15}
#clear
a
{10, 11, 12, 13, 14, 15}
a.clear()
a
set()
b=set()
b.set()
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    b.set()
AttributeError: 'set' object has no attribute 'set'
b.set()
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    b.set()
AttributeError: 'set' object has no attribute 'set'
>>> b
set()
>>> b.add(30)
>>> b
{30}
>>> #index
>>> a={1,2,3,4,5}
>>> a.index()
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    a.index()
AttributeError: 'set' object has no attribute 'index'
>>> len(a)
5
>>> a.count()
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    a.count()
AttributeError: 'set' object has no attribute 'count'
>>> #isdisjoint
>>> a={1,2,3,4,5}
>>> b={6,7,8,9,0}
>>> a.isdisjoint(b)
True
>>> a={1,2,3,4,5}
>>> b={5,6,7,8,9}
>>> a.isdisjoint(b)
False
