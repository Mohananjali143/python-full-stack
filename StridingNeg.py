Python 3.14.8 (tags/v3.14.8:8e6e75d, Sep 30 2026, 18:19:33) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #striding
>>> a="python course"
>>>  a[-1:-8:-2]
...  
IndentationError: unexpected indent
>>> a[-1:-8:-2]
'ero '
>>> a[-2:-10:-3]
'son'
>>> a[-3:-13:-4]
'r t'
>>> a[-1:-12:-6]
'e '
>>> a[-4:9:-2]
''
>>> a[-4:-9:-2]
'ucn'
>>> a[9:5:2]
''
>>> a[5:9:2]
'nc'
>>> a[-10:-6:-2]
''
>>> a[-6:-10:-2]
'cn'
>>> a[::1]
'python course'
>>> a[::-1]
'esruoc nohtyp'
