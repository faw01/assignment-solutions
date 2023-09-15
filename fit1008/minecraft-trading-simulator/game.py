from __future__ import annotations

import material
from player import Player
from trader import *
from material import Material
from cave import Cave
from food import Food
from random_gen import RandomGen
from hash_table import LinearProbeTable
from heap import MaxHeap

class Game:
    """
    Game Class.

    Attributes:
        _materials (list[Material]): The list of materials in the game.
        _caves (list[Cave]): The list of caves in the game.
        _traders (list[Trader]): The list of traders in the game.

    Constants:
        MIN_MATERIALS {int} -- The minimum number of materials is 4.
        MAX_MATERIALS {int} -- The maximum number of materials is 10.

        MIN_CAVES {int} -- The minimum number of caves in the is 5.
        MAX_CAVES {int} -- The maximum number of caves in the is 10.

        MIN_TRADERS {int} -- The minimum number of traders is 4.
        MAX_TRADERS {int} -- The maximum number of traders is 8.

        MIN_FOOD {int} -- The minimum amount of food is 2.
        MAX_FOOD {int} -- The maximum amount of food is 5.
    """

    MIN_MATERIALS = 5
    MAX_MATERIALS = 10

    MIN_CAVES = 5
    MAX_CAVES = 10

    MIN_TRADERS = 4
    MAX_TRADERS = 8

    MIN_FOOD = 2
    MAX_FOOD = 5

    def __init__(self) -> None:
        """
        Initialises game attributes.
        """

        # Initialisation of attributes
        self._materials = []
        self._caves = []
        self._traders = []

    def initialise_game(self) -> None:
        """
        Initialise all game objects: Materials, Caves, Traders.
        # """
        N_MATERIALS = RandomGen.randint(self.MIN_MATERIALS, self.MAX_MATERIALS)
        # N_MATERIALS = 5
        self.generate_random_materials(N_MATERIALS)
        print("Materials:\n\t", end="")
        print("\n\t".join(map(str, self.get_materials())))
        N_CAVES = RandomGen.randint(self.MIN_CAVES, self.MAX_CAVES)
        self.generate_random_caves(N_CAVES)
        print("Caves:\n\t", end="")
        print("\n\t".join(map(str, self.get_caves())))
        N_TRADERS = RandomGen.randint(self.MIN_TRADERS, self.MAX_TRADERS)
        self.generate_random_traders(N_TRADERS)
        print("Traders:\n\t", end="")
        print("\n\t".join(map(str, self.get_traders())))

    def initialise_with_data(self, materials: list[Material], caves: list[Cave], traders: list[Trader]):
        """
        Initialise the game with the given materials, caves and traders.

        Arguments:
            materials {list[Material]} -- The list of materials in the game
            caves {list[Cave]} -- The list of caves in the game
            traders {list[Trader]} -- The list of traders in the game
        """
        self.set_materials(materials)
        self.set_caves(caves)
        self.set_traders(traders)

    def set_materials(self, mats: list[Material]) -> None:
        """
        Sets the materials in the game.
        """
        for mat in mats:
            self._materials.append(mat)

    def set_caves(self, caves: list[Cave]) -> None:
        """
        Sets the caves in the game.
        """
        for cave in caves:
            self._caves.append(cave)

    def set_traders(self, traders: list[Trader]) -> None:
        """
        Sets the traders in the game.
        """
        for trader in traders:
            self._traders.append(trader)

    def get_materials(self) -> list[Material]:
        """
        Returns the list of materials in the game.
        """
        return self._materials

    def get_caves(self) -> list[Cave]:
        """
        Returns the list of caves in the game.
        """
        return self._caves

    def get_traders(self) -> list[Trader]:
        """
        Returns the list of traders in the game.
        """
        return self._traders

    def generate_random_materials(self, amount):
        """
        Generates <amount> random materials using Material.random_material
        Generated materials must all have different names and different mining_rates.
        (You may have to call Material.random_material more than <amount> times.)

        Arguments:
            amount {int} -- The number of random materials to generate.
        """
        rand_mat_list = []

        # Keep calling random_material till the list gets filled up with <amount> materials,
        # only add the material if it is not in the list of materia ls
        while len(rand_mat_list) < amount:
            material_to_add = Material.random_material()
            name_of_material = material_to_add.name
            mining_rate_of_material = material_to_add.mining_rate

            mat_names_list = []
            # mat_mine_rate_list = []
            # Loop through existing material list and extract existing material names/mining rates.
            for i in range(len(rand_mat_list)):
                mat_names_list.append(rand_mat_list[i].name)
                # mat_mine_rate_list.append(rand_mat_list[i].mining_rate)

            # Check if material name and mining rate is in list, if not then add.
            if name_of_material not in mat_names_list:
                # if mining_rate_of_material not in mat_mine_rate_list:
                rand_mat_list.append(material_to_add)

        # Set material list to rand_mat_list
        self.set_materials(rand_mat_list)


    def generate_random_caves(self, amount):
        """
        Generates <amount> random caves using Cave.random_cave
        Generated caves must all have different names
        (You may have to call Cave.random_cave more than <amount> times.)

        Arguments:
            amount {int} -- The number of random caves to generate.
        """

        rand_cave_list = []

        while len(rand_cave_list) < amount:
            chosen_material = Material.random_material()
            # Make a random cave with a material from the list
            cave_to_add = Cave.random_cave([chosen_material])


            caves_names_list = []
            for i in range(len(rand_cave_list)):
                caves_names_list.append(rand_cave_list[i].name)

            # Check name
            if cave_to_add.name not in caves_names_list:
                rand_cave_list.append(cave_to_add)

        # Set cave
        self.set_caves(rand_cave_list)
            
    def generate_random_traders(self, amount):
        """
        Generates <amount> random traders by selecting a random trader class
        and then calling <TraderClass>.random_trader()
        and then calling set_all_materials with some subset of the already generated materials.
        Generated traders must all have different names
        (You may have to call <TraderClass>.random_trader() more than <amount> times.)

        Arguments:
            amount {int} -- The number of random traders to generate.
        """
        rand_trader_list = []
        trader_types = [RandomTrader, RangeTrader, HardTrader]

        while len(rand_trader_list) < amount:
            # trader to add select a random trader type
            trader_to_add = RandomGen.random_choice(trader_types).random_trader()
            # # trader_to_add = Trader.random_trader()
            # print()
            # print(trader_to_add)
            # print()

            # Obtain subset of materials from pre-generated ones.
            # Get pre-generated materials, shuffle the materials, then take subset of it.
            generated_materials = self.get_materials()
            RandomGen.random_shuffle(generated_materials)

            # Obtain subset
            max = RandomGen.randint(0, len(generated_materials) - 2)
            subset_mat = generated_materials[0:max]

            # Set subset to the trader_to_add
            trader_to_add.set_all_materials(subset_mat)

            trader_name_list = []
            # Obtain trader names and put it in a list
            for i in range(len(rand_trader_list)):
                trader_name_list.append(rand_trader_list[i].name)

            # If trader name not in list, then add
            if trader_to_add.name not in trader_name_list:
                rand_trader_list.append(trader_to_add)

        # Set trader list
        self.set_traders(rand_trader_list)


    def finish_day(self):
        """
        DO NOT CHANGE
        Affects test results.
        """
        for cave in self.get_caves():
            if cave.quantity > 0 and RandomGen.random_chance(0.2):
                cave.remove_quantity(RandomGen.random_float() * cave.quantity)
            else:
                cave.add_quantity(round(RandomGen.random_float() * 10, 2))
            cave.quantity = round(cave.quantity, 2)

class SoloGame(Game):

    def initialise_game(self) -> None:
        """
        Initialise all game objects: Materials, Caves, Traders.
        """
        super().initialise_game()
        self.player = Player.random_player()
        self.player.set_materials(self.get_materials())
        self.player.set_caves(self.get_caves())
        self.player.set_traders(self.get_traders())

    def initialise_with_data(self, materials: list[Material], caves: list[Cave], traders: list[Trader], player_names: list[int], emerald_info: list[float]):
        """
        Initialise the game with the given materials, caves and traders.
        
        Arguments:
            materials {list[Material]} -- The list of materials in the game.
            caves {list[Cave]} -- The list of caves in the game.
            traders {list[Trader]} -- The list of traders in the game.
            player_names {list[int]} -- The list of player names.
            emerald_info {list[float]} -- The list of emerald info for each player.
        """
        super().initialise_with_data(materials, caves, traders)
        self.player = Player(player_names[0], emeralds=emerald_info[0])
        self.player.set_materials(self.get_materials())
        self.player.set_caves(self.get_caves())
        self.player.set_traders(self.get_traders())

    def simulate_day(self):
        """
        Generates and displays the deals, foods and caves for the day.
        """
        # raise NotImplementedError()
        # 1. Traders make deals
        for trader in self.get_traders():
            trader.generate_deal()
        print("Traders Deals:\n\t", end="")
        print("\n\t".join(map(str, self.get_traders())))
        # 2. Food is offered
        food_num = RandomGen.randint(self.MIN_FOOD, self.MAX_FOOD)
        foods = []
        for _ in range(food_num):
            foods.append(Food.random_food())
        print("\nFoods:\n\t", end="")
        print("\n\t".join(map(str, foods)))
        self.player.set_foods(foods)
        # 3. Select one food item to purchase
        food, balance, caves = self.player.select_food_and_caves()
        # print(food, balance, caves)
        # # 4. Quantites for caves is updated, some more stuff is added.
        self.verify_output_and_update_quantities(food, balance, caves)

    def verify_output_and_update_quantities(self, food: Food | None, balance: float, caves: list[tuple[Cave, float]]) -> None:
        """
        Verifies foods, balances, quantities and updates the quantities in the cave
        """

        # Check if food is purchasable.
        if not isinstance(food, Food) and not food is None:
            raise ValueError("The food has to be Food")


        # Check if the remaining balance is correct.
        if balance < 0:
            raise ValueError("The balance cannot be negative.")


        # Check if quantities are in line with what the player provided.
        for cave, quantity_mined_by_player in caves:
            if quantity_mined_by_player > cave[0].get_max_quantity():
                raise ValueError("The quantity mined by the player cannot be more than the max quantity in the cave.")

            # Remove quuantity
            cave[0].remove_quantity(quantity_mined_by_player)


class MultiplayerGame(Game):

    MIN_PLAYERS = 2
    MAX_PLAYERS = 5

    def __init__(self) -> None:
        super().__init__()
        self.players = []

    def initialise_game(self) -> None:
        """
        Initialises all game objects: Materials, caves, traders and players
        """
        super().initialise_game()
        N_PLAYERS = RandomGen.randint(self.MIN_PLAYERS, self.MAX_PLAYERS)
        self.generate_random_players(N_PLAYERS)
        for player in self.players:
            player.set_materials(self.get_materials())
            player.set_caves(self.get_caves())
            player.set_traders(self.get_traders())
        print("Players:\n\t", end="")
        print("\n\t".join(map(str, self.players)))

    def generate_random_players(self, amount) -> None:
        """Generate <amount> random players. Don't need anything unique, but you can do so if you'd like."""
        raise NotImplementedError()

    def initialise_with_data(self, materials: list[Material], caves: list[Cave], traders: list[Trader], player_names: list[int], emerald_info: list[float]):
        """
        Initialise the game with the given materials, caves and traders.
        
        Arguments:
            materials {list[Material]} -- The list of materials in the game.
            caves {list[Cave]} -- The list of caves in the game.
            traders {list[Trader]} -- The list of traders in the game.
            player_names {list[int]} -- The list of player names.
            emerald_info {list[float]} -- The list of emerald info for each player.
        """
        super().initialise_with_data(materials, caves, traders)
        for player, emerald in zip(player_names, emerald_info):
            self.players.append(Player(player, emeralds=emerald))
            self.players[-1].set_materials(self.get_materials())
            self.players[-1].set_caves(self.get_caves())
            self.players[-1].set_traders(self.get_traders())
        print("Players:\n\t", end="")
        print("\n\t".join(map(str, self.players)))

    def simulate_day(self):
        """
        Generates and displays the deals, foods and caves for the day.
        """
        # 1. Traders make deals
        print("Traders Deals:\n\t", end="")
        for traders in self.get_traders():
            traders.generate_deal()
        print("\n\t".join(map(str, self.get_traders())))
        # 2. Food is offered
        offered_food = Food.random_food()
        print(f"\nFoods:\n\t{offered_food}")
        # 3. Each player selects a cave - The game does this instead.
        foods, balances, caves = self.select_for_players(offered_food)
        # 4. Quantites for caves is updated, some more stuff is added.
        self.verify_output_and_update_quantities(foods, balances, caves)

    def choose_best_trader(self, material: Material) -> Trader:
        """
        Chooses trader that offers best price for the material. If there are multiple traders with the same price, choose the highest.
        """
        # Chooses trader that offers best price for the material. If there are multiple traders with the same price, choose the highest.
        best_trader = None
        best_price = 0
        for trader in self.get_traders():
            if trader.get_material() == material:
                if trader.current_deal()[1] > best_price:
                    best_trader = trader
                    best_price = trader.current_deal()[1]
        # print(f"Best trader for {material} is {best_trader} with price {best_price}")
        return best_trader

    def check_if_trader_sells_material(self, trader: Trader, material: Material) -> bool:
        """
        Checks if the trader sells the material.
        """
        return trader.get_material() == material

    def select_for_players(self, food: Food) -> tuple[list[Food|None], list[float], list[tuple[Cave, float]|None]]:
        """
        Returns list of foods purchased, list of emerald balances and list of tuples of caves each player visits and
        quantity of material mined.

        -----LENGTHY DOCSTRING DESCRIBING MOTIVATION FOR APPROACH-----

        1. List of foods that players buy.
            - Loop through players, get emerald balance, purchase food, add to purchased list, fill up hunger bar.
            - The purchased list will be returned later on.
            - If player balance is lesser than the price of the purchased food, that player cannot go mining, so we
              save his details in variables like (not_playing_player_xxx)
            - His final emeralds will be the same as the initial, later we will use it to append to a list.

        2. List of what caves each player visits, with quantity of material mined. (Emerald balance for each player is
           calculated here as well).
            a) Set necessary variables, namely :
                i) mining_potential (MP) = initial_player_hunger_bars / hunger_required_to_mine_entire_cave
                ii) hunger_required_to_mine_entire_cave = mining rate of material in cave x max quantity in cave.
                iii) potential_emeralds_gained (PE) = mining_potential (MP) X trader_buying_price

                The MP is basically "how much material a player can mine with his initial hunger bar". It is a
                constant for each cave, when the quantity is constant. The MP changes when the quantity changes,
                which we will handle with a heap later.

                The PE is basically the potential emeralds gained. It is a function of MP multiplied with trader
                buying price, which basically means "I take my material and sell it to the best trader, how many
                emeralds can I potentially make?"

                The higher the PE value, the more optimal the cave is to be mined. (Eureka, we can use Max Heap here!)

            b) Now that we have these values, we get to the meat and potatoes of this algorithm.

                ALGORITHM TO FIND OPTIMAL CAVE TO VISIT, GET QUANTITIY MINED AND EMERALDS, USING HASH TABLE AND MAX HEAP :

                The algorithm is simple in nature.

                - Create a hash table that maps PE values to Cave objects. This is because the heap can only store single
                  values, and we cannot get the Cave just with the PE value. Thus, this hash table is required.

                - Now, we create a MaxHeap() called get_cave_heap, with an initial size of len(potential_emeralds_gained_list)
                  because that is the maximum.

                - Now, we loop through the players that are actually playing the game. If the player did not buy the food,
                  then we do not loop through him because we already know he does not go to mine and thus his emerald
                  balance calculation will be trivial, it will just be the initial emerald balance.

                - In the loop, since each player has to go one after the other to mine in the cave, all we have to do is
                  get the MAX PE, which will map to the most optimal cave to mine at. To get the cave, we use our hash table
                  with the key being the PE value.

                - Now, we have the most optimal cave, and we obtain 4 variables, namely :
                    i) cave_chosen_max_quantity = cave_chosen.get_max_quantity()
                    ii) cave_chosen_hunger_required_to_mine_entire_cave = cave_chosen.get_material().get_mining_rate() * cave_chosen_max_quantity
                    iii) cave_chosen_mining_potential = min(initial_player_hunger_bars / cave_chosen_hunger_required_to_mine_entire_cave * cave_chosen_max_quantity, cave_chosen.get_quantity())
                    iv) cave_chosen_trader_buying_price = self.choose_best_trader(cave_chosen.get_material()).current_deal()[1]

                    The first two variables are self-explanatory, as explained earlier.
                    Note : cave_chosen_mining_potential has to take into account the min() due to the fact that the player
                           cannot mine more than the max quantity of the cave.
                           We also have a helper function called choose_best_trader(Material) that chooses the best trader
                           that sells a Material with the highest price. This is to optimise buying price.

                - Using the max PE obtained as the key, we get the cave_chosen from the hash table.

                - Now, we obtain the quantity of materials mined using this logic :
                    Try to mine using hunger bars, if can't mine all then use remaining hunger bars to mine.
                    if hunger to deduct is more than the remaining hunger bars for the player, then mine using
                    the player's remaining hunger bars, and find the number (a float).

                - Then, we get the new PE value of the cave after the materials have been mined, and dump this new
                  PE value in the MaxHeap.

                - Repeat.

                CALCULATE EMERALDS GAINED.
                emeralds_gained = quantity_of_material_mined * best_trader_buying_price

                - add emeralds using .get_balance() and emeralds_gained()

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
        not_playing = False

        # ----------LIST OF FOODS THAT PLAYERS BUY----------
        list_of_foods_purchased = []
        actual_players = []
        # Loop through players, get emerald balance, purchase food, add to purchased list,
        # fill up hunger bar.
        player_balance_list = []
        cave_and_quantity_mined_tuple_list = []
        trader_material_list = []

        for traders in self.get_traders():
            trader_material_list.append(traders.get_material())

        for i in range(len(self.players)):
            # Get emerald balance
            player_balance = self.players[i].get_balance()

            # Purchase food, add to list.
            if player_balance < food.get_food_price():
                list_of_foods_purchased.append(None)
                not_playing_player = self.players[i]
                not_playing_player_final_emeralds = self.players[i].get_balance()
                not_playing_player_cave = None
                not_playing_player_index = i
                not_playing = True
            else:
                list_of_foods_purchased.append(food)
                self.players[i].set_balance(self.players[i].get_balance() - food.get_food_price())

                # Fill up hunger bar
                self.players[i].set_hunger(self.players[i].get_hunger() + food.get_food_hunger_bars())
                actual_players.append(self.players[i])


        # ----------LIST OF CAVES EACH PLAYER VISITS----------
        initial_player_hunger_bars = food.get_food_hunger_bars()  # constant because everyone gets same food
        mining_potential_list = []
        potential_emeralds_gained_list = []
        hunger_required_to_mine_cave_list = []
        # MP LIST AND PE LIST
        for i in range(len(self._caves)):
            hunger_required_to_mine_cave = self._caves[i].get_material().get_mining_rate() * self._caves[
                i].get_quantity()
            hunger_required_to_mine_cave_list.append(hunger_required_to_mine_cave)
            try:
                mining_potential = min(
                    (initial_player_hunger_bars / hunger_required_to_mine_cave) * self._caves[i].get_max_quantity(),
                    self._caves[i].get_quantity())
                mining_potential_list.append(mining_potential)
            except ZeroDivisionError:
                mining_potential_list.append(0)

            # check if trader sells material
            if self.get_caves()[i].get_material() in trader_material_list:
                potential_emeralds_gained = mining_potential * self.choose_best_trader(self.get_caves()[i].get_material()).current_deal()[1]
                potential_emeralds_gained_list.append(potential_emeralds_gained)
            else:
                potential_emeralds_gained_list.append(0)


        # Create PE to cave hash table
        pe_to_cave_hash = LinearProbeTable(20)

        # PE (rounded off to 2 dp and str()) = key, Cave = Cave object
        for i in range(len(potential_emeralds_gained_list)):
            PE_key = str(round(potential_emeralds_gained_list[i], 2))
            pe_to_cave_hash[PE_key] = self._caves[i]

        # ALGORITHM
        get_cave_heap = MaxHeap(len(potential_emeralds_gained_list))

        # Fill up heap with initial PE values
        for i in range(len(potential_emeralds_gained_list)):
            get_cave_heap.add(potential_emeralds_gained_list[i])

        # Loop through actual players
        for i in range(len(actual_players)):
            # Get PE of cave
            PE_cave_chosen = get_cave_heap.get_max()

            # Get cave
            key = str(round(PE_cave_chosen, 2))
            cave_chosen = pe_to_cave_hash[key]

            cave_chosen_max_quantity = cave_chosen.get_max_quantity()
            cave_chosen_hunger_required_to_mine_entire_cave = cave_chosen.get_material().get_mining_rate() * cave_chosen_max_quantity
            cave_chosen_mining_potential = min(initial_player_hunger_bars / cave_chosen_hunger_required_to_mine_entire_cave * cave_chosen_max_quantity, cave_chosen.get_quantity())
            cave_chosen_trader_buying_price = self.choose_best_trader(cave_chosen.get_material()).current_deal()[1]

            # Calculate hunger to deduct (from player's hunger)
            max_num_mined = cave_chosen.get_quantity()
            cave_material = cave_chosen.get_material()

            hunger_to_deduct = round(max_num_mined * cave_material.get_mining_rate(), 2)

            # NOW, we obtain QUANTITY OF MATERIAL MINED using simple logic.
            # Try to mine using hunger bars, if can't mine all then use remaining hunger bars to mine.
            # if hunger to deduct is more than the remaining hunger bars for the player, then mine using
            # the player's remaining hunger bars, and find the number (a float).
            if hunger_to_deduct > initial_player_hunger_bars:
                quantity_of_material_mined = initial_player_hunger_bars / cave_material.get_mining_rate()
                cave_and_quantity_mined_tuple_list.append((cave_chosen, quantity_of_material_mined))
            else:
                quantity_of_material_mined = max_num_mined
                cave_and_quantity_mined_tuple_list.append((cave_chosen, quantity_of_material_mined))

            new_PE = (cave_chosen_max_quantity - cave_chosen_mining_potential) * cave_chosen_trader_buying_price

            # Update hash table with new PE value mapped to cave chosen
            new_PE_key = str(round(new_PE, 2))
            pe_to_cave_hash[new_PE_key] = cave_chosen

            # Dump new PE back in heap, then repeat.
            get_cave_heap.add(new_PE)

            # Calculate emerald balance.
            emeralds_gained = quantity_of_material_mined * self.choose_best_trader(cave_material).buying_price()

            # Add emeralds
            actual_players[i].set_balance(actual_players[i].get_balance() + emeralds_gained)
            player_balance_list.append(actual_players[i].get_balance())

        if not_playing:
            # Add not playing player info to list
            # list_of_foods_purchased.insert(not_playing_player_index, not)
            cave_and_quantity_mined_tuple_list.insert(not_playing_player_index, not_playing_player_cave)
            player_balance_list.insert(not_playing_player_index, not_playing_player_final_emeralds)

        return (list_of_foods_purchased, player_balance_list, cave_and_quantity_mined_tuple_list)

    def verify_output_and_update_quantities(self, foods: list[Food | None], balances: list[float], caves: list[tuple[Cave, float]|None]) -> None:
        """
        Verifies foods, balances, quantities and updates the quantities in the cave
        """

        caves_quantity_mined_list_tuples = caves

        # Check if food is purchasable.
        for i in range(len(foods)):
            if not isinstance(foods[i], Food) and not foods[i] is None:
                raise ValueError("The food has to be Food or None.")


        # Check if the remaining balance is correct.
        for i in range(len(balances)):
            if balances[i] < 0:
                raise ValueError("The balance cannot be negative.")


        # Check if quantities are in line with what the player provided.
        for cave, quantity_mined_by_player in caves_quantity_mined_list_tuples:
            if quantity_mined_by_player > cave.get_max_quantity():
                raise ValueError("The quantity mined by the player cannot be more than the max quantity in the cave.")


        # Update the quantities within each cave accordingly.
        cave = caves_quantity_mined_list_tuples[i][0]
        print()
        print("BEFORE")
        print()
        print(f'the cave is {cave}')

        quantity_mined_by_player = caves_quantity_mined_list_tuples[i][1]
        print(f'the quantity mined by the player is {quantity_mined_by_player}')

        cave.remove_quantity(quantity_mined_by_player)

        print()
        print("AFTER")
        print()
        print(f'the cave is {cave}')


if __name__ == "__main__":
    pass