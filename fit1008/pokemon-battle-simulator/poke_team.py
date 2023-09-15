from __future__ import annotations
from enum import Enum, auto
from pokemon_base import PokemonBase
from pokemon import *
from queue_adt import CircularQueue
from stack_adt import ArrayStack
from array_sorted_list import ArraySortedList
from sorted_list import ListItem
from random_gen import RandomGen

"""
This file header will provide a short description of poke_team.py.
poke_team.py holds the PokeTeam class, which represents a team of Pokemon. It consists of a random team generator as
well as returning/retrieving functionality based on a chosen battle mode. All battle modes have their own unique
mechanics for retrieving/returning Pokemon. Each battle mode also has their own special operation as defined in the
specs. Finally, each PokeTeam also has an optional AI which has a pre-determined set of AI logic.

Documentation by : Fawwad and Mandhiren Singh
"""
__author__ = "Scaffold by Jackson Goerner, Code by Mandhiren Singh"


class Action(Enum):
    """
    An enum that represents other possible team actions.
    """
    ATTACK = auto()
    SWAP = auto()
    HEAL = auto()
    SPECIAL = auto()


class Criterion(Enum):
    """
    An enum that represents possible criterions.
    """
    SPD = auto()
    HP = auto()
    LV = auto()
    DEF = auto()


class PokeTeam:
    """
    A class that represents a PokeTeam.

    Attributes:
        team_name : str
            name of team (trainer)
        team_numbers : list[int]
            amount of base Pokemon in team
        battle_mode : int
             battle mode chosen
        ai_type : PokeTeam.AI
             the type of AI used
        criterion : Criterion
            only used for battle mode 2 - is based on a stat criteria
    """
    # Class-Level Variable(s)
    POKE_TEAM_LIMIT = 6
    BATTLE_MODES = [0, 1, 2]

    class AI(Enum):
        """
        An enum that represents the AI of a class.
        """
        ALWAYS_ATTACK = auto()
        SWAP_ON_SUPER_EFFECTIVE = auto()
        RANDOM = auto()
        USER_INPUT = auto()


    def __init__(self, team_name: str, team_numbers: list[int], battle_mode: int, ai_type: PokeTeam.AI, criterion=None,
                 criterion_value=None) -> None:
        """
        Constructs all necessary attributes for a PokeTeam object.

        Args:
            team_name : str
                name of team (trainer)
            team_numbers : list[int]
                amount of base Pokemon in team
            battle_mode : int
                 battle mode chosen
            ai_type : PokeTeam.AI
                 the type of AI used
            criterion : Criterion
                only used for battle mode 2 - is based on a stat criteria

        Preconditions:
          checks if team_name is a string
          checks if team numbers is more than 6
          checks if battle mode is valid or not
          checks if ai type is valid or not
          checks if criterion is valid or not

        Returns:
          -

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """

        # User-facing : Pre-condition checks

        if not isinstance(team_name, str):
            raise TypeError("Team name must be a string!")

        if sum(team_numbers) > PokeTeam.POKE_TEAM_LIMIT:
            raise ValueError("Sum of Pokemon cannot exceed 6!")

        if battle_mode not in PokeTeam.BATTLE_MODES:
            raise ValueError("Valid battle modes are 0, 1 and 2 only!")

        if ai_type not in list(PokeTeam.AI):
            raise ValueError("Invalid AI type!")

        if criterion is not None and criterion not in list(Criterion):
            raise ValueError("Invalid Criterion provided!")



        # Instance variables initialisation
        self.team_name = team_name
        self.team_numbers = team_numbers
        self.battle_mode = battle_mode
        self.ai_type = ai_type
        self.criterion = criterion
        self.criterion_value = criterion_value  # FIT1054 - not needed

        # Initialises poke_team_adt to None
        self.poke_team_adt = None

        # Indicates the number of times a team has healed, if 3 then lose in battle.py later on.
        self.heal_count = 0

        # 1 indicates descending order, 0 indicates ascending order
        self.sorting_order = 1

        # Indicates the number of lives left in a team (initialised to None), for use in tower.py
        self.lives = None

        # Choose ADT based on battle mode provided - ArrayStack, CircularQueue or ArraySortedList
        self.choose_adt()

        # Assign team based on the chosen battle mode
        self.assign_team(self.team_numbers)


    # HELPER FUNCTION(S)
    def get_remainder_pokemon(self) -> int:
        """
        Gets number of alive Pokemon.

        Args:
          -

        Preconditions:
          -

        Returns:
          len of PokeTeam : int

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        return len(self.poke_team_adt)


    def choose_adt(self):
        """
        Initialises the ADT based on the battle mode.

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
        # Sets ADT corresponding to the chosen battle mode
        if self.get_battle_mode() == 0:
            self.poke_team_adt = ArrayStack(sum(self.team_numbers))
        elif self.get_battle_mode() == 1:
            self.poke_team_adt = CircularQueue(sum(self.team_numbers))
        elif self.get_battle_mode() == 2:
            self.poke_team_adt = ArraySortedList(sum(self.team_numbers))
        else:
            raise Exception("The battle mode entered is not 0, 1 or 2.")

    def increment_heal_count(self):
        """
        Increments heal_count of PokeTeam by 1

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
        self.set_heal_count(self.get_heal_count() + 1)

    def reset_heal_count(self):
        """
        Resets heal_count for a PokeTeam object to 0

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
        self.set_heal_count(0)


    def set_lives_initial(self, lives: int) -> None:
        """
        This function takes in an integer and sets the lives of the team to that integer.

        Args:
            lives : int
                number of lives to be set for the PokeTeam

        Preconditions:
          check if number of lives more than 0

        Returns:
          -

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        if lives > 0:
            self.lives = lives
        else:
            raise ValueError()

    def remove_life(self) -> None:
        """
        Removes 1 life from the PokeTeam.

        Args:
          -

        Preconditions:
          checks if lives > 0

        Returns:
          -

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        try:
            assert self.lives > 0
            self.lives -= 1

        except AssertionError:
            raise Exception("Team has no more lives.")

    def get_lives(self) -> int:
        """
        Returns the number of lives of the PokeTeam.

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
        return self.lives


    def assign_team(self, poke_team_numbers: list[int]) -> None:
        """
        Assigns the team into appropriate ADTS according to the battle mode chosen.

        Args:
            poke_team_numbers (list[int]): list of integers that correspond to number of Charmander,
                                         Bulbasaur, Squirtle, Gastly, Eevee respectively.

        Preconditions:
        checks if number of Pokemon in PokeTeam is at its limit, which is 6 Pokemon,
            if there are more than 6 Pokemon, raise an exception
                else continue.

        Returns:
          -

        Time Complexity:
          Best Case:
            O(N) when the add method immediately adds the element and the binary search in _index_to_add() has not started.
          Worst Case:
            O(N log N) because the ArraySortedList ADT's .add() method uses _index_to_add(), which uses a binary search
            algorithm to add new items to the ArraySorted List. That is where the log N comes from. N just means that
            we need to loop through the entire length of the poke_team_numbers.
        """

        assert sum(poke_team_numbers) <= PokeTeam.POKE_TEAM_LIMIT, "Team limit is 6."

        # Stack
        if self.get_battle_mode() == 0:

            # Push Eevee first because the first Pokemon to go into the ArrayStack is the last one out. Eevee should
            # be last according to the Pokedex.

            # Add Eevee(s)
            for _ in range(poke_team_numbers[4]):
                self.poke_team_adt.push(Eevee())

            # Add Gastly(s)
            for _ in range(poke_team_numbers[3]):
                self.poke_team_adt.push(Gastly())

            # Add Squirtle(s)
            for _ in range(poke_team_numbers[2]):
                self.poke_team_adt.push(Squirtle())

            # Add Bulbasaur(s)
            for _ in range(poke_team_numbers[1]):
                self.poke_team_adt.push(Bulbasaur())

            # Add Charmander(s)
            for _ in range(poke_team_numbers[0]):
                self.poke_team_adt.push(Charmander())

        # Queue
        elif self.get_battle_mode() == 1:

            # Append Charmander first to the CircularQueue because it is the first Pokemon in the Pokedex ordering.
            # Appending Charmander first will ensure that it is always in front of the CircularQueue.

            # Add Charmander(s)
            for _ in range(poke_team_numbers[0]):
                self.poke_team_adt.append(Charmander())

            # Add Bulbasaur(s)
            for _ in range(poke_team_numbers[1]):
                self.poke_team_adt.append(Bulbasaur())

            # Add Squirtle(s)
            for _ in range(poke_team_numbers[2]):
                self.poke_team_adt.append(Squirtle())

            # Add Gastly(s)
            for _ in range(poke_team_numbers[3]):
                self.poke_team_adt.append(Gastly())

            # Add Eevee(s)
            for _ in range(poke_team_numbers[4]):
                self.poke_team_adt.append(Eevee())


        # ArraySortedList
        elif self.get_battle_mode() == 2:

            # For the following if-elif-else block, the Pokemon are added based on its specific criterion in descending
            # order. Thus, for the ket, I multiply its stat (criterion) with -1 so that it gets sorted in descending
            # order in the list.

            if self.criterion == Criterion.SPD:

                # Add Eevee(s)
                for _ in range(poke_team_numbers[4]):
                    self.poke_team_adt.add(ListItem(Eevee(), -Eevee().get_speed()))

                # Add Gastly(s)
                for _ in range(poke_team_numbers[3]):
                    self.poke_team_adt.add(ListItem(Gastly(), -Gastly().get_speed()))

                # Add Squirtle(s)
                for _ in range(poke_team_numbers[2]):
                    self.poke_team_adt.add(ListItem(Squirtle(), -Squirtle().get_speed()))

                # Add Bulbasaur(s)
                for _ in range(poke_team_numbers[1]):
                    self.poke_team_adt.add(ListItem(Bulbasaur(), -Bulbasaur().get_speed()))

                # Add Charmander(s)
                for _ in range(poke_team_numbers[0]):
                    self.poke_team_adt.add(ListItem(Charmander(), -Charmander().get_speed()))

            elif self.criterion == Criterion.HP:

                # Add Eevee(s)
                for _ in range(poke_team_numbers[4]):
                    self.poke_team_adt.add(ListItem(Eevee(), -Eevee().get_hp()))

                # Add Gastly(s)
                for _ in range(poke_team_numbers[3]):
                    self.poke_team_adt.add(ListItem(Gastly(), -Gastly().get_hp()))

                # Add Squirtle(s)
                for _ in range(poke_team_numbers[2]):
                    self.poke_team_adt.add(ListItem(Squirtle(), -Squirtle().get_hp()))

                # Add Bulbasaur(s)
                for _ in range(poke_team_numbers[1]):
                    self.poke_team_adt.add(ListItem(Bulbasaur(), -Bulbasaur().get_hp()))

                # Add Charmander(s)
                for _ in range(poke_team_numbers[0]):
                    self.poke_team_adt.add(ListItem(Charmander(), -Charmander().get_hp()))

            elif self.criterion == Criterion.LV:

                # Add Eevee(s)
                for _ in range(poke_team_numbers[4]):
                    self.poke_team_adt.add(ListItem(Eevee(), -Eevee().get_level()))

                # Add Gastly(s)
                for _ in range(poke_team_numbers[3]):
                    self.poke_team_adt.add(ListItem(Gastly(), -Gastly().get_level()))

                # Add Squirtle(s)
                for _ in range(poke_team_numbers[2]):
                    self.poke_team_adt.add(ListItem(Squirtle(), -Squirtle().get_level()))

                # Add Bulbasaur(s)
                for _ in range(poke_team_numbers[1]):
                    self.poke_team_adt.add(ListItem(Bulbasaur(), -Bulbasaur().get_level()))

                # Add Charmander(s)
                for _ in range(poke_team_numbers[0]):
                    self.poke_team_adt.add(ListItem(Charmander(), -Charmander().get_level()))


            elif self.criterion == Criterion.DEF:

                # Add Eevee(s)
                for _ in range(poke_team_numbers[4]):
                    self.poke_team_adt.add(ListItem(Eevee(), -Eevee().get_defence()))

                # Add Gastly(s)
                for _ in range(poke_team_numbers[3]):
                    self.poke_team_adt.add(ListItem(Gastly(), -Gastly().get_defence()))

                # Add Squirtle(s)
                for _ in range(poke_team_numbers[2]):
                    self.poke_team_adt.add(ListItem(Squirtle(), -Squirtle().get_defence()))

                # Add Bulbasaur(s)
                for _ in range(poke_team_numbers[1]):
                    self.poke_team_adt.add(ListItem(Bulbasaur(), -Bulbasaur().get_defence()))

                # Add Charmander(s)
                for _ in range(poke_team_numbers[0]):
                    self.poke_team_adt.add(ListItem(Charmander(), -Charmander().get_defence()))

        return None


    # GETTERS AND SETTERS FOR INSTANCE VARS
    def set_battle_mode(self, battle_mode: int):
        """
        Sets battle mode.

        Args:
        battle_mode : int
            number of battle mode

        Preconditions:
          - check if battle_mode is valid or not

        Returns:
          -

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        if battle_mode not in PokeTeam.BATTLE_MODES:
            raise ValueError("Valid battle modes are 0, 1 and 2 only!")
        else:
            self.battle_mode = battle_mode

    def get_battle_mode(self) -> int:
        """
        Gets battle mode.

        Args:
         -

        Preconditions:
          -

        Returns:
          battle_mode : int

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        return self.battle_mode

    def set_team_name(self, team_name: str):
        """
        Sets team name.

        Args:
        team_name : str
            name of new team_name

        Preconditions:
          checks if name is a string or not

        Returns:
          -

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        if not isinstance(team_name, str):
            raise TypeError("Team name must be a string!")
        else:
            self.team_name = team_name

    def get_team_name(self) -> str:
        """
        Gets team name (trainer name).

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
        return self.team_name

    def set_team_numbers(self, team_numbers: list[int]):
        """
        Sets the team numbers of PokeTeam.

        Args:
          team_numbers (list[int]): list of integers representing the number of Charmander, Bulbasaur, Squirtle, Gastly,
                                    Eevee respectively.

        Preconditions:
          - check if team_numbers is more than the limit or not

        Returns:
          -

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        if sum(team_numbers) > PokeTeam.POKE_TEAM_LIMIT:
            raise ValueError("Sum of Pokemon cannot exceed 6!")
        else:
            self.team_numbers = team_numbers

    def get_team_numbers(self) -> list[int]:
        """
        Gets the team numbers of PokeTeam.

        Args:
        team_name : str
            name of new team_name

        Preconditions:
          -

        Returns:
          list[int] : list of integers representing the number of Charmander, Bulbasaur, Squirtle, Gastly,
                      Eevee respectively.

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        return self.team_numbers

    def set_ai_type(self, ai_type: PokeTeam.AI):
        """
        Sets the AI type for PokeTeam.

        Args:
          ai_type (PokeTeam.AI) : Enum representing AI type.

        Preconditions:
          - check if ai_type is valid or not

        Returns:
          -

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        if ai_type not in list(PokeTeam.AI):
            raise ValueError("Invalid AI type!")
        else:
            self.ai_type = ai_type

    def get_ai_type(self) -> PokeTeam.AI:
        """
        Gets the AI type for PokeTeam.

        Args:
          -

        Preconditions:
          - # PUT ASSERTION HERE

        Returns:
          PokeTeam.AI : Enum representing AI type.

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        return self.ai_type

    def set_criterion(self, criterion: Criterion):
        """
        Sets the criterion for PokeTeam.

        Args:
          criterion : Criterion
            new Criterion for PokeTeam.

        Preconditions:
          - # PUT ASSERTION HERE

        Returns:
          -

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        if criterion is not None and criterion not in list(Criterion):
            raise ValueError("Invalid Criterion provided!")
        else:
            self.criterion = criterion

    def get_criterion(self) -> Criterion:
        """
        Gets the criterion for PokeTeam.

        Args:
          -

        Preconditions:
          -

        Returns:
          Criterion : Criterion of PokeTeam

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        return self.criterion

    def set_heal_count(self, heal_count: int):
        """
        Sets heal count of PokeTeam.

        Args:
         heal_count : int
            new number of heal counts

        Preconditions:
          - check if heal count is non-negative

        Returns:
          -

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        if heal_count < 0:
            raise ValueError()
        else:
            self.heal_count = heal_count

    def get_heal_count(self) -> int:
        """
        Gets heal count of PokeTeam.

        Args:
         -

        Preconditions:
         -

        Returns:
          heal_count : int
            current heal_count of PokeTeam.

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        return self.heal_count


    @classmethod
    def random_team(cls, team_name: str, battle_mode: int, team_size=None, ai_mode=None, **kwargs):
        """
        This function generates a random team based on the rules provided in the assignment spec.

        Args:
            team_name : str
                string of the PokeTeam's name
            battle_mode : int
                battle mode integer
            team_size : int
                optional team_size
            ai_mode : PokeTeam.AI
                AI mode for the PokeTeam

        Preconditions:
          -

        Returns:
          -

        Time Complexity:
          Best Case:
            O(1) if the binary search in _index_to_add() in the add() method in the ArraySortedList ADT runs through
            the "else" block where the index to add is directly in the middle of the ArrayR.
          Worst Case:
            O(log n) if the binary search keeps going until the whole ArrayR is exhausted.
        """

        # If team_size = None, generate team_size = between half of pokemon limit (3) and the pokemon limit (6)
        if team_size is None:
            # gives us 6 with seed 123456789
            team_size = int(RandomGen.randint(PokeTeam.POKE_TEAM_LIMIT / 2, PokeTeam.POKE_TEAM_LIMIT))

        # Create sorted list, add the values 0 and team_size, and generate 4 random numbers from 0 to team_size and
        # insert them into the sorted list.
        rng_sorted_list = ArraySortedList(PokeTeam.POKE_TEAM_LIMIT)

        # Add values 0 and team_size to sorted list, with key being their int value.
        rng_sorted_list.add(ListItem(0, 0))
        rng_sorted_list.add(ListItem(team_size, team_size))

        # Generate 4 random numbers from 0 to team_size add insert them into the sorted list.
        for _ in range(4):
            random_number = int(RandomGen.randint(0, team_size))
            rng_sorted_list.add(ListItem(random_number, random_number))

        # # For each adjacent value in the list, their difference specifies how many C, B, S, G, E should be added.
        charm_num = rng_sorted_list[1].value - rng_sorted_list[0].value
        bulb_num = rng_sorted_list[2].value - rng_sorted_list[1].value
        squirt_num = rng_sorted_list[3].value - rng_sorted_list[2].value
        gastly_num = rng_sorted_list[4].value - rng_sorted_list[3].value
        eevee_num = rng_sorted_list[5].value - rng_sorted_list[4].value

        # Create list of team numbers
        team_numbers = [charm_num, bulb_num, squirt_num, gastly_num, eevee_num]

        # If no AI mode is specified, the PokeTeam should pick options from AI Enum at random (for available options),
        # (E.G: heal should be removed from options after 3 heals).
        if ai_mode is None:
            ai_mode = PokeTeam.AI.RANDOM

        if len(kwargs) == 1:
            poke_team = PokeTeam(team_name, team_numbers, battle_mode, ai_mode, criterion=kwargs["criterion"])
        else:
            poke_team = PokeTeam(team_name, team_numbers, battle_mode, ai_mode)

        return poke_team

    def return_pokemon(self, poke: PokemonBase) -> None:
        """
        Returns Pokemon back to ADT.

        Args:
            poke : PokemonBase
                pokemon to be returned back to PokeTeam

        Preconditions:
          - checks if the hp of poke is 0 or not

        Returns:
          -

        Time Complexity:
          Best Case:
            O(1) when the battle mode is 0 or 1, because the .push() and .append() instructions are in O(1)
          Worst Case:
            O(log n) when the battle mode is 2 and the .add() and _index_to_add() methods need to be called, where
            _index_to_add() is a binary search in O(log n)
        """
        # For reference :
        # team_numbers_order = [Charmander, Bulbasaur, Squirtle, Gastly, Eevee]

        # POKEDEX ORDER :
        # Charmander, Charizard, Bulbasaur, Venusaur, Squirtle,
        # Blastoise, Gastly, Haunter, Gengar, Eevee

        # If Pokemon HP is 0, then don't return it to the team
        if poke.get_hp() <= 0:
            return

        # Clears the status of the returning Pokemon
        poke.clear_status()

        # BATTLE MODE 0 - STACK ADT
        if self.get_battle_mode() == 0:
            # Push Pokemon to top of the stack (front of the team, having everyone shuffle back)
            self.poke_team_adt.push(poke)
        elif self.get_battle_mode() == 1:
            # Returns Pokemon to end of the team (Queue), having everyone stay where they are.
            self.poke_team_adt.append(poke)
        elif self.get_battle_mode() == 2:

            # If self.sorting_order = 1, we are sorting it in descending order
            if self.sorting_order == 1:
                if self.get_criterion() == Criterion.HP:
                    self.poke_team_adt.add(ListItem(poke, -poke.get_hp()))
                elif self.get_criterion() == Criterion.LV:
                    self.poke_team_adt.add(ListItem(poke, -poke.get_level()))
                elif self.get_criterion() == Criterion.SPD:
                    self.poke_team_adt.add(ListItem(poke, -poke.get_speed()))
                elif self.get_criterion() == Criterion.DEF:
                    self.poke_team_adt.add(ListItem(poke, -poke.get_defence()))

            # Ascending order
            else:
                if self.get_criterion() == Criterion.HP:
                    self.poke_team_adt.add(ListItem(poke, poke.get_hp()))
                elif self.get_criterion() == Criterion.LV:
                    self.poke_team_adt.add(ListItem(poke, poke.get_level()))
                elif self.get_criterion() == Criterion.SPD:
                    self.poke_team_adt.add(ListItem(poke, poke.get_speed()))
                elif self.get_criterion() == Criterion.DEF:
                    self.poke_team_adt.add(ListItem(poke, poke.get_defence()))


    def retrieve_pokemon(self) -> PokemonBase | None:
        """
        Retrieves the Pokemon from PokeTeam.

        Args:
          -

        Preconditions:
          - checks if ADT is empty or not

        Returns:
          retrieved_pokemon : PokemonBase
            retrieved Pokemon from PokeTeam

        Time Complexity:
          Best Case:
            O(1) if it is battle mode 0 or 1 because the .pop() and .serve() methods are in O(1)
          Worst Case:
            O(N) if it is battle mode 2 because the .delete_at_index() uses _shuffle_left() which loops
            from the index to the length of ArrayR, so O(N/2) which is just O(N).
        """
        # For reference :
        # team_numbers_order = [Charmander, Bulbasaur, Squirtle, Gastly, Eevee]

        # POKEDEX ORDER :
        # Charmander, Charizard, Bulbasaur, Venusaur, Squirtle,
        # Blastoise, Gastly, Haunter, Gengar, Eevee

        if self.poke_team_adt.is_empty():
            raise Exception()

        # Initialising variable to store retrieved Pokemon for return later on
        retrieved_pokemon = None

        # BATTLE MODE 0 - STACK ADT
        if self.get_battle_mode() == 0:
            # Pop Pokemon from top of stack
            retrieved_pokemon = self.poke_team_adt.pop()
        elif self.get_battle_mode() == 1:
            # Retrieve first Pokemon in the team (at the front of queue)
            retrieved_pokemon = self.poke_team_adt.serve()
        elif self.get_battle_mode() == 2:
            if len(self.poke_team_adt) != 0:
                retrieved_pokemon = self.poke_team_adt[0].value
                self.poke_team_adt.delete_at_index(0)

        return retrieved_pokemon

    def special(self):
        """
        Special

        Args:
          -

        Preconditions:
          -

        Returns:
          -

        Time Complexity:
          Best Case:
            O(1) if it is battle mode 0 or 1 because .append(), .push(), .pop() are all O(1).
          Worst Case:
            O(log n) if it is battle mode 2 because .add() uses a binary search in _index_to_add().
        """
        # For reference :
        # team_numbers_order = [Charmander, Bulbasaur, Squirtle, Gastly, Eevee]

        # POKEDEX ORDER :
        # Charmander, Charizard, Bulbasaur, Venusaur, Squirtle,
        # Blastoise, Gastly, Haunter, Gengar, Eevee

        # BATTLE MODE 0 - SWAP (FIRST and LAST PokeSwap)
        if self.get_battle_mode() == 0:

            # Get first and last Pokemon in the stack, and store them in vars.
            first_poke = self.poke_team_adt[0]
            last_poke = self.poke_team_adt[len(self.poke_team_adt)-1]

            # Commence swap
            self.poke_team_adt[0], self.poke_team_adt[len(self.poke_team_adt)-1] = last_poke, first_poke

        # BATTLE MODE 1 - SWAP FIRST AND SECOND HALVES, REVERSE FIRST HALF, THEN COMBINE SECOND + REVERSED FIRST
        # Note : For odd team numbers like 5, the middle Pokemon (3rd Pokemon) is considered to be in the second half.
        elif self.battle_mode == 1:
            temp_stack = ArrayStack(int(len(self.poke_team_adt) * 0.5))
            for i in range(int(len(self.poke_team_adt) * 0.5)):
                temp_stack.push(self.retrieve_pokemon())
            for i in range(len(temp_stack)):
                self.poke_team_adt.append(temp_stack.pop())

        # BATTLE MODE 2 - REVERSE
        elif self.get_battle_mode() == 2:

            # Change sorting order (-1 indicates opposite sorting order from before)
            self.sorting_order *= -1

            # Initialise reversed array sorted list
            reversed_array = ArraySortedList(len(self.poke_team_adt))

            # To reverse the sorting order, multiply the key for each ListItem by -1 (to sort it in the opposite order)
            # Then, I add the new ListItems with reversed index into
            for i in range(len(self.poke_team_adt)):
                poke_list_item = ListItem(self.poke_team_adt[i].value, self.poke_team_adt[i].key * -1)
                reversed_array.add(poke_list_item)

            # Set our ADT to be the new reversed one.
            self.poke_team_adt = reversed_array


    def regenerate_team(self):
        """
        Regenerates PokeTeam.

        Args:
          -

        Preconditions:
          -

        Returns:
          -

        Time Complexity:
          Best Case:
            O(1) if O(assign_team) is also O(1)
          Worst Case:
            O(log n) if O(assign_team) is O(log n)
        """
        # Resets sorting order of the team
        self.sorting_order = 1

        # Resets heal_count (num of times healed) to 0 for use in tower.py later
        self.set_heal_count(0)

        # Clear team
        self.poke_team_adt.clear()

        # Re-assign team
        self.assign_team(self.team_numbers)


    def __str__(self):
        """
        String method that represents PokeTeam.

        Args:
          -

        Preconditions:
          -

        Returns:
          str
            the string representation contains the current level, and hp of the Pokemon, but for all Pokemon in PokeTeam

        Time Complexity:
          Best Case:
            O(1) because for all battle modes, it will loop through a fixed number of times, that is it will loop
            through the length of self.poke_team_adt. All the lookups are also in O(1).
          Worst Case:
            O(1) because for all battle modes, it will loop through a fixed number of times, that is it will loop
            through the length of self.poke_team_adt. All the lookups are also in O(1).
        """

        # Initialise return string
        poke_team_str = f"{self.get_team_name()} ({self.get_battle_mode()}): ["

        poke_team_adt_lookup = self.poke_team_adt

        # Stack
        if self.get_battle_mode() == 0:
            for i in range(len(poke_team_adt_lookup)-1, -1, -1):
                if i != 0:
                    poke_team_str += str(poke_team_adt_lookup[i]) + ", "
                else:
                    poke_team_str += str(poke_team_adt_lookup[i])

        # Queue
        elif self.battle_mode == 1:
            for i in range(len(self.poke_team_adt)):
                if i == len(self.poke_team_adt) - 1:
                    poke_team_str += str(self.poke_team_adt[self.poke_team_adt.front - self.poke_team_adt.max_cap + i])
                else:
                    poke_team_str += str(self.poke_team_adt[self.poke_team_adt.front - self.poke_team_adt.max_cap + i]) + ", "

        # ArraySortedList
        elif self.get_battle_mode() == 2:
            for i in range(len(poke_team_adt_lookup)):
                if i == len(poke_team_adt_lookup) - 1:
                    poke_team_str += str(poke_team_adt_lookup[i].value)
                else:
                    poke_team_str += str(poke_team_adt_lookup[i].value) + ", "
        else:
            raise Exception("The battle mode entered is not 0, 1 or 2.")

        poke_team_str += "]"

        return poke_team_str

    def is_empty(self):
        """
        Checks if PokeTeam is currently empty.

        Args:
          -

        Preconditions:
          -

        Returns:
         bool
            True if PokeTeam is empty, False otherwise.

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        return self.poke_team_adt.is_empty()

    def choose_battle_option(self, my_pokemon: PokemonBase, their_pokemon: PokemonBase) -> Action:
        """
        Computes the battle option chosen by the AI

        Args:
          my_pokemon : PokemonBase
            current Pokemon
          their_pokemon : PokemonBase
            opposing Pokemon

        Preconditions:
          -

        Returns:
          action_chosen : Action

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        # Initialise return value, action chosen
        action_chosen = None

        # Implement "AI" logic
        # ALWAYS ATTACK - always chooses attack option
        if self.ai_type == PokeTeam.AI.ALWAYS_ATTACK:
            action_chosen = Action.ATTACK

        elif self.ai_type == PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE:
            # Select swap if their_pokemon's attack is super effective (effective damage >= 1.5 * their_pokemon.att_stat)

            if their_pokemon.effective_attack(my_pokemon) >= 1.5 * their_pokemon.get_attack_damage():
                action_chosen = Action.SWAP

            # Will otherwise attack.
            else:
                action_chosen = Action.ATTACK

        elif self.ai_type == PokeTeam.AI.RANDOM:
            actions = list(Action)
            # If healed 3 times, we remove the heal action itself.
            if self.get_heal_count() == 3:
                actions.remove(Action.HEAL)
            action_chosen = actions[RandomGen.randint(0, len(actions) - 1)]

        elif self.ai_type == PokeTeam.AI.USER_INPUT:
            user_chosen_action = str(input("\nA [ATTACK], P [POKEMON], H [HEAL], S [SPECIAL] \n Your Move: "))
            if user_chosen_action == "A":
                action_chosen = Action.ATTACK
            elif user_chosen_action == "P":
                action_chosen = Action.SWAP
            elif user_chosen_action == "H":
                action_chosen = Action.HEAL
            elif user_chosen_action == "S":
                action_chosen = Action.SPECIAL
            else:
                raise Exception("Invalid entry")

        return action_chosen


    def get_team_poke_types(self) -> str:
        """
        Gets elemental poke types of Pokemon in PokeTeam for use later in tournament.py

        Args:
          -

        Preconditions:
          -

        Returns:
            str: a string containing all poke types present in PokeTeam.

        Time Complexity:
          Best Case:
            O(1) because the for loop loops through a fixed number of times, that is the length of
            self.team_numbers.
          Worst Case:
            O(1) because the for loop loops through a fixed number of times, that is the length of
            self.team_numbers.
        """
        string_of_poketypes = ""

        for i in range(len(self.team_numbers)):

            if self.team_numbers[i] != 0:
                if i == 0:
                    string_of_poketypes += "Fire "
                elif i == 1:
                    string_of_poketypes += "Grass "
                elif i == 2:
                    string_of_poketypes += "Water "
                elif i == 3:
                    string_of_poketypes += "Ghost "
                elif i == 4:
                    string_of_poketypes += "Normal "

        return string_of_poketypes


    @classmethod
    def leaderboard_team(cls):
        pass