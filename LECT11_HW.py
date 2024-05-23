class Cat:
    """
    A class representing my cat.
    """

    # Class field
    cat_count = 0

    def __init__(self, name, breed, age):
        """
        Initialize a cat object.

        Parameters:
        - name (str): The name of the cat.
        - breed (str): The breed of the cat.
        - age (int): The age of the cat.
        """
        self.name = name
        self.breed = breed
        self.age = age
        Cat.cat_count += 1

    def hisss(self):
        """
        Produce a hissing sound.

        Returns:
        str: Hissing sound.
        """
        return f"{self.name}: Hissssss!"

    def play(self):
        """
        Simulate the cat playing with a ball.

        Returns:
        str: A message indicating the cat playing.
        """
        return f"{self.name}, {self.breed} is playing with a ball! {self.name} is {self.age} and still going!"

    @classmethod
    def get_cat_count(cls):
        """
        Get the total count of cats.

        Returns:
        int: The count of cat instances.
        """
        return cls.cat_count

    @staticmethod
    def hunt():
        """
        Simulate the cat hunting the mouse.

        Returns:
        str: A message indicating the cat is hunting.
        """
        return "Hunting.."


# Creating instances of Cat
cat1 = Cat("Margot", "Scottish fold", 8)
cat2 = Cat("Kuziya", "Metis", 12)


# ====================================================================== #

class Owl:
    """A class representing some species of owls."""

    # Class field
    owl_count = 0

    def __init__(self, name, area, size):
        """
        Initialize an Owl object.

        Parameters:
        - name (str): The name of the specie.
        - area (str): The area of habitat.
        - size (int): The size of the specie.
        """
        self.name = name
        self.area = area
        self.size = size
        Owl.owl_count += 1

    def display_info(self):
        """
        Display information about the particular owl.

        Returns:
        str: Information about the owl.
        """
        return f"This is {self.name}. It inhabits {self.area}. The bird can reach {self.size} cm."

    def howl(self):
        """
        Produce a hooting sound.

        Returns:
        str: A hooting sound.
        """
        return "Woooo! Woooo!"


# Creating instances of an Owl
owl1 = Owl("Bubo blakistoni", "Far Eastern countries", 190)
owl2 = Owl("Strix nebulosa", "forests of Eurasia and North America", 160)

# ====================================================================== #

# Displaying information about the instances
print(cat1.play())
print(cat2.hisss())

# Class method usage
print(f"Total number of cats: {Cat.get_cat_count()}")

# Static method usage
print(cat1.hunt())

# Displaying information about the instances
print(owl1.display_info())
print(owl2.display_info())

# Static method usage
print(owl1.howl())

