from poke_team import Action, Criterion, PokeTeam
from random_gen import RandomGen
from pokemon import Bulbasaur, Charizard, Charmander, Gastly, Squirtle, Eevee
from tests.base_test import BaseTest


class TestPokeTeam(BaseTest):

    def test_random(self):
        RandomGen.set_seed(123456789)
        t = PokeTeam.random_team("Cynthia", 0)
        pokemon = []
        while not t.is_empty():
            pokemon.append(t.retrieve_pokemon())
        expected_classes = [Squirtle, Gastly, Eevee, Eevee, Eevee, Eevee]
        self.assertEqual(len(pokemon), len(expected_classes))
        for p, e in zip(pokemon, expected_classes):
            self.assertIsInstance(p, e)

    def test_regen_team(self):
        RandomGen.set_seed(123456789)
        t = PokeTeam.random_team("Cynthia", 2, team_size=4, criterion=Criterion.HP)
        # This should end, since all pokemon are fainted, slowly.
        while not t.is_empty():
            p = t.retrieve_pokemon()
            p.lose_hp(1)
            t.return_pokemon(p)
        t.regenerate_team()
        pokemon = []
        while not t.is_empty():
            pokemon.append(t.retrieve_pokemon())
        expected_classes = [Bulbasaur, Eevee, Charmander, Gastly]
        self.assertEqual(len(pokemon), len(expected_classes))
        for p, e in zip(pokemon, expected_classes):
            self.assertIsInstance(p, e)

    def test_battle_option_attack(self):
        t = PokeTeam("Wallace", [1, 0, 0, 0, 0], 1, PokeTeam.AI.ALWAYS_ATTACK)
        p = t.retrieve_pokemon()
        e = Eevee()
        self.assertEqual(t.choose_battle_option(p, e), Action.ATTACK)

    def test_special_mode_1(self):
        t = PokeTeam("Lance", [1, 1, 1, 1, 1], 1, PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE)
        # C B S G E
        t.special()
        # S G E B C
        pokemon = []
        while not t.is_empty():
            pokemon.append(t.retrieve_pokemon())
        expected_classes = [Squirtle, Gastly, Eevee, Bulbasaur, Charmander]
        self.assertEqual(len(pokemon), len(expected_classes))
        for p, e in zip(pokemon, expected_classes):
            self.assertIsInstance(p, e)

    def test_string(self):
        t = PokeTeam("Dawn", [1, 1, 1, 1, 1], 2, PokeTeam.AI.RANDOM, Criterion.DEF)
        self.assertEqual(str(t),
                         "Dawn (2): [LV. 1 Gastly: 6 HP, LV. 1 Squirtle: 11 HP, LV. 1 Bulbasaur: 13 HP, LV. 1 Eevee: 10 HP, LV. 1 Charmander: 9 HP]")

    # |UNIT TESTS FOR TASK 3|
    def test_random_team(self):
        """
        Test that the random_team method successfully generates a random team based on the rules provided in the assignment spec
        """
        # Test 1 - Tests that the team generated is correct with only the trainer name and battle mode as the arguments
        RandomGen.set_seed(123456)  # Sets the seed to force a random team
        t = PokeTeam.random_team("Cynthia", 0)  # Creates a random team with battle mode 0
        pokemon = []  # Creates an empty list to store the Pokemon in
        while not t.is_empty():
            pokemon.append(t.retrieve_pokemon())  # Adds the Pokemon to the list
        expected_classes = [Bulbasaur, Bulbasaur, Squirtle, Gastly,
                            Eevee]  # Creates a list of the expected Pokemon classes
        self.assertEqual(len(pokemon),
                         len(expected_classes))  # Checks that the number of Pokemon in the team is correct
        for p, e in zip(pokemon, expected_classes):
            self.assertIsInstance(p,
                                  e)  # Checks that the Pokemon in the team are of the correct type and in the correct order

        # Test 2 - Tests that the team generated is correct with the trainer name, battle mode and team size as the arguments
        RandomGen.set_seed(123)  # Sets the seed to force a random team
        t = PokeTeam.random_team("Dawn", 1,
                                 team_size=4)  # Creates a random team with battle mode 1 and a team size of 4
        pokemon = []  # Creates an empty list to store the Pokemon in
        while not t.is_empty():
            pokemon.append(t.retrieve_pokemon())
        expected_classes = [Charmander, Bulbasaur, Bulbasaur, Gastly]  # Creates a list of the expected Pokemon classes
        self.assertEqual(len(pokemon),
                         len(expected_classes))  # Checks that the number of Pokemon in the team is correct
        for p, e in zip(pokemon, expected_classes):
            self.assertIsInstance(p,
                                  e)  # Checks that the Pokemon in the team are of the correct type and in the correct order

        # Test 3 - Tests that the team generated is correct with the trainer name, battle mode, team size and criterion as the arguments
        RandomGen.set_seed(123456)  # Sets the seed to force a random team
        t = PokeTeam.random_team("Misty", 2, team_size=5,
                                 criterion=Criterion.HP)  # Creates a random team with battle mode 2, a team size of 5 and a criterion of HP
        pokemon = []  # Creates an empty list to store the Pokemon in
        while not t.is_empty():
            pokemon.append(t.retrieve_pokemon())  # Adds the Pokemon to the list
        expected_classes = [Squirtle, Squirtle, Eevee, Gastly, Gastly]  # Creates a list of the expected Pokemon classes
        self.assertEqual(len(pokemon),
                         len(expected_classes))  # Checks that the number of Pokemon in the team is correct
        for p, e in zip(pokemon, expected_classes):
            self.assertIsInstance(p,
                                  e)  # Checks that the Pokemon in the team are of the correct type and in the correct order

    def test_return_pokemon(self):
        """
        Tests whether the Pokemon that are returned to the ADT are correct.
        """
        # Test 1 - Battle mode 0
        t = PokeTeam("Cynthia", [1, 1, 1, 1, 1], 0, PokeTeam.AI.RANDOM) # Creates a PokeTeam with battle mode 0
        p = t.retrieve_pokemon() # Retrieves the first Pokemon in the team
        t.return_pokemon(p) # Returns the Pokemon to the team
        self.assertEqual(str(t), "Cynthia (0): [LV. 1 Charmander: 9 HP, LV. 1 Bulbasaur: 13 HP, LV. 1 Squirtle: 11 HP, LV. 1 Gastly: 6 HP, LV. 1 Eevee: 10 HP]")

        # Test 2 - Battle mode 1
        t = PokeTeam("Dawn", [1, 1, 1, 1, 1], 1, PokeTeam.AI.RANDOM) # Creates a PokeTeam with battle mode 1
        p = t.retrieve_pokemon() # Retrieves the first Pokemon in the team (rear of CircularQueue)
        t.return_pokemon(p) # Returns the Pokemon to the team
        self.assertEqual(str(t), "Dawn (1): [LV. 1 Bulbasaur: 13 HP, LV. 1 Squirtle: 11 HP, LV. 1 Gastly: 6 HP, LV. 1 Eevee: 10 HP, LV. 1 Charmander: 9 HP]")

        # Test 3 - Battle mode 2
        t = PokeTeam("Misty", [1, 1, 1, 1, 1], 2, PokeTeam.AI.RANDOM, criterion=Criterion.HP) # Creates a PokeTeam with battle mode 2 with a criterion of HP
        self.assertEqual(str(t), "Misty (2): [LV. 1 Bulbasaur: 13 HP, LV. 1 Squirtle: 11 HP, LV. 1 Eevee: 10 HP, LV. 1 Charmander: 9 HP, LV. 1 Gastly: 6 HP]")
        t.poke_team_adt[0].value.lose_hp(5) # Reduces the HP of the first Pokemon in the team by 5
        p = t.retrieve_pokemon() # Retrieves the first Pokemon in the team
        t.return_pokemon(p) # Returns the Pokemon to the team
        self.assertEqual(str(t), "Misty (2): [LV. 1 Squirtle: 11 HP, LV. 1 Eevee: 10 HP, LV. 1 Charmander: 9 HP, LV. 1 Bulbasaur: 8 HP, LV. 1 Gastly: 6 HP]")

    def test_retrieve_pokemon(self):
        """
        Tests whether the Pokemon that are retrieved from each ADT are correct.
        """
        # Test 1 - Battle mode 0
        t = PokeTeam("Cynthia", [1, 1, 1, 1, 1], 0, PokeTeam.AI.RANDOM)  # Creates a PokeTeam with battle mode 0
        p = t.retrieve_pokemon()  # Retrieves the first Pokemon in the team (top of ArrayStack)

        # Check if retrieved Pokemon is a Charmander (because retrieve from top of stack)
        self.assertIsInstance(p, Charmander)

        # Check if Charmander is retrieved from the team and the string printing is correct
        self.assertEqual(str(t), "Cynthia (0): [LV. 1 Bulbasaur: 13 HP, LV. 1 Squirtle: 11 HP, LV. 1 Gastly: 6 HP, LV. 1 Eevee: 10 HP]")


        # Test 2 - Battle mode 1
        t = PokeTeam("Dawn", [1, 1, 1, 1, 1], 1, PokeTeam.AI.RANDOM)  # Creates a PokeTeam with battle mode 1
        p = t.retrieve_pokemon()  # Retrieves the last Pokemon in a team (rear of CircularQueue)

        # Check if retrieved Pokemon is an Eevee (because retrieve from back of the queue)
        self.assertIsInstance(p, Charmander)

        # Check if Eevee is retrieved from the team and the string printing is correct (NOTE : The "rear" of the CircularQueue is the "front" of the string)
        self.assertEqual(str(t), "Dawn (1): [LV. 1 Bulbasaur: 13 HP, LV. 1 Squirtle: 11 HP, LV. 1 Gastly: 6 HP, LV. 1 Eevee: 10 HP]")


        # Test 3 - Battle mode 2
        t = PokeTeam("Misty", [1, 1, 1, 1, 1], 2, PokeTeam.AI.RANDOM, criterion=Criterion.HP)  # Creates a PokeTeam with battle mode 2 with a criterion of HP
        self.assertEqual(str(t), "Misty (2): [LV. 1 Bulbasaur: 13 HP, LV. 1 Squirtle: 11 HP, LV. 1 Eevee: 10 HP, LV. 1 Charmander: 9 HP, LV. 1 Gastly: 6 HP]")
        p = t.retrieve_pokemon()  # Retrieves the first Pokemon in the team

        # Check if retrieved Pokemon is a Bulbasaur (because it has the highest HP amongst all the other Pokemon in the team)
        self.assertIsInstance(p, Bulbasaur)

        # Check if Bulbasaur is retrieved from the team and the string printing is correct, based on descending HP
        self.assertEqual(str(t), "Misty (2): [LV. 1 Squirtle: 11 HP, LV. 1 Eevee: 10 HP, LV. 1 Charmander: 9 HP, LV. 1 Gastly: 6 HP]")

    def test_special(self):
        """
        Tests the special() method for battle modes 0, 1 and 2.
        """
        # Test 1 - Battle mode 0
        t = PokeTeam("Cynthia", [1, 1, 1, 1, 1], 0, PokeTeam.AI.RANDOM)  # Creates a PokeTeam with battle mode 0
        self.assertEqual(str(t),
                         "Cynthia (0): [LV. 1 Charmander: 9 HP, LV. 1 Bulbasaur: 13 HP, LV. 1 Squirtle: 11 HP, LV. 1 Gastly: 6 HP, LV. 1 Eevee: 10 HP]")
        t.special()  # Performs special swapping by swapping the position of the first and last Pokemon in the team (Charmander swaps with Eevee)
        self.assertEqual(str(t),
                         "Cynthia (0): [LV. 1 Eevee: 10 HP, LV. 1 Bulbasaur: 13 HP, LV. 1 Squirtle: 11 HP, LV. 1 Gastly: 6 HP, LV. 1 Charmander: 9 HP]")

        # Test 2 - Battle mode 1
        t = PokeTeam("Dawn", [1, 1, 1, 1, 1], 1, PokeTeam.AI.RANDOM)  # Creates a PokeTeam with battle mode 1
        self.assertEqual(str(t),
                         "Dawn (1): [LV. 1 Charmander: 9 HP, LV. 1 Bulbasaur: 13 HP, LV. 1 Squirtle: 11 HP, LV. 1 Gastly: 6 HP, LV. 1 Eevee: 10 HP]")
        t.special()  # Performs special swapping by swapping the first and second halves of the team (the second half includes the middle pokemon for odd team numbers) and reverses the order of the previously front half of the team.
        self.assertEqual(str(t),
                         "Dawn (1): [LV. 1 Squirtle: 11 HP, LV. 1 Gastly: 6 HP, LV. 1 Eevee: 10 HP, LV. 1 Bulbasaur: 13 HP, LV. 1 Charmander: 9 HP]")

        # Test 3 - Battle mode 2
        t = PokeTeam("Misty", [1, 1, 1, 1, 1], 2, PokeTeam.AI.RANDOM,
                     criterion=Criterion.HP)  # Creates a PokeTeam with battle mode 2 with a criterion of HP
        self.assertEqual(str(t),
                         "Misty (2): [LV. 1 Bulbasaur: 13 HP, LV. 1 Squirtle: 11 HP, LV. 1 Eevee: 10 HP, LV. 1 Charmander: 9 HP, LV. 1 Gastly: 6 HP]")
        t.special()  # Performs special swapping by reversing the sorting order of the team based on the criterion (HP) | Order becomes HP ascending from first to last Pokemon
        self.assertEqual(str(t),
                         "Misty (2): [LV. 1 Gastly: 6 HP, LV. 1 Charmander: 9 HP, LV. 1 Eevee: 10 HP, LV. 1 Squirtle: 11 HP, LV. 1 Bulbasaur: 13 HP]")
        t.special()  # Performs special swapping by reversing the sorting order of the team based on the criterion (HP) | Order becomes HP descending from first to last Pokemon
        self.assertEqual(str(t),
                         "Misty (2): [LV. 1 Bulbasaur: 13 HP, LV. 1 Squirtle: 11 HP, LV. 1 Eevee: 10 HP, LV. 1 Charmander: 9 HP, LV. 1 Gastly: 6 HP]")

    def test_regenerate_team(self):
        """
        Tests whether the team is regenerated from the same battle numbers, heal_count is reset, and sorting order flag is reset.
        """

        # Test 1 - Check whether the team regenerates when a Pokemon is fainted (Charmander in this case :( )
        t = PokeTeam("Dhiren", [1, 1, 1, 1, 1], 0, PokeTeam.AI.RANDOM)

        # Kill the first Pokemon (Charmander 9 HP) in the team and return it to the team
        p = t.retrieve_pokemon()
        p.lose_hp(9)
        t.return_pokemon(p)

        # Check that team is missing the dead Charmander
        self.assertEqual(str(t), "Dhiren (0): [LV. 1 Bulbasaur: 13 HP, LV. 1 Squirtle: 11 HP, LV. 1 Gastly: 6 HP, LV. 1 Eevee: 10 HP]")

        # Regenerate the team and check whether the Charmander is there or not
        t.regenerate_team()
        self.assertEqual(str(t), "Dhiren (0): [LV. 1 Charmander: 9 HP, LV. 1 Bulbasaur: 13 HP, LV. 1 Squirtle: 11 HP, LV. 1 Gastly: 6 HP, LV. 1 Eevee: 10 HP]")


        # Test 2 - Check whether the heal count of the team is 0 after regenerating the team
        t = PokeTeam("Faw", [1, 1, 1, 1, 1], 0, PokeTeam.AI.RANDOM)

        # Set heal count of team to be 1 and check whether that is the case or not
        t.set_heal_count(1)
        self.assertEqual(t.get_heal_count(), 1)

        # Regenerate team (to make heal count 0)
        t.regenerate_team()

        # Check heal_count of team == 0
        self.assertEqual(t.get_heal_count(), 0)


        # Test 3 - Ensure sorting order of team is reset to be 1
        t = PokeTeam("Rys", [1, 1, 1, 1, 1], 0, PokeTeam.AI.RANDOM)

        # Set sorting order to be -1
        t.sorting_order = 1

        # Regenerate team
        t.regenerate_team()

        # Check sorting order == 1
        self.assertEqual(t.sorting_order, 1)


    def test_str(self):
        """
        Test that the str method returns the correct String representation of the PokeTeam.
        """
        # Test 1 - Test string method for Battle Mode 0
        t = PokeTeam("Misty", [1, 1, 1, 1, 1], 0, PokeTeam.AI.RANDOM)
        self.assertEqual(str(t),
                         "Misty (0): [LV. 1 Charmander: 9 HP, LV. 1 Bulbasaur: 13 HP, LV. 1 Squirtle: 11 HP, LV. 1 Gastly: 6 HP, LV. 1 Eevee: 10 HP]")

        # Test 2 -  Test string method for Battle Mode 1
        t = PokeTeam("Brock", [1, 1, 1, 1, 1], 1, PokeTeam.AI.RANDOM, Criterion.SPD)
        self.assertEqual(str(t),
                         "Brock (1): [LV. 1 Charmander: 9 HP, LV. 1 Bulbasaur: 13 HP, LV. 1 Squirtle: 11 HP, LV. 1 Gastly: 6 HP, LV. 1 Eevee: 10 HP]")

        # Test 3 -  Tests when the criterion is defence for battle mode 2
        t = PokeTeam("Misty", [1, 1, 1, 1, 1], 2, PokeTeam.AI.RANDOM, Criterion.DEF)
        self.assertEqual(str(t),
                         "Misty (2): [LV. 1 Gastly: 6 HP, LV. 1 Squirtle: 11 HP, LV. 1 Bulbasaur: 13 HP, LV. 1 Eevee: 10 HP, LV. 1 Charmander: 9 HP]")

    def test_is_empty(self):
        """
        Test that the is_empty method works correctly
        """
        # Test 1 - PokeTeam is empty
        t = PokeTeam("Misty", [0, 0, 0, 0, 0], 0, PokeTeam.AI.RANDOM)
        self.assertTrue(t.is_empty())

        # Test 2 - PokeTeam is not empty
        t = PokeTeam("Deliah", [1, 1, 1, 1, 1], 0, PokeTeam.AI.RANDOM)
        self.assertFalse(t.is_empty())

        # Test 3 - Pokemon faints
        t = PokeTeam("Red", [1, 0, 0, 0, 0], 0, PokeTeam.AI.RANDOM)
        self.assertFalse(t.is_empty())
        t.poke_team_adt[0].lose_hp(10)
        p = t.retrieve_pokemon()
        t.return_pokemon(p)
        self.assertTrue(t.is_empty())

    def test_choose_battle_option(self):
        """
        Tests whether the correct battle option is chosen or not.
        """
        # Test 1 - Tests when the AI is ALWAYS_ATTACK
        t = PokeTeam("Misty", [1, 1, 1, 1, 1], 0, PokeTeam.AI.ALWAYS_ATTACK)
        p = t.retrieve_pokemon()
        t2 = PokeTeam("Cynthia", [1, 1, 1, 1, 1], 0, PokeTeam.AI.ALWAYS_ATTACK)
        p2 = t2.retrieve_pokemon()
        self.assertEqual(t.choose_battle_option(p, p2), Action.ATTACK)

        # Test 2 - Tests when the AI is SWAP_ON_SUPER_EFFECTIVE for Action.SWAP
        t = PokeTeam("Misty", [1, 1, 1, 1, 1], 0, PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE)
        p = t.retrieve_pokemon()
        t2 = PokeTeam("Cynthia", [0, 0, 1, 1, 1], 0, PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE)
        p2 = t2.retrieve_pokemon()
        self.assertEqual(t.choose_battle_option(p, p2), Action.SWAP)

        # Test 3 - Tests when the AI is SWAP_ON_SUPER_EFFECTIVE for Action.ATTACK
        t = PokeTeam("Misty", [1, 1, 1, 1, 1], 0, PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE)
        p = t.retrieve_pokemon()
        t2 = PokeTeam("Cynthia", [0, 1, 1, 1, 1], 0, PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE)
        p2 = t2.retrieve_pokemon()
        self.assertEqual(t.choose_battle_option(p, p2), Action.ATTACK)

        # Test 4 - Tests when the AI is RANDOM
        RandomGen.set_seed(12)
        t = PokeTeam("Misty", [1, 1, 1, 1, 1], 0, PokeTeam.AI.RANDOM)
        p = t.retrieve_pokemon()
        t2 = PokeTeam("Cynthia", [1, 1, 1, 1, 1], 0, PokeTeam.AI.RANDOM)
        p2 = t2.retrieve_pokemon()
        self.assertEqual(t.choose_battle_option(p, p2), Action.HEAL)
