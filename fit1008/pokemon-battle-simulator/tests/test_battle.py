from random_gen import RandomGen
from battle import Battle
from poke_team import Criterion, PokeTeam
from pokemon import Blastoise, Charizard, Charmander, Eevee, Gastly, Gengar, Squirtle, Venusaur
from tests.base_test import BaseTest

class TestBattle(BaseTest):

    def test_basic_battle(self):
        RandomGen.set_seed(1337)
        team1 = PokeTeam("Ash", [1, 1, 1, 0, 0], 0, PokeTeam.AI.ALWAYS_ATTACK)
        team2 = PokeTeam("Gary", [0, 0, 0, 0, 3], 0, PokeTeam.AI.ALWAYS_ATTACK)
        b = Battle(verbosity=0)
        res = b.battle(team1, team2)
        self.assertEqual(res, 1)
        self.assertTrue(team2.is_empty())
        remaining = []
        while not team1.is_empty():
            remaining.append(team1.retrieve_pokemon())
        self.assertEqual(len(remaining), 2)
        self.assertEqual(remaining[0].get_hp(), 1)
        self.assertIsInstance(remaining[0], Venusaur)
        self.assertEqual(remaining[1].get_hp(), 11)
        self.assertIsInstance(remaining[1], Squirtle)

    def test_complicated_battle(self):
        RandomGen.set_seed(192837465)
        team1 = PokeTeam("Brock", [1, 1, 1, 1, 1], 2, PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE, criterion=Criterion.HP)
        team2 = PokeTeam("Misty", [0, 0, 0, 3, 3], 2, PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE, criterion=Criterion.SPD)
        b = Battle(verbosity=0)
        res = b.battle(team1, team2)
        self.assertEqual(res, 1)
        remaining = []
        while not team1.is_empty():
            remaining.append(team1.retrieve_pokemon())
        self.assertEqual(len(remaining), 2)
        self.assertEqual(remaining[0].get_hp(), 11)
        self.assertIsInstance(remaining[0], Charizard)
        self.assertEqual(remaining[1].get_hp(), 6)
        self.assertIsInstance(remaining[1], Gastly)

    # |UNIT TESTS FOR TASK 4|

    def test__init__(self):
        """
        Tests that the __init__ method works correctly.
        Tests the proper initialization of 3 different Pokemon and if they contain the correct attributes.
        """
        # Test 1 - Battle is instance
        team1 = PokeTeam("Lt. Surge", [1, 1, 1, 1, 1], 0, PokeTeam.AI.ALWAYS_ATTACK)
        team2 = PokeTeam("Misty", [0, 6, 0, 0, 0], 0, PokeTeam.AI.ALWAYS_ATTACK)
        b = Battle(verbosity=0)
        self.assertIsInstance(b, Battle)

        # Test 2 - Verbosity
        team1 = PokeTeam("Lt. Surge", [1, 1, 1, 1, 1], 0, PokeTeam.AI.ALWAYS_ATTACK)
        team2 = PokeTeam("Misty", [0, 6, 0, 0, 0], 0, PokeTeam.AI.ALWAYS_ATTACK)
        self.assertRaises(ValueError, lambda: Battle(verbosity=-1))
        self.assertRaises(ValueError, lambda: Battle(verbosity="1"))

        # Test 3 - Turns at the beginning should be 0, end of battle should be false.
        team1 = PokeTeam("Lt. Surge", [1, 1, 1, 1, 1], 0, PokeTeam.AI.ALWAYS_ATTACK)
        team2 = PokeTeam("Misty", [0, 6, 0, 0, 0], 0, PokeTeam.AI.ALWAYS_ATTACK)
        b = Battle(verbosity=0)
        self.assertEqual(b.turns, 0)
        self.assertEqual(b.end, False)

    def test_battle(self):
        """
        Tests that the __init__ method works correctly.
        Tests the proper initialization of 3 different Pokemon and if they contain the correct attributes.
        """        
        # Test 1 - Battle mode 0, AI.ALWAYS_ATTACK
        RandomGen.set_seed(42069) # Sets the seed 

        team1 = PokeTeam("Lt. Surge", [1, 1, 1, 1, 1], 0, PokeTeam.AI.ALWAYS_ATTACK)
        team2 = PokeTeam("Misty", [0, 0, 6, 0, 0], 0, PokeTeam.AI.ALWAYS_ATTACK)
        
        b = Battle(verbosity=0)
        res = b.battle(team1, team2) # team1 and team2 battle
        
        self.assertEqual(res, 1) # checks if the result of the battle is equal to 1, which in this case suggests that team 1 won
        self.assertFalse(team1.is_empty()) # checks if there are any remaining Pokemon that are in team1 since team 1 is not empty
        self.assertTrue(team2.is_empty()) # checks if there are any remaining Pokemon that are in team2 since team 2 is empty due to losing
        
        # adds all remaining pokemon in team 1 into a remaining list
        remaining = []
        while not team1.is_empty():
            remaining.append(team1.retrieve_pokemon())
        
        self.assertEqual(len(remaining), 4) # checks if the number of Pokemon retrieved into team 1 is equal to 4

        # checks the first index of remaining, which suggests it is the first Pokemon in the order
        self.assertIsInstance(remaining[0], Venusaur) # checks if first pokemon is equal to a Venusaur instance
        self.assertEqual(remaining[0].get_hp(), 5) # checks if Venusaur hp value is 5
        self.assertEqual(remaining[0].get_level(), 7) # checks if Venusaur level is 7

        # checks the last index of remaining, which suggests it is the last Pokemon in the order
        self.assertIsInstance(remaining[-1], Eevee) # checks if last pokemon is equal to an Eevee instance
        self.assertEqual(remaining[-1].get_hp(), 10) # checks if Eevee hp value is 10
        self.assertEqual(remaining[-1].get_level(), 1) # checks if Eevee level is 1

        # Test 2 - Battle mode 1, AI.SWAP_ON_SUPER_EFFECTIVE
        RandomGen.set_seed(42069) # Sets the seed 

        team1 = PokeTeam("Giovanni", [1, 1, 1, 1, 1], 1, PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE)
        team2 = PokeTeam("Blaine", [6, 0, 0, 0, 0], 1, PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE)
        
        b = Battle(verbosity=0)
        res = b.battle(team1, team2) # team1 and team2 battle
        
        self.assertEqual(res, 1) # checks if the result of the battle is equal to 1, which in this case suggests that team 1 won
        self.assertFalse(team1.is_empty()) # checks if there are any remaining Pokemon that are in team1 since team 1 is not empty
        self.assertTrue(team2.is_empty()) # checks if there are any remaining Pokemon that are in team2 since team 2 is empty due to losing
        
        # adds all remaining pokemon in team 1 into a remaining list
        remaining = []
        while not team1.is_empty():
            remaining.append(team1.retrieve_pokemon())
        
        self.assertEqual(len(remaining), 4) # checks if the number of Pokemon retrieved into team 1 is equal to 4

        # checks the first index of remaining, which suggests it is the first Pokemon in the order
        self.assertIsInstance(remaining[0], Gastly) # checks if first pokemon is equal to a Gastly instance
        self.assertEqual(remaining[0].get_hp(), 6) # checks if Gastly hp value is 5
        self.assertEqual(remaining[0].get_level(), 1) # checks if Gastly level is 7

        # checks the last index of remaining, which suggests it is the last Pokemon in the order
        self.assertIsInstance(remaining[-1], Blastoise) # checks if last pokemon is equal to an Blastoise instance
        self.assertEqual(remaining[-1].get_hp(), 24) # checks if Blastoise hp value is 10
        self.assertEqual(remaining[-1].get_level(), 6) # checks if Blastoise level is 1

        # Test 3 - Battle mode 1, AI.RANDOM, Criterion.LV, Criterion.DEF
        RandomGen.set_seed(42069) # Sets the seed 

        team1 = PokeTeam("Allister", [0, 0, 0, 6, 0], 2, PokeTeam.AI.RANDOM, criterion=Criterion.LV)
        team2 = PokeTeam("Fantina", [0, 0, 0, 6, 0], 2, PokeTeam.AI.RANDOM, criterion=Criterion.DEF)
        
        b = Battle(verbosity=0)
        res = b.battle(team1, team2) # team1 and team2 battle
        
        self.assertEqual(res, 1) # checks if the result of the battle is equal to 1, which in this case suggests that team 1 won
        self.assertFalse(team1.is_empty()) # checks if there are any remaining Pokemon that are in team1 since team 1 is not empty
        self.assertTrue(team2.is_empty()) # checks if there are any remaining Pokemon that are in team2 since team 2 is empty due to losing
        
        # adds all remaining pokemon in team 1 into a remaining list
        remaining = []
        while not team1.is_empty():
            remaining.append(team1.retrieve_pokemon())
        
        self.assertEqual(len(remaining), 1) # checks if the number of Pokemon retrieved into team 1 is equal to 4

        # checks the first index of remaining, which suggests it is the first Pokemon in the order
        self.assertIsInstance(remaining[0], Gengar) # checks if first pokemon is equal to a Gengar instance
        self.assertEqual(remaining[0].get_hp(), 8) # checks if Gengar hp value is 5
        self.assertEqual(remaining[0].get_level(), 6) # checks if Gengar level is 7
