# AirBnB clone
**Alx-HolbertonBnB** is a complete web application, integrating database storage, a back-end API, and front-end interfacing in a clone of AirBnB.

The project currently only implements the back-end console.

# Concepts
_For this project, we expect you to look at these concepts:_
* [Python packages](https://intranet.alxswe.com/concepts/66)
* [AirBnB clone](https://intranet.alxswe.com/concepts/74)

<br />
<details>
    <summary>Click to show/hide Content</summary><br />

# 1. Python packages
Read: [Packages](https://docs.python.org/3.4/tutorial/modules.html#packages)

A Python file can be a **module** but when this file is in a folder, we call this folder a **package**.

File organization is really important in a big project. This means for Python: packages everywhere.

## Compare with C
(file organization, not prototype vs code etc.)

In C: `#include "abs.h"`

In Python:
```groovy
import abs
abs.my_abs(89)
```
or
```groovy
from abs import my_abs
my_abs(89)
```
In C: `#include "my_math/abs.h"`

In Python:
```groovy
from my_math.abs import my_abs
my_abs(89)
```
or
```groovy
import my_math.abs
my_math.abs.my_abs(89)
```

## Dotted module names == Path
Let’s take this example of file organization:
```groovy
my_script.py
my_math/
    abs.py
```
How can I use my function `my_abs(a)` from the file `abs.py` in `my_script.py`?
* `import my_math/abs.py` => NO
* `import my_math/abs` => NO
* `import my_math.abs.py` => NO
* `import my_math.abs` => YES but you will use your function like that: `my_math.abs.my_abs(89)` => not friendly
* `from my_math.abs import my_abs` => YES YES YES! now you can use your function like that: `my_abs(89)`

Wait, does this really work?

NO! something is missing: the magic file `__init__.py`

Indeed, each folder must contain this file to be considered a package.

This file should be empty except if you want to import all the content of modules by using `*`.

More complicated?
```groovy
my_script.py
my_math/
    __init__.py
    abs.py
    functions/
        __init__.py
        add.py
```
How can I use my function `my_add(a, b)` from the file `add.py` in `my_script.py`?

`from my_math.functions.add import my_add`

Easy right?

**`import *` is dangerous**

Using `import *` is still considered bad practice in production code. In that case, `__init__.py` shouldn’t be empty but must contain the list of modules to load:
```groovy
my_script.py
my_math/
    __init__.py
    abs.py
    functions/
        __init__.py
        add.py
        sub.py
        mul.py
        div.py
```
```groovy
$ cat my_script.py
from my_math.functions import *
print(add.my_add(1, 3))
print(mul.my_mul(4, 2))
print(div.my_div(10, 2))

$ cat my_math/__init__.py  # empty file
$ cat my_math/functions/__init__.py
__all__ = ["add", "mul"]

$ python3 my_script.py
3
8
Traceback (most recent call last):
  File "my_script.py", line 4, in <module>
    print(div.my_div(10, 2))
NameError: name 'div' is not defined
$
```
## Relative versus Absolute import
In this example:
```groovy
my_script.py
my_math/
    __init__.py
    abs.py
    positive.py
```
`positive.py` contains one function `def is_positive(n)` and this function uses `my_abs(n)`. How it’s possible?

By importing: `from my_math.abs import my_abs` or `from abs import my_abs`

What the difference?
* `from abs import my_abs` is using a relative path between your file who imports and the module to import
* `from my_math.abs import my_abs` is using an absolute path between the file you execute and the module to import
```groovy
$ cat my_script.py
from my_math.positive import is_positive
print(is_positive(89))
print(is_positive(-89))
print(is_positive(333))

$ python3 my_script.py
True
False
True
$
```
Now, let’s execute a file in `my_math`:
```groovy
$ cd my_math ; cat test_positive.py
from positive import is_positive
print(is_positive(89))
print(is_positive(-89))
print(is_positive(333))

$ cat positive.py
from my_math.abs import my_abs

def is_positive(n):
    return my_abs(n) == n

$ python3 test_positive.py
Traceback (most recent call last):
  File "test_positive.py", line 1, in <module>
    from positive import is_positive
  File "/vagrant/my_math/positive.py", line 1, in <module>
    from my_math.abs import my_abs
ImportError: No module named 'my_math'
$
```
Ahh! If you are using an absolute path, you can’t execute this module from another point as the “root” of your project.

Let’s change to relative path:
```groovy
$ cd my_math ; cat test_positive.py
from positive import is_positive
print(is_positive(89))
print(is_positive(-89))
print(is_positive(333))

$ cat positive.py
from abs import my_abs

def is_positive(n):
    return my_abs(n) == n

$ python3 test_positive.py
True
False
True
$
```

<br />
<hr /><br />

# 2. AirBnB clone

![65f4a1dd9c51265f49d0](https://github.com/elyse502/AirBnB_clone/assets/125453474/acf08a8b-f4e4-47b6-b32e-25d73c434b32)

I know you were waiting for it: it’s here!

The AirBnB clone project starts now until… the end of the first year. The goal of the project is to deploy on your server a simple copy of the [AirBnB website](https://www.airbnb.com/).

You won’t implement all the features, only some of them to cover all fundamental concepts of the higher level programming track.

After 4 months, you will have a complete web application composed by:
* A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
* A website (the front-end) that shows the final product to everybody: static and dynamic
* A database or files that store data (data = objects)
* An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

## Final product

![fe2e3e7701dec72ce612472dab9bb55fe0e9f6d4](https://github.com/elyse502/AirBnB_clone/assets/125453474/25b2713a-ff3d-496e-ac61-c82173a11825)


![da2584da58f1d99a72f0a4d8d22c1e485468f941](https://github.com/elyse502/AirBnB_clone/assets/125453474/1841b787-c8af-49b4-9c5e-dab0a5633846)

## Concepts to learn
* [Unittest](https://docs.python.org/3.4/library/unittest.html#module-unittest) - and please work all together on tests cases
* **Python packages** concept page
* Serialization/Deserialization
* `*args, **kwargs`
* `datetime`
* More coming soon!

## Steps
You won’t build this application all at once, but step by step.

Each step will link to a concept:

## The console
* create your data model
* manage (create, update, destroy, etc) objects via a console / command interpreter
* store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine

![815046647d23428a14ca](https://github.com/elyse502/AirBnB_clone/assets/125453474/10c12086-2708-4322-b6b4-a3df7a66123b)

## Web static
* learn HTML/CSS
* create the HTML of your application
* create template of each object

![87c01524ada6080f40fc](https://github.com/elyse502/AirBnB_clone/assets/125453474/704ad78d-053c-4c30-bedc-3d87b19ebc69)

## MySQL storage
* replace the file storage by a Database storage
* map your models to a table in database by using an O.R.M.

![5284383714459fa68841](https://github.com/elyse502/AirBnB_clone/assets/125453474/f492838c-4d2a-4a75-8324-cc903634c361)

## Web framework - templating
* create your first web server in Python
* make your static HTML file dynamic by using objects stored in a file or database

![cb778ec8a13acecb53ef](https://github.com/elyse502/AirBnB_clone/assets/125453474/e801f00d-ced0-42ce-9bfc-acd1c2273f3e)

## RESTful API
* expose all your objects stored via a JSON web interface
* manipulate your objects via a RESTful API

![06fccc41df40ab8f9d49](https://github.com/elyse502/AirBnB_clone/assets/125453474/d0515e05-f4b0-44a7-bbbc-f7ad7ecc159f)

## Web dynamic
* learn JQuery
* load objects from the client side by using your own RESTful API

![d2d06462824fab5846f3](https://github.com/elyse502/AirBnB_clone/assets/125453474/50a350bb-2492-4701-a198-ef284721d971)

## Files and Directories
* `models` directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
* `tests` directory will contain all unit tests.
* `console.py` file is the entry point of our command interpreter.
* `models/base_model.py` file is the base class of all our models. It contains common elements:
    * attributes: `id`, `created_at` and `updated_at`
    * methods: `save()` and `to_json()`
* `models/engine` directory will contain all storage classes (using the same prototype). For the moment you will have only one: `file_storage.py`.

## Storage
Persistency is really important for a web application. It means: every time your program is executed, it starts with all objects previously created from another execution. Without persistency, all the work done in a previous execution won’t be saved and will be gone.

In this project, you will manipulate 2 types of storage: file and database. For the moment, you will focus on file.

Why separate “storage management” from “model”? It’s to make your models modular and independent. With this architecture, you can easily replace your storage system without re-coding everything everywhere.

You will always use class attributes for any object. Why not instance attributes? For 3 reasons:
* Provide easy class description: everybody will be able to see quickly what a model should contain (which attributes, etc…)
* Provide default value of any attribute
* In the future, provide the same model behavior for file storage or database storage

## How can I store my instances?
That’s a good question. So let’s take a look at this code:
```groovy
class Student():
    def __init__(self, name):
        self.name = name

students = []
s = Student("John")
students.append(s)
```
Here, I’m creating a student and store it in a list. But after this program execution, my Student instance doesn’t exist anymore.
```groovy
class Student():
    def __init__(self, name):
        self.name = name

students = reload() # recreate the list of Student objects from a file
s = Student("John")
students.append(s)
save(students) # save all Student objects to a file
```
Nice!

But how it works?

First, let’s look at `save(students)`:
* Can I write each `Student` object to a file => _NO_, it will be the memory representation of the object. For another program execution, this memory representation can’t be reloaded.
* Can I write each `Student.name` to a file => _YES_, but imagine you have other attributes to describe `Student`? It would start to be become too complex.

The best solution is to convert this list of `Student` objects to a JSON representation.

Why JSON? Because it’s a standard representation of object. It allows us to share this data with other developers, be human readable, but mainly to be understood by another language/program.

Example:
* My Python program creates `Student` objects and saves them to a JSON file
* Another Javascript program can read this JSON file and manipulate its own `Student` class/representation

And the `reload()`? now you know the file is a JSON file representing all `Student` objects. So `reload()` has to read the file, parse the JSON string, and re-create `Student` objects based on this data-structure.

## File storage == JSON serialization
For this first step, you have to write in a file all your objects/instances created/updated in your command interpreter and restore them when you start it. You can’t store and restore a Python instance of a class as “Bytes”, the only way is to convert it to a serializable data structure:
* convert an instance to Python built in serializable data structure (list, dict, number and string) - for us it will be the method `my_instance.to_json()` to retrieve a dictionary
* convert this data structure to a string (JSON format, but it can be YAML, XML, CSV…) - for us it will be a `my_string = JSON.dumps(my_dict)`
* write this string to a file on disk

And the process of deserialization?

The same but in the other way:
* read a string from a file on disk
* convert this string to a data structure. This string is a JSON representation, so it’s easy to convert - for us it will be a `my_dict = JSON.loads(my_string)`
* convert this data structure to instance - for us it will be a `my_instance = MyObject(my_dict)`

### `*args, **kwargs`

#### [`How To Use them`](https://www.digitalocean.com/community/tutorials/how-to-use-args-and-kwargs-in-python-3)
How do you pass arguments to a function?
```groovy
def my_fct(param_1, param_2):
    ...

my_fct("Best", "School")
```
But with this function definition, you must call `my_fct` with 2 parameters, no more, no less.

Can it be dynamic? Yes you can:
```groovy
def my_fct(*args, **kwargs):
    ...

my_fct("Best", "School")
```
What? What’s `*args` and `**kwargs`?
* `*args` is a Tuple that contains all arguments
* `*kwargs` is a dictionary that contains all arguments by key/value

A dictionary? But why?

So, to make it clear, `*args` is the list of anonymous arguments, no name, just an order. `**kwargs` is the dictionary with all named arguments.

Examples:
```groovy
def my_fct(*args, **kwargs):
    print("{} - {}".format(args, kwargs))

my_fct() # () - {}
my_fct("Best") # ('Best',) - {}
my_fct("Best", 89) # ('Best', 89) - {}
my_fct(name="Best") # () - {'name': 'Best'}
my_fct(name="Best", number=89) # () - {'name': 'Best', 'number': 89}
my_fct("School", 12, name="Best", number=89) # ('School', 12) - {'name': 'Best', 'number': 89}
```
Perfect? Of course you can mix both, but the order should be first all anonymous arguments, and after named arguments.

Last example:
```groovy
def my_fct(*args, **kwargs):
    print("{} - {}".format(args, kwargs))

a_dict = { 'name': "Best", 'age': 89 }

my_fct(a_dict) # ({'age': 89, 'name': 'Best'},) - {}
my_fct(*a_dict) # ('age', 'name') - {}
my_fct(**a_dict) # () - {'age': 89, 'name': 'Best'}
```
You can play with these 2 arguments to clearly understand where and how your variables are stored.

### `datetime`
`datetime` is a Python module to manipulate date, time etc…

In this example, you create an instance of `datetime` with the current date and time:
```groovy
from datetime import datetime

date_now = datetime.now()
print(type(date_now)) # <class 'datetime.datetime'>
print(date_now) # 2017-06-08 20:42:42.170922
```
`date_now` is an object, so you can manipulate it:
```groovy
from datetime import timedelta

date_tomorrow = date_now + timedelta(days=1)
print(date_tomorrow) # 2017-06-09 20:42:42.170922
```
… you can also store it:
```groovy
a_dict = { 'my_date': date_now }
print(type(a_dict['my_date'])) # <class 'datetime.datetime'>
print(a_dict) # {'my_date': datetime.datetime(2017, 6, 8, 20, 42, 42, 170922)}
```
What? What’s this format when a `datetime` instance is in a datastructure??? It’s unreadable.

How to make it readable: [`strftime`](https://strftime.org/)
```groovy
print(date_now.strftime("%A")) # Thursday
print(date_now.strftime("%A %d %B %Y at %H:%M:%S")) # Thursday 08 June 2017 at 20:42:42
```
## Data diagram

![99e1a8f2be8c09d5ce5ac321e8cf39f0917f8db5](https://github.com/elyse502/AirBnB_clone/assets/125453474/3d7ad352-6e69-479b-be7c-96e850e0cb2c)

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br><br>
    
</details>

![65f4a1dd9c51265f49d0](https://github.com/elyse502/AirBnB_clone/assets/125453474/19069322-8089-4715-bdc2-6420b2e5f5b0)

# Background Context
### Welcome to the AirBnB clone project!
Before starting, please read the **AirBnB** concept page.

#### First step: Write a command interpreter to manage your AirBnB objects.
This is the first step towards building your first full web application: the **AirBnB clone**. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:
* put in place a parent class (called `BaseModel`) to take care of the initialization, serialization and deserialization of your future instances
* create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
* create all classes used for AirBnB (`User`, `State`, `City`, `Place`…) that inherit from `BaseModel`
* create the first abstracted storage engine of the project: File storage.
* create all unittests to validate all our classes and storage engine

## What’s a command interpreter?
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

# Resources🏗️
### Read or watch:
* [cmd module](https://docs.python.org/3.8/library/cmd.html)
* [cmd module in depth](http://pymotw.com/2/cmd/)
* **packages** concept page
* [uuid module](https://docs.python.org/3.8/library/uuid.html)
* [datetime](https://docs.python.org/3.8/library/datetime.html)
* [unittest module](https://docs.python.org/3.8/library/unittest.html#module-unittest)
* [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
* [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)
* [cmd module wiki page](https://wiki.python.org/moin/CmdModule)
* [python unittest](https://realpython.com/python-testing/)

# General
* How to create a Python package
* How to create a command interpreter in Python using the `cmd` module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage `datetime`
* What is an `UUID`
* What is `*args` and how to use it
* What is `**kwargs` and how to use it
* How to handle named arguments in a function

# Requirements
## Python Scripts
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version `2.8.*`)
* All your files must be executable
* The length of your files will be tested using `wc`
* All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
* All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## Python Unit Tests
* Allowed editors: `vi`, `vim`, `emacs`
* All your files should end with a new line
* All your test files should be inside a folder `tests`
* You have to use the [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
* All your test files should be python files (extension: `.py`)
* All your test files and folders should start by `test_`
* Your file organization in the tests folder should be the same as your project
* e.g., For `models/base_model.py`, unit tests must be in: `tests/test_models/test_base_model.py`
* e.g., For `models/user.py`, unit tests must be in: `tests/test_models/test_user.py`
* All your tests should be executed by using this command: `python3 -m unittest discover tests`
* You can also test file by file by using this command: `python3 -m unittest tests/test_models/test_base_model.py`
* All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
* All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
* We strongly encourage you to work together on test cases, so that you don’t miss any edge case

# More Info
## Execution
Your shell should work like this in interactive mode:
```groovy
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
But also in non-interactive mode: (like the Shell project in C)
```groovy
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
All tests should also pass in non-interactive mode: `$ echo "python3 -m unittest discover tests" | bash`

![815046647d23428a14ca](https://github.com/elyse502/AirBnB_clone/assets/125453474/850db2f3-a0e2-4c18-bb54-eb4a491705a0)

<br /><hr />

# Tasks📃
## 0. README, AUTHORS: [README.md](https://github.com/elyse502/AirBnB_clone/blob/master/README.md), [AUTHORS](https://github.com/elyse502/AirBnB_clone/blob/master/AUTHORS)
A `README.md`:
* description of the project
* description of the command interpreter:
    * how to start it
    * how to use it
    * examples
* You should have an `AUTHORS` file at the root of your repository, listing all individuals having contributed
* content to the repository. For format, reference [Docker’s AUTHORS page](https://github.com/moby/moby/blob/master/AUTHORS)
* You should use branches and pull requests on GitHub - it will help you as team to organize your work

---

## 1. Be pycodestyle compliant!: [AirBnB_clone](https://github.com/elyse502/AirBnB_clone)
A beautiful code that passes the pycodestyle checks.

---

## 2. Unittests: [tests/](https://github.com/elyse502/AirBnB_clone/tree/master/tests)
All your files, classes, functions must be tested with unit tests
```groovy
guillaume@ubuntu:~/AirBnB$ python3 -m unittest discover tests
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 189 tests in 13.135s

OK
guillaume@ubuntu:~/AirBnB$
```
_Note that this is just an example, the number of tests you create can be different from the above example._

**Warning**:

Unit tests must also pass in non-interactive mode:
```groovy
guillaume@ubuntu:~/AirBnB$ echo "python3 -m unittest discover tests" | bash
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 189 tests in 13.135s

OK
guillaume@ubuntu:~/AirBnB$
```

---

## 3. BaseModel: [models/base_model.py](https://github.com/elyse502/AirBnB_clone/blob/master/models/base_model.py), [models/__init__.py](https://github.com/elyse502/AirBnB_clone/blob/master/models/__init__.py), [tests/](https://github.com/elyse502/AirBnB_clone/tree/master/tests)
A class `BaseModel` that defines all common attributes/methods for other classes:
* `models/base_model.py`
* Public instance attributes:
    * `id`: string - assign with an `uuid` when an instance is created:
        * you can use `uuid.uuid4()` to generate unique `id` but don’t forget to convert to a string
        * the goal is to have unique `id` for each `BaseModel`
    * `created_at`: datetime - assign with the current datetime when an instance is created
    * `updated_at`: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object
* `__str__`: should print: `[<class name>] (<self.id>) <self.__dict__>`
* Public instance methods:
    * `save(self)`: updates the public instance attribute `updated_at` with the current datetime
    * `to_dict(self)`: returns a dictionary containing all keys/values of `__dict__` of the instance:
        * by using `self.__dict__`, only instance attributes set will be returned
        * a key `__class__` must be added to this dictionary with the class name of the object
        * `created_at` and `updated_at` must be converted to string object in ISO format:
            * format: `%Y-%m-%dT%H:%M:%S.%f` (ex: `2017-06-14T22:31:03.285259`)
            * you can use `isoformat()` of `datetime` object
        * This method will be the first piece of the serialization/deserialization process: create a dictionary representation with “simple object type” of our `BaseModel`
```groovy
guillaume@ubuntu:~/AirBnB$ cat test_base_model.py
#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

guillaume@ubuntu:~/AirBnB$ ./test_base_model.py
[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'my_number': 89, 'name': 'My First Model', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119434), 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}
[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'my_number': 89, 'name': 'My First Model', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119572), 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}
{'my_number': 89, 'name': 'My First Model', '__class__': 'BaseModel', 'updated_at': '2017-09-28T21:05:54.119572', 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': '2017-09-28T21:05:54.119427'}
JSON of my_model:
    my_number: (<class 'int'>) - 89
    name: (<class 'str'>) - My First Model
    __class__: (<class 'str'>) - BaseModel
    updated_at: (<class 'str'>) - 2017-09-28T21:05:54.119572
    id: (<class 'str'>) - b6a6e15c-c67d-4312-9a75-9d084935e579
    created_at: (<class 'str'>) - 2017-09-28T21:05:54.119427

guillaume@ubuntu:~/AirBnB$
```

---

## 4. Create BaseModel from dictionary: [models/base_model.py](https://github.com/elyse502/AirBnB_clone/blob/master/models/base_model.py), [tests/](https://github.com/elyse502/AirBnB_clone/tree/master/tests)
Previously we created a method to generate a dictionary representation of an instance (method to_dict()).

Now it’s time to re-create an instance with this dictionary representation.
```groovy
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>
```
Update `models/base_model.py`:

* `__init__(self, *args, **kwargs)`:
    * you will use `*args, **kwargs arguments` for the constructor of a `BaseModel`. (more information inside the AirBnB clone concept page)
    * `*args` won’t be used
    * if `kwargs` is not empty:
        * each key of this dictionary is an attribute name (Note `__class__` from `kwargs` is the only one that should not be added as an attribute. See the example output, below)
        * each value of this dictionary is the value of this attribute name
        * **Warning**: `created_at` and `updated_at` are strings in this dictionary, but inside your `BaseModel` instance is working with `datetime` object. You have to convert these strings into `datetime` object. Tip: you know the string format of these datetime
    * otherwise:
        * create `id` and `created_at` as you did previously (new instance)
```groovy
guillaume@ubuntu:~/AirBnB$ cat test_base_model_dict.py
#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)

guillaume@ubuntu:~/AirBnB$ ./test_base_model_dict.py
56d43177-cc5f-4d6c-a0c1-e167f8c27337
[BaseModel] (56d43177-cc5f-4d6c-a0c1-e167f8c27337) {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52298), 'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52302), 'name': 'My_First_Model'}
<class 'datetime.datetime'>
--
{'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': '2017-09-28T21:03:54.052298', '__class__': 'BaseModel', 'my_number': 89, 'updated_at': '2017-09-28T21:03:54.052302', 'name': 'My_First_Model'}
JSON of my_model:
    id: (<class 'str'>) - 56d43177-cc5f-4d6c-a0c1-e167f8c27337
    created_at: (<class 'str'>) - 2017-09-28T21:03:54.052298
    __class__: (<class 'str'>) - BaseModel
    my_number: (<class 'int'>) - 89
    updated_at: (<class 'str'>) - 2017-09-28T21:03:54.052302
    name: (<class 'str'>) - My_First_Model
--
56d43177-cc5f-4d6c-a0c1-e167f8c27337
[BaseModel] (56d43177-cc5f-4d6c-a0c1-e167f8c27337) {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52298), 'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52302), 'name': 'My_First_Model'}
<class 'datetime.datetime'>
--
False
guillaume@ubuntu:~/AirBnB$
```

---

## 5. Store first object: [models/engine/file_storage.py](https://github.com/elyse502/AirBnB_clone/blob/master/models/engine/file_storage.py), [models/engine/__init__.py](https://github.com/elyse502/AirBnB_clone/blob/master/models/engine/__init__.py), [models/__init__.py](https://github.com/elyse502/AirBnB_clone/blob/master/models/__init__.py), [models/base_model.py](https://github.com/elyse502/AirBnB_clone/blob/master/models/base_model.py), [tests/](https://github.com/elyse502/AirBnB_clone/tree/master/tests)
Now we can recreate a `BaseModel` from another one by using a dictionary representation:
```groovy
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>
```
It’s great but it’s still not persistent: every time you launch the program, you don’t restore all objects created before… The first way you will see here is to save these objects to a file.

Writing the dictionary representation to a file won’t be relevant:
* Python doesn’t know how to convert a string to a dictionary (easily)
* It’s not human readable
* Using this file with another program in Python or other language will be hard.

So, you will convert the dictionary representation to a JSON string. JSON is a standard representation of a data structure. With this format, humans can read and all programming languages have a JSON reader and writer.

Now the flow of serialization-deserialization will be:
```groovy
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump -> <class 'str'> -> FILE -> <class 'str'> -> JSON load -> <class 'dict'> -> <class 'BaseModel'>
```
Magic right?

Terms:
* **simple Python data structure**: Dictionaries, arrays, number and string. ex: `{ '12': { 'numbers': [1, 2, 3], 'name': "John" } }`
* **JSON string representation**: String representing a simple data structure in JSON format. ex: `'{ "12": { "numbers": [1, 2, 3], "name": "John" } }'`

Write a class `FileStorage` that serializes instances to a JSON file and deserializes JSON file to instances:
* `models/engine/file_storage.py`
* Private class attributes:
    * `__file_path`: string - path to the JSON file (ex: `file.json`)
    * `__objects`: dictionary - empty but will store all objects by `<class name>.id` (ex: to store a `BaseModel` object with `id=12121212`, the key will be `BaseModel.12121212`)
* Public instance methods:
    * `all(self)`: returns the dictionary `__objects`
    * `new(self, obj)`: sets in `__objects` the `obj` with key `<obj class name>.id`
    * `save(self)`: serializes `__objects` to the JSON file (path: `__file_path`)
    * `reload(self)`: deserializes the JSON file to `__objects` (only if the JSON file (`__file_path`) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)

Update `models/__init__.py`: to create a unique `FileStorage` instance for your application
* import `file_storage.py`
* create the variable `storage`, an instance of `FileStorage`
* call `reload()` method on this variable

Update `models/base_model.py`: to link your `BaseModel` to `FileStorage` by using the variable `storage`
* import the variable `storage`
* in the method `save(self)`:
    * call `save(self)` method of `storage`
* `__init__(self, *args, **kwargs)`:
    * if it’s a new instance (not from a dictionary representation), add a call to the method `new(self)` on `storage`
```groovy
guillaume@ubuntu:~/AirBnB$ cat test_save_reload_base_model.py
#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)

guillaume@ubuntu:~/AirBnB$ cat file.json
cat: file.json: No such file or directory
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_base_model.py
-- Reloaded objects --
-- Create a new object --
[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47372), 'name': 'My_First_Model', 'id': 'ee49c413-023a-4b49-bd28-f2936c95460d'}
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ cat file.json ; echo ""
{"BaseModel.ee49c413-023a-4b49-bd28-f2936c95460d": {"my_number": 89, "__class__": "BaseModel", "updated_at": "2017-09-28T21:07:25.047381", "created_at": "2017-09-28T21:07:25.047372", "name": "My_First_Model", "id": "ee49c413-023a-4b49-bd28-f2936c95460d"}}
guillaume@ubuntu:~/AirBnB$
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_base_model.py
-- Reloaded objects --
[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {'name': 'My_First_Model', 'id': 'ee49c413-023a-4b49-bd28-f2936c95460d', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), 'my_number': 89, 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47372)}
-- Create a new object --
[BaseModel] (080cce84-c574-4230-b82a-9acb74ad5e8c) {'name': 'My_First_Model', 'id': '080cce84-c574-4230-b82a-9acb74ad5e8c', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973308), 'my_number': 89, 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973301)}
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_base_model.py
-- Reloaded objects --
[BaseModel] (080cce84-c574-4230-b82a-9acb74ad5e8c) {'id': '080cce84-c574-4230-b82a-9acb74ad5e8c', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973308), 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973301), 'name': 'My_First_Model', 'my_number': 89}
[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {'id': 'ee49c413-023a-4b49-bd28-f2936c95460d', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47372), 'name': 'My_First_Model', 'my_number': 89}
-- Create a new object --
[BaseModel] (e79e744a-55d4-45a3-b74a-ca5fae74e0e2) {'id': 'e79e744a-55d4-45a3-b74a-ca5fae74e0e2', 'updated_at': datetime.datetime(2017, 9, 28, 21, 8, 6, 151750), 'created_at': datetime.datetime(2017, 9, 28, 21, 8, 6, 151711), 'name': 'My_First_Model', 'my_number': 89}
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ cat file.json ; echo ""
{"BaseModel.e79e744a-55d4-45a3-b74a-ca5fae74e0e2": {"__class__": "BaseModel", "id": "e79e744a-55d4-45a3-b74a-ca5fae74e0e2", "updated_at": "2017-09-28T21:08:06.151750", "created_at": "2017-09-28T21:08:06.151711", "name": "My_First_Model", "my_number": 89}, "BaseModel.080cce84-c574-4230-b82a-9acb74ad5e8c": {"__class__": "BaseModel", "id": "080cce84-c574-4230-b82a-9acb74ad5e8c", "updated_at": "2017-09-28T21:07:51.973308", "created_at": "2017-09-28T21:07:51.973301", "name": "My_First_Model", "my_number": 89}, "BaseModel.ee49c413-023a-4b49-bd28-f2936c95460d": {"__class__": "BaseModel", "id": "ee49c413-023a-4b49-bd28-f2936c95460d", "updated_at": "2017-09-28T21:07:25.047381", "created_at": "2017-09-28T21:07:25.047372", "name": "My_First_Model", "my_number": 89}}
guillaume@ubuntu:~/AirBnB$
```

---

## 6. Console 0.0.1: [console.py](https://github.com/elyse502/AirBnB_clone/blob/master/console.py)
A program called `console.py` that contains the entry point of the command interpreter:
* You must use the module `cmd`
* Your class definition must be: class `HBNBCommand(cmd.Cmd):`
* Your command interpreter should implement:
    * `quit` and `EOF` to exit the program
    * `help` (this action is provided by default by `cmd` but you should keep it updated and documented as you work through tasks)
    * a custom prompt: `(hbnb)`
    * an empty line + `ENTER` shouldn’t execute anything
* Your code should not be executed when imported

### Warning:
You should end your file with:
```groovy
if __name__ == '__main__':
    HBNBCommand().cmdloop()
```
to make your program executable except when imported. Please don’t add anything around - the Checker won’t like it otherwise
```groovy
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) help quit
Quit command to exit the program

(hbnb) 
(hbnb) 
(hbnb) quit 
guillaume@ubuntu:~/AirBnB$ 
```
#### No unittests needed

---

## 7. Console 0.1: [console.py](https://github.com/elyse502/AirBnB_clone/blob/master/console.py)
Update your command interpreter (`console.py`) to have these commands:
* `create`: Creates a new instance of `BaseModel`, saves it (to the JSON file) and prints the `id`. Ex: `$ create BaseModel`
    * If the class name is missing, print `** class name missing **` (ex: `$ create`)
    * If the class name doesn’t exist, print `** class doesn't exist **` (ex: `$ create MyModel`)
* `show`: Prints the string representation of an instance based on the class name and `id`. Ex: `$ show BaseModel 1234-1234-1234`.
    * If the class name is missing, print `** class name missing **` (ex: `$ show`)
    * If the class name doesn’t exist, print `** class doesn't exist **` (ex: `$ show MyModel`)
    * If the `id` is missing, print `** instance id missing **` (ex: `$ show BaseModel`)
    * If the instance of the class name doesn’t exist for the `id`, print `** no instance found **` (ex: `$ show BaseModel 121212`)
* `destroy`: Deletes an instance based on the class name and `id` (save the change into the JSON file). Ex: `$ destroy BaseModel 1234-1234-1234`.
    * If the class name is missing, print `** class name missing **` (ex: `$ destroy`)
    * If the class name doesn’t exist, print `** class doesn't exist **` (ex:`$ destroy MyModel`)
    * If the `id` is missing, print `** instance id missing **` (ex: `$ destroy BaseModel`)
    * If the instance of the class name doesn’t exist for the `id`, print `** no instance found **` (ex: `$ destroy BaseModel 121212`)
* `all`: Prints all string representation of all instances based or not on the class name. Ex: $ all BaseModel or $ all.
    * The printed result must be a list of strings (like the example below)
    * If the class name doesn’t exist, print `** class doesn't exist **` (ex: `$ all MyModel`)
* `update`: Updates an instance based on the class name and `id` by adding or updating attribute (save the change into the JSON file). Ex: `$ update BaseModel 1234-1234-1234 email "aibnb@mail.com"`.
    * Usage: `update <class name> <id> <attribute name> "<attribute value>"`
    * Only one attribute can be updated at the time
    * You can assume the attribute name is valid (exists for this model)
    * The attribute value must be casted to the attribute type
    * If the class name is missing, print `** class name missing **` (ex: `$ update`)
    * If the class name doesn’t exist, print `** class doesn't exist **` (ex: `$ update MyModel`)
    * If the `id` is missing, print `** instance id missing **` (ex: `$ update BaseModel`)
    * If the instance of the class name doesn’t exist for the `id`, print `** no instance found **` (ex: `$ update BaseModel 121212`)
    * If the attribute name is missing, print `** attribute name missing **` (ex: `$ update BaseModel existing-id`)
    * If the value for the attribute name doesn’t exist, print `** value missing **` (ex: `$ update BaseModel existing-id first_name`)
    * All other arguments should not be used (Ex: `$ update BaseModel 1234-1234-1234 email "aibnb@mail.com" first_name "Betty"` = `$ update BaseModel 1234-1234-1234 email "aibnb@mail.com"`)
    * `id`, `created_at` and `updated_at` can't be updated. You can assume they won’t be passed in the `update` command
    * Only “simple” arguments can be updated: string, integer and float. You can assume nobody will try to update list of ids or datetime

Let’s add some rules:
* You can assume arguments are always in the right order
* Each arguments are separated by a space
* A string argument with a space must be between double quote
* The error management starts from the first argument to the last one
```groovy
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) all MyModel
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel My_First_Model
** no instance found **
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) destroy
** class name missing **
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
(hbnb) create BaseModel
2dd6ef5c-467c-4f82-9521-a772ea7d84e9
(hbnb) all BaseModel
["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(hbnb) 
```

---

## 8. First User: [models/user.py](https://github.com/elyse502/AirBnB_clone/blob/master/models/user.py), [models/engine/file_storage.py](https://github.com/elyse502/AirBnB_clone/blob/master/models/engine/file_storage.py), [console.py](https://github.com/elyse502/AirBnB_clone/blob/master/console.py), [tests/](https://github.com/elyse502/AirBnB_clone/tree/master/tests)
A class `User` that inherits from `BaseModel`:
* `models/user.py`
* Public class attributes:
    * `email`: string - empty string
    * `password`: string - empty string
    * `first_name`: string - empty string
    * `last_name`: string - empty string

Update `FileStorage` to manage correctly serialization and deserialization of `User`.

Update your command interpreter (`console.py`) to allow `show`, `create`, `destroy`, `update` and `all` used with `User`.
```groovy
guillaume@ubuntu:~/AirBnB$ cat test_save_reload_user.py
#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new User --")
my_user = User()
my_user.first_name = "Betty"
my_user.last_name = "Bar"
my_user.email = "airbnb@mail.com"
my_user.password = "root"
my_user.save()
print(my_user)

print("-- Create a new User 2 --")
my_user2 = User()
my_user2.first_name = "John"
my_user2.email = "airbnb2@mail.com"
my_user2.password = "root"
my_user2.save()
print(my_user2)

guillaume@ubuntu:~/AirBnB$ cat file.json ; echo ""
{"BaseModel.2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4": {"__class__": "BaseModel", "id": "2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4", "updated_at": "2017-09-28T21:11:14.333862", "created_at": "2017-09-28T21:11:14.333852"}, "BaseModel.a42ee380-c959-450e-ad29-c840a898cfce": {"__class__": "BaseModel", "id": "a42ee380-c959-450e-ad29-c840a898cfce", "updated_at": "2017-09-28T21:11:15.504296", "created_at": "2017-09-28T21:11:15.504287"}, "BaseModel.af9b4cbd-2ce1-4e6e-8259-f578097dd15f": {"__class__": "BaseModel", "id": "af9b4cbd-2ce1-4e6e-8259-f578097dd15f", "updated_at": "2017-09-28T21:11:12.971544", "created_at": "2017-09-28T21:11:12.971521"}, "BaseModel.38a22b25-ae9c-4fa9-9f94-59b3eb51bfba": {"__class__": "BaseModel", "id": "38a22b25-ae9c-4fa9-9f94-59b3eb51bfba", "updated_at": "2017-09-28T21:11:13.753347", "created_at": "2017-09-28T21:11:13.753337"}, "BaseModel.9bf17966-b092-4996-bd33-26a5353cccb4": {"__class__": "BaseModel", "id": "9bf17966-b092-4996-bd33-26a5353cccb4", "updated_at": "2017-09-28T21:11:14.963058", "created_at": "2017-09-28T21:11:14.963049"}}
guillaume@ubuntu:~/AirBnB$
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_user.py
-- Reloaded objects --
[BaseModel] (38a22b25-ae9c-4fa9-9f94-59b3eb51bfba) {'id': '38a22b25-ae9c-4fa9-9f94-59b3eb51bfba', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 13, 753337), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 13, 753347)}
[BaseModel] (9bf17966-b092-4996-bd33-26a5353cccb4) {'id': '9bf17966-b092-4996-bd33-26a5353cccb4', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 963049), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 963058)}
[BaseModel] (2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4) {'id': '2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 333852), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 333862)}
[BaseModel] (a42ee380-c959-450e-ad29-c840a898cfce) {'id': 'a42ee380-c959-450e-ad29-c840a898cfce', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 15, 504287), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 15, 504296)}
[BaseModel] (af9b4cbd-2ce1-4e6e-8259-f578097dd15f) {'id': 'af9b4cbd-2ce1-4e6e-8259-f578097dd15f', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 12, 971521), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 12, 971544)}
-- Create a new User --
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'id': '38f22813-2753-4d42-b37c-57a17f1e4f88', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), 'email': 'airbnb@mail.com', 'first_name': 'Betty', 'last_name': 'Bar', 'password': 'root'}
-- Create a new User 2 --
[User] (d0ef8146-4664-4de5-8e89-096d667b728e) {'id': 'd0ef8146-4664-4de5-8e89-096d667b728e', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848280), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848294), 'email': 'airbnb2@mail.com', 'first_name': 'John', 'password': 'root'}
guillaume@ubuntu:~/AirBnB$
guillaume@ubuntu:~/AirBnB$ cat file.json ; echo ""
{"BaseModel.af9b4cbd-2ce1-4e6e-8259-f578097dd15f": {"id": "af9b4cbd-2ce1-4e6e-8259-f578097dd15f", "updated_at": "2017-09-28T21:11:12.971544", "created_at": "2017-09-28T21:11:12.971521", "__class__": "BaseModel"}, "BaseModel.38a22b25-ae9c-4fa9-9f94-59b3eb51bfba": {"id": "38a22b25-ae9c-4fa9-9f94-59b3eb51bfba", "updated_at": "2017-09-28T21:11:13.753347", "created_at": "2017-09-28T21:11:13.753337", "__class__": "BaseModel"}, "BaseModel.9bf17966-b092-4996-bd33-26a5353cccb4": {"id": "9bf17966-b092-4996-bd33-26a5353cccb4", "updated_at": "2017-09-28T21:11:14.963058", "created_at": "2017-09-28T21:11:14.963049", "__class__": "BaseModel"}, "BaseModel.2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4": {"id": "2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4", "updated_at": "2017-09-28T21:11:14.333862", "created_at": "2017-09-28T21:11:14.333852", "__class__": "BaseModel"}, "BaseModel.a42ee380-c959-450e-ad29-c840a898cfce": {"id": "a42ee380-c959-450e-ad29-c840a898cfce", "updated_at": "2017-09-28T21:11:15.504296", "created_at": "2017-09-28T21:11:15.504287", "__class__": "BaseModel"}, "User.38f22813-2753-4d42-b37c-57a17f1e4f88": {"id": "38f22813-2753-4d42-b37c-57a17f1e4f88", "created_at": "2017-09-28T21:11:42.848279", "updated_at": "2017-09-28T21:11:42.848291", "email": "airbnb@mail.com", "first_name": "Betty", "__class__": "User", "last_name": "Bar", "password": "root"}, "User.d0ef8146-4664-4de5-8e89-096d667b728e": {"id": "d0ef8146-4664-4de5-8e89-096d667b728e", "created_at": "2017-09-28T21:11:42.848280", "updated_at": "2017-09-28T21:11:42.848294", "email": "airbnb_2@mail.com", "first_name": "John", "__class__": "User", "password": "root"}}
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_user.py
-- Reloaded objects --
[BaseModel] (af9b4cbd-2ce1-4e6e-8259-f578097dd15f) {'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 12, 971544), 'id': 'af9b4cbd-2ce1-4e6e-8259-f578097dd15f', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 12, 971521)}
[BaseModel] (2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4) {'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 333862), 'id': '2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 333852)}
[BaseModel] (9bf17966-b092-4996-bd33-26a5353cccb4) {'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 963058), 'id': '9bf17966-b092-4996-bd33-26a5353cccb4', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 963049)}
[BaseModel] (a42ee380-c959-450e-ad29-c840a898cfce) {'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 15, 504296), 'id': 'a42ee380-c959-450e-ad29-c840a898cfce', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 15, 504287)}
[BaseModel] (38a22b25-ae9c-4fa9-9f94-59b3eb51bfba) {'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 13, 753347), 'id': '38a22b25-ae9c-4fa9-9f94-59b3eb51bfba', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 13, 753337)}
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'password': '63a9f0ea7bb98050796b649e85481845', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'email': 'airbnb@mail.com', 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), 'last_name': 'Bar', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88', 'first_name': 'Betty'}
[User] (d0ef8146-4664-4de5-8e89-096d667b728e) {'password': '63a9f0ea7bb98050796b649e85481845', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848280), 'email': 'airbnb_2@mail.com', 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848294), 'id': 'd0ef8146-4664-4de5-8e89-096d667b728e', 'first_name': 'John'}
-- Create a new User --
[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {'password': 'root', 'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611352), 'email': 'airbnb@mail.com', 'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611363), 'last_name': 'Bar', 'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68', 'first_name': 'Betty'}
-- Create a new User 2 --
[User] (fce12f8a-fdb6-439a-afe8-2881754de71c) {'password': 'root', 'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611354), 'email': 'airbnb_2@mail.com', 'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611368), 'id': 'fce12f8a-fdb6-439a-afe8-2881754de71c', 'first_name': 'John'}
guillaume@ubuntu:~/AirBnB$
guillaume@ubuntu:~/AirBnB$ cat file.json ; echo ""
{"BaseModel.af9b4cbd-2ce1-4e6e-8259-f578097dd15f": {"updated_at": "2017-09-28T21:11:12.971544", "__class__": "BaseModel", "id": "af9b4cbd-2ce1-4e6e-8259-f578097dd15f", "created_at": "2017-09-28T21:11:12.971521"}, "User.38f22813-2753-4d42-b37c-57a17f1e4f88": {"password": "63a9f0ea7bb98050796b649e85481845", "created_at": "2017-09-28T21:11:42.848279", "email": "airbnb@mail.com", "id": "38f22813-2753-4d42-b37c-57a17f1e4f88", "last_name": "Bar", "updated_at": "2017-09-28T21:11:42.848291", "first_name": "Betty", "__class__": "User"}, "User.d0ef8146-4664-4de5-8e89-096d667b728e": {"password": "63a9f0ea7bb98050796b649e85481845", "created_at": "2017-09-28T21:11:42.848280", "email": "airbnb_2@mail.com", "id": "d0ef8146-4664-4de5-8e89-096d667b728e", "updated_at": "2017-09-28T21:11:42.848294", "first_name": "John", "__class__": "User"}, "BaseModel.9bf17966-b092-4996-bd33-26a5353cccb4": {"updated_at": "2017-09-28T21:11:14.963058", "__class__": "BaseModel", "id": "9bf17966-b092-4996-bd33-26a5353cccb4", "created_at": "2017-09-28T21:11:14.963049"}, "BaseModel.a42ee380-c959-450e-ad29-c840a898cfce": {"updated_at": "2017-09-28T21:11:15.504296", "__class__": "BaseModel", "id": "a42ee380-c959-450e-ad29-c840a898cfce", "created_at": "2017-09-28T21:11:15.504287"}, "BaseModel.38a22b25-ae9c-4fa9-9f94-59b3eb51bfba": {"updated_at": "2017-09-28T21:11:13.753347", "__class__": "BaseModel", "id": "38a22b25-ae9c-4fa9-9f94-59b3eb51bfba", "created_at": "2017-09-28T21:11:13.753337"}, "BaseModel.2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4": {"updated_at": "2017-09-28T21:11:14.333862", "__class__": "BaseModel", "id": "2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4", "created_at": "2017-09-28T21:11:14.333852"}, "User.246c227a-d5c1-403d-9bc7-6a47bb9f0f68": {"password": "root", "created_at": "2017-09-28T21:12:19.611352", "email": "airbnb@mail.com", "id": "246c227a-d5c1-403d-9bc7-6a47bb9f0f68", "last_name": "Bar", "updated_at": "2017-09-28T21:12:19.611363", "first_name": "Betty", "__class__": "User"}, "User.fce12f8a-fdb6-439a-afe8-2881754de71c": {"password": "root", "created_at": "2017-09-28T21:12:19.611354", "email": "airbnb_2@mail.com", "id": "fce12f8a-fdb6-439a-afe8-2881754de71c", "updated_at": "2017-09-28T21:12:19.611368", "first_name": "John", "__class__": "User"}}
guillaume@ubuntu:~/AirBnB$
```
#### No unittests needed for the console

---

# 9. More classes!: [models/state.py](https://github.com/elyse502/AirBnB_clone/blob/master/models/state.py), [models/city.py](https://github.com/elyse502/AirBnB_clone/blob/master/models/amenity.py), [models/amenity.py](https://github.com/elyse502/AirBnB_clone/blob/master/models/amenity.py), [models/place.py](https://github.com/elyse502/AirBnB_clone/blob/master/models/place.py), [models/review.py](https://github.com/elyse502/AirBnB_clone/blob/master/models/review.py), [tests/](https://github.com/elyse502/AirBnB_clone/tree/master/tests)

Write all those classes that inherit from `BaseModel`:
* `State` (`models/state.py`):
    * Public class attributes:
        * `name`: string - empty string
* `City` (`models/city.py`):
    * Public class attributes:
        * `state_id`: string - empty string: it will be the `State.id`
        * `name`: string - empty string
* `Amenity` (`models/amenity.py`):
    * Public class attributes:
        * `name`: string - empty string
* `Place` (`models/place.py`):
    * Public class attributes:
        * `city_id`: string - empty string: it will be the `City.id`
        * `user_id`: string - empty string: it will be the `User.id`
        * `name`: string - empty string
        * `description`: string - empty string
        * `number_rooms`: integer - 0
        * `number_bathrooms`: integer - 0
        *` max_guest`: integer - 0
        * `price_by_night`: integer - 0
        * `latitude`: float - 0.0
        * `longitude`: float - 0.0
        * `amenity_ids`: list of string - empty list: it will be the list of `Amenity.id` later
* `Review` (`models/review.py`):
    * Public class attributes:
        * `place_id`: string - empty string: it will be the `Place.id`
        * `user_id`: string - empty string: it will be the `User.id`
        * `text`: string - empty string

---

## 10. Console 1.0: [console.py](https://github.com/elyse502/AirBnB_clone/blob/master/console.py), [models/engine/file_storage.py](https://github.com/elyse502/AirBnB_clone/blob/master/models/engine/file_storage.py), [tests/](https://github.com/elyse502/AirBnB_clone/tree/master/tests)
Update `FileStorage` to manage correctly serialization and deserialization of all our new classes: `Place`, `State`, `City`, `Amenity` and `Review`

Update your command interpreter (`console.py`) to allow those actions: `show`, `create`, `destroy`, `update` and `all` with all classes created previously.

Enjoy your first console!

#### No unittests needed for the console

---

## 11. All instances by class name: [console.py](https://github.com/elyse502/AirBnB_clone/blob/master/console.py)
Update your command interpreter (`console.py`) to retrieve all instances of a class by using: `<class name>.all()`.
```groovy
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) User.all()
[[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {'first_name': 'Betty', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611352), 'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611363), 'password': '63a9f0ea7bb98050796b649e85481845', 'email': 'airbnb@mail.com', 'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68'}, [User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'first_name': 'Betty', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@mail.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}]
(hbnb)
``` 
#### No unittests needed

---

## 12. Count instances: [console.py](https://github.com/elyse502/AirBnB_clone/blob/master/console.py)
Update your command interpreter (console.py) to retrieve the number of instances of a class: `<class name>.count()`.
```groovy
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) User.count()
2
(hbnb)
```
#### No unittests needed

---

## 13. Show: [console.py](https://github.com/elyse502/AirBnB_clone/blob/master/console.py)
Update your command interpreter (`console.py`) to retrieve an instance based on its ID: `<class name>.show(<id>)`.

Errors management must be the same as previously.
```groovy
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) User.show("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {'first_name': 'Betty', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611352), 'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611363), 'password': '63a9f0ea7bb98050796b649e85481845', 'email': 'airbnb@mail.com', 'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68'}
(hbnb) User.show("Bar")
** no instance found **
(hbnb) 
```
#### No unittests needed

---

## 14. Destroy: [console.py](https://github.com/elyse502/AirBnB_clone/blob/master/console.py)
Update your command interpreter (`console.py`) to destroy an instance based on his ID: `<class name>.destroy(<id>)`.

Errors management must be the same as previously.
```groovy
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) User.count()
2
(hbnb) User.destroy("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
(hbnb) User.count()
1
(hbnb) User.destroy("Bar")
** no instance found **
(hbnb) 
````
#### No unittests needed

---

## 15. Update: [console.py](https://github.com/elyse502/AirBnB_clone/blob/master/console.py)
Update your command interpreter (`console.py`) to update an instance based on his ID: `<class name>.update(<id>, <attribute name>, <attribute value>)`.

Errors management must be the same as previously.
```groovy
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'first_name': 'Betty', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@mail.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}
(hbnb)
(hbnb) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "first_name", "John")
(hbnb) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "age", 89)
(hbnb)
(hbnb) User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'age': 89, 'first_name': 'John', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 15, 32, 299055), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@mail.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}
(hbnb) 
```
#### No unittests needed

---

## 16. Update from dictionary: [console.py](https://github.com/elyse502/AirBnB_clone/blob/master/console.py)
Update your command interpreter (`console.py`) to update an instance based on his ID with a dictionary: `<class name>.update(<id>, <dictionary representation>)`.

Errors management must be the same as previously.
```groovy
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'age': 23, 'first_name': 'Bob', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 15, 32, 299055), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@mail.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}
(hbnb) 
(hbnb) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", {'first_name': "John", "age": 89})
(hbnb) 
(hbnb) User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'age': 89, 'first_name': 'John', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 17, 10, 788143), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@mail.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}
(hbnb) 
```
#### No unittests needed

---

## 17. Unittests for the Console!: [tests/test_console.py](https://github.com/elyse502/AirBnB_clone/blob/master/tests/test_console.py)
Write all unittests for `console.py`, all features!

For testing the console, you should “intercept” STDOUT of it, we highly recommend you to use:
```groovy
with patch('sys.stdout', new=StringIO()) as f:
    HBNBCommand().onecmd("help show")
```
Otherwise, you will have to re-write the console by replacing `precmd` by `default`.

<hr />

## Author :black_nib:
_[NIYIBIZI Elysée](https://mail.google.com/mail/u/0/#inbox) | [Github](https://github.com/elyse502) | [Linkedin](https://www.linkedin.com/in/niyibizi-elys%C3%A9e/) | [Twitter](https://twitter.com/Niyibizi_Elyse)._

## Acknowledgements 🤝
_All work contained in this project was completed as part of the curriculum for Alx-Holberton School. Alx-Holberton School is a Remote-based full-stack software engineering program that prepares students for careers in the tech industry using project-based peer learning. For more information_, visit [This link](https://www.alxafrica.com/).

<p align="center">
<h2 align="center"><img align="center" src="https://github.com/elyse502/AirBnB_clone/assets/125453474/ab3c1e01-2b98-47ae-96b7-37c07c85a2f1" alt="footer" width="150"  height="150"/></h2>





