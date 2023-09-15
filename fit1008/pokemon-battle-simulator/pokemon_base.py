from __future__ import annotations
from typing import Tuple
from abc import ABC, abstractmethod
from random_gen import RandomGen

"""
This file header will provide a short description of pokemon_base.py.
pokemon_base.py implements the abstract class called "PokemonBase", it is a class in which objects cannot be
instantiated from. It will be used later as a base class (parent class) in pokemon.py, to implement the functionality
of each individual Pokemon, as per the assignment specs.

Documentation by : Fawwad and Mandhiren Singh
"""
__author__ = "Scaffold by Jackson Goerner, Code by Nisha, Mandhiren Singh and Fawwad"

class PokemonBase(ABC):
    """
    An abstract class that represents a Pokemon.

    Attributes:
    hp : int
        hp of Pokemon
    poke_type : str
        elemental type of Pokemon
    level : int
        level of Pokemon
    status : int
        status of Pokemon   
    """
    BASE_LEVEL = 1
    POKE_TYPES = ["Fire", "Grass", "Water", "Ghost", "Normal"]
    STATUS_EFFECTS = ["burn", "poison", "paralysis", "sleep", "confuse", "free"]

    def __init__(self, hp: int, poke_type: str) -> None:
        """
        Constructs all necessary attributes for a PokemonBase

        Args:
            hp : int
                the hp of a Pokemon
            poke_type : str
                the elemental poke_type of a Pokemon

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
        # User-facing : Check pre-conditions
        if poke_type not in PokemonBase.POKE_TYPES:
            raise ValueError("Type value is invalid!")

        if not isinstance(hp, int):
            raise TypeError("HP value provided is not an integer!")

        if hp <= 0:
            raise ValueError("Only positive HP values are allowed!")


        # Instance variables initialisation
        self.level = self.BASE_LEVEL
        self.hp = hp
        self.poke_type = poke_type
        self.status = "free"
    
    def get_poke_name(self) -> str:
        """
        Gets name of Pokemon.

        Args:
          -

        Preconditions:
          -

        Returns:
          name : str
            name of the Pokemon.

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        return self.name

    def get_hp(self) -> int:
        """
        Gets current hp stat of Pokemon.

        Args:
          -

        Preconditions:
          -

        Returns:
          hp : int
            current hp of Pokemon.

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        return self.hp

    def set_hp(self, hp: int) -> None:
        """
        Sets Pokemon hp.

        Args:
          hp : int
            new hp of Pokemon.

        Preconditions:
          hp must be valid.
            i.e. hp is positive and be of integer type.
              else an ValueError is raised.

        Returns:
          -

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        if type(hp) != int:
          raise ValueError("Invalid hp - hp is not an integer.")
        elif hp < 0:
          raise ValueError("Invalid hp - hp cannot be negative.")
        else:
          self.hp = int(hp)

    def get_level(self) -> int:
        """
        Gets level of Pokemon.

        Args:
          -

        Preconditions:
          -

        Returns:
          level : int
            current level of Pokemon.

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        return self.level

    def set_level(self, level: int) -> None:
        """
        Sets level of Pokemon.

        Args:
          level : int
            new level of Pokemon.

        Preconditions:
          level must be valid.
            i.e. level is not zero, is positive and is of integer type,
              else an ValueError is raised.

        Returns:
          -

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        if type(level) != int:
            raise ValueError("Invalid level - level is not an integer.")
        elif level < 0:
            raise ValueError("Invalid level - level is negative.")
        elif level == 0:
            raise ValueError("Invalid level - level is zero.")
        else:
            self.level = level

    def get_poke_type(self) -> str:
        """
        Gets elemental type of Pokemon.

        Args:
          -

        Preconditions:
          -

        Returns:
          poke_type : str
            Elemental type of the Pokemon.

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        return self.poke_type

    def get_status_inflicted(self) -> str:
        """
        Gets the current status of Pokemon.

        Args:
          -

        Preconditions:
          -

        Returns:
          status : str
            current status inflicted on the Pokemon.

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        return self.status

    def set_status(self, status: str) -> None:
        """
        Sets status on Pokemon.

        Args:
          status : str
            new status of Pokemon.

        Preconditions:
          status must be valid.
            i.e. status belongs to the pre-existing status list,
              else an ValueError is raised

        Returns:
          name : str
            name of the Pokemon.

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        if status not in PokemonBase.STATUS_EFFECTS:
            raise ValueError("Invalid status - status not found in list.")
        else:
            self.status = status

    def clear_status(self) -> None:
        """
        Clears current status of Pokemon and sets it to "free".

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
        self.set_status("free")

    def get_speed(self) -> int:
        """
        Gets speed stat of Pokemon.

        Args:
          -

        Preconditions:
          checks if Pokemon is currently paralysed, if True, then return halve the speed,
            else return the speed.

        Returns:
          speed : int
            speed of the Pokemon.

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        if self.get_status_inflicted() == "paralysis":
            return self.speed // 2
        return self.speed

    def set_speed(self, speed: int) -> None:
        """
        Sets speed stat of Pokemon.

        Args:
          speed : int
            new speed of Pokemon.

        Preconditions:
          speed must be valid.
            i.e. speed is not zero, is positive and is of integer type,
              else an ValueError is raised.

        Returns:
          -

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        if type(speed) != int:
            raise ValueError("Invalid speed - speed is not an integer.")
        elif speed < 0:
            raise ValueError("Invalid speed - speed is negative.")
        elif speed == 0:
            raise ValueError("Invalid speed - speed is zero.")
        else:
            self.speed = int(speed)

    def get_attack_damage(self) -> int:
        """
        Gets attack damage stat of Pokemon.

        Args:
          -

        Preconditions:
          -

        Returns:
          attack_damage : int
            attack damage stat of Pokemon.

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        return self.attack_damage

    def set_attack_damage(self, attack_stat: int) -> None:
        """
        Sets attack damage stat of Pokemon.

        Args:
          attack_stat : int
            new attack stat of Pokemon.

        Preconditions:
          attack_stat must be valid.
            i.e. attack must not be zero, positive and must be of integer type,
              else an ValueError is raised.

        Returns:
          -

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        if type(attack_stat) != int:
            raise ValueError("Invalid attack damage - attack damage is not an integer.")
        elif attack_stat < 0:
            raise ValueError("Invalid attack damage - attack damage is negative.")
        elif attack_stat == 0:
            raise ValueError("Invalid attack damage - attack damage is zero.")
        else:
            self.attack_damage = attack_stat

    def get_defence(self) -> int:
        """
        Gets defence stat of Pokemon.

        Args:
          -

        Preconditions:
          -

        Returns:
          defence : int
            defence stat of Pokemon.

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        return self.defence

    def set_defence(self, defence_stat) -> None:
        """
        Sets defence stat of Pokemon.

        Args:
          defence_stat : int
            new speed of Pokemon.

        Preconditions:
          defence_stat must be valid.
            i.e. defence_stat is not zero, is positive and is of integer type,
              else an ValueError is raised.

        Returns:
          -

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        if type(defence_stat) != int:
            raise ValueError("Invalid defence - defence is not an integer.")
        elif defence_stat < 0:
            raise ValueError("Invalid defence - defence is negative.")
        elif defence_stat == 0:
            raise ValueError("Invalid defence - defence is zero.")
        else:
            self.defence = defence_stat

    def get_pokedex_id(self) -> int:
        """
        Gets Pokedex id of Pokemon.

        Args:
          -

        Preconditions:
          -

        Returns:
          pokedex_id : int
            pokedex_id of the Pokemon, used for ordering.

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        return self.pokedex_id

    def is_fainted(self) -> bool:
        """
        Checks whether the Pokemon has fainted or not.

        Args:
          -

        Preconditions:
          -

        Returns:
          hp == 0 : bool
          is_fainted is True when self.hp is 0 as the Pokemon has no remaining hp to continue.
          is_fainted is False otherwise.


        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        return self.hp == 0

    def lose_hp(self, lost_hp: int) -> int:
        """
        Subtracts hp of Pokemon.????????????????????????????????????

        Args:
          -

        Preconditions:
          checks if Pokemon is currently paralysed, if True, then return halve the speed,
            else return the speed.

        Returns:
          speed : int
            speed of the Pokemon.

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        if (self.get_hp() - lost_hp) < 0:
            hp_lost = self.get_hp()
        else:
            hp_lost = lost_hp

        self.set_hp(self.get_hp() - hp_lost)
        return hp_lost

    def heal(self) -> None:
        """
        Heals Pokemon to full health and clears any status effects inflicted.

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
        self.clear_status()
        self.set_hp(self.get_max_hp())

    def attack(self, defender: PokemonBase) -> Tuple[PokemonBase, PokemonBase, int, int]:
        """
        Heals Pokemon to full health and clears any status effects inflicted.

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

        absolute_damage = 0
        status_effect_dmg = 0

        # gets current status of attaking pokemon
        poke_current_stat = self.get_status_inflicted()

        # if attacker is asleep, terminate attacking process
        if poke_current_stat == "sleep":
            return self, defender, absolute_damage, status_effect_dmg

        # if attacker is confused, there is a 50% chance it will attack itself
        if poke_current_stat == "confuse":
            if RandomGen.random_chance(0.5):
                defender = self

        # calculates max amount of damage attacker can inflict
        calc_dmg = self.effective_attack(defender)

        # calculates max damage defender can take based on defense calculations
        hp_to_lose = defender.defend(calc_dmg)

        # lose_hp returns damage actually taken by the defender (no overflow, defender hp does not go below 0)
        absolute_damage = defender.lose_hp(hp_to_lose)

        # LOSE HP FROM STATUS EFFECTS
        if poke_current_stat == "burn":
            status_effect_dmg = self.lose_hp(1)

        if poke_current_stat == "poison":
            status_effect_dmg = self.lose_hp(3)

        # NEW STATUS INFLICTION
        self.inflict_status(defender)

        # RETURNS ATTACKER AND DEFENDER POKEMON, DAMAGE DEALT TO DEFENDING POKEMON AND STATUS EFFECT DAMAGE TAKEN BY ATTACKER POKEMON
        return self, defender, absolute_damage, status_effect_dmg


    # ABSTRACT METHODS (THAT MUST BE IMPLEMENTED FOR EACH INDIVIDUAL POKEMON)
    @abstractmethod
    def defend(self, effective_damage: int) -> int:
        """
        Calculates the damage taken by the Pokemon after the defence calculation.

        Args:
          effective_damage : int
            a byproduct from effective_attack

        Preconditions:
          -

        Returns:
          -

        Time Complexity:
          Best Case:
            -
          Worst Case:
            -
        """
        pass

    @abstractmethod
    def get_max_hp(self) -> int:
        """
        Gets the max hp of Pokemon.

        Args:
          -

        Preconditions:
          -

        Returns:
          -

        Time Complexity:
          Best Case:
            -
          Worst Case:
            -
        """
        pass

    @abstractmethod
    def level_up(self) -> None:
        """
        Levels up Pokemon.

        Args:
            -

        Preconditions:
            -

        Returns:
            -

        Time Complexity:
          Best Case:
            -
          Worst Case:
            -
        """
        pass

    @abstractmethod
    def should_evolve(self) -> bool:
        """
        Checks if Pokemon fulfills the level criteria to evolve.

        Args:
          -

        Preconditions:
          -

        Returns:
          -

        Time Complexity:
          Best Case:
            -
          Worst Case:
            -
        """
        pass

    @abstractmethod
    def can_evolve(self) -> bool:
        """
        Checks if Pokemon can evolve.

        Args:
          -

        Preconditions:
          -

        Returns:
          -

        Time Complexity:
          Best Case:
            -
          Worst Case:
            -
        """
        pass

    @abstractmethod
    def get_evolved_version(self) -> PokemonBase:
        """
        Gets the evolved version of Pokemon.

        Args:
          -

        Preconditions:
            -

        Returns:
            -

        Time Complexity:
          Best Case:
            -
          Worst Case:
            -
        """
        pass

    @abstractmethod
    def unique_status_effect(self) -> str:
        """
        Gets the evolved version of Pokemon.

        Args:
          -

        Preconditions:
            -

        Returns:
            -

        Time Complexity:
          Best Case:
            -
          Worst Case:
            -
        """
        pass

    def __str__(self) -> str:
        """
        String method that represents Pokemon.

        Args:
          -

        Preconditions:
          -

        Returns:
          level : int
          name : str
          hp: : int
            the string representation contains the current level, and hp of the Pokemon

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        return f"LV. {self.level} {self.name}: {self.hp} HP"

    def damage_multiplier_calc(self, defender: PokemonBase) -> float:
        """
        Calculates damage multiplier. (E.g : multiplier is 2 if self is a water type and defender is a fire type)

        Args:
          defender : PokemonBase

        Preconditions:
          -

        Returns:
          damage_multiplier : float

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        damage_multiplier = 1

        if self.get_poke_type() == "Fire":
            if defender.get_poke_type() == "Fire":
                damage_multiplier = 1
            if defender.get_poke_type() == "Grass":
                damage_multiplier = 2
            if defender.get_poke_type() == "Water":
                damage_multiplier = 0.5
            if defender.get_poke_type() == "Ghost":
                damage_multiplier = 1
            if defender.get_poke_type() == "Normal":
                damage_multiplier = 1

        elif self.get_poke_type() == "Grass":
            if defender.get_poke_type() == "Fire":
                damage_multiplier = 0.5
            if defender.get_poke_type() == "Grass":
                damage_multiplier = 1
            if defender.get_poke_type() == "Water":
                damage_multiplier = 2
            if defender.get_poke_type() == "Ghost":
                damage_multiplier = 1
            if defender.get_poke_type() == "Normal":
                damage_multiplier = 1

        elif self.get_poke_type() == "Water":
            if defender.get_poke_type() == "Fire":
                damage_multiplier = 2
            if defender.get_poke_type() == "Grass":
                damage_multiplier = 0.5
            if defender.get_poke_type() == "Water":
                damage_multiplier = 1
            if defender.get_poke_type() == "Ghost":
                damage_multiplier = 1
            if defender.get_poke_type() == "Normal":
                damage_multiplier = 1

        elif self.get_poke_type() == "Ghost":
            if defender.get_poke_type() == "Fire":
                damage_multiplier = 1.25
            if defender.get_poke_type() == "Grass":
                damage_multiplier = 1.25
            if defender.get_poke_type() == "Water":
                damage_multiplier = 1.25
            if defender.get_poke_type() == "Ghost":
                damage_multiplier = 2
            if defender.get_poke_type() == "Normal":
                damage_multiplier = 0

        elif self.get_poke_type() == "Normal":
            if defender.get_poke_type() == "Fire":
                damage_multiplier = 1.25
            if defender.get_poke_type() == "Grass":
                damage_multiplier = 1.25
            if defender.get_poke_type() == "Water":
                damage_multiplier = 1.25
            if defender.get_poke_type() == "Ghost":
                damage_multiplier = 0
            if defender.get_poke_type() == "Normal":
                damage_multiplier = 1

        return damage_multiplier

    def effective_attack(self, defender: PokemonBase) -> int:
        """
        Calculates the effective damage and returns it.

        Args:
          defender : PokemonBase

        Preconditions:
          -

        Returns:
            effective_damage : int (effective damage after attack stat, type and status multiplier calculation)

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        attacker_attack_stat = self.get_attack_damage()
        type_multiplier = self.damage_multiplier_calc(defender)
        status_multiplier = 1

        if self.get_status_inflicted() == "burn":
            status_multiplier = 0.5

        effective_damage = int(attacker_attack_stat * type_multiplier * status_multiplier)

        return effective_damage

    def inflict_status(self, defender: PokemonBase) -> None:
        """
        Inflicts the appropriate status effect based on the element type of Pokemon if the condition is met.

        Args:
          defender : PokemonBase

        Preconditions:
          Status only has a 20% of being inflicted.

        Returns:
          -

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        attacker_poke_type = self.get_poke_type()
        if RandomGen.random_chance(0.2):
            if attacker_poke_type == "Fire":
                self.status_burn(defender)
            elif attacker_poke_type == "Grass":
                self.status_poison(defender)
            elif attacker_poke_type == "Water":
                self.status_paralysis(defender)
            elif attacker_poke_type == "Ghost":
                self.status_sleep(defender)
            elif attacker_poke_type == "Normal":
                self.status_confusion(defender)
        return

    def status_burn(self, defender: PokemonBase) -> None:
        """
        Applies the "burn" status to Pokemon.

        Args:
          defender : PokemonBase

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
        return defender.set_status("burn")

    def status_poison(self, defender: PokemonBase) -> None:
        """
        Applies the "poison" status to Pokemon.

        Args:
          defender : PokemonBase

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
        return defender.set_status("poison")

    def status_paralysis(self, defender: PokemonBase) -> None:
        """
        Applies the "paralysis" status to Pokemon.

        Args:
          defender : PokemonBase

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
        return defender.set_status("paralysis")

    def status_sleep(self, defender: PokemonBase) -> None:
        """
        Applies the "sleep" status to Pokemon.

        Args:
          defender : PokemonBase

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
        return defender.set_status("sleep")

    def status_confusion(self, defender: PokemonBase) -> None:
        """
        Applies the "confuse" status to Pokemon.

        Args:
          defender : PokemonBase

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
        return defender.set_status("confuse")