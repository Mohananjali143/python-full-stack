Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#dict{} :dict is used to store the key value paires,and it is denoted with{}
a={"name":"anjali","year":2026,"month":10}
print(a)
{'name': 'anjali', 'year': 2026, 'month': 10}
type(a)
<class 'dict'>
b={"name","anjali","year",2026}
print(b)
{'name', 'year', 2026, 'anjali'}
type(b)
<class 'set'>
a={"year":2026,"month":"oct","date":31}
a.keys()
dict_keys(['year', 'month', 'date'])
a.values()
dict_values([2026, 'oct', 31])
a.items()
dict_items([('year', 2026), ('month', 'oct'), ('date', 31)])
b={1:2,3:4}
type(b)
<class 'dict'>
a.keys()
dict_keys(['year', 'month', 'date'])
b.keys()
dict_keys([1, 3])
b.values()
dict_values([2, 4])
b.items()
dict_items([(1, 2), (3, 4)])
#accessing
a={"course":"python","code":"gnan","data":"coding"}
a["course"]
'python'
a
{'course': 'python', 'code': 'gnan', 'data': 'coding'}
#get :get means read
a.get("code")
'gnan'
a
{'course': 'python', 'code': 'gnan', 'data': 'coding'}
#update :update means to add the elements
a={"year":2026,"month":11}
a.update({"time":10})
a
{'year': 2026, 'month': 11, 'time': 10}
a.update({"hours":2},{"min":10})
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a.update({"hours":2},{"min":10})
TypeError: update expected at most 1 argument, got 2
#in update we can pass the keyvalues in only one {}
a.update({"hours":10,"min":15})
a
{'year': 2026, 'month': 11, 'time': 10, 'hours': 10, 'min': 15}
#setdefault
a={"colour":"black","food":"biryani","desert":"cake"}
a.setdefault("place","vja")
'vja'
a
{'colour': 'black', 'food': 'biryani', 'desert': 'cake', 'place': 'vja'}
#setdefault is used to add something as default like any thing string or int ,it takes as 1st is key and 2nd is value ,and in setdefault we can add only one pair
#pop
a.pop("colour")
'black'
a
{'food': 'biryani', 'desert': 'cake', 'place': 'vja'}
#in pop we have give the key then it delete the key value
#popitem
a.popiteam()
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    a.popiteam()
AttributeError: 'dict' object has no attribute 'popiteam'. Did you mean: 'popitem'?
a.popitem()
('place', 'vja')
a
{'food': 'biryani', 'desert': 'cake'}
#popitem can delete the last key value in the dict
#copy
>>> a={"hours":10,"min":11,"sec":5}
>>> a.copy()
{'hours': 10, 'min': 11, 'sec': 5}
>>> b=a.copy()
>>> b
{'hours': 10, 'min': 11, 'sec': 5}
>>> #clear
>>> a.clear()
>>> a
{}
>>> #we can use the clear to delete all the keyvalue pairs and it gives empty dict
>>> #do's and dont's
>>> a={"name":"anju","city":"vja","name":"anju"}
>>> print(a)
{'name': 'anju', 'city': 'vja'}
>>> #here in dict duplicate values are not allowed
>>> a={"name":"anju","city":"vja","name2":"anju"}
>>> print(a)
{'name': 'anju', 'city': 'vja', 'name2': 'anju'}
>>> #here if we give key names different but the values are same it can print all the key value pairs
>>> a={"idnos":[10,20,30],"names":["anjali","anju","anu"],"marks":[60,70,80]}
>>> print(a)
{'idnos': [10, 20, 30], 'names': ['anjali', 'anju', 'anu'], 'marks': [60, 70, 80]}
>>> type(a)
<class 'dict'>
>>> a.keys()
dict_keys(['idnos', 'names', 'marks'])
>>> a.values()
dict_values([[10, 20, 30], ['anjali', 'anju', 'anu'], [60, 70, 80]])
>>> a.items()
dict_items([('idnos', [10, 20, 30]), ('names', ['anjali', 'anju', 'anu']), ('marks', [60, 70, 80])])
