from __future__ import annotations

from abc import abstractmethod, ABC
from multiprocessing.sharedctypes import Value
from re import X
from typing import List
from material import Material
from random_gen import RandomGen
from hash_table import LinearProbeTable

# Generated with https://www.namegenerator.co/real-names/english-name-generator
TRADER_NAMES = [
    "Pierce Hodge",
    "Loren Calhoun",
    "Janie Meyers",
    "Ivey Hudson",
    "Rae Vincent",
    "Bertie Combs",
    "Brooks Mclaughlin",
    "Lea Carpenter",
    "Charlie Kidd",
    "Emil Huffman",
    "Letitia Roach",
    "Roger Mathis",
    "Allie Graham",
    "Stanton Harrell",
    "Bert Shepherd",
    "Orson Hoover",
    "Lyle Randall",
    "Jo Gillespie",
    "Audie Burnett",
    "Curtis Dougherty",
    "Bernard Frost",
    "Jeffie Hensley",
    "Rene Shea",
    "Milo Chaney",
    "Buck Pierce",
    "Drew Flynn",
    "Ruby Cameron",
    "Collie Flowers",
    "Waldo Morgan",
    "Winston York",
    "Dollie Dickson",
    "Etha Morse",
    "Dana Rowland",
    "Eda Ryan",
    "Audrey Cobb",
    "Madison Fitzpatrick",
    "Gardner Pearson",
    "Effie Sheppard",
    "Katherine Mercer",
    "Dorsey Hansen",
    "Taylor Blackburn",
    "Mable Hodge",
    "Winnie French",
    "Troy Bartlett",
    "Maye Cummings",
    "Charley Hayes",
    "Berta White",
    "Ivey Mclean",
    "Joanna Ford",
    "Florence Cooley",
    "Vivian Stephens",
    "Callie Barron",
    "Tina Middleton",
    "Linda Glenn",
    "Loren Mcdaniel",
    "Ruby Goodman",
    "Ray Dodson",
    "Jo Bass",
    "Cora Kramer",
    "Taylor Schultz",
]

class Trader(ABC):
    """
    Abstract class for a trader.
    
    Unless specified, all functions have time complexity of O(1).
    """
    def __init__(self, name: str) -> None:
        """
        Initialise a trader with a name.
        
        Arguments:
            name {str} -- The name of the trader.
            materials {list[Material]} -- The materials the trader is selling.
        """
        self.name = name
        self.materials = []
        self.selling = False
        self.sell = None

    def get_name(self) -> str:
        """
        Returns the name of the trader.
        
        Returns:
            str -- The name of the trader.
        """
        return self.name
    
    @classmethod
    def random_trader(cls):
        """
        Creates a random trader based on all trader types
        
        Returns:
            Trader -- A random trader.
        """
        return cls(RandomGen.random_choice(TRADER_NAMES))

    @abstractmethod
    def set_all_materials(self, mats: list[Material]) -> None:
        """
        Set all the materials that the trader can buy.
        
        Arguments:
            mats {list[Material]} -- A list of materials.
        """
        pass
    
    def add_material(self, mat: Material) -> None:
        """
        Add a material to the trader's inventory.
        
        Arguments:
            mat {Material} -- The material to add.
        """
        self.materials.append(mat)

    def remove_material(self, mat: Material) -> None:
        """
        Remove a material from the trader's inventory.
        
        Arguments:
            mat {Material} -- The material to remove.
        """
        self.materials.remove(mat)
        
    def is_currently_selling(self) -> bool:
        """
        Returns whether the trader is currently selling.
        
        Returns:
            bool -- Whether the trader is currently selling.
        """
        return self.selling

    def get_material(self) -> list[Material]:
        """
        Returns the materials the trader is selling.
        
        Returns:
            list[Material] -- The materials the trader is selling.
        """
        return self.materials[0]

    def current_deal(self) -> tuple[Material, float]:
        """
        Returns the current deal for the trader.

        Precondition: 
            Trader is currently selling.
        
        Returns:
            tuple[Material, float] -- A tuple containing the material and the price.
        """
        if self.is_currently_selling() == False:
            raise ValueError(f"{self.name} not current buying")

        buying_price = self.buying_price()
        return self.materials[0], buying_price

    def buying_price(self) -> float:
        """
        Returns the buying price for a material.
        
        Returns:
            float -- The buying price.
        """
        if self.sell is not None:
            buying_price = self.sell[1]
        else:
            buying_price = round(2 + 8 * RandomGen.random_float(), 2)
        
        return buying_price

    def sell(self, price: float) -> None:
        """
        Hackily set price (to follow the spec)
        
        Arguments:
            price {float} -- The price to set.
        """
        self.selling = True
        self.materials[0].set_price(price)
  
    @abstractmethod
    def generate_deal(self) -> None:
        """
        Generate a deal for the trader.
        """
        pass

    def stop_deal(self) -> None:
        """
        Stop the current deal.
        """
        self.selling = False
        self.materials.clear()
    
    def __str__(self) -> str:
        """
        String representation for trader
        example __str__: <RandomTrader: Mr Barnes buying [Pickaxe: 7🍗/💎] for 7.57💰>
        
        Returns:
            str -- String representation of trader.
        """
        if self.is_currently_selling():
            mat, price = self.current_deal()
            return f"<{self.__class__.__name__}: {self.name} buying [{mat}] for {price}💰>"
        else:
            return f"<{self.__class__.__name__}: {self.name} not current buying>"

class RandomTrader(Trader): 
    """
    A random trader.
    """
    def __init__(self, name: str) -> None:
        """
        Generate a RandomTrader object.
        """
        super().__init__(name)

    def generate_deal(self) -> None:
        """
        Generate a deal for the trader.
        """
        self.selling = True
        self.materials = [RandomGen.random_choice(self.materials)]

    def set_all_materials(self, mats: list[Material]) -> None:
        """
        Set all the materials that the trader can buy.
        
        Arguments:
            mats {list[Material]} -- A list of materials.

        Time Complexity Analysis:
            Best Case: O(1)
            Worst Case: O(n)
        """
        for materials in mats:
            self.materials.append(materials)

class RangeTrader(Trader):

    def __init__(self, name: str) -> None:
        """
        Generate a RangeTrader object.
        """
        super().__init__(name)

    def generate_deal(self) -> None:
        """
        Generate a deal for the trader.
        """
        self.selling = True
        i = RandomGen.randint(0, len(self.materials) - 1)
        j = RandomGen.randint(i, len(self.materials) - 1)
        self.materials = [RandomGen.random_choice(self.materials[i:j+1])]

    def materials_between(self, i: int, j: int) -> list[Material]:
        """
        Returns a list containing the materials which are somewhere between the ith and jth easiest to mine, inclusive

        Arguments:
            i {int} -- The ith easiest material to mine
            j {int} -- The jth easiest material to mine

        Returns:
            list[Material] -- A list of materials

        Time Complexity Analysis:
            Best Case: O(1)
            Worst Case: O(n)
        """
        return self.materials[i:j+1]

    def set_all_materials(self, mats: list[Material]) -> None:
        """
        Set all the materials that the trader can buy.
        
        Arguments:
            mats {list[Material]} -- A list of materials.

        Time Complexity Analysis:
            Best Case: O(1)
            Worst Case: O(n)
        """
        for materials in mats:
            self.materials.append(materials)

class HardTrader(Trader):
    def __init__(self, name: str) -> None:
        """
        Generate a HardTrader object.
        """
        super().__init__(name)
        
    def generate_deal(self) -> None:
        """
        Generate a deal for the trader.

        Time Complexity Analysis:
            Best Case: O(1)
            Worst Case: O(n)
        """
        self.selling = True
        current_max = self.materials[0]
        for i in range(len(self.materials)):
            if self.materials[i].mining_rate >= current_max.mining_rate:
                current_max = self.materials[i]
        self.materials.remove(current_max)
        self.materials = [current_max]

    def set_all_materials(self, mats: list[Material]) -> None:
        """
        Set all the materials that the trader can buy.
        
        Arguments:
            mats {list[Material]} -- A list of materials.

        Time Complexity Analysis:
            Best Case: O(1)
            Worst Case: O(n)
        """
        for materials in mats:
            self.materials.append(materials)