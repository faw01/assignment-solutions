from poke_team import PokeTeam
from random_gen import RandomGen
from tournament import Tournament
from battle import Battle
from tests.base_test import BaseTest

class TestTournament(BaseTest):

    def test_creation(self):
        t = Tournament(Battle(verbosity=0))
        t.set_battle_mode(1)
        self.assertRaises(ValueError, lambda: t.start_tournament("Roark Gardenia + Maylene Crasher_Wake + + + Fantina Byron + Candice Volkner + + +"))
        t.start_tournament("Roark Gardenia + Maylene Crasher_Wake + Fantina Byron + + + Candice Volkner + +")

    def test_random(self):
        RandomGen.set_seed(123456)
        t = Tournament(Battle(verbosity=0))
        t.set_battle_mode(0)
        t.start_tournament("Roark Gardenia + Maylene Crasher_Wake + Fantina Byron + + + Candice Volkner + +")

        team1, team2, res = t.advance_tournament() # Roark vs Gardenia
        self.assertEqual(res, 1)
        self.assertTrue(str(team1).startswith("Roark"))
        self.assertTrue(str(team2).startswith("Gardenia"))

        team1, team2, res = t.advance_tournament() # Maylene vs Crasher_Wake
        self.assertEqual(res, 1)
        self.assertTrue(str(team1).startswith("Maylene"))
        self.assertTrue(str(team2).startswith("Crasher_Wake"))

        team1, team2, res = t.advance_tournament() # Fantina vs Byron
        self.assertEqual(res, 1)
        self.assertTrue(str(team1).startswith("Fantina"))
        self.assertTrue(str(team2).startswith("Byron"))

        team1, team2, res = t.advance_tournament() # Maylene vs Fantina
        self.assertEqual(res, 2)
        self.assertTrue(str(team1).startswith("Maylene"))
        self.assertTrue(str(team2).startswith("Fantina"))

        team1, team2, res = t.advance_tournament() # Roark vs Fantina
        self.assertEqual(res, 1)
        self.assertTrue(str(team1).startswith("Roark"))
        self.assertTrue(str(team2).startswith("Fantina"))

        team1, team2, res = t.advance_tournament() # Candice vs Volkner
        self.assertEqual(res, 1)
        self.assertTrue(str(team1).startswith("Candice"))
        self.assertTrue(str(team2).startswith("Volkner"))

        team1, team2, res = t.advance_tournament() # Roark vs Candice
        self.assertEqual(res, 2)
        self.assertTrue(str(team1).startswith("Roark"))
        self.assertTrue(str(team2).startswith("Candice"))

    def test_metas(self):
        RandomGen.set_seed(123456)
        t = Tournament(Battle(verbosity=0))
        t.set_battle_mode(0)
        t.start_tournament("Roark Gardenia + Maylene Crasher_Wake + Fantina Byron + + + Candice Volkner + +")
        l = t.linked_list_with_metas()
        # Roark = [0, 2, 1, 1, 1]
        # Garderia = [0, 0, 2, 0, 1]
        # Maylene = [6, 0, 0, 0, 0]
        # Crasher_Wake = [0, 2, 0, 1, 0]
        # Fantina = [0, 0, 1, 1, 1]
        # Byron = [0, 2, 0, 0, 1]
        # Candice = [2, 2, 1, 0, 0]
        # Volkner = [0, 5, 0, 0, 0]
        expected = [
            [],
            [],
            ['FIRE'], # Roark Fantina do not have Fire types, but Maylene does (lost to Fantina)
            ['GRASS'], # Maylene Fantina do not have Grass types, but Byron/Crasher_Wake does (lost to Fantina/Maylene)
            [],
            [],
            [],
        ]
        for x in range(len(l)):
            team1, team2, types = l[x]
            self.assertEqual(expected[x], types)

    def test_balance(self):
        # 1054
        t = Tournament()
        self.assertFalse(t.is_balanced_tournament("Roark Gardenia + Maylene Crasher_Wake + Fantina Byron + + + Candice Volkner + +"))

    ##
    ## NEW TESTS
    ##

    def custom_test_valid(self):
        """
        Checks if there are two teams per match.
        """
        # Checks if .is_valid_tournament() returns False if an invalid string is parsed into it, based per match.
        t = Tournament()
        self.assertFalse(t.is_valid_tournament("Roark Gardenia + Maylene + Fantina Byron + + + Candice Volkner + +"))


    def custom_test_valid2(self):
        """
        Checks validity of the matchups indicated by the operators.
        """
        # Checks if .is_valid_tournament() returns False if an invalid string is parsed into it, based on operators.
        t = Tournament()
        self.assertFalse(t.is_valid_tournament("Roark Gardenia + Maylene Crasher_Wake + Fantina Byron + + Candice Volkner + +"))


    def custom_test_valid3(self):
        """
        Checks validity of tournament string.
        """
        # Checks if .is_valid_tournament() returns False if a blatantly invalid string is parsed into it.
        t = Tournament()
        self.assertTrue(t.is_valid_tournament("Schmidt Hunter + Dunn Mills + + Grant Nichols + Stone Elliot + + + Spencer Ryan + +"))


    def custom_test_battle_mode(self):
        """
        Checks if set_battle_mode() works if the battle mode is set to 0.
        """
        t = Tournament()

        # Set battle mode to 0
        t.set_battle_mode(0)
        t.start_tournament("Roark Gardenia + Maylene Crasher_Wake + Fantina Byron + + + Candice Volkner + +")
        poke= t.tournament_queue.serve()

        # Check if battle mode is equal to 0
        self.assertEqual(poke.get_battle_mode(), 0)

    def custom_test_battle_mode2(self):
        """
        Checks if set_battle_mode() works if the battle mode is set to 1.
        """
        t = Tournament()

        # Set battle mode to 0
        t.set_battle_mode(0)
        t.start_tournament("Roark Gardenia + Maylene Crasher_Wake + Fantina Byron + + + Candice Volkner + +")
        poke = t.tournament_queue.serve()

        # Check if battle mode is equal to 1
        self.assertEqual(poke.get_battle_mode(), 1)

    def custom_test_battle_mode3(self):
        """
        Checks if a ValueError is raised when an invalid battle mode is parsed into set_battle_mode().
        """
        t = Tournament()

        # Checks if a ValueError is raised or not.
        self.assertRaises(ValueError, lambda: t.set_battle_mode(3))


    def custom_test_start(self):
        """
        Tests that the .start_tournament() returns None
        """
        t = Tournament()
        t.set_battle_mode(0)

        # Store in var
        ret_val = t.start_tournament("Roark Gardenia + Maylene Crasher_Wake + Fantina Byron + + + Candice Volkner + +")
        self.assertIs(ret_val, None)


    def custom_test_start2(self):
        """
        Tests whether a ValueError is raised when an invalid string is parsed into .start_tournament()
        """
        t = Tournament()
        t.set_battle_mode(0)
        self.assertRaises(ValueError, lambda: t.start_tournament("Schmidt Hunter + Gao Mills + + + Grant Nichols + Stone Elliot + + + Spencer Ryan + +"))

    def custom_test_start3(self):
        """
        Tests whether a ValueError is raised when .start_tournament() is called but no battle mode is set
        """
        t = Tournament()
        t.battle = None
        t.set_battle_mode(0)
        self.assertRaises(ValueError, lambda: t.start_tournament("Schmidt Hunter + Gao Mills + + Grant Nichols + Stone Elliot + + + Spencer Ryan + + Chen Mills + +"))

    def custom_test_advance(self):
        """
        Tests whether the tournament battles are simulated following the order of a specific tournament string.
        """
        t = Tournament()
        t.set_battle_mode(0)
        t.start_tournament("Roark Gardenia + Maylene Crasher_Wake + Fantina Byron + + + Candice Volkner + +")
        res = t.advance_tournament()
        self.assertEqual(res[0].get_team_name(), "Roark")
        self.assertEqual(res[1].get_team_name(), "Gardenia")
        res = t.advance_tournament()
        self.assertEqual(res[0].get_team_name(), "Maylene")
        self.assertEqual(res[1].get_team_name(), "Crasher_Wake")
        res = t.advance_tournament()
        self.assertEqual(res[0].get_team_name(), "Fantina")
        self.assertEqual(res[1].get_team_name(), "Byron")

    def custom_test_advance2(self):
        """
        Tests whether the tournament battles are simulated following the order of a specific tournament string.
        """
        t = Tournament()
        t.set_battle_mode(0)
        t.start_tournament("Schmidt Hunter + Gao Mills + + Grant Nichols + Stone Elliot + + + Spencer Ryan + +")
        res = t.advance_tournament()
        res = t.advance_tournament()
        self.assertEqual(res[0].get_team_name(), "Schmidt")
        self.assertEqual(res[1].get_team_name(), "Hunter")
        res = t.advance_tournament()
        self.assertEqual(res[0].get_team_name(), "Gao")
        self.assertEqual(res[1].get_team_name(), "Mills")
        res = t.advance_tournament()
        self.assertIn(res[0].get_team_name(), ["Schmidt","Gao"])
        self.assertIn(res[1].get_team_name(), ["Hunter","Mills"])


    def custom_test_advance3(self):
        """
        Tests whether the tournament battles are simulated following the order of a specific tournament string.
        """
        t = Tournament()
        t.set_battle_mode(0)
        t.start_tournament("Roark Gardenia + Maylene Crasher_Wake + + Fantina Byron + + Candice Volkner + +")
        res = t.advance_tournament()
        self.assertEqual(res[0].get_team_name(), "Roark")
        self.assertEqual(res[1].get_team_name(), "Gardenia")
        res = t.advance_tournament()
        self.assertEqual(res[0].get_team_name(), "Maylene")
        self.assertEqual(res[1].get_team_name(), "Crasher_Wake")
        res = t.advance_tournament()
        self.assertIn(res[0].get_team_name(), ["Roark","Maylene"])
        self.assertIn(res[1].get_team_name(), ["Gardenia","Crasher_Wake"])

