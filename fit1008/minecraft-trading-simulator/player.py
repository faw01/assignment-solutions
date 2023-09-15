from __future__ import annotations
from unicodedata import name

from cave import Cave
from material import Material
from trader import Trader
from food import Food
from random_gen import RandomGen
import constants
from hash_table import LinearProbeTable
from avl import AVLTree

# List taken from https://minecraft.fandom.com/wiki/Mob
PLAYER_NAMES = [
    "Steve",
    "Alex",
    "ɘᴎiɿdoɿɘH",
    "Allay",
    "Axolotl",
    "Bat",
    "Cat",
    "Chicken",
    "Cod",
    "Cow",
    "Donkey",
    "Fox",
    "Frog",
    "Glow Squid",
    "Horse",
    "Mooshroom",
    "Mule",
    "Ocelot",
    "Parrot",
    "Pig",
    "Pufferfish",
    "Rabbit",
    "Salmon",
    "Sheep",
    "Skeleton Horse",
    "Snow Golem",
    "Squid",
    "Strider",
    "Tadpole",
    "Tropical Fish",
    "Turtle",
    "Villager",
    "Wandering Trader",
    "Bee",
    "Cave Spider",
    "Dolphin",
    "Enderman",
    "Goat",
    "Iron Golem",
    "Llama",
    "Panda",
    "Piglin",
    "Polar Bear",
    "Spider",
    "Trader Llama",
    "Wolf",
    "Zombified Piglin",
    "Blaze",
    "Chicken Jockey",
    "Creeper",
    "Drowned",
    "Elder Guardian",
    "Endermite",
    "Evoker",
    "Ghast",
    "Guardian",
    "Hoglin",
    "Husk",
    "Magma Cube",
    "Phantom",
    "Piglin Brute",
    "Pillager",
    "Ravager",
    "Shulker",
    "Silverfish",
    "Skeleton",
    "Skeleton Horseman",
    "Slime",
    "Spider Jockey",
    "Stray",
    "Vex",
    "Vindicator",
    "Warden",
    "Witch",
    "Wither Skeleton",
    "Zoglin",
    "Zombie",
    "Zombie Villager",
    "H̴͉͙̠̥̹͕͌̋͐e̸̢̧̟͈͍̝̮̹̰͒̀͌̈̆r̶̪̜͙̗̠̱̲̔̊̎͊̑̑̚o̷̧̮̙̗̖̦̠̺̞̾̓͆͛̅̉̽͘͜͝b̸̨̛̟̪̮̹̿́̒́̀͋̂̎̕͜r̸͖͈͚̞͙̯̲̬̗̅̇̑͒͑ͅi̶̜̓̍̀̑n̴͍̻̘͖̥̩͊̅͒̏̾̄͘͝͝ę̶̥̺̙̰̻̹̓̊̂̈́̆́̕͘͝͝"
]

class Player():
    """
    Player Class.

    Attributes:
        name {string} -- The name of the player
        emeralds {float} -- The number of emeralds the player has

    Constants:
        DEFAULT_EMERALDS {float} -- The default number of emeralds is 50.
        MIN_EMERALDS {float} -- The minimum number of emeralds is 14. 
        MAX_EMERALDS {float} -- The maximum number of emeralds is 40. 

    Unless specified, all functions have time complexity of O(1).
    """

    DEFAULT_EMERALDS = 50

    MIN_EMERALDS = 14
    MAX_EMERALDS = 40

    def __init__(self, name, emeralds=None) -> None:
        """
        Initialises a Player object.

        Arguments:
            name {string} -- The name of the player
            emeralds {float} -- The number of emeralds the player has
        """
        self.name = name
        self.balance = self.DEFAULT_EMERALDS if emeralds is None else emeralds
        self.hunger = 0
        self.traders = None
        self.food = None
        self.material_choices = None
        self.cave_choices = None

    def get_name(self):
        """
        Returns the name of the player.
        """
        return self.name

    def get_caves(self):
        """
        Get caves.
        """
        return self.cave_choices

    def get_hunger(self):
        """
        Get hunger of the player.
        """
        return self.hunger

    def get_traders(self):
        """
        Get list of traders. 
        """
        return self.traders

    def set_name(self, new_name):
        """
        Sets the name of the player.
        """
        self.name = new_name

    def get_balance(self):
        """
        Gets the number of emeralds the player currently has.
        """
        return self.balance

    def set_balance(self, new_balance):
        """
        Sets the new number of emeralds of the player.
        """
        self.balance = new_balance

    def set_traders(self, traders_list: list[Trader]) -> None:
        """
        Sets the traders to traders_list
        """
        self.traders = traders_list

    def set_foods(self, foods_list: list[Food]) -> None:
        """
        Sets food to foods_list.
        """
        self.food = foods_list

    def set_hunger(self, hunger: int) -> None:
        """
        Sets hunger to hunger.
        """
        self.hunger = hunger

    def get_hunger(self):
        """
        Gets the hunger of the player.
        """
        return self.hunger

    @classmethod
    def random_player(cls) -> Player:
        """
        Returns random player from PLAYER_NAMES.
        """
        return cls(RandomGen.random_choice(PLAYER_NAMES))

    def set_materials(self, materials_list: list[Material]) -> None:
        """
        Sets the materials.
        """
        self.material_choices = materials_list

    def set_caves(self, caves_list: list[Cave]) -> None:
        """
        Sets the materials.
        """
        self.cave_choices = caves_list

    def select_food_and_caves(self) -> tuple[Food | None, float, list[tuple[Cave, float]]]:
        """
        Returns the Food that the player will buy, the emerald balance of the player after he/she makes a move and a
        list of tuples of all caves plundered on their journey, paired with the quantity of each material mined.

        -----LENGTHY DOCSTRING DESCRIBING MOTIVATION FOR APPROACH-----

        1. Get the food that the player will buy.
            - From the list of foods, we calculate the food hunger to price ratio (FHPR), the higher this number is,
            the more value we get from the food because we will be getting more food hunger bars per emerald.
            - We calculate the FHPRs for all foods and put them in a list, then use max() to get the best ratio, which
            would be the best food.
            - Then, we purchase the food and deduct emeralds from the player's balance.

        2. List of what caves plundered, with quantity of material mined. (Emerald balance for each player is
           calculated here as well).
            a) Set necessary variables, namely :
                i) EV (effort-value) = (quantity of materials in cave x mining rate of material)/(trader buying price)

                The EV value denotes the effort-value required to mine the materials in the cave, and when divided by the
                BEST trader buying price. The lower the EV, the lower the "effort" to gain emeralds. Thus, EV is inversely
                proportional to the emerald gains.

                The way we came up with EV was because quantity of materials in cave x mining rate of material gives us
                the hunger required to mine those materials, then we divide it by trader buying price to maximise the emerald
                gains.

            b) Now that we have these values, we get to the meat and potatoes of this algorithm.

                ALGORITHM TO FIND OPTIMAL CAVE TO VISIT, GET QUANTITY MINED AND EMERALDS, AVL :

                The algorithm is simple in nature.

                - Calculate EV values using the above formula, and store them in an EV_list. The best buying price is chosen
                using choose_best_trader(), which is a helper function. It chooses the best trader to sell the material to,
                then gets the buying price of that trader. This is because, obviously we want to sell our materials to the
                trader that's offering a higher price for it.

                - Now, we insert the EV_values into an AVL tree. This is because we will be able to carry out in-order traversal
                using the iterator of the AVL tree. The binary search runs in O(log C) time, thus it is efficient for this task.

                - For each iterations in the BST Iterator, we append the cave to a cave path list, which is an ordered collection
                of caves in which we want to traverse/plunder over.

                CALCULATE EMERALDS GAINED AND MATERIALS MINED
                - Set necessary variables, namely :
                    i) max_num_mined = cave's quantity of material mined.
                    ii) cave_material = cave's Material
                    iii) player_hunger = player's hunger
                    iv) hunger_

                - Loop through caves in cave_path_list,

                - Store the necessary values in lists using .append(), to return.


        -----COMPLEXITY JUSTIFICATION-----
        The complexity is O(M+T+P+C log C). I have added in-line comments to label the complexities below. We loop through
        the materials, traders, players in non-nested for loops, that's where I obtain O(M+T+P), then we loop through the caves
        and use the .add() function of heap, which is O(C) and O(log C) respectively. They are nested, so O(C * log C).
        Finally, combining all, we get O(M + T + P + C * log C)


        -----EXAMPLE-----
        For example, if cooked chicken cuts were offered with 100 hunger bars filled, and two players are playing the game.
        The two players names are Dhiren and Faw. Now, it's Dhiren's turn. I (Dhiren) have 100 hunger bars and I want to choose the
        best cave that maximises my emeralds at the end of the day. What does my AI do? Well, I look at how many material
        I can mine in the cave using my hunger bars (mining potential, MP). Then, I estimate my potential emeralds gained.
        I do this by looking at the traders and obtaining the best buying price for my material using choose_best_trader(), then
        obviously I sell it to that trader. Then, Faw repeats the entire process and we see who has the most emeralds at the end
        of the day.

        Returns:
            list[Food|None] -- list of Food items, None if no food purchased
            list[float] -- list of emerald balances of players
            list[tuple[Cave, float]|None] -- list of tuples which contains (caves, quantity of materials mined)
        """
        trader_material_list = []
        for traders in self.get_traders():
            trader_material_list.append(traders.get_material())

        ### FOOD THAT THE PLAYER WILL BUY ###
        # divide hunger bars with food price to find hunger bars to price ratio
        # have the player choose the highest ratio (optimal choice)

        food_list = self.food

        # Calculate hunger ratios and put in list
        # ratio = food_hunger_bar/price

        ratio_list = []

        for food in food_list:
            # Calculate ratio
            food_hunger_to_price_ratio = food.hunger_bars/food.get_food_price()
            # Add to list
            ratio_list.append(food_hunger_to_price_ratio)

        # Get max hunger ratio
        max_ratio = max(ratio_list)

        # Loop through food list and check
        for i in range(len(food_list)):
            if (food_list[i].hunger_bars)/(food_list[i].get_food_price()) - max_ratio == constants.EPSILON:
                food = food_list[i]

        # Deduct emeralds for food purchase
        self.set_balance(self.get_balance() - food.get_food_price())

        # Fill player's tummy with chosen food
        self.set_hunger(food.get_food_hunger_bars())
        # Calculate EV (Effort Value), the higher the EV, the later the cave gets visited.
        # <Cave: Castle Karstaag Ruins. 4 of [Netherite Ingot: 20.95🍗/💎]
        # Store EV values in list.

        EV_list = []
        for i in range(len(self.get_caves())):
            try:
                cave_EV = ((self.get_caves()[i].get_quantity() * self.get_caves()[i].get_material().get_mining_rate())) / (
                self.choose_best_trader(self.get_caves()[i].get_material()).current_deal()[1])
                EV_list.append(cave_EV)
            except AttributeError:
                EV_list.append(1000)

        ev_cave_tuples = []
        for cave, ev in zip(self.get_caves(), EV_list):
            ev_cave_tuples.append((ev, cave))


        # Sort EV values in ascending order in AVL
        # MR FAW, SORT EV_list in ascending order here using AVL.
        EV_avl_tree = AVLTree()

        for i in range(len(ev_cave_tuples)):
            EV_avl_tree[ev_cave_tuples[i][0]] = ev_cave_tuples[i][1]

        cave_path_list = []

        # Sorted EV's
        bst_iter = iter(EV_avl_tree)

        for EV in bst_iter:
            cave_path_list.append(EV_avl_tree[EV])

        # Initialise, to return later
        cave_and_material_tuple_list = []

        #------------EMERALD BALANCE AND MATERIAL MINED ALGO----------------

        # Loop through caves in cave path list
        for i in range(len(cave_path_list)):
            # Get maximum mine-able number for later use.
            max_num_mined = cave_path_list[i].get_quantity()

            # Get material info
            cave_material = cave_path_list[i].get_material()

            # Get player hunger bars
            player_hunger = self.get_hunger()

            # Calculate hunger to deduct (from player's hunger)
            hunger_to_deduct = round(max_num_mined * cave_material.get_mining_rate(), 2)

            # NOW, we obtain QUANTITY OF MATERIAL MINED using simple logic.
            # Try to mine using hunger bars, if can't mine all then use remaining hunger bars to mine.
            # if hunger to deduct is more than the remaining hunger bars for the player, then mine using
            # the player's remaining hunger bars, and find the number (a float).
            if hunger_to_deduct > player_hunger:
                quantity_of_material_mined = player_hunger / cave_material.get_mining_rate()
                cave_and_material_tuple_list.append((cave_path_list, quantity_of_material_mined))
            else:
                quantity_of_material_mined = max_num_mined
                cave_and_material_tuple_list.append((cave_path_list, quantity_of_material_mined))

            # Update player hunger after each cave-visit
            self.set_hunger(self.get_hunger() - hunger_to_deduct)

            try:
                # Calculate emerald balance.
                emeralds_gained = quantity_of_material_mined * self.choose_best_trader(cave_material).buying_price()
            except AttributeError:
                emeralds_gained = 0

            # Add emeralds
            self.set_balance(self.get_balance() + emeralds_gained)

        emerald_balance = self.get_balance()

        return (food, emerald_balance, cave_and_material_tuple_list)

    def choose_best_trader(self, material: Material) -> Trader:
        """
        Chooses trader that offers best price for the material.

        Arguments:
            material: material to get the best trader.

        Returns:
            Trader: Trader that offers best price for the material.

        Time Complexity Analysis:
            Best Case: O(1)
            Worst Case: O(n)
        """
        best_trader = None
        best_price = 0
        for trader in self.traders:
            if trader.current_deal()[0] == material and trader.current_deal()[1] > best_price:
                best_trader = trader
                best_price = trader.current_deal()[1]
        return best_trader

    def __str__(self) -> str:
        """
        Returns a string representation of the player.
        """
        return f"{self.name}"