#welcome



# creating a project where we understand python and oop
# class=blueeprint
# methods=functions
# attrbutes=variable
# object=instance of a class
# inheritance = inherit a property of a class by another class
# composition = building complex object

#under standing data class
#automate the class which only holds the data


from dataclasses import dataclass , field
import random
def price_func():
        return float(random.randrange(20,40))

@dataclass(frozen=True)#so with the help of this you can fix the value of the attribute 
class book:
        title :str = "No title"
        author :str = "no author"
        pages : int = 0
        price :int = field(default_factory=price_func)

        #def __post_init__(self):
         #       self.description =f"{self.title} by {self.title} , {self.pages}"



b1 = book()

#b2 = book("ahd" , "kd" , "999" , "9")

#print(b1)
#print(b2)
print(b1.author)
#print(b1.description)
#print(b1.__post_init__())

print((b1.price))





















#part 5

#magic function of python
#__str__ __repr__
# class book:
#     def __init__(self,title , auther , price):
#         super().__init__()
#         self.title = title
#         self.auther = auther
#         self.price = price
#
#     #use the __str__ method to return the string
#     def __str__(self):
#         return f"{self.title} by {self.auther} costs {self.price}"
#     #use the __Repr method to return an obj reprsentation
#     def __repr__(self):
#         return f"{self.title} by {self.auther} costs {self.price}"
#
# b1 = book("War and peace" , "Leo Tolstoy" , 39.2)
#
# print(b1)
# print(str(b1))
# print(repr(b1))
#























#using abstract and base class together
# #part 4
# #multiple inheritance
# class c:
#     def __init__(self):
#         super().__init__()
#         self.foo = "foo"
#         self.name = "class A"
#
# class b:
#     def __init__(self):
#         super().__init__()
#         self.bar = "bar"
#         self.name = "class B"
#
# class a(c,b):
#     def __int__(self):
#         super().__int__()
#
#     def superprops(self):
#         print(self.foo)
#         print(self.bar)
#         print(self.name)#here only class c gets printed becoz c is first parametere
#
# d = a()
# d.superprops()
#




















#part 3 lets us understand inheritance
#
# class publication:
#     def __init__(self,title,price):
#         self.title = title
#         self.price = price
#
# class periodical(publication):
#     def __init__(self,title,price,period,publisher):
#         super().__init__(title,price)
#         self.period = period
#         self.publisher = publisher
#
#
# class book(publication):
#     def __init__(self,title,auther,pages,price):
#         super().__init__(title,price)
#         # self.title = title
#         self.auther = auther
#         #self.price = price
#         self.pages = pages
#
# class magzine(periodical):
#     def __init__(self,title,publisher,price,period):
#         super().__init__(title,publisher,price,period)
#         # self.title = title
#         # self.publisher = publisher
#         # self.price = price
#         # self.period = period
#
# class newspaper(periodical):
#     def __init__(self,title,publisher,price,period):
#         super().__init__(title,publisher,price,period)
#         self.title = title
#         self.publisher = publisher
#         self.price = price
#         self.period = period
#
#
#
# b1 = book("money" , "kd" , "999" , "3333")
# n1 = newspaper("toi" , "toii" , "5" , 'daily')
# m1 = magzine("et" , "ett" , "50" , "monthly")
#
#
# print(b1.title)
# print(b1.auther)
# print(m1.title)
# print(m1.price)
# print(n1.price)
# print(n1.title)
#
























#this was all about decoraters
#
# class book:
#
#     BOOK_TYPE =  ("HARDCOVER" , "EBOOK")
#   #STATIC METHOD
#
#   #CLASS METHOD
#     @classmethod
#     def getbooktypes(cls):
#         return cls.BOOK_TYPE
#
#
#
#     def setTitle(self,newtitle):
#         self.title = newtitle
#
#     def __init__(self,title,booktype):
#         self.title =  title
#         if(not booktype in book.BOOK_TYPE):
#             raise ValueError(f"{booktype} is not a valid booktype")
#         else:
#             self.booktype = booktype
#
#
# print("booktypes:" , book.getbooktypes())
# b1 = book("Title 1" , "HARDCOVER" )





















#part 2 start
# class
# class book:
#       def __init__(self,title):
#           self.title = title
# class newspaper:
#     def __init__(self,name):
#         self.name = name
#
#
#
# b1 = book("war and peace")
# b2 = book("name book")
# n1 = newspaper("toi")
# n2 =  newspaper("et")
#
# #lets use type functions
# #useful for comparing two objects
#
# print(type(b1))
# print(type(n2))
#
# #lets compare
# print(type(b1)==type(b2))
# print(type(b1)==type(n1))
# print("----------")
# #understanding isinstance function
# print(isinstance(b1 , book))
# print(isinstance(n1 , newspaper))
# print(isinstance(n2 , book))
# print(isinstance(b1 , object))
#part 2 end







#part 1
# class book:
# #init function act as a initilizer and it is used to specify attributes of a class
# #it is some what like a constructor
# def __init__(self, title,auther , pagecount , price): #method 1 # initilizer function
# self.title = title
# self.auther = auther            #instance atrributes
# self.pagecount = pagecount
# self.price = price
# self.__secret="this attribute cant be accessed by sub class or outside "
#
# def getprice(self):
# return self.price
# #creating a class named newspaper
# class newspaper:
# def __init__(self,name):
# self.name=name
#

#at the very basics we are printing the attribute information in a class by creating a object
# b1 = book("Brave New World","ketan","1001","999")
# print(b1)
# print("title =" , b1.title)
# print("auther = " , b1.auther)
# print("pagecout = " , b1.pagecount)
# print("price = " , b1.price)
# print(b1.getprice())
# print(b1.__secret)