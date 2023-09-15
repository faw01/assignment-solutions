from random_gen import RandomGen
from pokemon_base import PokemonBase
from pokemon import Venusaur, Charizard, Blastoise, Charmander, Squirtle, Bulbasaur, Gastly, Haunter, Eevee, Gengar
from tests.base_test import BaseTest


class TestPokemonBase(BaseTest):

    def test_cannot_init(self):
        """Tests that we cannot initialise PokemonBase, and that it raises the correct error."""
        self.assertRaises(TypeError, lambda: PokemonBase(30, "Fire"))

    def test_level(self):
        e = Eevee()
        self.assertEqual(e.get_level(), 1)
        e.level_up()
        self.assertEqual(e.get_level(), 2)

    def test_hp(self):
        e = Eevee()
        self.assertEqual(e.get_hp(), 10)
        e.lose_hp(4)
        self.assertEqual(e.get_hp(), 6)
        e.heal()
        self.assertEqual(e.get_hp(), 10)

    def test_status(self):
        RandomGen.set_seed(0)
        e1 = Eevee()
        e2 = Eevee()
        e1.attack(e2)
        # e2 now is confused.
        e2.attack(e1)
        # e2 takes damage in confusion.
        self.assertEqual(e1.get_hp(), 10)

    def test_evolution(self):
        g = Gastly()
        self.assertEqual(g.can_evolve(), True)
        self.assertEqual(g.should_evolve(), True)
        new_g = g.get_evolved_version()
        self.assertIsInstance(new_g, Haunter)

    # |UNIT TESTS FOR TASK 1|

    def test_init(self):
        """
        Tests whether a Pokemon can be initialised or not
        """

        # Test 1 - initialise Charmander
        # Charmander
        p = Charmander()
        assert isinstance(p, Charmander)

        # Test 2 - initialise Blastoise
        p = Blastoise()
        assert isinstance(p, Blastoise)

        # Test 3 - initialise Gengar
        p = Gengar()
        assert isinstance(p, Gengar)


    def test_get_attack_damage(self):
        """
        Tests that the get_attack_damage method works correctly by calling get_attack_damage on 3 different Pokemon
        """
        # Test 1 - Eevee (Lv 1 | Attack : 7)
        p = Eevee()
        self.assertEqual(p.get_attack_damage(), 7)  # Checks that the attack damage is 7

        # Test 2 - Gastly (Lv 1 | Attack : 4)
        p = Gastly()
        self.assertEqual(p.get_attack_damage(), 4)  # Checks that the attack damage is 4

        # Test 3 - Venusaur (Lv 2 | Attack : 12)
        p = Venusaur()
        self.assertEqual(p.get_attack_damage(), 5)  # Checks that the attack damage is 5

    def test_get_speed(self):
        """
        Tests that the get_speed method works correctly by calling get_speed on 3 different Pokemon
        """
        # Test 1 - Charmander (Lv 1 | Speed : 8)
        p = Charmander()
        self.assertEqual(p.get_speed(), 8)  # Checks that the speed is 8

        # Test 2 - Haunter (Lv 1 | Speed : 6)
        p = Haunter()
        self.assertEqual(p.get_speed(), 6)  # Checks that the speed is 6

        # Test 3 - Blastoise (Lv 3 | Speed : 10)
        p = Blastoise()
        self.assertEqual(p.get_speed(), 10)  # Checks that the speed is 10

    def test_get_poke_name(self):
        """
        Tests that the get_poke_name method works correctly by calling get_poke_name on 3 different Pokemon
        """
        # Test 1 - Charmander
        p = Charmander()
        self.assertEqual(p.get_poke_name(), "Charmander")  # Checks that the Pokemon name is "Charmander"

        # Test 2 - Squirtle
        p = Squirtle()
        self.assertEqual(p.get_poke_name(), "Squirtle")  # Checks that the Pokemon name is "Squirtle"

        # Test 3 - Bulbasaur
        p = Bulbasaur()
        self.assertEqual(p.get_poke_name(), "Bulbasaur")  # Checks that the Pokemon name is "Bulbasaur"

    def test_get_hp(self):
        """
        Tests that the get_hp method works correctly by calling get_hp on 3 different Pokemon
        """
        # Test 1 - Charizard (Lv 3 | HP : 10)
        p = Charizard()
        self.assertEqual(p.get_hp(), 15)  # Checks that the HP is 15

        # Test 2 - Blastoise (Lv 3 | HP : 21)
        p = Blastoise()
        self.assertEqual(p.get_hp(), 21)  # Checks that the HP is 21

        # Test 3 - Venusaur (Lv 2 | HP : 21)
        p = Venusaur()
        self.assertEqual(p.get_hp(), 21)  # Checks that the HP is 21

    def test_get_level(self):
        """
        Tests that the get_level method works correctly by calling get_level on 3 different Pokemon
        """
        # Test 1 - Gastly (Lv 1)
        p = Gastly()
        self.assertEqual(p.get_level(), 1)  # Checks that Gastly's level is 1

        # Test 2 - Haunter (Lv 2)
        p = Haunter()
        p.level_up()
        self.assertEqual(p.get_level(), 2)  # Checks that Haunter's level is 2, after levelling up

        # Test 3 - Gengar (Lv 3)
        p = Gengar()
        self.assertEqual(p.get_level(), 3)  # Checks that Gengar's level is 3

    def test_get_poke_type(self):
        """
        Tests that the get_poke_type method works correctly by calling get_poke_type on 3 different Pokemon
        """
        # Test 1 - Charmander (Lv 1 | "Fire")
        p = Charmander()
        self.assertEqual(p.get_poke_type(), "Fire")  # Checks that the Pokemon type is "Fire"

        # Test 2 - Haunter (Lv 1 | "Ghost")
        p = Haunter()
        self.assertEqual(p.get_poke_type(), "Ghost")  # Checks that the Pokemon type is "Ghost"

        # Test 3 - Eevee (Lv 1 | "Normal")
        p = Eevee()
        self.assertEqual(p.get_poke_type(), "Normal")  # Checks that the Pokemon type is "Normal"

    def test_get_status_inflicted(self):
        """
        Tests that the get_status_inflicted method works correctly by calling get_status_inflicted on 3 different Pokemon
        """
        # Test 1 - No status effect
        p = Squirtle()  # (Status : "free")
        self.assertEqual(p.get_status_inflicted(), "free")  # Checks that the status is "free"

        # Test 2 - Paralysis
        p = Blastoise()  # (Status : "paralysis")
        p.status = "paralysis"
        self.assertEqual(p.get_status_inflicted(), "paralysis")  # Checks that the status is "paralysis"

        # Test 3 - Sleep
        p = Gastly()  # (Status : "sleep")
        p.status = "sleep"
        self.assertEqual(p.get_status_inflicted(), "sleep")  # Checks that the status is "sleep"

    def test_get_defence(self):
        """
        Tests that the get_defence method works correctly by calling get_defence on 3 different Pokemon
        """
        # Test 1 - Gastly (Lv 1 | Defence : 8)
        p = Gastly()
        self.assertEqual(p.get_defence(), 8)  # Checks that Gastly's defence is 8

        # Test 2 - Haunter (Lv 1 | Defence : 6)
        p = Haunter()
        self.assertEqual(p.get_defence(), 6)  # Checks that Haunter's defence is 6

        # Test 3 - Gengar (Lv 3 | Defence : 3)
        p = Gengar()
        self.assertEqual(p.get_defence(), 3)  # Checks that Gengar's defence is 3

    def test_get_pokedex_id(self):
        """
        Tests that the get_pokedex_id method works correctly by calling get_pokedex_id on 3 different Pokemon
        """
        # Test 1 - Charmander (Pokedex ID : 0)
        p = Charmander()
        self.assertEqual(p.get_pokedex_id(), 0)  # Checks that Charmander's Pokedex ID is 0

        # Test 2 - Charizard (Pokedex ID : 1)
        p = Charizard()
        self.assertEqual(p.get_pokedex_id(), 1)  # Checks that Charizard's Pokedex ID is 1

        # Test 3 - Eevee (Pokedex ID : 9)
        p = Eevee()
        self.assertEqual(p.get_pokedex_id(), 9)  # Checks the Eevee's Pokedex ID is 9

    def test_is_fainted(self):
        """
        Tests that the is_fainted method works correctly by calling is_fainted on 3 different Pokemon
        """
        # Test 1 - Pokemon's hp is not 0 so it will not faint
        p = Charizard()  # (HP : 15)
        p.lose_hp(13)  # 15 - 13 = 2
        self.assertEqual(p.is_fainted(), False)  # Checks that Charizard did not faint

        # Test 2 - Pokemon's hp is 0 so it will faint
        p = Squirtle()  # (HP : 11)
        p.lose_hp(11)  # 11 - 11 = 0
        self.assertEqual(p.is_fainted(), True)  # Checks that Squirtle fainted

        # Test 3 - Pokemon's hp is below 0 so it will faint
        p = Gastly()  # (HP : 6)
        p.lose_hp(12)  # 6 - 12 = -6
        self.assertEqual(p.is_fainted(), True)  # Checks that Gastly fainted

    def test_lose_hp(self):
        """
        Tests that the lose_hp method works correctly by calling lose_hp on 3 different Pokemon
        """
        # Test 1 - Losing 2 hp
        p = Venusaur()  # (HP : 21)
        p.lose_hp(2)  # (HP : 19)
        self.assertEqual(p.get_hp(), 19)  # Checks the current hp of Venusaur after losing hp

        # Test 2 - Losing 12 hp
        p = Charizard()  # (HP : 15)
        p.lose_hp(12)  # (HP : 3)
        self.assertEqual(p.get_hp(), 3)  # Checks the current hp of Charizard after losing hp

        # Test 3 - Losing 20 hp
        p = Blastoise()  # (HP : 21)
        p.lose_hp(20)  # (HP : 1)
        self.assertEqual(p.get_hp(), 1)  # Checks the current hp of Blastoise after losing hp

    def test_attack(self):
        """
        Tests that the attack method works correctly by testing attacks with varying type effectiveness and status effects
        """
        # Test 1 - No status, type effectiveness is 0.5
        attacker = Squirtle()  # (Lv 1 | HP : 11 | Attack : 4))
        defender = Venusaur()  # (Lv 3 | HP : 21 | Defence : 10)
        self.assertEqual(defender.get_hp(), 21)  # Checks the current hp of defender
        attacker.attack(defender)  # Defender (Lv 3 | HP : 20 | Defence : 10) takes 1 damage
        self.assertEqual(defender.get_hp(), 20)  # Checks the current hp of defender

        # Test 2 - No status, type effectiveness is 2
        attacker = Gastly()  # (Lv 1 | HP : 6 | Attack : 4)
        defender = Gengar()  # (Lv 3 | HP: 13 | Defence : 3)
        self.assertEqual(defender.get_hp(), 13)  # Checks the current hp of defender
        attacker.attack(defender)  # Defender (Lv 3 | HP : 5 | Defence : 3) takes 8 damage
        self.assertEqual(defender.get_hp(), 5)  # Checks the current hp of defender

        # Test 3 - Burn, type effectiveness is 1
        RandomGen.set_seed(12)  # Setting the seed to 12 forces the infliction of a burn
        attacker = Charmander()  # (Lv 1 | HP : 9 | Attack : 7 | Defence : 4 | Status : "free")
        defender = Gengar()  # (Lv 3 | HP : 13 | Attack: 18 | Defence : 3 | Status : "free")
        self.assertEqual(defender.get_hp(), 13)  # Checks the current hp of defender
        attacker.attack(
            defender)  # Defender (Lv 3 | HP : 6 | Attack: 18 | Defence : 3 | Status : "burn") takes 7 damage and burn is inflicted
        self.assertEqual(defender.get_hp(), 6)  # Checks the hp of defender is 6
        self.assertEqual(defender.get_status_inflicted(), "burn")  # Checks that burn was inflicted on Gengar
        defender.attack(
            attacker)  # Attacker (Lv 1 | HP : 0 | Attack : 7 | Defence : 4 | Status : "free") takes 9 damage
        self.assertEqual(attacker.get_hp(), 0)  # Checks the hp of attacker is 0
        self.assertEqual(defender.get_hp(),
                         5)  # Defender (Lv 3 | HP : 5 | Attack: 18 | Defence : 3 | Status : "burn") takes 1 damage

    def test_str(self):
        """
        Tests that the str method works correctly for base lv and hp, after levelling up and after losing hp
        """
        # Test 1 - Base Pokemon
        p = Charizard()  # (Lv 3 | HP : 15)
        self.assertEqual(str(p), "LV. 3 Charizard: 15 HP")  # Checks the string representation of Charizard is correct

        # Test 2 - Levelled up Pokemon by 2 levels
        p = Charizard()  # (Lv 3 | HP : 15)
        p.level_up()  # (Lv 4 | HP : 16)
        p.level_up()  # (Lv 5 | HP : 17)
        self.assertEqual(str(p),
                         "LV. 5 Charizard: 17 HP")  # Checks the string representation of Charizard is correct after levelling up

        # Test 3 - Pokemon loses 2 hp
        p = Charizard()  # (Lv 3 | HP : 15)
        p.lose_hp(2)  # (Lv 3 | HP : 13)
        self.assertEqual(str(p),
                         "LV. 3 Charizard: 13 HP")  # Checks the string representation of Charizard is correct after losing hp

    def test_heal(self):
        """
        Tests that the heal method works correctly by calling heal on 3 different Pokemon
        3 tests will be done for when hp is lost, status is inflicted, and when status is inflicted and hp is lost
        """
        # Test 1 - Pokemon loses 2 hp and will be back to full health after heal
        p = Charizard()  # (Lv 3 | HP : 15)
        p.lose_hp(2)  # (Lv 3 | HP : 13)
        self.assertEqual(p.get_hp(), 13)  # Checks the current hp of Charizard after losing hp
        p.heal()  # (Lv 3 | HP : 15)
        self.assertEqual(p.get_hp(), 15)  # Checks the current hp of Charizard after healing

        # Test 2 - Pokemon with status "sleep" with no lost of hp will have status be "free" after heal
        p = Squirtle()  # (Lv 1 | HP : 11 | Status : "free")
        p.status = "sleep"  # (Lv 1 | HP : 11 | Status : "sleep")
        self.assertEqual(p.get_status_inflicted(), "sleep")  # Checks that status is "sleep"
        p.heal()  # (Lv 1 | HP : 11 | Status : "free")
        self.assertEqual(p.get_status_inflicted(), "free")  # Checks that status is "free"

        # Test 3 - Pokemon with status "paralysis" loses 5 hp and will be back to full health after heal with status "free"
        p = Eevee()  # (Lv 1 | HP : 10 | Status : "free")
        p.status = "paralysis"  # (Lv 1 | HP : 10 | Status : "paralysis")
        self.assertEqual(p.get_status_inflicted(), "paralysis")  # Checks that status is "paralysis"
        p.lose_hp(5)  # (Lv 1 | HP : 5 | Status : "paralysis")
        self.assertEqual(p.get_hp(), 5)  # Checks the current hp of Eevee after losing hp
        p.heal()  # (Lv 1 | HP : 10 | Status : "free")
        self.assertEqual(p.get_hp(), 10)  # Checks the current hp of Eevee after healing
        self.assertEqual(p.get_status_inflicted(), "free")  # Checks that status is "free"
