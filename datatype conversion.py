Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> int(9)
9
>>> int(6.7)
6
>>> int("hello")
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    int("hello")
ValueError: invalid literal for int() with base 10: 'hello'
>>> int(7+5j)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    int(7+5j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> int(True)
1
>>> int(Flase)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(Flase)
NameError: name 'Flase' is not defined. Did you mean: 'False'?
>>> int(False)
0
>>> float(6)
6.0
>>> float(6.4)
6.4
>>> float("hii")
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    float("hii")
ValueError: could not convert string to float: 'hii'
float(5+6j)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    float(5+6j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0
str(5)
'5'
str(4.7)
'4.7'
str("anjali")
'anjali'
str(6+8j)
'(6+8j)'
str(True)
'True'
str(False)
'False'
complex(4)
(4+0j)
complex(5.3)
(5.3+0j)
complex(3+7j)
(3+7j)
complex("python")
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    complex("python")
ValueError: complex() arg is a malformed string
complex(True)
(1+0j)
complex(False)
0j
bool(5)
True
bool(4.6)
True
bool("codegnan")
True
bool(5+7j)
True
bool(True)
True
bool(Flase)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    bool(Flase)
NameError: name 'Flase' is not defined. Did you mean: 'False'?
bool(False)
False
