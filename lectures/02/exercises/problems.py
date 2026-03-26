
"""Lecture 02 exercises (classes) - implement from scratch.
Any 14 / 16 problems solved count as 100%
"""

"""
1) Create class User with:
    name,
    method say_hi() which prints "Hello, I am {name}"
    """

class User:
  def __init__(self, name):
    self.name = name 
  
  def say_hi(self):
    return f"Hello, I'am {self.name}"
    
u1 = User("Togzhan")
u1.say_hi()
    
"""
2) BankAccount
Create class `BankAccount` with:
- `__init__(self, owner: str, balance: float = 0.0) -> None`
- `deposit(self, amount: float) -> None`
- `withdraw(self, amount: float) -> None`
Rules:
- Initial negative balance becomes `0.0`.
- Non-positive `deposit`/`withdraw` amounts are ignored.
- `withdraw` bigger than current balance is ignored.
"""

class BankAccount:
  def __init__(self, owner: str, balance: float = 0.0)-> None:
    self.owner = owner
    self.balance = balance if balance >0 else 0.0
  
  def deposite(self, amount: float) -> None:
    if amount > 0:
      self.balance += amount
    
  def withfdraw(self, amount: float) -> None:
    if 0 < amount < self.balance:
      self.balance  -= amount 
  
  


"""
3) Team
Create class `Team` with:
- `__init__(self) -> None`
- `add(self, name: str) -> None`
- `__len__(self) -> int`
Rules:
- Members are stored in insertion order.
- Each instance has independent member storage.
"""

class Team:
  def __init__(self):
    self.list1 = []
    
  def add(self, name:str):
    self.list1.append(name)
  
  def  __len__(self):
    return len(self.list1)
    
    
    
    


""" (Advanced, optional)
5) QueueState
Create class `QueueState`:
- `__init__(self) -> None` (initialize empty `items` list)
Methods:
- `push(self, item: str) -> None`
- `pop(self) -> str | None`
Rules:
- FIFO behavior.
- `pop` returns `None` when empty.
"""
class QueueState:
  def __init__(self):
    self.items = []
    
  def push(self, item :str):
    self.items.append(item)
    
  def pop(self):
    self.items.pop(0)
    
    



""" (Advanced, optional)
6) Wallet + custom errors
Create:
- `class PaymentError(Exception): ...`
- `class InsufficientFunds(PaymentError): ...`
- `class Wallet` with:
  - `__init__(self, balance: float = 0.0) -> None`
  - `top_up(self, amount: float) -> None`
  - `pay(self, amount: float) -> None`
Rules:
- Initial balance must be >= 0.
- `top_up` and `pay` require amount > 0.
- If `pay` exceeds balance, raise `InsufficientFunds`.
"""


  
  
  


"""
7) ShoppingCart
Create class `ShoppingCart` with:
- `__init__(self) -> None`
- `add_item(self, name: str, price: float, qty: int = 1) -> None`
- `total_items(self) -> int`
- `total_price(self) -> float`
Rules:
- `price < 0` or `qty <= 0` items are ignored.
- `repr` must include `ShoppingCart`.
"""
class ShoppingCart:
  def __init__(self):
    self.lst = []
    
  def add_item(self, name: str, price: float, qty: int = 1):
    if price <0 or qty <= 0:
      return
    else:
      self.lst.append((name, price, qty))
    
  def total_items(self):
    total = 0
    for name, price, qty in self.lst:
       total += qty
    return total 
       
      
  def total_price(self):
    total = 0
    for name, price, qty in self.lst:
      total += price * qty
    return total
  
  def __repr__(self):
     return f"ShoppingCart {self.lst} "
  
    
    
        
      
    

"""
8) Classroom (class attribute)
Create class `Classroom` with class attribute:
- `school_name = "Harbour Space"`
Methods:
- `__init__(self, group_name: str) -> None`
- `add_student(self, name: str) -> None`
- `__len__(self) -> int`
- `set_school_name(self, new_name: str) -> None`
Rules:
- `set_school_name` must update shared class attribute for all instances.
"""

class Classroom:
  school_name = "Harbour Space"
  
  def __init__(self, group_name:str):
    self.group_name = group_name
    self.items = []
  
  def add_student(self, name: str):
    self.items.append(name)
  
  def __len__(self):
    return len(self.items)
  
  def set_school_name(self, new_name:str):
    Classroom.school_name = new_name
    
    
    
"""
9) Rectangle
Create class `Rectangle` with:
- `__init__(self, width: float, height: float) -> None`
- `area(self) -> float`
- `perimeter(self) -> float`
Rules:
- Store positive dimensions using absolute values.
"""
class Rectangle:
  def __init__(self, width: float, height: float):
    self.width = abs(width) 
    self.height = abs(height)
    
  def area(self):
    return self.width * self.height
    
  
  def perimeter(self):
   return 2*(self.width + self.height)
  
  
  
    
    
    

"""
10) Playlist
Create class `Playlist` with:
- `__init__(self) -> None`
- `add(self, song: str) -> None`
- `__len__(self) -> int`
- `__iter__(self)`
- `__contains__(self, song: str) -> bool`
Rules:
- Preserve insertion order.
"""

class Playlist:
  def __init__(self):
    self.items = []
    
  def add(self, song:str):
    self.items.append(song)
    
  def __len__(self):
    return len(self.items)
  
  def __iter__(self):
    return iter(self.items)
  
  def __contains__(self, song: str):
    return song in self.items
    


"""
11) Product
Create class `Product` with:
- `__init__(self, name: str, price: float) -> None`
- `get_price(self) -> float`
- `set_price(self, value: float) -> None`
- `apply_discount(self, percent: float) -> None`
Rules:
- Negative price is clamped to `0`.
- Discount percent is clamped to `[0, 100]`.
"""
class Product:
  def __init__(self, name:str, price: float):
    self.name = name
    self.price = price if price > 0 else 0
  
  def get_price(self):
    return self.price
  
  def set_price(self, value: float):
    return value if value > 0 else 0
  
  def apply_discount(self, percent: float):
    if percent <0:
      percent = 0
    elif percent >100:
      percent = 100
    self.price *=  (1 - percent %100)
      
    
    

"""
12) Person + Student (inheritance)
Create:
- `class Person` with `__init__(name)` and `describe()`
- `class Student(Person)` with `__init__(name, group)` and overridden `describe()`
Required format:
- `Person(name=Ana)`
- `Student(name=Bo, group=G2)`
"""

class Person:
  def __init__(self, name):
    self.name = name
  def describe(self):
    return 
  
class Student(Person):
  def __init__(self, name, group):
    self.name = name
    self.group = group
    
  def describe(self):
    return
  
p1 = Person("Anna")
p2 = Student("Anna" "G2")
    
    





"""
13) Point2D (magic methods)
Create class `Point2D` with:
- `__init__(self, x: float, y: float) -> None`
- `distance_to(self, other: "Point2D") -> float`
- `__eq__(self, other: object) -> bool`
Rules:
- Euclidean distance.
- `repr` format: `Point2D(x, y)`.
"""
import math
class Point2D:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  
  def distance_to(self, other:object):
    return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)

  def __eq__(self, other:object):
    return isinstance(other, Point2D) and self.x == other.x and self.y== other
      

"""
14) Inventory
Create class `Inventory` with:
- `__init__(self) -> None`
- `add(self, name: str, qty: int = 1) -> None`
- `remove(self, name: str, qty: int = 1) -> None`
- `count(self, name: str) -> int`
- `__contains__(self, name: str) -> bool`
- `__len__(self) -> int`
Rules:
- Non-positive `qty` is ignored.
- Removing too much removes item completely (count becomes `0`).
"""
class Inventory:
  def __init__(self):
    self.items = {}
    
  def add(self, name:str, qty:int = 1):
    if qty <=0:
      return
    self.items[name] = self.items.get(name, 0) + qty
    
  def remove(self, name:str, qty: int = 1):
    if qty  <= 0 or name not in self.items:
      return
    if qty >= self.items[name]:
      del self.items[name]
    else:
      self.items[name] -= qty
      
  def count(self, name:str):
    return self.items.get(name, 0)
  
  def __contains__(self, name:str):
    return name in self.items
  
  def __len__(self):
    return len(self.items)
    

"""
15) CourseCatalog
Create class `CourseCatalog` with:
- `__init__(self) -> None`
- `add_course(self, code: str, title: str) -> None`
- `get_title(self, code: str) -> str | None`
- `__iter__(self)` returning `(code, title)` sorted by code
- `__len__(self) -> int`
"""
class CourseCatalog:
  def __init__(self):
    self.items = {}
    
  def add_course(self, code : str, title: str):
    self.items[code] = title
    
  def get_title(self, code:str):
    self.items.get(code)
    
  def __iter__(self):
    return iter(self.items)
  
  def __len__(self):
    return len(self.items)
    
    
    
    

"""
16) DefaultDict (magic methods)
Create class `DefaultDict` with:
- `__init__(self, default_factory=None) -> None`
- `__getitem__(self, key)`
- `__setitem__(self, key, value) -> None`
- `__contains__(self, key) -> bool`
- `__len__(self) -> int`
Rules:
- On missing key:
  - if `default_factory` is `None`, return `None`.
  - otherwise create value using `default_factory()`, store, return.
- If `default_factory` is not callable, treat it as `None`.
"""
class DefaultDict:
  def __init__(self, default_factory= None):
   self.items = {}
   if default_factory == "None":
     return
   
  def _getitem__(self, key):
    return self.items[key]
  
  


