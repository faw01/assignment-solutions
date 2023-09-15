from __future__ import annotations
from queue_adt import CircularQueue
from poke_team import PokeTeam
from battle import Battle
from random_gen import RandomGen
from stack_adt import ArrayStack

__author__ = "Code by Nisha Kannapper and Mandhiren Singh"


class BattleTower:
    """
    A class that represents a BattleTower.

    Attributes:
        player_team : PokeTeam
            player's team that is challenging tower
        tower_teams : PokeTeam
            teams in the battle tower that will fight against player_team
        defeat : bool
             player_team loses
        victory : bool
             player_team wins
    """

    def __init__(self, battle: Battle | None = None) -> None:
        """
        Constructs all necessary attributes for a BattleTower

        Args:
          battle : Battle

        Preconditions:
          checks whether the battle is an instance of Battle

        Returns:
          -

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        # Pre-condition check
        if not isinstance(battle, Battle) and battle is not None:
            raise ValueError()



        # Initialise player_team (your team) and tower_teams (randomly generated PokeTeams)
        self.player_team = None
        self.tower_teams = None
        self.defeat = False
        self.victory = False

        if battle is None:
            self.battle = Battle()
        else:
            self.battle = battle
    
    def set_my_team(self, team: PokeTeam) -> None:
        """
        Sets the team that will be fighting through the tower.

        Args:
          team : PokeTeam
            team that will challenge the tower. 

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
        if not isinstance(team, PokeTeam):
            raise ValueError()
        else:
            self.player_team = team
    
    def generate_teams(self, n: int) -> None:
        """
        Randomly generates teams for the battle tower according to n.

        Args:
          n : int
            number of teams generated for the battle tower.

        Preconditions:
          n must be valid.
            i.e. n is non-zero, positive and be of integer type.
              else an exception is raised.

        Returns:
          -

        Time Complexity:
          Best Case:
            O(n) 
          Worst Case:
            O(n) 
        """
        if not isinstance(n, int):
            raise ValueError("Invalid n - n is not an integer.")

        if n <= 0:
            raise ValueError("Invalid n - n must be positive.")


        # Initialise team_queue as a CitcularQueue ADT
        team_queue = CircularQueue(n)

        # For each team, generate the team using PokeTeam.random_team() and number of lives.
        for count in range(n):

            # Battle mode chosen (constant across all teams)
            battle_mode = RandomGen.randint(0, 1)

            # Generate team name
            team_name = f"Trainer {count + 1}'s team"

            # Generate randomly generated team using PokeTeam.random_team()
            randomly_generated_team = PokeTeam.random_team(team_name, battle_mode)

            # Generate number of lives and set lives
            num_of_lives = RandomGen.randint(2, 10)
            randomly_generated_team.set_lives_initial(num_of_lives)

            team_queue.append(randomly_generated_team)

        self.tower_teams = team_queue
    
    def __iter__(self) -> BattleTowerIterator:
        """
        Iterator for Battle Tower.

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
        bt_iter = BattleTowerIterator(self)
        return bt_iter

class BattleTowerIterator:
    """
    A class that represents BattleTowerIterator

    Attributes:
    battle_tower : BattleTower
        the battle tower that holds battles between tower_teams and player_team
    tower_teams : PokeTeam
        teams in the battle tower that will fight against player_team
    player_team : PokeTeam
        player's team that is challenging tower
    battle : Battle
        the battle that takes place between tower_teams and player_team
    defeat : bool
        player_team loses
    victory : bool
        player_team wins
    """

    def __init__(self, battle_tower: BattleTower) -> None:
        """
        Constructs all necessary attributes for a PokemonBase

        Args:
          battle_tower : BattleTower
            
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
        self.battle_tower = battle_tower
        self.tower_teams = self.battle_tower.tower_teams  # CircularQueue of PokeTeams
        self.player_team = self.battle_tower.player_team  # PokeTeam
        self.battle = self.battle_tower.battle  # Battle instance
        self.defeat = self.battle_tower.defeat
        self.victory = self.battle_tower.victory

    def __iter__(self):
        """
        Battle Tower Iterator

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
        return self

    def __next__(self) -> tuple[int, PokeTeam, PokeTeam, int]:
        """
        Moves to the next battle in BattleTower sequence.

        Args:
          -

        Preconditions:
          -

        Returns:
          a tuple containing result, player_team, current_tower_team, tower_lives

        Time Complexity:
          Best Case:
            O(b) - according to the time complexity of the battle function
          Worst Case:
            O(b) - according to the time complexity of the battle function
        """
        # StopIteration if win or defeat (nothing left to iterate over)
        if self.defeat or self.victory:
            raise StopIteration()

        # Get player_team and current_tower_team (if queue is not empty) after battle, else raise StopIteration
        player_team = self.player_team

        # player_team.regenerate_team()

        if not self.tower_teams.is_empty():
            current_tower_team = self.tower_teams.serve()
        else:
            raise StopIteration()

        # result = self.tester_results.pop()
        result = self.battle.battle(player_team, current_tower_team) #TODO uncomment when battle.py is complete

        # Regenerate teams
        player_team.regenerate_team()
        current_tower_team.regenerate_team()

        # If no tower_teams are left, player is victorious.
        if (result == 0) or (result == 1) and (len(self.tower_teams) == 0):
            self.victory = True

        elif (result == 2):
            # tower_lives = self.tower_teams.serve().get_lives()
            self.defeat = True

        # Get player team and tower team after the battle, and the num of lives of tower team
        # If result == 0 or 1, player_team wins, tower_team loses and tower_team.remove_life()
        # If result == 2, game ends

        if result == 0 or result == 1:

            # Remove 1 life from current tower_team
            current_tower_team.remove_life()

            # Get num of lives of current tower team
            tower_lives = current_tower_team.get_lives()

            # Move the losing tower team to the back of queue if lives != 0
            if current_tower_team.get_lives() != 0:
                self.tower_teams.append(current_tower_team)

        elif result == 2:
            tower_lives = current_tower_team.get_lives()

        return result, player_team, current_tower_team, tower_lives

    def avoid_duplicates(self) -> None:
        """
        Avoids duplicates by deleting teams with multiple Pokemon which has the same type.

        Args:
          -

        Preconditions:
          -

        Returns:
          -

        Time Complexity:
          Best Case:
            O(N * P) - where N is the number of trainers remaining in the BattleTower and P is the max limit of the number of Pokemon in a PokeTeam,
                        First, the function loops through each and every trainer in the BattleTower (outer loop),
                            Second, the function loops through each Pokemon in PokeTeam and determines if there is a duplicate (inner loop),
          Worst Case:
            O(N * P) - where N is the number of trainers remaining in the BattleTower and P is the max limit of the number of Pokemon in a PokeTeam,
                        First, the function loops through each and every trainer in the BattleTower (outer loop),
                            Second, the function loops through each Pokemon in PokeTeam and determines if there is a duplicate (inner loop),
        """
        no_duplicates_queue = CircularQueue(len(self.tower_teams))

        # Iterate through each and every team in self.tower_teams
        for i in range(len(self.tower_teams)):

            # For each team, iterate through their team_numbers and check if every element in team_numbers is either a 0 or 1
            # If it is, OK - keep team
            # Else - remove team because there are duplicates

            for j in range(0, len((self.tower_teams[i].get_team_numbers()))):
                num_of_specific_poke = self.tower_teams[i].get_team_numbers()[j]

                # If the number of pokemon
                if num_of_specific_poke != 0 and num_of_specific_poke != 1:
                    if len(self.tower_teams) != 0:
                        self.tower_teams.serve()
                        break
                else:
                    if len(self.tower_teams) != 0 and num_of_specific_poke == 0 or num_of_specific_poke == 1:
                        if j == len(self.tower_teams[i].get_team_numbers()) - 1:
                            no_duplicates_queue.append(self.tower_teams.serve())
                            continue

            # Reset self.battle_tower.tower_teams to the new no_duplicates_queue
            self.battle_tower.tower_teams = no_duplicates_queue

    def sort_by_lives(self):
        # 1054
        pass
