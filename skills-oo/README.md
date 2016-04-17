## Part 1: Discussion

1. What are the three main design advantages that object orientation can provide? Explain each concept.

    Abstraction - Don't need to know the information about what a method does or uses internally. Abstraction allows for only the most important features of the object to be available.
    
    Polymorphism - Also known as interchangability. Different object types should have the same structure as each other.
    
    Encapsulation - The class contains all we need for that object (methods, for instance are contained in the class).

2. What is a class?
    
    A class is used to contain methods and attributes and a 'skeleton' for creating objects of that type.
    
3. What is an instance attribute?

    An instance attribute are values that are unique to the object.
    
4. What is a method?

    You might not like my explanation, but a method is essentially a function that is embedded in a class and accessed by doing self.method_name(params) where self is the object of that class.
    
5. What is an instance in object orientation?

    An instance is an object of type <class>. For instance, if we have a class called Cat, and we create a new object of type Cat, called jerry (Jerry the cat), jerry is the instance of Cat class.
    
6. How is a class attribute different than an instance attribute? Give an example where you would use both?

    A class attribute is different since it is contained outside of the __init__ method, while an instance attribute is defined in the __init__ and also is denoted by self.attribute_name. A class attribute is best for holding constants of the class since class attributes are for more static attributes of an object. That being said, all objects of type <class> will have the same class attribute values upon instantiation, unless modified.