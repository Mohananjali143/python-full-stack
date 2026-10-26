Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#slicing
a="codegnan"
a[0:3]
'cod'
a[0:4]
'code'
a[4:8]
'gnan'
a[:4]
'code'
a[4:]
'gnan'
a="work until you succeed"
a[0:7]
'work un'
a[15:22]
'succeed'
a[5:10]
'until'
>>> a[0:4]
'work'
>>> a[11:14]
'you'
>>> b="simple is better than complex"
>>> b[9:15]
' bette'
>>> b[10:16]
'better'
>>> b[0:6]
'simple'
>>> b[22:29]
'complex'
>>> b[7:9]
'is'
>>> 
>>> 
>>> #negative
>>> a="python is easy to learn"
>>> a[-13:-10]
'eas'
>>> a[-13:-9]
'easy'
>>> a[:-17]
'python'
>>> a[-5:]
'learn'
>>> b="god is grate"
>>> b[-5:]
'grate'
>>> b[:-9]
'god'
b[-10:-11]
''
b[-10:-13]
''
b[-6:-8]
''
b[-8:-6]
'is'
b[-14:-9]
'god'
b[-12:-9]
'god'
