import pandas as pd
import numpy as np
# from matplotlib.pyplot import plot

# x= pd.read_csv('/home/user/Desktop/mgak_doctors.csv')

# print x.head()
# user_cols=['user_id','age','gender','name','zicode']
#df=pd.read_table('http://bit.ly/movieusers',sep='|',header=None,names=user_cols)
#print df


# data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
#         'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions', 'Lions', 'Lions'],
#         'wins': [11, 8, 10, 15, 11, 6, 10, 4],
#         'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
# football = pd.DataFrame(data, columns=['year', 'team', 'wins', 'losses'])
# print football

'''
def dec(func):
  def infnc():
    print "Hi"
    func()
  return infnc
@dec
def hi():
  print "Hi Subhash"
hi()'''





# def dec(func):
#   def wrap(a,b):
#     if b==0:
#       return "error"
#     return func(a,b)
#   return wrap

# @dec
# def div(a,b):
#   return a/b

# a = div
# print a(10,0)

# class File():
#   def __init__(self,file,method):
#     self.file_obj = open(file,method)
#   def __enter__(self):
#         return self.file_obj
#   def __exit__(self, type, value, traceback):
#       print("Exception has been handled")
#       self.file_obj.close()
#       # return True

# with File('demo.txt', 'w') as opened_file:
#     opened_file.undefined_function('Hola!')



# class A():
#   @classmethod
#   def get(name):
#     return name

#   def __init__():
#     return self.get(name)

# class B(A):
#   attr= "Some class Value"
#   def __init__( self ):
#       """Create a new Instance"""
#       self.instVar= "some instance value"
#   def __str__( self ):
#       """Display an instance"""
#       return "%s %s" % ( self.attr, self.instVar )

# c=B()
# print A.get()
# print c.get()

# import types
# class SelfDocumenting( object ):
#     @classmethod
#     def getMethods( aClass ):
#       print "hai"
#       return [ (n,v.__doc__) for n,v in aClass.__dict__.items()
#                  if type(v) == types.FunctionType ]
#     def help( self ):
#         """Part of the self-documenting framework"""
#         print self.getMethods()

# class SomeClass( SelfDocumenting ):
#     attr= "Some class Value"
#     def __init__( self ):
#         """Create a new Instance"""
#         self.instVar= "some instance value"
#     def __str__( self ):
#         """Display an instance"""
#         return "%s %s" % ( self.attr, self.instVar )
# ac= SomeClass()
# ac.help()
# def clos(name):
#   def get():
#     print name
#   return get
# # del clos
# x = clos('Subhash')

# x()






















# def make_multiplier_of(n):
#     def multiplier(x):
#       print x,n
#       return x * n
#     return multiplier

# # Multiplier of 3
# times3 = make_multiplier_of(3)
# print times3.__name__,"fgggffg"
# print times3(5)



# import logging
# logging.basicConfig(filename='example.log', level=logging.INFO)


# def logger(func):
#     print func.__name__
#     def log_func(*args):
#         print args
#         logging.info(
#             'Running "{}" with arguments {}'.format(func.__name__, args))
#         print(func(*args))
#     return log_func


# def add(x, y):
#     return x+y


# def sub(x, y):
#     return x-y

# add_logger = logger(add)
# sub_logger = logger(sub)

# add_logger(3, 3)
# add_logger(4, 5)

# sub_logger(10, 5)
# sub_logger(20, 10)


# def print_msg(number):
#     def printer():
#         "Here we are using the nonlocal keyword"
#         nonlocal number
#         number=3
#         print(number)
#     printer()
#     print(number)

# print_msg(9)


# from pathlib import Path
# p = Path('/home/user/Subhash/').glob('*.*')
# # print (p.is_dir())
# # print (p.is_file())
# # print p
# print (sorted(p))


# try:
#   open(p)
# except IOError as e:
#   print (e)
# a={'name':'SUBHASH','age':21}
# b={'salary':16000,'tech':'python'}
# print({**a,**b})

# from collections import ChainMap
# c=ChainMap(a,b)
# print(c)


# class A:
#   counter=0
#   def __init__(self,name,age):
#     self.name=name
#     self.age=age
#     self.counter+=1
#   def get_data(self):
#     return self.name + ' ' +self.age



# a=A('SUBHASH','21')
# a.get_data()

# def out_side_func():
#   msg='Hi'
#   def inside_func():
#     msg = 'Hello'
#     print msg
#   return inside_func
#   print msg
# print out_side_func()



# def ot_func(n):
#   def in_func(m):
#     print n*m
#   return in_func

# o = ot_func(5)
# o(6)



# class Person:
#   def __init__(self,name):
#     self.name=name
#   @classmethod
#   def get_name(cls,name):
#     print cls.name

#   def get_nm(self):
#     print self.name

#   @staticmethod
#   def stat():
#     print Person.name

# c=Person(name='Chandra')
# # c.name='Chandra'
# c.get_name()
# c.get_nm()
# c.stat()


# x=10
# def myFunc(y):
#   # global x

#   x=y=20
#   return x

# print(myFunc(10))
# print (x)


# from Car import display

# display.display()


# 9727007337


# def spam():
#   eggs= 99
#   func()
#   print(eggs)

# def func():
#   eggs=0

# spam()
# def spam():
#   print eggs

# eggs = 10
# spam()
# print eggs

# def spam():
#   eggs = 'spam local'
#   print(eggs)
# # prints 'spam local'
# def bacon():
#   eggs = 'bacon local'
#   print(eggs)
#   # prints 'bacon local'
#   spam()
#   print(eggs)
# # prints 'bacon local'
# eggs = 'global'
# bacon()
# print(eggs)
# def get():
#   print(msg)
#   msg='ggggg'

# msg='gggg'
# get()

# def div(num):
#   try:
#     return 20/num
#   except ZeroDivisionError as e:
#     return e

# print(div(5))
# print(div(0))
# print(div(1))

# def div(num):
#   return 25/num

# try:
#   print(div(5))
#   print(div(0))
#   print(div(15))
#   print(div(10))
# except ZeroDivisionError as e:
#   print e

# import random
# secretNumber = random.randint(1, 20)
# print('I am thinking of a number between 1 and 20.')
# # Ask the player to guess 6 times.
# for guessesTaken in range(1, 7):
#   print('Take a guess.')
#   guess = int(input())
#   if guess < secretNumber:
#     print('Your guess is too low.')
#   elif guess > secretNumber:
#     print('Your guess is too high.')
#   else:
#     break
# # This condition is the correct guess!
# if guess == secretNumber:
#   print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
# else:
#   print('Nope. The number I was thinking of was ' + str(secretNumber))



# def collatz(number):
#   if number%2==0:
#     return number//2
#   else:
#     return 3*number+1


# print collatz(int(input('enter a number')))

# catNames = []
# while True:
#   print('Enter the name of cat ' + str(len(catNames) + 1) +
#   ' (Or enter nothing to stop.):')
#   name = input()
#   if name == '':
#     break
# catNames = catNames + [name] # list concatenation
# print('The cat names are:')
# for name in catNames:
#   print(' ' + name)
# import random

# def func(type_='s'):
#   if type_== 's':
#     return Mart
#   elif type_== 'i':
#     return random.randint (0, 1000)

# def   dec(func, type_ ):
#   x = 0
#   def wrapper ():
#     value = func(type_)
#     if isinstance (value, int):
#       return value + x
#     elif isinstance (value, basestring) :
#       return 'This value'

#     return wrapper

# print dec(func, 'i')()


# names = ['sai','satish','siva','subhash']
# salary = [35000,16000,40000,15000]
# ages = [27,26,26,26]
# data = {'names':names,'salary':salary,'age':ages}
# df = pd.DataFrame(data)
# df['gender']='M'
# print df
# df['salary']<15000 = 10000
# print df
# df = pd.read_csv('http://bit.ly/movieusers',sep='|',index_col='user_id',header=None,names=['user_id','age','gender','name','zicode'])
# # df = pd.read_csv('http://bit.ly/movieusers',sep='|',header=None,names=['user_id','age','gender','name','zicode'])
# print df.head()
# print df.iloc[1:3,:]
# print df
# df[(df['age']>40) & (df['gender']=='M')] =45
# print df[df['gender']==45]
# print df.shape
# df =df.T
# print df.set_index('user_id   ')
# a = df['age']
# print a.value_counts()
# df1['age']=45
# # print df[df.age>40]
# print df1.shape
# df2 = df.merge(df1,on='gender')
# print df2.shape
# df2 = df2.drop_duplicates(keep="first")
# print df2.shape
# df2.to_csv('/home/user/Subhash/data.csv')
# df.set_index('user_id',inplace=True)
# print df.tail(3)
# print df.groupby('gender').count()
# print df.groupby('gender').sum()[2:5]
# iloc-> Positional Indexing
# loc-> label based index
# print df.gender.value_counts()
# x = df.rename(columns={"age":'age_in'})
# print x.head(3)

# df = pd.read_excel('/home/user/projects/escpmtool/media/locations/East_Godavari.xlsx')
# # print df.head()
# # df.columns = ['subfacility_code','subfacility_name']
# print df.head()

# df = pd.ExcelFile('/home/user/projects/escpmtool/media/locations/East_Godavari.xlsx')
# print df.parse().head(),df
# df_1 = df.copy()
# print df_1['subfacility'],type(df_1['subfacility']),str(df_1['subfacility']),type(str(df_1['subfacility']))
# df_1.set_index(str(df_1['subfacility_code'])+df_1['subfacility'],inplace=True)
# print df.head()
# print df_1['district'].value_counts()
# print df_1.loc[0],df_1.subfacility_code.astype(str)
# print df_1.reindex(df_1.index[::-1])
# df_1_range = range(df_1.index.values.min(),df_1.index.values.max())
# print df_1_range
# print df.reindex(df_1_range).head()
# print df_1.drop([1,2])
# df_1.drop(['village','village_code'],axis=1)
# print df_1.head()
# print df_1.ix[0,['district','subfacility']]
# print df_1.xs(0)
# print df_1
# print df_1.ix[['subfacility_code','district_code']].apply(np.sqrt)
# print df_1['subfacility_code'].apply(np.sqrt)
# print df_1['subfacility_code'].plot()
# how=all-->It will check all values are epty then only it will drop
# trash=number->based on number provided the operation is performed

# print lambda x: " ".join(["_".join(i.split(" ")) for i in df1['subfacility_code'].head()])


# df = pd.read_csv('/home/user/sample.csv',sep='\t')
# print df.values

#Ranking of a dataFrame

# rank = df.rank(ascending=1)
# df['rank']=rank
# df.set_index(rank)
# print df.head()

# print df[df['village'].str.contains('B V Lanka')].head()
# for key,each in df.iterrows():
#   print each[key]

# left_frame = pd.DataFrame({'key': range(5), 
#                            'left_value': ['a', 'b', 'c', 'd', 'e']})
# right_frame = pd.DataFrame({'key': range(2, 7), 
#                            'right_value': ['f', 'g', 'h', 'i', 'j']})

# print left_frame.merge(right_frame) ,"inner"                       
# print left_frame.merge(right_frame,how='left'),"left"                        
# print left_frame.merge(right_frame,how='right'),"right"                        
# print left_frame.merge(right_frame,how='outer'),"outer" 

# print pd.concat([right_frame,left_frame],axis=1)                       
# df = left_frame.merge(right_frame)
# print df
# print df.sort_values(['key','left_value','right_value'],ascending=False)










# data = { 
#     'A':['A1', 'A2', 'A3', 'A4', 'A5'],  
#     'B':['B1', 'B2', 'B3', 'B4', 'B5'],  
#     'C':['C1', 'C2', 'C3', 'C4', 'C5'],  
#     'D':['D1', 'D2', 'D3', 'D4', 'D5'],  
#     'E':['E1', 'E2', 'E3', 'E4', 'E5'] } 
  
# # Convert the dictionary into DataFrame  
# df = pd.DataFrame(data) 
  
# # Remove column name 'A' 
# df.drop([0]) 
# print df



# def func(arg1,*arg2,**arg3):
#   print arg1,'argq',arg2,'arg2',arg3

# func(12,34,43,next=33,last=44)
# func("tezt",*[9,9])
# func(last=66,arg1="test",next=45)


# class A:
# 	pass

# def func():
# 	pass

# i=2
# s="Some String"
# t=A()
# f=func
# print isinstance(i,int)
# print isinstance(s,str)
# print isinstance(t,A)
# print isinstance(i,object)
# print isinstance(s,object)
# print isinstance(t,object)
# print isinstance(f,object)
# print isinstance(func,object)
# print isinstance(A,object)
# print isinstance(object,object)
# print isinstance(isinstance,object)
# print callable(func)
# print callable(A)
# print callable(f)
# print callable(t)

# birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
# while True:
# 	print('Enter a name: (blank to quit)')
# 	name = input()
# 	if name == '':
# 		break
	
# 	if name in birthdays:
# 		print(birthdays[name] + ' is the birthday of ' + name)
# 	else:
# 		print('I do not have birthday information for ' + name)
# 		print('What is their birthday?')
# 		bday = input()
# 		birthdays[name] = bday
# 		print('Birthday database updated.')
# from collections import Counter
# message = 'It was a bright cold day in AprIl, and the clocks were striking thirteen.'
# count = {}
# for character in message:
# 	count.setdefault(character, 0)
# 	count[character] = count[character] + 1
# print(count)
# # print Counter(message)

# allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
# 'Bob': {'ham sandwiches': 3, 'apples': 2},
# 'Carol': {'cups': 3, 'apple pies': 1}}
# def totalBrought(guests, item):
# 	numBrought = 0
# 	for k, v in guests.items():
# 		print v,"v"
# 		numBrought = numBrought + v.get(item, 0)
# 	return numBrought
# print('Number of things being brought:')
# print(' - Apples' + str(totalBrought(allGuests,'apples')))
# print(' - Cups' + str(totalBrought(allGuests,'cups')))
# print(' - Cakes' + str(totalBrought(allGuests,'cakes')))
# print(' - Ham Sandwiches ' + str(totalBrought(allGuests,'ham sandwiches')))
# print(' - Apple Pies' + str(totalBrought(allGuests,'apple pies')))


# def printPicnic(itemsDict, leftWidth, rightWidth):
# 	print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
# 	for k, v in itemsDict.items():
# 		print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))


# picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
# printPicnic(picnicItems, 12, 5)
# printPicnic(picnicItems, 20, 6)


# def squares1(p):
# 	return [a*a for a in p]
# def squares2(p):
# 	for each in p:
# 		yield each*each

# p=[1,2,3,4]
# y1=squares1(p)
# y2=squares2(p)
# y3=squares2(p)

# for s1 in y1:
# 	print s1 '''1,4,9,16'''

# print('---------')

# for s2 in y2:
# 	print s2 '''generator object'''

# print('---------')

# for s3 in y1:
# 	print s3 '''1,4,9,16'''

# print('---------')

# for s4 in y2:
# 	print s4, '''1'''



# with open('/home/user/Downloads/latlon.bin','rb+') as f:
# 	print f.readlines()




# class A:
# 	name="Subhash"
# 	@staticmethod
# 	def getName():
# 		name
# 		if name is None:
			
# 			print name
# 		else:
# 			print name
# 	@classmethod
# 	def getclassName(cls):
# 		print cls.name

# a=A()
# a.getclassName()
# a.getName()

import re
# phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
# pattern = phoneNumRegex.search('my number is 222-122-1244')
# print pattern.group()
# pateern_list = re.findall(r'\d{2}+-\d{2}-\d{2}+','my dob is 22-08-1994 and original is 1994-06-10')
# print pateern_list



# pattern = re.compile(r'\d\d-\d\d\d\d\d\d\d\d\d\d')
# (?# pattern = re.compile(r'\d{2}-\d{10}'))
# pattern = re.compile(r'(\d{2}-)?\d{10}')
# res = pattern.search('my mobile number is 91-9642286149 tyrtyrtyrtyrty')
# res = pattern.search('my mobile number is 9642286149 tyrtyrtyrtyrty')
# print res.group()
# pattern = re.compile(r'Sub(h)?ash'))
# pattern = pattern = re.compile(r'Sub(hhhh)*')

# r1=pattern.search('my name is Subhash')
# r2=pattern.search('my name is Subash')
# r3 = pattern.search('my name is Subhhhhash')

# print r1.group(),r2.group()	
# print r3.group()


# p1 = re.compile(r'\d+\s\w+$')
# r1 = p1.findall('ssf 12 ffdsfsd 1 dssfdfdsf 14 dfsdfsdfsdf dsfsdfsdfsdsfd 1 1 1 4 23')
# print r1
# # a = r1[4]
# # print a,type(a)
# endsWithNumber = re.compile(r'\d$')
# a = endsWithNumber.search('Your number is 42')
# print a,a.group()

# p2 = re.compile(r'.at')
# p3 = re.compile(r'.*',re.DOTALL)
# r2 = p3.search('adadas at the \ncat bart bat mat dort rat')
# print r2.group()

# a = re.findall(r'sf',"sfsdfsdsdfsdf 3 sdsdfdf 3 SF SDFSDFSDF ASASASSFFF" ,re.I)
# print a

# Replacing a string in regular expression

# a=re.sub(r'ba(\w)\w*','**','Subash')
# print a

# agentNamesRegex = re.compile(r'Agent (\w)\w*')
# a = agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
# print a

# mobile_pattern = r'^[6-9][0-9]+'
# a= re.findall(r'[6-9][0-9]{9}','my mobile number is 9642286148 and im having a mobile number 6302431362 and 7887123457 dfsdfjsdfsdf 6765435678 dfsdfsdf 5421234567')
# print a

# class Sample:
# 	def __new__():
# 		print "benfore __init__"
# 		inst = object.__new__(cls)
#     return inst
# 	def __init__(self):
# 		print "In __init__"


# s=Sample()

# def product(a,b):
#     print a*b

# def product(a,b,c):
#     print a*b*c

# product(1,5)

# from collections import defaultdict

# d=defaultdict(list)
# print d
# for i,j in [('a',(1,2)),('b',(3,4)),('c',(5,6))]:
#     d[i].append(j)
# print d


# class A:
#     def a(name):
#         print name

#     @staticmethod
#     def get_age(age):
#         print age


# obj=A()
# obj.a()
# A.get_age(25)


# def func(start=None,end=None,skip=None):
#     if end==None and skip==None:
#         end,start = start,0
#     while end>start:
#         print start
#         if skip is not None:
#             start +=skip
#         else:
#             start+=1
# func(1,10,3)


# from math import pow
# class complex:
#     def __init__(self, real, imag):
#         self.real = real
#         self.imag = imag
#     def __add__(self, other):
#         return complex(self.real+other.real, self.imag+other.imag)
#     def __sub__(self, other):
#         return complex(self.real-other.real, self.imag-other.imag)
#     def __mul__(self, other):
#         return complex(self.real*other.real-self.imag*other.imag, self.real*other.imag+self.imag*other.real)
#     def __div__(self, other):
#         try: 
#             return self.__mul__(complex(other.real, -1*other.imag)).__mul__(complex(1.0/(other.mod().real)**2, 0))
#         except ZeroDivisionError as e:
#             print e
#             return None
#     def mod(self):
#         return complex(pow(self.real**2+self.imag**2, 0.5), 0)
#     def __str__(self, precision=2):
#         return str(("%."+"%df"%precision)%float(self.real))+('+' if self.imag>=0 else '-')+str(("%."+"%df"%precision)%float(abs(self.imag)))+'i'

    
# A = complex(*map(float, raw_input().strip().split()))
# B = complex(*map(float, raw_input().strip().split()))

# print A+B
# print A-B
# print A*B
# print A/B
# print A.mod()
# print B.mod()


# Complex number  addition
# class Complex:
#     def __init__(self,real,img):
#         self.real = real
#         self.img = img
#     def __add__(self,other):
#         return Complex(self.real+other.real , self.img+other.img)

#     def __repr__(self):
#         return str(self.real) +'+'+ str(self.img) +'j'
#     def __str__(self):  
#         return str(self.real) +'+'+ str(self.img) +'j'


# c=Complex(2,3)
# d = Complex(3,2)
# # print c+d
# print Complex(3,5).__add__(Complex(5,3))


# str1=""
# name="Subhash"
# for each in name:
#     str1=each+str1
# if str1==name:
#     print True
# else:
#     print False

# a = 1
# def func1():
#     a = 2
#     print(a)
#     def func2():
#         nonlocal a
#         a=3
#         print(a)
#     func2()
#     print(a)
# func1()
# print(a)

l=[1,2,4,6,1,2,4,6,6,1,2,1]
for each in l:
    if l.count(each)>=2 and l.count(each)<=4:
        print each
    elif l.count(each)>=4:
        print each,"4"