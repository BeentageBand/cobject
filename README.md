# cobject
This library support basic Object Oriented Programing (OOP) using C language.
The cobject library supports the following OOP features:
- Data Hiding: structures/unions can be write-protected. Data hiding is not possible for reading data
- Inheritance: child structures/unions can be expanded from parent. Inherit is limited to 1 parent class
- Polymorphism: structures can override class virtual table. Only virtual table functions can be overriden
- Encapsulation: the full object is composed by union object and class structure. These objects are tightly coupled so they act as 1 entity only.

## struct Object
struct Object is a struct type which acts as a object (class instance).

## struct Class
struct Class is a struct type which acts as a class 

## Use cobject_model.py
cobject_mode.py generates the following files:
- <object>.h : api header with methods and object structure. This header can be used by other clients
- <object>-impl.h : implementation header for other -cobjects. This header can be used by other clients if inheritance is needed.
- <object>-impl.c : source implementation for object. 
- <object>.c : template source so client can implement object methods.
