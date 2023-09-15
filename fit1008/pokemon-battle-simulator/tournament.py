from __future__ import annotations

"""
"""
__author__ = "Scaffold by Jackson Goerner, Code by ______________"

from pokemon_base import PokemonBase
from poke_team import PokeTeam
from battle import Battle
from linked_list import LinkedList
from stack_adt import ArrayStack
from queue_adt import CircularQueue

class Tournament:
    """
    A class that represents Tournament

    Attributes:
    battle_mode : int
        battle mode chosen
    match_counter : int
        keeps track of the number of matches in tournament
    teams : PokeTeam
        player's team that is participating in tournament
    winners : ArrayStack(1)
        winners of each match
    losers : ArrayStack(1)
        losers of each match
    tournament_queue : bool
        contains tournament lineup
    self.queue_temp : PokeTeam|str
        temporary storage used with self.advance_tournament and self.linked_list_with_metas 
        used when checking if tournament queue serves a "+" or a PokeTeam instance
    """
    
    def __init__(self, battle: Battle|None=None) -> None:
        """
        Constructs all necessary attributes for a Tournament

        Args:
            battle : Battle
                battle instance, if no battle passed = None

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

        if battle == None:
            self.battle = Battle()
        else:
            self.battle = battle

        self.battle_mode = None
        self.match_counter = 0

        self.teams = LinkedList()
        self.winners = ArrayStack(1) # placeholder stack
        self.losers = ArrayStack(1) # placeholder stack
        
        self.tournament_queue = CircularQueue(1) # placeholder queue
        

    def set_battle_mode(self, battle_mode: int) -> None:
        """
        Sets battle mode for randomly generated tournament teams.

        Args:
          battle_mode : int
            battle mode chosen

        Preconditions:
          battle mode must be valid.
            i.e. battle mode must belong to either 0, 1 or 2,
              else an ValueError is raised.

        Returns:
            -

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        if battle_mode not in [0,1,2]:
            raise ValueError("Invalid battle mode.")

        self.battle_mode = battle_mode


    def is_valid_tournament(self, tournament_str: str) -> bool:
        """
        Checks whether a given string represents a valid tournament.

        Args:
          tournament_str : str
            string representing a tournament, written in postfix notation


        Preconditions:
            -

        Returns:
            bool: indicates whether a tournament is valid or not

        Time Complexity:
          Best Case:
            O(N) - where N is the number of elements in tournament_str.split()
          Worst Case:
            O(N) - where N is the number of elements in tournament_str.split()
        """
        split_postfix = tournament_str.split()

        prev_elem = None
        team_count = 0
        operator_count = 0

        for elem in split_postfix:

            if elem != "+":

                team_count += 1

                # if there is more than two teams in a match, return false
                if team_count > 2:
                    return False

            elif elem == "+":

                operator_count += 1

                # if there is not exactly two teams in a match, return false
                # if there are no teams at all thats okay
                if team_count != 2 and team_count != 0:
                    return False

                team_count = 0

                if prev_elem == elem:
                    operator_count -= 2

                    # if the matchups as defined by the + operator are not valid, return false
                    if operator_count < 0:
                        return False            

            prev_elem = elem

        
        if operator_count != 1:
            return False

        return True


    def is_balanced_tournament(self, tournament_str: str) -> bool:
        # 1054 only
        pass

    def start_tournament(self, tournament_str: str) -> None:
        """
        Sets up a tournament based on a provided string.

        Args:
          tournament_str : str
            string representing a tournament, written in postfix notation

        Preconditions:
          tournament_str must be valid.
          battle must not be None
            i.e. tournament_str must be valid according to the is_valid_tournament function (must return True),
              else an ValueError is raised.
            i.e. battle must be valid according to setting a battle_mode,
              else an ValueError is raised.   

        Returns:
            bool: indicates whether a tournament is valid or not

        Time Complexity:
          Best Case:
            O(N) - where N is the number of elements in tournament_str.split()
          Worst Case:
            O(N) - where N is the number of elements in tournament_str.split()
        """
        if not self.is_valid_tournament(tournament_str):
            raise ValueError("Invalid tournament.")
        if self.battle == None:
            raise ValueError("No battle mode set.")

        split_postfix = tournament_str.split()
        operator_count = 0

        self.tournament_queue = CircularQueue(len(split_postfix))

        for counter in range(len(split_postfix)):
            
            team = split_postfix[counter]

            if team == "+":
                operator_count += 1
                self.tournament_queue.append("+")
                continue
            
            random_team = PokeTeam.random_team(team, self.battle_mode)

            self.teams.insert(0, random_team)
            self.tournament_queue.append(random_team)

        self.winners = ArrayStack(operator_count)
        self.losers = ArrayStack(operator_count)


    def advance_tournament(self) -> tuple[PokeTeam, PokeTeam, int] | None:
        """
        Advances the tournament by playing a match.

        Args:
          -

        Preconditions:
            -

        Returns:
            tuple[PokeTeam, PokeTeam, int]
                tuple containing both teams that played a match and the result of said match
            None
                if end of tournament has been reached.

        Time Complexity:
          Best Case:
            O(B+P) - where B is complexity of a battle and P is number of pokemon in a team,
                        to get the result of the battle between the two teams, the battle function is passed 
          Worst Case:
            O(B+P) - where B is complexity of a battle and P is number of pokemon in a team.
                         to get the result of the battle between the two teams, the battle function is passed 
        """
        team_1: PokeTeam
        team_2: PokeTeam
        
        try:

            self.queue_temp = self.tournament_queue.serve()

            if self.queue_temp == "+":
                team_2 = self.winners.pop()
                team_1 = self.winners.pop()

            else:
                team_1 = self.queue_temp
                team_2 = self.tournament_queue.serve()
                self.tournament_queue.serve()


        except Exception:
            return None

        res = self.battle.battle(team_1, team_2)

        team_1.regenerate_team()
        team_2.regenerate_team()

        # if team 2 wins, team 2 is pushed to winner stack and team 1 is pushed to loser stack
        # else team 2 is pushed to loser stack and team 1 is pushed to winner stack
        # we are allowed to handle draws however, so a draw means team 1 wins by default
        if res == 2:
            self.losers.push(team_1)
            self.winners.push(team_2)
        else:
            self.losers.push(team_2)
            self.winners.push(team_1)

        self.match_counter += 1

        return team_1, team_2, res

    def linked_list_of_games(self) -> LinkedList[tuple[PokeTeam, PokeTeam]]:
        """
        Linked list of all the tournament matches 

        Args:
          -

        Preconditions:
          -

        Returns:
            LinkedList[tuple[PokeTeam, PokeTeam]]
                linkedlist containg a tuple containing both teams that played a match and the result of said match

        Time Complexity:
          Best Case:
            O(n)
          Worst Case:
            O(n)
        """
        l = LinkedList()
        while True:
            res = self.advance_tournament()
            if res is None:
                break
            l.insert(0, (res[0], res[1]))
        return l


    def linked_list_with_metas(self) -> LinkedList[tuple[PokeTeam, PokeTeam, list[str]]]:
        """
        Get a linked list

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

        l = LinkedList()
        poke_types = PokemonBase.POKE_TYPES

        while True:

            res = self.advance_tournament()
            if res is None:
                break

            loser_types = list()

            team1 = res[0]
            team2 = res[1]

            if self.queue_temp == "+":

                team1_types = team1.get_team_poke_types()
                team2_types = team1.get_team_poke_types()

                loser1 = self.losers.pop()
                loser2 = self.losers.pop()

                loser1_types = loser1.get_team_poke_types()
                loser2_types = loser2.get_team_poke_types()

                for type in poke_types:

                    if type in team1_types or type in team2_types:
                        continue

                    if type in loser1_types or type in loser2_types:
                        loser_types.append(type.upper())

                self.losers.push(loser2)
                self.losers.push(loser1)
        
            l.insert(0, (team1, team2, loser_types))

        return l
    
    def flip_tournament(self, tournament_list: LinkedList[tuple[PokeTeam, PokeTeam]], team1: PokeTeam, team2: PokeTeam) -> None:
        # 1054
        pass


