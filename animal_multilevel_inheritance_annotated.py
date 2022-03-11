# Annotated multilevel inheritance example (not multiple inheritence)
#     by: Alex Hoffman

class Animal:
    # class attribute - all animals are multicellular, thus
    # all objects belonging to this class and ALL subclasses must
    # inherit this class attribute.
    # class attributes must be assigned an initial value
    multicellular = True
    
    # initialize instance attributes - not all animals have legs and tails,
    #     so it depends on the specific (instance) of Animal
    def __init__(self, legs, tail):
        # the double_underscore (could be single underscore) indicates 
        # the attribute is private. Python doesn't enforce 
        # public/protected like c++/java.
        self.__legs = legs
        self.__tail = tail
        
        # eats is public, so it can be accessed directly
        # it also isn't initialized to a value, so it must be set
        self.eats = bool
    
    # In python, having an @xxx (any name) right on top of a function
    # definition is called a decorator. There are built-in decorators
    # like the @property decorator below or you can create your own.
    # The property decorator is similar to having a getter (accessor)
    # in other languages. Here it just returns the attribute value.
    @property
    def legs(self):
        return self.__legs
    
    # A setter decorator is similar to having a setter (mutator)
    # in other languages. Here it lets you directly alter the attribute
    # after instantiation. There could be logic here if desired/needed.
    @legs.setter
    def legs(self, legs):
        self.__legs = legs
    
    # This getter has some logic. many times you'll see a
    # getter just return, like the legs getter above.
    # java devs almost always have setters/getters for every
    # attribute that you might want to access, so it can get
    # overloading quickly.
    @property
    def tail(self):
        if self.__tail == True:
            return "has"
        else:
            return "does not have"
    
    @tail.setter
    def tail(self, tail):
        self.__tail = tail
    
    
# Putting Animal in parenthesis here means that class Dog inherits
# from class Animal. It inherits all attributes and methods.    
class Dog(Animal):
    ## this init overrides the parent classes's init (constructor)
    # legs and tail have default values set to the average dog
    # but....(see more below)
    def __init__(self, name, legs=4, tail=True):
        self.__name = name
        self.__sound = "woof"
        
        # you have to explicitly call Parent class Animal's constructor
        # in order to invoke the parent (super) class's constructor
        Animal.__init__(self, legs, tail)
    
    # a bark function that is unique to Dogs (in this example)
    # I could have made a generic "sound()" function in the Animal
    # superclass and each Animal have a __sound attribute,
    # but I didn't want to :)
    def bark(self):
        print(self.__sound)
    
    # other properties/setters similar to Animal...more of the same below, too
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
        

# class Reptile inherits from Animal, so you get all the 
# attributes and actions from Animal as well as ones
# created specifically for Reptile.
class Reptile(Animal):
    # this also overrides the super class's default
    # constructor, but.... (see below)
    def __init__(self, legs, tail=True):
        self.__scales = True
        
        # here calling super() implicitly inherrits the
        # Animal super class constructor, so you don't have 
        # to use the Animal name and you don't have to pass self
        super().__init__(legs, tail)        
    
    @property    
    def scales(self):
        if self.__scales == True:
            return "has"
        else:
            return "does not have"
        
    @scales.setter
    def scales(self, scales):
        self.__scales = scales


# this class doesn't have any implementation, so it works exactly like
# its super class Reptile and Reptile's super class Animal
class Lizard(Reptile):
    pass
        
        
# class Snake inherits from Reptile which inherits from Animal, so
# you get all the attributes and actions from them as well as ones
# created specifically for Snake.
class Snake(Reptile):
    # note the default values for legs/tail and venom
    def __init__(self, legs=0, tail=True):
        self.__venom = False
        self.__tail = True
        super().__init__(legs, self.__tail)
        
    @property
    def venom(self):
        if self.__venom == False: return "is not"
        else: return "is"
    
    @venom.setter
    def venom(self, has_venom):
        self.__venom = has_venom

    # here, both of the tail functions override the parent
    # class's tail function, so invoking them will invoke this
    # method's behavior (unless you call the superclass's behavior)
    # this is python polymorphism
    @property
    def tail(self):
        if self.__tail == True:
            return "is mostly"
        else:
            return "must be dead"
    
    @tail.setter
    def tail(self, tail):
        self.__tail = tail
        
# Bacterium is in a class heirarchy of its own at the same "top" level as Animal
class Bacterium:
    # class attribute - All bacteria are single-cellular
    multicellular = False
    

if __name__ == "__main__":
    
    # create (aka instantiate) a Dog object named George and do not override the defalt values
    george = Dog('George')

    print(f"Speak George!")
    george.bark()
    # .name is implemented in Dog and .legs and .tail are inherited from Animal
    print(f"{george.name} has {george.legs} legs and {george.tail} a tail")

    # several print()s just for output spacing...
    print()

    # here we create a 3 legged Dog object named Fido with its tail docked by overriding the default values
    fido = Dog('Fido', 3, False)

    print(f"Speak Fido!")
    fido.bark()
    fido.bark()
    # .name is implemented in Dog and .legs and .tail are inherited from Animal
    print(f"{fido.name} has {fido.legs} legs and {fido.tail} a tail")

    print()
    # create a Reptile object which inherits from Animal
    croc = Reptile(4)
    # Reptiles don't have a .name, .scales is implemented in Reptile, and .legs and .tail are inherited from Animal
    print(f"A croc has {croc.legs} legs, {croc.tail} a tail and {croc.scales} scales")

    # Create a Lizard object which inherits everything from Reptile (by default due to 'pass') which inherits from Animal
    gecko = Lizard(4)
    # Lizards don't have a .name, .scales is inherited from Reptile, and .legs and .tail are inherited from Animal
    print(f"A gecko has {gecko.legs} legs, {gecko.tail} a tail and {gecko.scales} scales")


    print()
    # create a Snake object which inherits from Reptile which inherits from Animal
    rattlesnake = Snake()
    
    # this uses the .venom setter attribute to override the default value when Snake was instantiated
    rattlesnake.venom = True
    # Snakes don't have a .name, .venom is implemented in Snake, 
    # tail is reimplemented in Snake to override the parent class's implementation
    # .scales is inherited from Reptile, and .legs is inherited from Animal
    print(f"A rattlesnake has {rattlesnake.legs} legs, {rattlesnake.tail} a tail, {rattlesnake.scales} scales, "
                    f"and {rattlesnake.venom} venomous.")

    # create another Snake object which also inherits from Reptile which inherits from Animal
    cornsnake = Snake()
    # this uses the .scales setter attribute to override the default value in Reptile
    cornsnake.scales = False
    
    # Snakes don't have a .name, .venom is implemented in Snake, 
    # tail is reimplemented in Snake to override the parent class's implementation
    # .scales is inherited from Reptile, and .legs is inherited from Animal    
    print(f"A cornsnake has {cornsnake.legs} legs, {cornsnake.tail} a tail, {cornsnake.scales} scales, "
                    f"and {cornsnake.venom} venomous.")
    
    print()

    # modifying the public .eats attribute from Animal
    cornsnake.eats = True
    print(f"A cornsnake eats: {cornsnake.eats}")
    
    cornsnake.tail = False
    print(f"A cornsnake without a tail {cornsnake.tail} because it is only a head :D")
    
    # now we access the behavior of the Snake superclass's .tail implementation
    print(f"A living cornsnake {super(Snake, cornsnake).tail} a tail")
    
    cornsnake.eats = False
    print(f"A cornsnake can eat after it dies: {cornsnake.eats}")

    print()
    # displays the .multicellular class attribute in Animal
    print(f"A cornsnake is multicellular: {cornsnake.multicellular}")
    
    

    print()
    # create an unknown Animal with 6 legs and does not have a tail
    unknown_animal = Animal(6, False)
    # here you only have the Animal class's attributes and methods to work with
    print(f"I'm not sure what kind of Animal has {unknown_animal.legs} legs and {unknown_animal.tail} a tail!")
    unknown_animal.eats = True
    print(f"At least we know it is {unknown_animal.eats} that it eats, and"
            f" it is {unknown_animal.multicellular} that it is multicellular")

    print()
    # create a new Bacterium object
    strep = Bacterium()
    # displays the .multicellular class attribute in Bacterium,
    # which is different from Animal and why it is in a different class
    print(f"Streptococcus is multicellular: {strep.multicellular}")

    ''' side note: if we wanted, we could create a higher level class called
        Organism and have Animal and Bacerium inherit from Organism. For example, 
        the Organism class could have a class attribute has_cell_nucleus = True as
        something that Animals and Bacteria both share.
    '''

# END annotated multilevel inheritance example
#     by: Alex Hoffman
