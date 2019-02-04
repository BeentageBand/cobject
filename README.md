# cobject
This library support basic Object Oriented Programing (OOP) using C language.
The cobject library supports the following OOP features:
- Data Hiding: structures/unions can be write-protected. Data hiding is not possible for reading data
- Inheritance: child structures/unions can be expanded from parent. Inherit is limited to 1 parent class
- Polymorphism: structures can override class virtual table. Only virtual table functions can be overriden
- Encapsulation: the full object is composed by union object and class structure. These objects are tightly coupled so they act as 1 entity only.

## struct Object
struct Object is an struct type which acts as a object (class instance).
