# ENSF 692 Spring 2024
# May 21 Lab 5
# Reviewing Classes and Objects
# This code expands on the example shown in the lecture videos

# Some documentation is included as an example (in mostly Google Style). The documentation is not complete!
# All methods should have their own docstrings unless otherwise specified (i.e. __init__ and  properties)
# The specifics of other formats may vary- you may choose whichever format you prefer as long as you are consistent.

class Horse:
    """A class used to create Horse object.

        Attributes:
            name (str): String that represents the horse's name
            age (int): Integer that represents the horse's age
            colour (str): String that represents the horse's colour
            breed (str): String that represents the horse's breed
            ***Note that self is implicit and is not included!

    """

    sci_name = "Equus caballus"
    """sci_name (str): Class variable with default string value of "Equus caballus"
    """

    def __init__(self, name, age, colour, breed):
        ### __init__ methods don't need docstrings- their information is covered in the class docstring above.

        # all private variables
        # double underline means private
        self.__name = name
        self.__age = age
        self.__colour = colour
        self.__breed = breed


    # Define all private instance variables as properties to get getters/setters
    # Note that properties are usually only documented in their getter method
    # For this class, you can skip documentation of property getters/setters unless they are customized (see below)

    @property #decorator
    def name(self):
        return self.__name

    @property #decorator
    def colour(self):
        return self.__colour

    @property #decorator
    def age(self):
        return self.__age

    @property #decorator
    def breed(self):
        return self.__breed


    # Define any customized getters/setters

    @age.setter
    def age(self, new_val):
        """age: Set a new age value for a Horse object as long as it is greater than zero. A message is printed if update is successful.
        
        Args:
            new_val (int): Integer value that represents the new age of the horse

        Returns:
            None
        """

        try:
            if new_val <= 0:
                raise ValueError()
            else:
                self.__age = new_val
                print("Happy birthday!")
        except ValueError:
            print("Age must be greater than 0.")


    # define instance methods
    def print_all_stats(self):
        print("""{0} stats: Age = {1}, Colour = {2}, Breed = {3}.""".format(self.name, self.age, self.colour, self.breed))


    # define class methods
    @classmethod
    def horse_info(cls):
        print("The scientific name of a horse is: " + cls.sci_name)


class Rider:
    
    def __init__(self, age, horse):
        self.age = age
        self.horse = horse

    def print_all_stats(self):
        print("""Rider stats: Age = {0}, Horse Age = {1}, Horse Colour = {2}, Horse Breed = {3}."""
        .format(str(self.age), str(self.horse.age), self.horse.colour, self.horse.breed))        



def main():
    print("\n***Horse and Rider Program***\n")

    # Class variable and method demo
    print("Sci name = " + Horse.sci_name)
    Horse.horse_info()

    horse_demo1 = Horse("Blaze", 14, "bay", "Morgan")
    horse_demo2 = Horse("Socks", 14, "bay", "Morgan")

    print("1demo_1Sci name = " + horse_demo1.sci_name)
    print("1demo_2Sci name = " + horse_demo2.sci_name)

    Horse.sci_name = "Something else!"

    print("2demo1_Sci name = " + horse_demo1.sci_name)
    print("2demo2_Sci name = " + horse_demo2.sci_name)

    horse_demo1.sci_name = "Different value"

    print("3demo1_Sci name = " + horse_demo1.sci_name)
    print("3demo2_Sci name = " + horse_demo2.sci_name)

    Horse.sci_name = "Change again!"

    print("4demo1_Sci name = " + horse_demo1.sci_name)
    print("4demo2_Sci name = " + horse_demo2.sci_name)

    horse_demo1.print_all_stats()
    #horse_demo1.age


if __name__ == '__main__':  # optional in Python 3
    main()

