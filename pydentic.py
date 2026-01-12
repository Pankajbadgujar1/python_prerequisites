'''

Pydantic 
Pydantic is the most widely used data validation library for Python.

Fast and extensible, Pydantic plays nicely with your linters/IDE/brain. Define how data should be in pure, canonical Python 3.9+; validate it with Pydantic.


Why use Pydantic?
Powered by type hints — with Pydantic, schema validation and serialization are controlled by type annotations;
 less to learn, less code to write, and integration with your IDE and static analysis tools

Speed — Pydantic's core validation logic is written in Rust. As a result, Pydantic is among the fastest data validation libraries for Python.

JSON Schema — Pydantic models can emit JSON Schema, allowing for easy integration with other tools.

Strict and Lax mode — Pydantic can run in either strict mode (where data is not converted) or lax mode where Pydantic tries to coerce data to the correct type where appropriate. 

Dataclasses, TypedDicts and more — Pydantic supports validation of many standard library types including dataclass and TypedDict.

Customisation — Pydantic allows custom validators and serializers to alter how data is processed in many powerful ways.

Ecosystem — around 8,000 packages on PyPI use Pydantic, including massively popular libraries like FastAPI, huggingface, Django Ninja, SQLModel, & LangChain.

Battle tested — Pydantic is downloaded over 360M times/month and is used by all FAANG companies and 20 of the 25 largest companies on NASDAQ. If you're trying to do something with Pydantic, someone else has probably already done it.


'''
## Pydantic Basics : Creating and Using Models 
from pydantic import BaseModel

class Person(BaseModel):
    name:str
    age:int
    city:str

person = Person(name="pankaj",age=23,city="jalgaon")

print(person)

## Example 2
from pydantic import BaseModel
from typing import Optional
class Employee(BaseModel):
    id : int
    name: str
    department: str
    salary: Optional[float] = None #Optional with default value
    is_active:Optional[bool] = True # Optional with default True


emp = Employee(id=1, name="John", department="IT")
print(emp) 

# emp = Employee(id=1, name="John", department="IT", salary= 6000,is_active=False)
# print(emp)

'''
Defination : 
- Optional[type] : Indicates the filed can be None

- Default value = (None or True) : Makes the field optional

- Required fields must still be provided

- pydantic validates types even for optional fileds when values
'''


# Example 3
from pydantic import BaseModel
from typing import List

class Classroom(BaseModel):
    room_number : str
    students :List[str] # list of strings
    capacity : int
    
# Create a classroom
classroom = Classroom(
    room_number="101",
    students= ['ram','sita','lav','kush'],
    capacity=30
    )
print(classroom)

# Create a classroom with Tuple ## Atomatic typecasting is happend
classroom = Classroom(
    room_number="101",
    students= ('ram','sita','lav','kush'),
    capacity=30
    )
print(classroom)

# use of try Except
try:
    invalid_val=Classroom(room_number=34,students= ['ram','sita','lav','kush'],capacity=30)
except ValueError as e:
    print(e)


# Example 4 :  Model with Nested class
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    zip_code: int

class Customer(BaseModel):
    customer_id : int
    name : str
    address : Address # nested Address model

# create a customer with nested address 

customer  = Customer(
    customer_id=1,
    name="Pankaj",
    address={ "street":"123 main st",  "city":"Jalgoan",
              "zip_code":"12345"}
    )
print(customer)


# Example 5 of Field
from pydantic import BaseModel,Field
class Item(BaseModel):
    name:str=Field(min_lenght=2,max_length=50)
    price:float=Field(gt=0,le=1000) # greater that 0, less than or equal to 1000
    quantity:int=Field(ge=0)

# valid instance
item = Item(name="Book", price=456, quantity=10)

print(item)