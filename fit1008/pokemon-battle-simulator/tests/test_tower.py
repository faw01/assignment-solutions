from random_gen import RandomGen
from poke_team import Criterion, PokeTeam
from battle import Battle
from tower import BattleTower
from tests.base_test import BaseTest


class TestTower(BaseTest):

    def test_creation(self):
        RandomGen.set_seed(51234)
        bt = BattleTower(Battle(verbosity=0))
        bt.set_my_team(PokeTeam.random_team("N", 2, team_size=6, criterion=Criterion.HP))
        bt.generate_teams(4)
        # Teams have 7, 10, 10, 3 lives.
        RandomGen.set_seed(1029873918273)
        results = [
            (1, 6),
            (1, 9),
            (2, 10)
        ]
        it = iter(bt)
        for (expected_res, expected_lives), (res, me, tower, lives) in zip(results, it):
            self.assertEqual(expected_res, res, (expected_res, expected_lives))
            self.assertEqual(expected_lives, lives)

    def test_duplicates(self):
        RandomGen.set_seed(29183712400123)

        bt = BattleTower(Battle(verbosity=0))
        bt.set_my_team(PokeTeam.random_team("Jackson", 0, team_size=6))
        bt.generate_teams(10)

        # Team numbers before:
        # [0, 4, 1, 0, 0], 6
        # [1, 0, 2, 0, 0], 5
        # [1, 1, 0, 1, 0], 8
        # [1, 2, 1, 1, 0], 10
        # [0, 0, 2, 1, 1], 8
        # [1, 1, 3, 0, 0], 4
        # [0, 2, 0, 1, 0], 5
        # [1, 0, 0, 4, 0], 3
        # [1, 1, 1, 0, 2], 7
        # [0, 1, 1, 1, 0], 9
        it = iter(bt)
        it.avoid_duplicates()
        # Team numbers after:
        # [1, 1, 0, 1, 0], 8
        # [0, 1, 1, 1, 0], 9

        l = []
        for res, me, tower, lives in bt:
            tower.regenerate_team()
            l.append((res, lives))

        self.assertEqual(l, [
            (1, 7),
            (1, 8),
            (2, 7)
        ])



    # |UNIT TESTS FOR TASK 5|

    def test_init(self):
        """
        Tests for __init__() method in tower.py. (3 test cases)
        """

        # Test 1 - Check if it raises ValueError if a non-Battle instance is parsed into BattleTower()
        self.assertRaises(ValueError, lambda: BattleTower(1))


        # Test 2 - Check if attributes are correct
        bt = BattleTower(Battle())

        # Checks whether player_team and tower_teams are initialised as None or not
        self.assertIs(bt.player_team, None)
        self.assertIs(bt.tower_teams, None)

        # Checks whether defeat and victory flags are False
        self.assertFalse(bt.defeat)
        self.assertFalse(bt.victory)

        # Checks if battle is a Battle instance or not
        self.assertIsInstance(bt.battle, Battle)


        # Test 3 - Check that self.battle is a Battle instance if no argument is parsed into
        #          the __init__() method.

        # Make a new BattleTower instance with no arguments
        bt = BattleTower()

        # Check if self.battle is an instance of Battle
        self.assertIsInstance(bt.battle, Battle)


    def test_set_my_team(self):
        """
        Tests for set_my_team() method in tower.py. (3 test cases)
        """

        # Test 1 - Make sure it raises a ValueError if you try to set a team that is not a PokeTeam
        bt = BattleTower()
        self.assertRaises(ValueError, lambda: bt.set_my_team(1))


        # Test 2 - Check if bt.player_team = team when setting it
        bt = BattleTower()

        # Make valid team
        dhiren_team = PokeTeam("Dhiren", [1, 1, 1, 1, 1], 0, PokeTeam.AI.RANDOM)

        # Set team
        bt.set_my_team(dhiren_team)

        # Check bt.player_team = team
        self.assertEqual(bt.player_team, dhiren_team)


        # Test 3 - Try to parse a string while instantiating a BattleTower
        bt = BattleTower()
        self.assertRaises(ValueError, lambda: bt.set_my_team("this_is_invalid"))


    def test_generate_teams(self):
        """
        Tests if team generation works or not in tower.py. (3 test cases)
        """

        # Test 1 - Check that a ValueError is raised if n is non-zero and positive
        bt = BattleTower()
        self.assertRaises(ValueError, lambda: bt.generate_teams(-1))


        # Test 2 - Checks the number of teams generated
        bt = BattleTower()

        # Set seed
        RandomGen.set_seed(69420)

        # Create 10 teams
        bt.generate_teams(10)

        # Check is len(tower_teams) == 10
        self.assertEqual(len(bt.tower_teams), 10)


        # Test 3 - Check that a ValueError is raised if n is not an instance of int
        bt = BattleTower()
        self.assertRaises(ValueError, lambda: bt.generate_teams("hope you have a nice day :)"))


    def test_next_my_iterable(self):
        """
        Test if magic method __next__() works or not in BattleTowerIterator. (3 test cases)
        """

        # Test 1 - Check if StopIteration error is raised when there is nothing left to iterate
        #          over.

        # I shall use the same seed as in test_duplicates to ensure correctness
        RandomGen.set_seed(29183712400123)

        bt = BattleTower(Battle(verbosity=0))
        bt.set_my_team(PokeTeam.random_team("Jackson", 0, team_size=6))
        bt.generate_teams(10)

        # Get the iterator
        it = iter(bt)

        # There are 4 teams generated so we should only be able to loop 4 times. We manually call
        # the next(it) function 4 times, then call it again to raise StopIteration
        for _ in range(4):
            next(it)

        # Check whether StopIteration is raised or not
        self.assertRaises(StopIteration, lambda: next(it))


        # Test 2 - Player team instantly loses using the seed "69420"
        RandomGen.set_seed(69420)
        bt = BattleTower(Battle(verbosity=0))
        bt.set_my_team(PokeTeam.random_team("N", 2, team_size=6, criterion=Criterion.HP))
        bt.generate_teams(4)
        # Teams have 5, 3, 2, 7 lives.
        RandomGen.set_seed(69420)
        results = [
            (2, 5)
        ]
        it = iter(bt)
        for (expected_res, expected_lives), (res, me, tower, lives) in zip(results, it):
            self.assertEqual(expected_res, res, (expected_res, expected_lives))
            self.assertEqual(expected_lives, lives)


        # Test 3 - Check that the result returned by next(my_iterable) is an instance of tuple
        RandomGen.set_seed(69420)
        bt = BattleTower(Battle(verbosity=0))
        bt.set_my_team(PokeTeam.random_team("N", 2, team_size=6, criterion=Criterion.HP))
        bt.generate_teams(4)
        # Teams have 5, 3, 2, 7 lives.
        RandomGen.set_seed(69420)
        results = [
            (2, 5)
        ]
        it = iter(bt)

        # Check if the result is an instance of a tuple
        self.assertIsInstance(next(it), tuple)


    def test_avoid_duplicates(self):
        """
        Test if the BattleTowerIterator's avoid_duplicates() method works or not. (3 test cases)
        """

        # Test 1 - Check if TypeError is raised when we call avoid_duplicates with an argument()
        RandomGen.set_seed(29183712400123)

        bt = BattleTower(Battle(verbosity=0))
        bt.set_my_team(PokeTeam.random_team("Jackson", 0, team_size=6))
        bt.generate_teams(10)

        it = iter(bt)

        # Check if TypeError is raised when parsing int 1000 into avoid_duplicates()
        self.assertRaises(TypeError, lambda: it.avoid_duplicates(1000))


        # Test 2 - Check if avoid_duplicates() returns None
        RandomGen.set_seed(29183712400123)

        bt = BattleTower(Battle(verbosity=0))
        bt.set_my_team(PokeTeam.random_team("Jackson", 0, team_size=6))
        bt.generate_teams(10)

        it = iter(bt)

        # Check if it.avoid_duplicates returns None
        self.assertIs(it.avoid_duplicates(), None)


        # Test 3 - Using a set seed, test if avoid_duplicates() work
        RandomGen.set_seed(69420)

        bt = BattleTower(Battle(verbosity=0))
        bt.set_my_team(PokeTeam.random_team("Jackson", 0, team_size=6))
        bt.generate_teams(10)

        # Team numbers before with lives:
        # [0, 3, 1, 0, 0], 5
        # [1, 1, 0, 0, 2], 3
        # [0, 0, 1, 0, 2], 2
        # [0, 0, 1, 1, 1], 7
        # [1, 3, 1, 1, 0], 4
        # [0, 1, 3, 1, 0], 5
        # [0, 0, 1, 1, 1], 9
        # [0, 1, 1, 1, 1], 10
        # [0, 2, 1, 0, 2], 10
        # [2, 1, 0, 0, 1], 2
        it = iter(bt)
        it.avoid_duplicates()
        # Team numbers after with lives
        # [0, 0, 1, 1, 1], 7
        # [0, 0, 1, 1, 1], 9
        # [0, 1, 1, 1, 1], 10

        # Store the expected team_numbers lists in a list
        nested_expected_team_numbers_list = [[0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 1, 1, 1, 1]]


        # Iterate through the remaining teams and append our results to another list
        no_duplicates_team_numbers_list = []

        for i in range(len(bt.tower_teams)):
            no_duplicates_team_numbers_list.append(bt.tower_teams[i].get_team_numbers())

        # Check whether the expected team_numbers nested list is the same as ours
        self.assertListEqual(no_duplicates_team_numbers_list, nested_expected_team_numbers_list)

