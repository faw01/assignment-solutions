from pokemon import Venusaur, Charizard, Blastoise, Charmander, Squirtle, Bulbasaur, Gastly, Haunter, Eevee, Gengar
from tests.base_test import BaseTest


class TestPokemon(BaseTest):

    def test_venusaur_stats(self):
        v = Venusaur()
        self.assertEqual(v.get_hp(), 21)
        self.assertEqual(v.get_level(), 2)
        self.assertEqual(v.get_attack_damage(), 5)
        self.assertEqual(v.get_speed(), 4)
        self.assertEqual(v.get_defence(), 10)
        v.level_up()
        v.level_up()
        v.level_up()
        self.assertEqual(v.get_hp(), 22)
        self.assertEqual(v.get_level(), 5)
        self.assertEqual(v.get_attack_damage(), 5)
        self.assertEqual(v.get_speed(), 5)
        self.assertEqual(v.get_defence(), 10)
        v.lose_hp(5)

        self.assertEqual(str(v), "LV. 5 Venusaur: 17 HP")

    # |UNIT TESTS FOR TASK 2|

    def test__init__(self):
        """
        Tests that the __init__ method works correctly.
        Tests the proper initialization of 3 different Pokemon and if they contain the correct attributes.
        """

        # Test 1 - Charmander
        p = Squirtle()  # (Lv 1 | HP : 11 | Attack : 4 | Defence : 7 | Speed : 7 | Status : "free" | Type : "Water" | Pokedex ID : 4)
        self.assertIsInstance(p, Squirtle)  # Check if the object is an instance of Squirtle
        self.assertEqual(p.get_level(), 1)  # Check if the level is 1
        self.assertEqual(p.get_hp(), 11)  # Check if the hp is 11
        self.assertEqual(p.get_attack_damage(), 4)  # Check if the attack damage is 4
        self.assertEqual(p.get_speed(), 7)  # Check if the speed is 7
        self.assertEqual(p.get_defence(), 7)  # Check if the defence is 7
        self.assertEqual(p.get_pokedex_id(), 4)  # Check if the pokedex id is 4
        self.assertEqual(p.get_poke_type(), "Water")  # Check if the Pokemon type is Water
        self.assertEqual(p.get_status_inflicted(), "free")  # Check if the status is "free"

        # Test 2 - Eevee
        p = Eevee()  # (Lv 1 | HP : 10 | Attack : 7 | Defence : 5 | Speed : 8 | Status : "free" | Type : "Normal" | Pokedex ID : 9)
        self.assertIsInstance(p, Eevee)  # Check if the object is an instance of Eevee
        self.assertEqual(p.get_level(), 1)  # Check if the level is 1
        self.assertEqual(p.get_hp(), 10)  # Check if the hp is 10
        self.assertEqual(p.get_attack_damage(), 7)  # Check if the attack damage is 7
        self.assertEqual(p.get_speed(), 8)  # Check if the speed is 8
        self.assertEqual(p.get_defence(), 5)  # Check if the defence is 5
        self.assertEqual(p.get_pokedex_id(), 9)  # Check if the pokedex id is 9
        self.assertEqual(p.get_poke_type(), "Normal")  # Check if the Pokemon type is Normal
        self.assertEqual(p.get_status_inflicted(), "free")  # Check if the status is "free"

        # Test 3 - Charizard
        p = Charizard()  # (Lv 3 | HP : 15 | Attack : 16 | Defence : 4 | Speed : 12 | Status : "free" | Type : "Fire" | Pokedex ID : 1)
        self.assertIsInstance(p, Charizard)  # Check if the object is an instance of Charizard
        self.assertEqual(p.get_level(), 3)  # Check if the level is 3
        self.assertEqual(p.get_hp(), 15)  # Check if the hp is 15
        self.assertEqual(p.get_attack_damage(), 16)  # Check if the attack damage is 16
        self.assertEqual(p.get_speed(), 12)  # Check if the speed is 12
        self.assertEqual(p.get_defence(), 4)  # Check if the defence is 4
        self.assertEqual(p.get_pokedex_id(), 1)  # Check if the pokedex id is 1
        self.assertEqual(p.get_poke_type(), "Fire")  # Check if the Pokemon type is Fire
        self.assertEqual(p.get_status_inflicted(), "free")  # Check if the status is "free"

    def test_get_max_hp(self):
        """
        Tests that the get_max_hp method works correctly by calling get_max_hp on 3 different Pokemon
        """
        # Test 1 - Gengar
        p = Gengar()  # (Lv 3 | HP : 13)
        self.assertEqual(p.get_max_hp(), 13)  # Check if the max hp is 13

        # Test 2 - Charizard
        p = Charizard()  # (Lv 3 | HP : 15)
        self.assertEqual(p.get_max_hp(), 15)  # Check if the max hp is 15

        # Test 3 - Eevee
        p = Eevee()  # (Lv 1 | HP : 10)
        self.assertEqual(p.get_max_hp(), 10)  # Check if the max hp is 10

    def test_level_up(self):
        """
        Tests that the level_up method works correctly by calling level_up on 3 different Pokemon
        """

        # Test 1 - For the level after being levelled up 2 times
        p = Squirtle()  # (Lv 1)
        p.level_up()  # (Lv 2)
        p.level_up()  # (Lv 3)
        self.assertEqual(p.get_level(), 3)  # Check if the level is 3

        # Test 2 - For the level after being levelled up 20 times
        p = Gengar()  # (Lv 3)
        for i in range(1, 20):
            p.level_up()  # (Lv 4 - 22)
        self.assertEqual(p.get_level(), 22)  # Check if the level is 22

        # Test 3 - If the adjustment of hp for the levelled up Pokemon is done correctly
        p = Gengar()  # (Lv 3 | HP : 13)
        self.assertEqual(p.get_hp(), 13)  # Check if the hp is 13
        p.lose_hp(3)  # (HP : 10)
        self.assertEqual(p.get_hp(), 10)  # Check if the hp is 10
        p.level_up()  # (Lv 4 | HP : 11)
        self.assertEqual(p.get_hp(), 11)  # Check if the hp is 11

    def test_can_evolve(self):
        """
        Tests that the can_evolve method works correctly by calling can_evolve on 3 different Pokemon
        """

        # Test 1 - Bulbasaur
        p = Bulbasaur()  # (Lv 1) Can evolve at Lv 3
        self.assertEqual(p.can_evolve(), True)  # Check if the Pokemon can evolve

        # Test 2 - Blastoise
        p = Blastoise()  # (Lv 3) Cannot evolve
        self.assertEqual(p.can_evolve(), False)  # Check if the Pokemon can evolve

        # Test 3 - Eevee
        p = Eevee()  # (Lv 1) Cannot evolve
        self.assertEqual(p.can_evolve(), False)  # Check if the Pokemon can evolve

    def test_should_evolve(self):
        """
        Tests that the should_evolve method works correctly by calling should_evolve on 3 different Pokemon
        """
        # Test 1 - Charmander will only evolve when it reaches level 3
        p = Charmander()  # (Lv 1) Should not evolve
        self.assertEqual(p.should_evolve(), False)  # Check if the Pokemon should evolve
        p.level_up()  # (Lv 2) Should not evolve
        self.assertEqual(p.should_evolve(), False)  # Check if the Pokemon should evolve
        p.level_up()  # (Lv 3) Should evolve
        self.assertEqual(p.should_evolve(), True)  # Check if the Pokemon should evolve

        # Test 2 - Gastly will evolve at level 1
        p = Gastly()  # (Lv 1) Should evolve
        self.assertEqual(p.should_evolve(), True)  # Check if the Pokemon should evolve

        # Test 3 - Eevee will never evolve
        p = Eevee()  # (Lv 1) Should not evolve
        self.assertEqual(p.should_evolve(), False)  # Check if the Pokemon should evolve

    def test_get_evolved_version(self):
        """
        Tests that the get_evolved_version method works correctly by calling get_evolved_version on 3 different Pokemon with no evolution,
        having a status before and after evolution, hp loss is included after evolution, and level is correct from levelling up after evolution
        """
        # Test 1 - Eevee has no evolution
        p = Eevee()  # (Lv 1) No evolution
        self.assertEqual(p.get_evolved_version(), None)  # Check if the there is an evolved version

        # Test 2 - If status stays after evolution
        p = Gastly()  # (Lv 1 | Status : "free")
        p.status = "burn"  # Set the status to "burn"
        # (Lv 1 | Status : "burn")
        p = p.get_evolved_version()  # Evolve Gastly
        self.assertIsInstance(p, Haunter)  # Check if the evolved Pokemon is Haunter
        self.assertEqual(p.get_status_inflicted(), "burn")  # Check if the status is still "burn" after evolution

        # Test 3 - If missing hp is adjusted after evolution
        p = Charmander()  # (Lv 1 | HP : 9)
        p.lose_hp(3)  # (Lv 1 | HP : 6)
        p.level_up()  # (Lv 2 | HP : 7)
        p.level_up()  # (Lv 3 | HP : 12)
        p = p.get_evolved_version()  # Evolve Charmander
        self.assertIsInstance(p, Charizard)  # Check if the evolved Pokemon is Charizard
        self.assertEqual(p.get_hp(), 12)  # Check if the hp is loss is included after evolution

        # Test 4 - If level is correct after evolution
        p = Bulbasaur()  # (Lv 1)
        p.level_up()  # (Lv 2)
        p.level_up()  # (Lv 3)
        p.level_up()  # (Lv 4)
        p.level_up()  # (Lv 5)
        p.level_up()  # (Lv 6)
        p = p.get_evolved_version()  # Evolve Bulbasaur
        self.assertIsInstance(p, Venusaur)  # Check if the evolved Pokemon is Venusaur
        self.assertEqual(p.get_level(), 6)  # Check if the level is correct after evolution

    def test_defend(self):
        """
        Tests that the defend method works correctly by calling defend on 3 different Pokemon
        """
        # Test 1 - Bulbasaur
        defender = Bulbasaur()  # (Lv 1 | HP : 13 | Defence : 5)
        defender.lose_hp(defender.defend(5))  # Defender (Lv 1 | HP : 11 | Defence : 5) takes 2 damage
        self.assertEqual(defender.get_hp(), 11)  # Check if the defender's hp is 11

        # Test 2 - Haunter
        defender = Haunter()  # (Lv 1 | HP : 9 | Defence : 6)
        defender.lose_hp(defender.defend(4))  # Defender (Lv 1 | HP : 5 | Defence : 6) takes 4 damage
        self.assertEqual(defender.get_hp(), 5)  # Check if the defender's hp is 5

        # Test 3 - Charizard
        defender = Charizard()  # (Lv 3 | HP : 15 | Defence : 6)
        defender.lose_hp(defender.defend(7))  # Defender (Lv 3 | HP : 1 | Defence : 6) takes 14 damage
        self.assertEqual(defender.get_hp(), 1)  # Check if the defender's hp is 1

    def test_unique_status_effect(self):
        """
        Tests that the unique_status_effect method works correctly by calling unique_status_effect on 3 different Pokemon
        """
        # Test 1 - Charizard
        p = Charizard()  # (Lv 3 | Unique Status Effect : "burn")
        self.assertEqual(p.unique_status_effect(), "burn")  # Check if Charizard's unique status effect is "burn"

        # Test 2 - Gengar
        p = Gengar()  # (Lv 3 | Unique Status Effect : "sleep")
        self.assertEqual(p.unique_status_effect(), "sleep")  # Check if Gengar's unique status effect is "sleep"

        # Test 3 - Blastoise
        p = Blastoise()  # (Lv 3 | Unique Status Effect : "paralysis")
        self.assertEqual(p.unique_status_effect(),
                         "paralysis")  # Check if Blastoise's unique status effect is "paralysis"
