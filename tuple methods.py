Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #tuple()
>>> a=(6,8.9,"python",2+9j,True,False)
>>> print(a)
(6, 8.9, 'python', (2+9j), True, False)
>>> type(a)
<class 'tuple'>
>>> #index
>>> a.index(2+9j)
3
>>> a.count(True)
1
>>> len(a)
6
