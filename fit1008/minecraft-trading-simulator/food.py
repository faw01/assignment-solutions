from __future__ import annotations

from material import Material
from random_gen import RandomGen

# List of food names from https://github.com/vectorwing/FarmersDelight/tree/1.18.2/src/main/resources/assets/farmersdelight/textures/item
FOOD_NAMES = [
    "Apple Cider",
    "Apple Pie",
    "Apple Pie Slice",
    "Bacon",
    "Bacon And Eggs",
    "Bacon Sandwich",
    "Baked Cod Stew",
    "Barbecue Stick",
    "Beef Patty",
    "Beef Stew",
    "Cabbage",
    "Cabbage Leaf",
    "Cabbage Rolls",
    "Cabbage Seeds",
    "Cake Slice",
    "Chicken Cuts",
    "Chicken Sandwich",
    "Chicken Soup",
    "Chocolate Pie",
    "Chocolate Pie Slice",
    "Cod Slice",
    "Cooked Bacon",
    "Cooked Chicken Cuts",
    "Cooked Cod Slice",
    "Cooked Mutton Chops",
    "Cooked Rice",
    "Cooked Salmon Slice",
    "Dog Food",
    "Dumplings",
    "Egg Sandwich",
    "Fish Stew",
    "Fried Egg",
    "Fried Rice",
    "Fruit Salad",
    "Grilled Salmon",
    "Ham",
    "Hamburger",
    "Honey Cookie",
    "Honey Glazed Ham",
    "Honey Glazed Ham Block",
    "Horse Feed",
    "Hot Cocoa",
    "Melon Juice",
    "Melon Popsicle",
    "Milk Bottle",
    "Minced Beef",
    "Mixed Salad",
    "Mutton Chops",
    "Mutton Wrap",
    "Nether Salad",
    "Noodle Soup",
    "Onion",
    "Pasta With Meatballs",
    "Pasta With Mutton Chop",
    "Pie Crust",
    "Pumpkin Pie Slice",
    "Pumpkin Slice",
    "Pumpkin Soup",
    "Ratatouille",
    "Raw Pasta",
    "Rice",
    "Rice Panicle",
    "Roast Chicken",
    "Roast Chicken Block",
    "Roasted Mutton Chops",
    "Rotten Tomato",
    "Salmon Slice",
    "Shepherds Pie",
    "Shepherds Pie Block",
    "Smoked Ham",
    "Squid Ink Pasta",
    "Steak And Potatoes",
    "Stuffed Potato",
    "Stuffed Pumpkin",
    "Stuffed Pumpkin Block",
    "Sweet Berry Cheesecake",
    "Sweet Berry Cheesecake Slice",
    "Sweet Berry Cookie",
    "Tomato",
    "Tomato Sauce",
    "Tomato Seeds",
    "Vegetable Noodles",
    "Vegetable Soup",
]

class Food:
    """
    Food class.

    Attributes:
        name {str} -- The name of the food.
        hunger_bars {int} -- The number of hunger bars the food restores.
        price {int} -- The price of the food.

    Unless specified, all functions have time complexity of O(1).
    """
    
    def __init__(self, name: str, hunger_bars: int, price: int) -> None:
        """
        Initialises a Food object.
        
        Arguments:
            name {str} -- The name of the food.
            hunger_bars {int} -- The number of hunger bars the food restores.
            price {int} -- The price of the food.

        Precondition:
            hunger_bars >= 0
            price >= 0
            food in FOOD_NAMES
        """
        if hunger_bars < 0:
            raise ValueError("hunger_bars must be >= 0")
        if price < 0:
            raise ValueError("price must be >= 0")
        if name not in FOOD_NAMES:
            raise ValueError(f"{name} not in FOOD_NAMES")
            
        self.name = name
        self.hunger_bars = hunger_bars
        self.price = price

    def get_food_name(self) -> str:
        """
        Returns the name of the food.

        Returns:
            str -- The name of the food.
        """
        return self.name

    def get_food_price(self) -> int:
        """
        Returns the price of the food.

        Returns:
            int -- The price of the food.
        """
        return self.price

    def get_food_hunger_bars(self) -> int:
        """
        Returns the number of hunger bars the food restores.

        Returns:
            int -- The number of hunger bars the food restores.
        """
        return self.hunger_bars
    
    def __str__(self) -> str:
        """
        Returns a string representation of the food.

        Returns:
            str -- A string representation of the food.
        """
        return f"{self.name}"

    @classmethod
    def random_food(cls) -> Food:
        """
        Returns a random food.

        Returns:
            Food -- A random food.
        """
        return Food(RandomGen.random_choice(FOOD_NAMES), RandomGen.randint(1, 5), RandomGen.randint(1, 5))