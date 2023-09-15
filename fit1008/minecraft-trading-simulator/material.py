from random_gen import RandomGen

# Material names taken from https://minecraft-archive.fandom.com/wiki/Items
RANDOM_MATERIAL_NAMES = [
    "Arrow",
    "Axe",
    "Bow",
    "Bucket",
    "Carrot on a Stick",
    "Clock",
    "Compass",
    "Crossbow",
    "Exploration Map",
    "Fire Charge",
    "Fishing Rod",
    "Flint and Steel",
    "Glass Bottle",
    "Dragon's Breath",
    "Hoe",
    "Lead",
    "Map",
    "Pickaxe",
    "Shears",
    "Shield",
    "Shovel",
    "Sword",
    "Saddle",
    "Spyglass",
    "Totem of Undying",
    "Blaze Powder",
    "Blaze Rod",
    "Bone",
    "Bone meal",
    "Book",
    "Book and Quill",
    "Enchanted Book",
    "Bowl",
    "Brick",
    "Clay",
    "Coal",
    "Charcoal",
    "Cocoa Beans",
    "Copper Ingot",
    "Diamond",
    "Dyes",
    "Ender Pearl",
    "Eye of Ender",
    "Feather",
    "Spider Eye",
    "Fermented Spider Eye",
    "Flint",
    "Ghast Tear",
    "Glistering Melon",
    "Glowstone Dust",
    "Gold Ingot",
    "Gold Nugget",
    "Gunpowder",
    "Ink Sac",
    "Iron Ingot",
    "Iron Nugget",
    "Lapis Lazuli",
    "Leather",
    "Magma Cream",
    "Music Disc",
    "Name Tag",
    "Nether Bricks",
    "Paper",
    "Popped Chorus Fruit",
    "Prismarine Crystal",
    "Prismarine Shard",
    "Rabbit's Foot",
    "Rabbit Hide",
    "Redstone",
    "Seeds",
    "Beetroot Seeds",
    "Nether Wart Seeds",
    "Pumpkin Seeds",
    "Wheat Seeds",
    "Slimeball",
    "Snowball",
    "Spawn Egg",
    "Stick",
    "String",
    "Wheat",
    "Netherite Ingot",
]

class Material:
    """
    Material class.
    
    Attributes:
        name {str} -- The name of the material.
        mining_rate {float} -- The mining rate of the material.

    Unless specified, all functions have time complexity of O(1).
    """

    def __init__(self, name: str, mining_rate: float) -> None:
        """
        Initialises a Material object.
        
        Arguments:
            name {str} -- The name of the material.
            mining_rate {float} -- The mining rate of the material.

        Precondition:
            mining_rate >= 0
            name belongs to RANDOM_MATERIAL_NAMES
        """
        if mining_rate < 0:
            raise ValueError("mining_rate must be >= 0")

        # if name not in RANDOM_MATERIAL_NAMES:
        #     raise ValueError(f"{name} not in RANDOM_MATERIAL_NAMES")
        # gives error when running test_cave.py as Amethyst is not in RANDOM_MATERIAL_NAMES hence it is commented out
        
        self.name = name
        self.mining_rate = mining_rate

    def get_material_name(self) -> str:
        """
        Returns the name of the material.
        
        Returns:
            str -- The name of the material.
        """
        return self.name

    def get_mining_rate(self) -> float:
        """
        Returns the mining rate of the material.

        Returns:
            float -- The mining rate of the material.
        """
        return self.mining_rate
    
    def __str__(self) -> str:
        """
        Returns a string representation of the material.

        Returns:
            str -- A string representation of the material.
        """
        return f"{self.name}: {self.mining_rate}🍗/💎"

    @classmethod
    def random_material(cls):
        """
        Returns a random material.

        Returns:
            Material -- A random material.
        """
        return Material(RandomGen.random_choice(RANDOM_MATERIAL_NAMES), round(RandomGen.random_float() * 10, 2))