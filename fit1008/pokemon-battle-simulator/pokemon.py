from pokemon_base import PokemonBase
from random_gen import RandomGen

"""
This file header will provide a short description of pokemon.py.
pokemon.py consists of many child Pokemon classes, with unique names, all derived from the abstract class PokemonBase.
These child classes will be forced to implement any abstract functionality in PokemonBase. Thus, this will reduce
the number of errors we make when creating Pokemon objects.

Documentation by : Fawwad and Mandhiren Singh
"""
__author__ = "Scaffold by Jackson Goerner, Code by Fawwad and Mandhiren Singh"

class Charmander(PokemonBase):
    """
    A class to represent an individual Charmander Pokemon.

    Attributes:
        hp : int
            hp of Pokemon
        poke_type : str
            elemental type of Pokemon
        name : str
             name of Pokemon
        level : int
             level of Pokemon
        attack_damage : int
            attack damage stat of Pokemon
        speed : int
             speed stat of Pokemon
        defence : int
             defence stat of Pokemon
        pokedex_id : int
             pokedex id of Pokemon
    """

    def __init__(self):
        """
        Constructs all necessary attributes for a Charmander object.

        Args:
          -

        Preconditions:
          -

        Returns:
          -

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        PokemonBase.__init__(self, 8  + (1 * Charmander.BASE_LEVEL), "Fire")
        self.name = "Charmander"
        self.level = 1
        self.attack_damage = 6 + (1 * Charmander.BASE_LEVEL)
        self.speed = 7 + (1 * Charmander.BASE_LEVEL)
        self.defence = 4
        self.pokedex_id = 0

    def get_max_hp(self) -> int:
        """
        Gets the max hp of Charmander.

        Args:
          -

        Preconditions:
          -

        Returns:
          max_hp : int
            the max hp of Charmander based on current level.

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        max_hp = int(8 + (1 * self.get_level()))
        return max_hp

    def level_up(self) -> None:
        """
        Levels up Pokemon.

        Args:
            -

        Preconditions:
            checks if Charmander is fainted,
                if True, raise an exception,
                    if False, level up.

        Returns:
            -

        Time Complexity:
            Best Case:
                O(1)
            Worst Case:
                O(1)
        """
        old_max_hp = self.get_max_hp()
        self.set_level(self.get_level() + 1)
        new_max_hp = self.get_max_hp()

        self.set_hp(new_max_hp - (old_max_hp - self.get_hp()))

        self.set_attack_damage(6 + (1 * self.get_level()))

        self.set_speed(7 + (1 * self.get_level()))

    def can_evolve(self) -> bool:
        """
        Checks if Charmander can evolve.

        Args:
        -

        Preconditions:
        -

        Returns:
            True - as Charmander has the capability to evolve into Charizard.

        Time Complexity:
            Best Case:
                O(1)
            Worst Case:
                O(1)
        """
        return True

    def should_evolve(self) -> bool:
        """
        Checks if Charmander fulfills the level criteria to evolve.

        Args:
            -

        Preconditions:
            -

        Returns:
            level : int
                checks if level is greater than or equal to 3,
                    if it is, return True,
                        else False.

        Time Complexity:
            Best Case:
                O(1)
            Worst Case:
                O(1)
        """
        return self.level >= 3

    def get_evolved_version(self) -> PokemonBase:
        """
        Gets the evolved version of Charmander.

        Args:
          -

        Preconditions:
          -

        Returns:
          Charizard : PokemonBase
            the final stage evolved version of Charmander.

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        evolved_poke = Charizard()

        evolved_poke.level = self.get_level()

        evolved_poke.hp = evolved_poke.get_max_hp() - (self.get_max_hp() - self.get_hp())

        if self.get_status_inflicted() != "free":
            evolved_poke.status = self.get_status_inflicted()

        return evolved_poke

    def defend(self, effective_damage: int) -> int:
        """
        Calculates the damage taken by the Pokemon after the defence calculation.

        Args:
            effective_damage : int
                a byproduct from effective_attack

        Preconditions:
            -

        Returns:
            damage : int
                damage that is mitigated according to Charmander's damage calculation

        Time Complexity:
            Best Case:
                O(1)
            Worst Case:
                O(1)
        """
        if effective_damage > self.get_defence():
            damage = effective_damage
        else:
            damage = effective_damage // 2
        return damage

    def unique_status_effect(self) -> str:
        """
        Gets the unique status effect the Pokemon can inflict.

        Args:
         -

        Preconditions:
         -

        Returns:
            unique_status : str
                the unique elemental status effect that Charmander can inflict, which is "burn".

        Time Complexity:
            Best Case:
                O(1)
            Worst Case:
                O(1)
        """
        unique_status = "burn"
        return unique_status

class Squirtle(PokemonBase):
    """
    A class to represent an individual Squirtle Pokemon.

    Attributes:
        hp : int
            hp of Pokemon
        poke_type : str
            elemental type of Pokemon
        name : str
             name of Pokemon
        level : int
             level of Pokemon
        attack_damage : int
            attack damage stat of Pokemon
        speed : int
             speed stat of Pokemon
        defence : int
             defence stat of Pokemon
        pokedex_id : int
             pokedex id of Pokemon
    """

    def __init__(self):
        """
        Constructs all necessary attributes for a Squirtle object.

        Args:
          -

        Preconditions:
          -

        Returns:
          -

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        PokemonBase.__init__(self, 9 + (2 * Squirtle.BASE_LEVEL), "Water")
        self.name = "Squirtle"
        self.level = 1
        self.attack_damage = 4 + (Squirtle.BASE_LEVEL // 2)
        self.speed = 7
        self.defence = 6 + (Squirtle.BASE_LEVEL)
        self.pokedex_id = 4

    def get_max_hp(self) -> int:
        """
        Gets the max hp of Squirtle.

        Args:
          -

        Preconditions:
          -

        Returns:
          max_hp : int
            the max hp of Squirtle based on current level.

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        max_hp = int(9 + (2 * self.get_level()))
        return max_hp

    def level_up(self) -> None:
        """
        Levels up Pokemon.

        Args:
            -

        Preconditions:
            checks if Squirtle is fainted,
                if True, raise an exception,
                    if False, level up.

        Returns:
            -

        Time Complexity:
            Best Case:
                O(1)
            Worst Case:
                O(1)
        """
        old_max_hp = self.get_max_hp()
        self.set_level(self.get_level() + 1)
        new_max_hp = self.get_max_hp()

        self.set_hp(new_max_hp - (old_max_hp - self.get_hp()))

        self.set_attack_damage(4 + (self.get_level() // 2))

        self.set_defence(6 + self.get_level())

    def can_evolve(self) -> bool:
        """
        Checks if Squirtle can evolve.

        Args:
        -

        Preconditions:
        -

        Returns:
            True - as Squirtle has the capability to evolve into Blastoise.

        Time Complexity:
            Best Case:
                O(1)
            Worst Case:
                O(1)
        """
        return True

    def should_evolve(self) -> bool:
        """
        Checks if Squirtle fulfills the level criteria to evolve.

        Args:
            -

        Preconditions:
            -

        Returns:
            level : int
                checks if level is greater than or equal to 3,
                    if it is, return True,
                        else False.

        Time Complexity:
            Best Case:
                O(1)
            Worst Case:
                O(1)
        """
        return self.level >= 3

    def get_evolved_version(self) -> PokemonBase:
        """
        Gets the evolved version of Squirtle.

        Args:
          -

        Preconditions:
          -

        Returns:
          Blastoise : PokemonBase
            the final stage evolved version of Squirtle.

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        evolved_poke = Blastoise()

        evolved_poke.level = self.get_level()

        evolved_poke.hp = evolved_poke.get_max_hp() - (self.get_max_hp() - self.get_hp())

        if self.get_status_inflicted() != "free":
            evolved_poke.status = self.get_status_inflicted()

        return evolved_poke

    def defend(self, effective_damage: int) -> int:
        """
        Calculates the damage taken by the Pokemon after the defence calculation.

        Args:
            effective_damage : int
                a byproduct from effective_attack

        Preconditions:
            -

        Returns:
            damage : int
                damage that is mitigated according to Squirtle's damage calculation

        Time Complexity:
            Best Case:
                O(1)
            Worst Case:
                O(1)
        """
        if effective_damage > (2 * self.get_defence()):
            damage = effective_damage
        else:
            damage = effective_damage // 2
        return damage

    def unique_status_effect(self) -> str:
        """
        Gets the unique status effect the Pokemon can inflict.

        Args:
         -

        Preconditions:
         -

        Returns:
            unique_status : str
                the unique elemental status effect that Squirtle can inflict, which is "paralysis".

        Time Complexity:
            Best Case: s
                O(1)
            Worst Case:
                O(1)
        """
        unique_status = "paralysis"
        return unique_status

class Bulbasaur(PokemonBase):
    """
    A class to represent an individual Bulbasaur Pokemon.

    Attributes:
        hp : int
            hp of Pokemon
        poke_type : str
            elemental type of Pokemon
        name : str
             name of Pokemon
        level : int
             level of Pokemon
        attack_damage : int
            attack damage stat of Pokemon
        speed : int
             speed stat of Pokemon
        defence : int
             defence stat of Pokemon
        pokedex_id : int
             pokedex id of Pokemon
    """

    def __init__(self):
        """
        Constructs all necessary attributes for a Bulbasaur object.

        Args:
          -

        Preconditions:
          -

        Returns:
          -

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        PokemonBase.__init__(self, 12 + (1 * Bulbasaur.BASE_LEVEL), "Grass")
        self.name = "Bulbasaur"
        self.level = 1
        self.attack_damage = 5
        self.speed = 7 + (Bulbasaur.BASE_LEVEL // 2)
        self.defence = 5
        self.pokedex_id = 2

    def get_max_hp(self) -> int:
        """
        Gets the max hp of Bulbasaur.

        Args:
          -

        Preconditions:
          -

        Returns:
          max_hp : int
            the max hp of Bulbasaur based on current level.

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        max_hp = int(12 + (1 * self.get_level()))
        return max_hp

    def level_up(self) -> None:
        """
        Levels up Pokemon.

        Args:
            -

        Preconditions:
            checks if Bulbasaur is fainted,
                if True, raise an exception,
                    if False, level up.

        Returns:
            -

        Time Complexity:
            Best Case:
                O(1)
            Worst Case:
                O(1)
        """
        old_max_hp = self.get_max_hp()
        self.set_level(self.get_level() + 1)
        new_max_hp = self.get_max_hp()

        self.set_hp(new_max_hp - (old_max_hp - self.get_hp()))

        self.set_speed(7 + (self.get_level() // 2))

    def can_evolve(self) -> bool:
        """
        Checks if Bulbasaur can evolve.

        Args:
        -

        Preconditions:
        -

        Returns:
            True - as Bulbasaur has the capability to evolve into Venusaur.

        Time Complexity:
            Best Case:
                O(1)
            Worst Case:
                O(1)
        """
        return True

    def should_evolve(self) -> bool:
        """
        Checks if Bulbasaur fulfills the level criteria to evolve.

        Args:
            -

        Preconditions:
            -

        Returns:
            level : int
                checks if level is greater than or equal to 2,
                    if it is, return True,
                        else False.

        Time Complexity:
            Best Case:
                O(1)
            Worst Case:
                O(1)
        """
        return self.level >= 2

    def get_evolved_version(self) -> PokemonBase:
        """
        Gets the evolved version of Bulbasaur.

        Args:
          -

        Preconditions:
          -

        Returns:
          Venusaur : PokemonBase
            the final stage evolved version of Bulbasaur.

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        evolved_poke = Venusaur()

        evolved_poke.level = self.get_level()

        evolved_poke.hp = evolved_poke.get_max_hp() - (self.get_max_hp() - self.get_hp())

        if self.get_status_inflicted() != "free":
            evolved_poke.status = self.get_status_inflicted()

        return evolved_poke

    def defend(self, effective_damage: int) -> int:
        """
        Calculates the damage taken by the Pokemon after the defence calculation.

        Args:
            effective_damage : int
                a byproduct from effective_attack

        Preconditions:
            -

        Returns:
            damage : int
                damage that is mitigated according to Bulbasaur's damage calculation

        Time Complexity:
            Best Case:
                O(1)
            Worst Case:
                O(1)
        """
        if effective_damage > (self.get_defence() + 5):
            damage = effective_damage
        else:
            damage = effective_damage // 2
        return damage

    def unique_status_effect(self) -> str:
        """
        Gets the unique status effect the Pokemon can inflict.

        Args:
         -

        Preconditions:
         -

        Returns:
            unique_status : str
                the unique elemental status effect that Bulbasaur can inflict, which is "poison".

        Time Complexity:
            Best Case:
                O(1)
            Worst Case:
                O(1)
        """
        unique_status = "poison"
        return unique_status

class Gastly(PokemonBase):
    """
    A class to represent an individual Gastly Pokemon.

    Attributes:
        hp : int
            hp of Pokemon
        poke_type : str
            elemental type of Pokemon
        name : str
             name of Pokemon
        level : int
             level of Pokemon
        attack_damage : int
            attack damage stat of Pokemon
        speed : int
             speed stat of Pokemon
        defence : int
             defence stat of Pokemon
        pokedex_id : int
             pokedex id of Pokemon
    """

    def __init__(self):
        """
        Constructs all necessary attributes for a Gastly object.

        Args:
          -

        Preconditions:
          -

        Returns:
          -

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        PokemonBase.__init__(self, 6 + (Gastly.BASE_LEVEL // 2), "Ghost")
        self.name = "Gastly"
        self.level = 1
        self.attack_damage = 4
        self.speed = 2
        self.defence = 8
        self.pokedex_id = 6

    def get_max_hp(self) -> int:
        """
        Gets the max hp of Gastly.

        Args:
          -

        Preconditions:
          -

        Returns:
          max_hp : int
            the max hp of Gastly based on current level.

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        max_hp = int(6 + (self.get_level() // 2))
        return max_hp

    def level_up(self) -> None:
        """
        Levels up Pokemon.

        Args:
            -

        Preconditions:
            checks if Gastly is fainted,
                if True, raise an exception,
                    if False, level up.

        Returns:
            -

        Time Complexity:
            Best Case:
                O(1)
            Worst Case:
                O(1)
        """
        old_max_hp = self.get_max_hp()
        self.set_level(self.get_level() + 1)
        new_max_hp = self.get_max_hp()

        self.set_hp(new_max_hp - (old_max_hp - self.get_hp()))

    def can_evolve(self) -> bool:
        """
        Checks if Gastly can evolve.

        Args:
        -

        Preconditions:
        -

        Returns:
            True - as Gastly has the capability to evolve into Haunter.

        Time Complexity:
            Best Case:
                O(1)
            Worst Case:
                O(1)
        """
        return True

    def should_evolve(self) -> bool:
        """
        Checks if Gastly fulfills the level criteria to evolve.

        Args:
            -

        Preconditions:
            -

        Returns:
            level : int
                checks if level is greater than or equal to 1,
                    if it is, return True,
                        else False.

        Time Complexity:
            Best Case:
                O(1)
            Worst Case:
                O(1)
        """
        return self.level >= 1

    def get_evolved_version(self) -> PokemonBase:
        """
        Gets the evolved version of Gastly.

        Args:
          -

        Preconditions:
          -

        Returns:
          Haunter : PokemonBase
            the second stage evolved version of Gastly.

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        evolved_poke = Haunter()

        evolved_poke.level = self.get_level()

        evolved_poke.hp = evolved_poke.get_max_hp() - (self.get_max_hp() - self.get_hp())

        if self.get_status_inflicted() != "free":
            evolved_poke.status = self.get_status_inflicted()

        return evolved_poke

    def defend(self, effective_damage: int) -> int:
        """
        Calculates the damage taken by the Pokemon after the defence calculation.

        Args:
            effective_damage : int
                a byproduct from effective_attack

        Preconditions:
            -

        Returns:
            damage : int
                damage that is mitigated according to Gastly's damage calculation

        Time Complexity:
            Best Case:
                O(1)
            Worst Case:
                O(1)
        """
        damage = effective_damage
        return damage

    def unique_status_effect(self) -> str:
        """
        Gets the unique status effect the Pokemon can inflict.

        Args:
         -

        Preconditions:
         -

        Returns:
            unique_status : str
                the unique elemental status effect that Gastly can inflict, which is "sleep".

        Time Complexity:
            Best Case:
                O(1)
            Worst Case:
                O(1)
        """
        unique_status = "sleep"
        return unique_status

class Eevee(PokemonBase):
    """
    A class to represent an individual Eevee Pokemon.

    Attributes:
        hp : int
            hp of Pokemon
        poke_type : str
            elemental type of Pokemon
        name : str
             name of Pokemon
        level : int
             level of Pokemon
        attack_damage : int
            attack damage stat of Pokemon
        speed : int
             speed stat of Pokemon
        defence : int
             defence stat of Pokemon
        pokedex_id : int
             pokedex id of Pokemon
    """

    def __init__(self):
        """
        Constructs all necessary attributes for a Eevee object.

        Args:
          -

        Preconditions:
          -

        Returns:
          -

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        PokemonBase.__init__(self, 10, "Normal")
        self.name = "Eevee"
        self.level = 1
        self.attack_damage = 6 + Eevee.BASE_LEVEL
        self.speed = 7 + Eevee.BASE_LEVEL
        self.defence = 4 + Eevee.BASE_LEVEL
        self.pokedex_id = 9

    def get_max_hp(self) -> int:
        """
        Gets the max hp of Eevee.

        Args:
          -

        Preconditions:
          -

        Returns:
          max_hp : int
            the max hp of Eevee based on current level.

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        max_hp = int(10)
        return max_hp

    def level_up(self) -> None:
        """
        Levels up Pokemon.

        Args:
            -

        Preconditions:
            checks if Eevee is fainted,
                if True, raise an exception,
                    if False, level up.

        Returns:
            -

        Time Complexity:
            Best Case:
                O(1)
            Worst Case:
                O(1)
        """
        old_max_hp = self.get_max_hp()
        self.set_level(self.get_level() + 1)
        new_max_hp = self.get_max_hp()

        self.set_hp(new_max_hp - (old_max_hp - self.get_hp()))

        self.set_attack_damage(6 + self.get_level())

        self.set_speed(7 + self.get_level())

        self.set_defence(4 + self.get_level())

    def can_evolve(self) -> bool:
        """
        Checks if Eevee can evolve.

        Args:
        -

        Preconditions:
        -

        Returns:
            False - as Eevee does not have the capability to evolve.

        Time Complexity:
            Best Case:
                O(1)
            Worst Case:
                O(1)
        """
        return False

    def should_evolve(self) -> bool:
        """
        Checks if Eevee fulfills the level criteria to evolve.

        Args:
            -

        Preconditions:
            -

        Returns:
            False

        Time Complexity:
            Best Case:
                O(1)
            Worst Case:
                O(1)
        """
        return False

    def get_evolved_version(self) -> None:
        """
        This function returns the evolved version of the Pokemon.
        Time Complexity : O(1)

        Args:
          -

        Returns:
          PokemonBase : instance of the Pokemon.
        """
        return None

    def defend(self, effective_damage: int) -> int:
        """
        Calculates the damage taken by the Pokemon after the defence calculation.

        Args:
            effective_damage : int
                a byproduct from effective_attack

        Preconditions:
            -

        Returns:
            damage : int
                damage that is mitigated according to Eevee's damage calculation

        Time Complexity:
            Best Case:
                O(1)
            Worst Case:
                O(1)
        """
        if effective_damage >= self.get_defence():
            damage = effective_damage
        else:
            damage = 0
        return damage

    def unique_status_effect(self) -> str:
        """
        Gets the unique status effect the Pokemon can inflict.

        Args:
         -

        Preconditions:
         -

        Returns:
            unique_status : str
                the unique elemental status effect that Eevee can inflict, which is "confuse".

        Time Complexity:
            Best Case:
                O(1)
            Worst Case:
                O(1)
        """
        unique_status = "confuse"
        return unique_status

class Charizard(PokemonBase):
    BASE_LEVEL = 3
    """
    A class to represent an individual Charizard Pokemon.

    Attributes:
        hp : int
            hp of Pokemon
        poke_type : str
            elemental type of Pokemon
        name : str
             name of Pokemon
        level : int
             level of Pokemon
        attack_damage : int
            attack damage stat of Pokemon
        speed : int
             speed stat of Pokemon
        defence : int
             defence stat of Pokemon
        pokedex_id : int
             pokedex id of Pokemon
    """

    def __init__(self):
        """
        Constructs all necessary attributes for a Charizard object.

        Args:
          -

        Preconditions:
          -

        Returns:
          -

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        PokemonBase.__init__(self, 12 + (1 * Charizard.BASE_LEVEL), "Fire")
        self.name = "Charizard"
        self.evolves_from = "Charmander"
        self.level = 3
        self.attack_damage = 10 + (2 * Charizard.BASE_LEVEL)
        self.speed = 9 + (1 * Charizard.BASE_LEVEL)
        self.defence = 4
        self.pokedex_id = 1

    def get_max_hp(self) -> int:
        """
        Gets the max hp of Charizard.

        Args:
          -

        Preconditions:
          -

        Returns:
          max_hp : int
            the max hp of Charizard based on current level.

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        max_hp = int(12 + (1 * self.get_level()))
        return max_hp

    def level_up(self) -> None:
        """
        Levels up Pokemon.

        Args:
            -

        Preconditions:
            checks if Charizard is fainted,
                if True, raise an exception,
                    if False, level up.

        Returns:
            -

        Time Complexity:
            Best Case:
                O(1)
            Worst Case:
                O(1)
        """
        old_max_hp = self.get_max_hp()
        self.set_level(self.get_level() + 1)
        new_max_hp = self.get_max_hp()

        self.set_hp(new_max_hp - (old_max_hp - self.get_hp()))

        # Setting Attack stat upon levelling
        self.set_attack_damage(10 + (2 * self.get_level()))

        # Set Speed Stat upon levelling
        self.set_speed(9 + (1 * self.get_level()))

    def can_evolve(self) -> bool:
        """
        Checks if Charizard can evolve.

        Args:
        -

        Preconditions:
        -

        Returns:
            False - as Charizard does not have the capability to evolve.

        Time Complexity:
            Best Case:
                O(1)
            Worst Case:
                O(1)
        """
        return False

    def should_evolve(self) -> bool:
        """
        Checks if Charizard fulfills the level criteria to evolve.

        Args:
            -

        Preconditions:
            -

        Returns:
            False

        Time Complexity:
            Best Case:
                O(1)
            Worst Case:
                O(1)
        """
        return False

    def get_evolved_version(self) -> None:
        """
        Gets the evolved version of Charizard.

        Args:
          -

        Preconditions:
          -

        Returns:
          None

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        return None

    def defend(self, effective_damage: int) -> int:
        """
        Calculates the damage taken by the Pokemon after the defence calculation.

        Args:
            effective_damage : int
                a byproduct from effective_attack

        Preconditions:
            -

        Returns:
            damage : int
                damage that is mitigated according to Charizard's damage calculation

        Time Complexity:
            Best Case:
                O(1)
            Worst Case:
                O(1)
        """
        if effective_damage > self.get_defence():
            damage = 2 * effective_damage
        else:
            damage = effective_damage
        return damage

    def unique_status_effect(self) -> str:
        """
        Gets the unique status effect the Pokemon can inflict.

        Args:
         -

        Preconditions:
         -

        Returns:
            unique_status : str
                the unique elemental status effect that Charizard can inflict, which is "burn".

        Time Complexity:
            Best Case:
                O(1)
            Worst Case:
                O(1)
        """
        unique_status = "burn"
        return unique_status

class Blastoise(PokemonBase):
    BASE_LEVEL = 3
    """
    A class to represent an individual Blastoise Pokemon.

    Attributes:
        hp : int
            hp of Pokemon
        poke_type : str
            elemental type of Pokemon
        name : str
             name of Pokemon
        level : int
             level of Pokemon
        attack_damage : int
            attack damage stat of Pokemon
        speed : int
             speed stat of Pokemon
        defence : int
             defence stat of Pokemon
        pokedex_id : int
             pokedex id of Pokemon
    """

    def __init__(self):
        """
        Constructs all necessary attributes for a Blastoise object.

        Args:
          -

        Preconditions:
          -

        Returns:
          -

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        PokemonBase.__init__(self, 15 + (2 * Blastoise.BASE_LEVEL), "Water")
        self.name = "Blastoise"
        self.evolves_from = "Squirtle"
        self.level = 3
        self.attack_damage = 8 + (Blastoise.BASE_LEVEL // 2)
        self.speed = 10
        self.defence = 8 + (1 * Blastoise.BASE_LEVEL)
        self.pokedex_id = 5

    def get_max_hp(self) -> int:
        """
        Gets the max hp of Blastoise.

        Args:
          -

        Preconditions:
          -

        Returns:
          max_hp : int
            the max hp of Blastoise based on current level.

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        max_hp = int(15 + (2 * self.get_level()))
        return max_hp

    def level_up(self) -> None:
        """
        Levels up Pokemon.

        Args:
            -

        Preconditions:
            checks if Blastoise is fainted,
                if True, raise an exception,
                    if False, level up.

        Returns:
            -

        Time Complexity:
            Best Case:
                O(1)
            Worst Case:
                O(1)
        """
        old_max_hp = self.get_max_hp()
        self.set_level(self.get_level() + 1)
        new_max_hp = self.get_max_hp()

        self.set_hp(new_max_hp - (old_max_hp - self.get_hp()))

        self.set_attack_damage(8 + (self.get_level() // 2))

        self.set_defence(8 + (1 * self.get_level()))

    def can_evolve(self) -> bool:
        """
        Checks if Blastoise can evolve.

        Args:
        -

        Preconditions:
        -

        Returns:
            False - as Blastoise does not have the capability to evolve.

        Time Complexity:
            Best Case:
                O(1)
            Worst Case:
                O(1)
        """
        return False

    def should_evolve(self) -> bool:
        """
        Checks if Blastoise fulfills the level criteria to evolve.

        Args:
            -

        Preconditions:
            -

        Returns:
            False

        Time Complexity:
            Best Case:
                O(1)
            Worst Case:
                O(1)
        """
        return False

    def get_evolved_version(self) -> None:
        """
        Gets the evolved version of Blastoise.

        Args:
          -

        Preconditions:
          -

        Returns:
          None

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        return None

    def defend(self, effective_damage: int) -> int:
        """
        Calculates the damage taken by the Pokemon after the defence calculation.

        Args:
            effective_damage : int
                a byproduct from effective_attack

        Preconditions:
            -

        Returns:
            damage : int
                damage that is mitigated according to Blastoise's damage calculation

        Time Complexity:
            Best Case:
                O(1)
            Worst Case:
                O(1)
        """
        if effective_damage > (2 * self.get_defence()):
            damage = effective_damage
        else:
            damage = effective_damage // 2
        return damage

    def unique_status_effect(self) -> str:
        """
        Gets the unique status effect the Pokemon can inflict.

        Args:
         -

        Preconditions:
         -

        Returns:
            unique_status : str
                the unique elemental status effect that Blastoise can inflict, which is "paralysis".

        Time Complexity:
            Best Case:
                O(1)
            Worst Case:
                O(1)
        """
        unique_status = "paralysis"
        return unique_status

class Venusaur(PokemonBase):
    BASE_LEVEL = 2
    """
    A class to represent an individual Venusaur Pokemon.

    Attributes:
        hp : int
            hp of Pokemon
        poke_type : str
            elemental type of Pokemon
        name : str
             name of Pokemon
        level : int
             level of Pokemon
        attack_damage : int
            attack damage stat of Pokemon
        speed : int
             speed stat of Pokemon
        defence : int
             defence stat of Pokemon
        pokedex_id : int
             pokedex id of Pokemon
    """

    def __init__(self):
        """
        Constructs all necessary attributes for a Venusaur object.

        Args:
          -

        Preconditions:
          -

        Returns:
          -

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        PokemonBase.__init__(self, 20 + (Venusaur.BASE_LEVEL // 2), "Grass")
        self.name = "Venusaur"
        self.evolves_from = "Bulbasaur"
        self.level = 2
        self.attack_damage = 5
        self.speed = 3 + (Venusaur.BASE_LEVEL // 2)
        self.defence = 10
        self.pokedex_id = 3

    def get_max_hp(self) -> int:
        """
        Gets the max hp of Venusaur.

        Args:
          -

        Preconditions:
          -

        Returns:
          max_hp : int
            the max hp of Venusaur based on current level.

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        max_hp = int(20 + (self.get_level() // 2))
        return max_hp

    def level_up(self) -> None:
        """
        Levels up Pokemon.

        Args:
            -

        Preconditions:
            checks if Venusaur is fainted,
                if True, raise an exception,
                    if False, level up.

        Returns:
            -

        Time Complexity:
            Best Case:
                O(1)
            Worst Case:
                O(1)
        """
        old_max_hp = self.get_max_hp()
        self.set_level(self.get_level() + 1)
        new_max_hp = self.get_max_hp()

        self.set_hp(new_max_hp - (old_max_hp - self.get_hp()))

        self.set_speed(3 + (self.get_level() // 2))

    def can_evolve(self) -> bool:
        """
        Checks if Venusaur can evolve.

        Args:
        -

        Preconditions:
        -

        Returns:
            False - as Venusaur does not have the capability to evolve.

        Time Complexity:
            Best Case:
                O(1)
            Worst Case:
                O(1)
        """
        return False

    def should_evolve(self) -> bool:
        """
        Checks if Venusaur fulfills the level criteria to evolve.

        Args:
            -

        Preconditions:
            -

        Returns:
            False

        Time Complexity:
            Best Case:
                O(1)
            Worst Case:
                O(1)
        """
        return False

    def get_evolved_version(self) -> None:
        """
        Gets the evolved version of Venusaur.

        Args:
          -

        Preconditions:
          -

        Returns:
          None

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        return None

    def defend(self, effective_damage: int) -> int:
        """
        Calculates the damage taken by the Pokemon after the defence calculation.

        Args:
            effective_damage : int
                a byproduct from effective_attack

        Preconditions:
            -

        Returns:
            damage : int
                damage that is mitigated according to Venusaur's damage calculation

        Time Complexity:
            Best Case:
                O(1)
            Worst Case:
                O(1)
        """
        if effective_damage > (self.get_defence() + 5):
            damage = effective_damage
        else:
            damage = effective_damage // 2
        return damage

    def unique_status_effect(self) -> str:
        """
        Gets the unique status effect the Pokemon can inflict.

        Args:
         -

        Preconditions:
         -

        Returns:
            unique_status : str
                the unique elemental status effect that Venusaur can inflict, which is "poison".

        Time Complexity:
            Best Case:
                O(1)
            Worst Case:
                O(1)
        """
        unique_status = "poison"
        return unique_status

class Haunter(PokemonBase):
    """
    A class to represent an individual Haunter Pokemon.

    Attributes:
        hp : int
            hp of Pokemon
        poke_type : str
            elemental type of Pokemon
        name : str
             name of Pokemon
        level : int
             level of Pokemon
        attack_damage : int
            attack damage stat of Pokemon
        speed : int
             speed stat of Pokemon
        defence : int
             defence stat of Pokemon
        pokedex_id : int
             pokedex id of Pokemon
    """

    def __init__(self):
        """
        Constructs all necessary attributes for a Haunter object.

        Args:
          -

        Preconditions:
          -

        Returns:
          -

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        PokemonBase.__init__(self, 9 + (Haunter.BASE_LEVEL // 2), "Ghost")
        self.name = "Haunter"
        self.evolves_from = "Gastly"
        self.level = 1
        self.attack_damage = 8
        self.speed = 6  
        self.defence = 6
        self.pokedex_id = 7

    def get_max_hp(self) -> int:
        """
        Gets the max hp of Haunter.

        Args:
          -

        Preconditions:
          -

        Returns:
          max_hp : int
            the max hp of Haunter based on current level.

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        max_hp = int(9 + (self.get_level() // 2))
        return max_hp

    def level_up(self) -> None:
        """
        Levels up Pokemon.

        Args:
            -

        Preconditions:
            checks if Haunter is fainted,
                if True, raise an exception,
                    if False, level up.

        Returns:
            -

        Time Complexity:
            Best Case:
                O(1)
            Worst Case:
                O(1)
        """
        old_max_hp = self.get_max_hp()
        self.set_level(self.get_level() + 1)
        new_max_hp = self.get_max_hp()

        self.set_hp(new_max_hp - (old_max_hp - self.get_hp()))

    def can_evolve(self) -> bool:
        """
        Checks if Haunter can evolve.

        Args:
        -

        Preconditions:
        -

        Returns:
            True - as Haunter does have the capability to evolve.

        Time Complexity:
            Best Case:
                O(1)
            Worst Case:
                O(1)
        """
        return True

    def should_evolve(self) -> bool:
        """
        Checks if Haunter fulfills the level criteria to evolve.

        Args:
            -

        Preconditions:
            -

        Returns:
            level : int
                checks if level is greater than or equal to 3,
                    if it is, return True,
                        else False.

        Time Complexity:
            Best Case:
                O(1)
            Worst Case:
                O(1)
        """
        return self.get_level() >= 3

    def get_evolved_version(self) -> PokemonBase:
        """
        Gets the evolved version of Haunter.

        Args:
          -

        Preconditions:
          -

        Returns:
          Gengar : PokemonBase
            the final stage evolved version of Gastly.

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        evolved_poke = Gengar()

        evolved_poke.level = self.get_level()

        evolved_poke.hp = evolved_poke.get_max_hp() - (self.get_max_hp() - self.get_hp())

        if self.get_status_inflicted() != "free":
            evolved_poke.status = self.get_status_inflicted()

        return evolved_poke

    def defend(self, effective_damage: int) -> int:
        """
        Calculates the damage taken by the Pokemon after the defence calculation.

        Args:
            effective_damage : int
                a byproduct from effective_attack

        Preconditions:
            -

        Returns:
            damage : int
                damage that is mitigated according to Haunter's damage calculation

        Time Complexity:
            Best Case:
                O(1)
            Worst Case:
                O(1)
        """
        damage = effective_damage
        return damage

    def unique_status_effect(self) -> str:
        """
        Gets the unique status effect the Pokemon can inflict.

        Args:
         -

        Preconditions:
         -

        Returns:
            unique_status : str
                the unique elemental status effect that Haunter can inflict, which is "sleep".

        Time Complexity:
            Best Case:
                O(1)
            Worst Case:
                O(1)
        """
        unique_status = "sleep"
        return unique_status

class Gengar(PokemonBase):
    BASE_LEVEL = 3
    """
    A class to represent an individual Gengar Pokemon.

    Attributes:
        hp : int
            hp of Pokemon
        poke_type : str
            elemental type of Pokemon
        name : str
             name of Pokemon
        level : int
             level of Pokemon
        attack_damage : int
            attack damage stat of Pokemon
        speed : int
             speed stat of Pokemon
        defence : int
             defence stat of Pokemon
        pokedex_id : int
             pokedex id of Pokemon
    """

    def __init__(self):
        """
        Constructs all necessary attributes for a Gengar object.

        Args:
          -

        Preconditions:
          -

        Returns:
          -

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        PokemonBase.__init__(self, 12 + (Gengar.BASE_LEVEL // 2), "Ghost")
        self.name = "Gengar"
        self.evolves_from = "Gastly"
        self.level = 3
        self.attack_damage = 18
        self.speed = 12  
        self.defence = 3
        self.pokedex_id = 8

    def get_max_hp(self) -> int:
        """
        Gets the max hp of Gengar.

        Args:
          -

        Preconditions:
          -

        Returns:
          max_hp : int
            the max hp of Gengar based on current level.

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        max_hp = int(12 + (self.get_level() // 2))
        return max_hp

    def level_up(self) -> None:
        """
        Levels up Pokemon.

        Args:
            -

        Preconditions:
            checks if Gengar is fainted,
                if True, raise an exception,
                    if False, level up.

        Returns:
            -

        Time Complexity:
            Best Case:
                O(1)
            Worst Case:
                O(1)
        """
        old_max_hp = self.get_max_hp()
        self.set_level(self.get_level() + 1)
        new_max_hp = self.get_max_hp()

        self.set_hp(new_max_hp - (old_max_hp - self.get_hp()))

    def can_evolve(self) -> bool:
        """
        Checks if Gengar can evolve.

        Args:
        -

        Preconditions:
        -

        Returns:
            False - as Gengar does not have the capability to evolve.

        Time Complexity:
            Best Case:
                O(1)
            Worst Case:
                O(1)
        """
        return False

    def should_evolve(self) -> bool:
        """
        Checks if Gengar fulfills the level criteria to evolve.

        Args:
            -

        Preconditions:
            -

        Returns:
            False

        Time Complexity:
            Best Case:
                O(1)
            Worst Case:
                O(1)
        """
        return False

    def get_evolved_version(self) -> None:
        """
        Gets the evolved version of Gengar.

        Args:
          -

        Preconditions:
          -

        Returns:
            None

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        return None

    def defend(self, effective_damage: int) -> int:
        """
        Calculates the damage taken by the Pokemon after the defence calculation.

        Args:
            effective_damage : int
                a byproduct from effective_attack

        Preconditions:
            -

        Returns:
            damage : int
                damage that is mitigated according to Gengar's damage calculation

        Time Complexity:
            Best Case:
                O(1)
            Worst Case:
                O(1)
        """
        damage = effective_damage
        return damage

    def unique_status_effect(self) -> str:
        """
        Gets the unique status effect the Pokemon can inflict.

        Args:
         -

        Preconditions:
         -

        Returns:
            unique_status : str
                the unique elemental status effect that Gengar can inflict, which is "sleep".

        Time Complexity:
            Best Case:
                O(1)
            Worst Case:
                O(1)
        """
        unique_status = "sleep"
        return unique_status
