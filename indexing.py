Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#indexing

a=
SyntaxError: incomplete input
a="vijayawada"
a[4]
'y'
a[0]
'v'
a[0],a[4]
('v', 'y')
a[0]+a[1]+a[2]+a[3]+a[4]
'vijay'

a=i am in class
SyntaxError: invalid syntax
A=i am in class
SyntaxError: invalid syntax
b=codegnan python full stack
SyntaxError: invalid syntax
a="i am in class"
a[0]
'i'
a[8]+a[9]+a[10]+a[11]+a[12]
'class'
a[5]+
SyntaxError: incomplete input
a[5]+a[6]
'in'
a[2]+a[3]
'am'
a[4]
' '
a="i am learning python full stack"
a[15]+a[16]+a[17]+a[18]+a[19]+a[20]
'ython '
a[14]+a[15]+a[16]+a[17]+a[18]+a[19]+a[20]
'python '
a[5]+a[6]+a[7]+a[8]+a[9]+a[10]+a[11]+a[12]
'learning'
a[2]+a[3]
'am'
a[22]+a[23]+a[24]+a[25]
'ull '
a[22]+a[23]+a[24]+a[25]
'ull '
a[21]+a[22]+a[23]+a[24]+a[25]
'full '
a[21]+a[22]+a[23]+a[24]
'full'
[5]+a[6]+a[7]+a[8]+a[9]
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    [5]+a[6]+a[7]+a[8]+a[9]
TypeError: can only concatenate list (not "str") to list
a[5]+a[6]+a[7]+a[8]+a[9]
'learn'
b="time is very precious"
b[13]+b[14]+b[15]+b[16]+b[17]+b[18]+b[19]+b[20]
'precious'
b[8]+b[9]+b[10]+b[11]
'very'
a[0]+a[1]+a[2]+a[3]
'i am'
b[0]+b[1]+b[2]+b[3]
'time'



>>> #negative
>>> a=vijayawada is a royal city
SyntaxError: invalid syntax
>>> a="vijayawada is a royal city"
>>> a[-1]+a[-2]+a[-3]+a[-4]
'ytic'
>>> a[-10]+a[-9]+
SyntaxError: incomplete input
>>> a[-10]+a[-9]+a[-8]+a[-7]+a[-6]
'royal'
>>> a[-4]+a[-3]+a[-2]+a[-1]
'city'
>>> a[-14]+a[-13]
's '
>>> a[-13]+a[-12]
' a'
>>> a[-15]+a[-14]
'is'
>>> b=vizag is a city of destiny
SyntaxError: invalid syntax
>>> b="vizag is a city of destiny"
>>> a[-7]+a[-6]+a[-5]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'al  city'
>>> a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'al city'
>>> b[-7]+b[-6]+b[-5]+b[-4]+b[-3]+b[-2]+b[-1]
'destiny'
>>> b[-15]+b[-14]+b[-13]+b[-12]
'city'
>>> b[-26]+b[-25]+b[-24]+b[-23]+b[-22]
'vizag'
