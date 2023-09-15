from enum import Enum, auto
from pokemon import PokemonBase
from random_gen import RandomGen
from poke_team import Action, PokeTeam, Criterion
from print_screen import print_game_screen

"""
This file header will provide a short description of battle.py.
battle.py implements the battle logic of the Pokemon battles as specified in the assignment specs.
It does this by creating a Battle class that has a .battle(PokeTeam 1, PokeTeam 2) method which pits two PokeTeams against each other
and returns the result (1 if PokeTeam 1 wins, 2 if PokeTeam 2 wins, 0 if draw (we considered it a win)).

Documentation by : Mandhiren Singh
"""
__author__ = "Scaffold by Jackson Goerner, Code by Nisha Kannapper and Mandhiren Singh"


class Battle:
    """
    A class that represents a Battle.

    Attributes:
        verbosity : int
            0 if no verbosity, >= 0 if you want the cool optional verbosity (with extra custom verbosity) :)
    """

    # class with other actions
    # used for implementation of verbosity
    class Other_Action(Enum):
        """
        An enum that represents other possible actions.
        """
        FAINTED = auto()
        INITIAL_DEPLOYED = auto()
        DEPLOYED = auto()
        HEAL_FAILED = auto()
        RETURNED = auto()
        LEVEL_UP = auto()
        EVOLVE = auto()
        CONFUSE = auto()
        HURTITSELF = auto()
        BURN = auto()
        PARALYSIS = auto()
        POISON = auto()
        SLEEP = auto()
        DEAL_DMG = auto()
        LOSE_HP = auto()
    
    # list of actions by battle priority
    ACTION_PRIORITY = [Action.SWAP, Action.SPECIAL, Action.HEAL, Action.ATTACK]

    # used with verbosity
    # verbosity is optional, used for fun and also for manual debugging
    STATUS_OBJECT = {"burn": Other_Action.BURN,
                        "poison": Other_Action.POISON,
                        "paralysis": Other_Action.PARALYSIS,
                        "sleep": Other_Action.SLEEP,
                        "confuse": Other_Action.CONFUSE}
    ACTION_STRINGS = {Action.SWAP: "{poke_name} is swapped out!", 
                        Action.SPECIAL: "{poke_name} used SPECIAL!", 
                        Action.HEAL: "{poke_name} is healed!", 
                        Action.ATTACK: "{poke_name} used ATTACK!",
                        Other_Action.FAINTED: "{poke_name} has fainted!",
                        Other_Action.INITIAL_DEPLOYED: "{team_name} sends out {poke_name}!",
                        Other_Action.DEPLOYED: "Go, {poke_name}!",
                        Other_Action.HEAL_FAILED: "{poke_name}'s heal FAILED!",
                        Other_Action.RETURNED: "{poke_name} is returned to the team!",
                        Other_Action.LEVEL_UP: "{poke_name} levelled up!",
                        Other_Action.EVOLVE: "Oh? {poke_name} is evolving? \n{poke_name} evolved into {evo_name}!",
                        Other_Action.CONFUSE: "{poke_name} is confused!",
                        Other_Action.HURTITSELF: "{poke_name} hurt itself in its confusion!",
                        Other_Action.BURN: "{poke_name} was burnt!",
                        Other_Action.PARALYSIS: "{poke_name} is paralyzed!",
                        Other_Action.POISON: "{poke_name} was poisoned!",
                        Other_Action.SLEEP: "{poke_name} is asleep! It can't attack!",
                        Other_Action.DEAL_DMG: "{poke_name} deals {dmg} points of damage to {other_poke}!",
                        Other_Action.LOSE_HP: "{poke_name} loses {dmg} HP!"
                        }
    
    def __init__(self, verbosity: int = 0) -> None:
        """
        Constructs all necessary attributes for a PokeTeam object.

        Args:
            verbosity : int (optional)
                determines how much text is printed during battle execution (>=0)

        Preconditions:
          verbosity must be valid.
            i.e. verbosity is positive and be of integer type.
              else an ValueError is raised.

        Returns:
          -

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """

        # Initialisation of attributes
        if type(verbosity) != int:
          raise ValueError("Invalid verbosity - verbosity is not an integer.")
        elif verbosity < 0:
          raise ValueError("Invalid verbosity - verbosity cannot be negative.")
        else:
         self.verbose = verbosity
        self.end = False
        self.turns = 0

    def reset(self) -> None:
        """
        Resets the instance variables for a Battle instance.

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
        self.end = False
        self.turns = 0

    def new_turn(self) -> None:
        """
        Increments turn counter.

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
        self.turns += 1

    def get_turn(self) -> int:
        """
        Getter for turn counter.

        Args:
          -

        Preconditions:
          -

        Returns:
          self.turns : int
            number of turns executed during battle process

        Time Complexity:
          Best Case:
            O(1)
          Worst Case:
            O(1)
        """
        return self.turns


    def battle(self, team1: PokeTeam, team2: PokeTeam) -> int:
        """
        Executes a battle with the two teams provided and returns the result of said battle.

        Args:
            team1 : PokeTeam
                PokeTeam 1 involved in battle
            team2 : PokeTeam
                PokeTeam 2 involved in battle

        Preconditions:
          -

        Returns:
            result : int
                indicates result of battle (0 for a draw, 1 for team1's win, 2 for team2's win)

        Time Complexity:
          Best Case:
            O(1) when both the PokeTeams are in battle mode 0, where the ADT implementation only uses constant O(1)
            operations.
          Worst Case:
            O(log n) when both the PokeTeams are in battle mode 2, where the function has to use the ArraySortedList
            ADT's .add() and _index_to_add() methods, that use a binary search to find the index to add.
        """
        # initialises result as 0 (a draw)
        result = 0

        # takes out the initial pokemon for battle
        team1_current = team1.retrieve_pokemon()
        team2_current = team2.retrieve_pokemon()

        # sending out pokemon strings printed (if verbosity is activated)
        if self.verbose:
            print()
            print(f"-- [[ BATTLE START! ]] --")
            print()
            print(team1)
            print(team2)
            print()
            self.print_action_line(team1_current.get_poke_name(),Battle.Other_Action.INITIAL_DEPLOYED, team1.get_team_name())
            self.print_action_line(team2_current.get_poke_name(),Battle.Other_Action.INITIAL_DEPLOYED, team2.get_team_name())

        # battle loop 
        # while self.end is False it keeps going
        while not self.end:

            self.new_turn()
            if self.verbose:
                # print the big game screen
                print_game_screen(team1_current.get_poke_name(), team2_current.get_poke_name(), team1_current.get_hp(), team1_current.get_max_hp(), team2_current.get_hp(), team2_current.get_max_hp(),team1_current.get_level(), team2_current.get_level(), team1_current.get_status_inflicted(), team2_current.get_status_inflicted(), team1.get_remainder_pokemon() + 1 , team2.get_remainder_pokemon() + 1)
                
                print()
                print(f"--- [ TURN {self.get_turn()} ] ---")
                print()
                print(team1)
                print(team2)
                print()
                print(team1.get_team_name() + "'s current Pokemon: " + str(team1_current))
                print(team2.get_team_name() + "'s current Pokemon: " + str(team2_current))
                print()

            # gets the choices of actions from both teams
            choice1 = team1.choose_battle_option(team1_current, team2_current)
            choice2 = team2.choose_battle_option(team2_current, team1_current)
            
            # iterates through actions in ACTION_PRIORITY
            for action in Battle.ACTION_PRIORITY:
                
                # if current action is attack and both teams chose to attack, the fastest pokemon goes first
                # if both pokemon have the same speed, team 1's pokemon goes first
                if action == Action.ATTACK and choice1 == Action.ATTACK and choice2 == Action.ATTACK:

                    if team1_current.get_speed() > team2_current.get_speed():
                        self.execute_choice(team1_current, team2_current, team1, choice1)

                        if team2_current.is_fainted():
                            break
                              	
                        self.execute_choice(team2_current, team1_current, team2, choice2)

                    elif team1_current.get_speed() == team2_current.get_speed():
                        self.execute_choice(team1_current, team2_current, team1, choice1)
                        self.execute_choice(team2_current, team1_current, team2, choice2)

                    else:  # team 2's pokemon speed is higher, so execute that first
                        self.execute_choice(team2_current, team1_current, team2, choice2)

                        if team1_current.is_fainted():
                            break

                        self.execute_choice(team1_current, team2_current, team1, choice1)


                else:

                    # if team 1's choice == action, execute the action
                    if choice1 == action:
                        team1_current = self.execute_choice(team1_current, team2_current, team1, choice1)

                    # if team 1 chose to heal but the battle is over, 
                    # they lose and the battle is over
                    # caused when team 1 chooses heal but they have already healed three times
                    if choice1 == Action.HEAL and self.end:
                        result = 2
                        break
                    
                    # if team 2's choice == action, execute the action
                    if choice2 == action:
                        team2_current = self.execute_choice(team2_current, team1_current, team2, choice2)
                    
                    # if team 2 chose to heal but the battle is over, 
                    # they lose and the battle is over
                    # caused when team 2 chooses heal but they have already healed three times
                    if choice2 == Action.HEAL and self.end:
                        result = 1
                        break
            
            if not self.end:

                # if both pokemon haven't fainted, both lose 1HP
                if not team1_current.is_fainted() and not team2_current.is_fainted():
                    team2_current.lose_hp(1)
                    team1_current.lose_hp(1)

                    try:
                        # If team2_current has fainted, return it to the PokeTeam
                        if team2_current.is_fainted():
                            team2.return_pokemon(team2_current)
                            team2_current = team2.retrieve_pokemon()

                            # Level up team1_current
                            team1_current.level_up()

                            # Evolution check
                            if team1_current.can_evolve() and team1_current.should_evolve():
                                non_evo_name = team1_current.get_poke_name()
                                team1_current = team1_current.get_evolved_version()

                                if self.verbose:
                                    self.print_action_line(non_evo_name, Battle.Other_Action.EVOLVE, evo_name=team1_current.get_poke_name())
                    except Exception:
                        self.end = 1
                        result = 1


                    try:
                        # If team1_current has fainted, return it to the PokeTeam and level_up team 2's current.
                        # Do evolution check also and evolve if necessary.
                        if team1_current.is_fainted():
                            team1.return_pokemon(team1_current)
                            team1_current = team1.retrieve_pokemon()

                            # Level up team2_current
                            team2_current.level_up()

                            # Evolution check
                            if team2_current.can_evolve() and team2_current.should_evolve():
                                non_evo_name = team2_current.get_poke_name()
                                team2_current = team2_current.get_evolved_version()

                                if self.verbose:
                                    self.print_action_line(non_evo_name, Battle.Other_Action.EVOLVE, evo_name=team2_current.get_poke_name())
                    except Exception:
                        self.end = 1
                        result = 2


                elif not team1_current.is_fainted() and team2_current.is_fainted():

                    if self.verbose:
                        self.print_action_line(team2_current.get_poke_name(), Battle.Other_Action.FAINTED)

                    # if only team 1's pokemon is not fainted
                    # it levels up and evolves if possible
                    team1_current.level_up()

                    if self.verbose:
                        self.print_action_line(team1_current.get_poke_name(), Battle.Other_Action.LEVEL_UP)

                    if team1_current.can_evolve() and team1_current.should_evolve():
                        non_evo_name = team1_current.get_poke_name()
                        team1_current = team1_current.get_evolved_version()

                        if self.verbose:
                            self.print_action_line(non_evo_name, Battle.Other_Action.EVOLVE, evo_name = team1_current.get_poke_name())
                        
                    
                    # attempts to retrieve a replacement for team 2's fainted pokemon
                    # if this fails then team 2 has no more pokemon 
                    # so team 2 loses
                    try:                    
                        team2_current = team2.retrieve_pokemon()
                        if self.verbose:
                            self.print_action_line(team2_current.get_poke_name(), Battle.Other_Action.INITIAL_DEPLOYED, team2.get_team_name())

                    except Exception:
                        self.end = True
                        result = 1

                elif not team2_current.is_fainted() and team1_current.is_fainted():

                    if self.verbose:
                        self.print_action_line(team1_current.get_poke_name(), Battle.Other_Action.FAINTED)
                    
                    # if only team 2's pokemon is not fainted
                    # it levels up and evolves if possible
                    team2_current.level_up()
                    if team2_current.can_evolve() and team2_current.should_evolve():
                        non_evo_name = team2_current.get_poke_name()
                        team2_current = team2_current.get_evolved_version()

                        if self.verbose:
                            self.print_action_line(non_evo_name, Battle.Other_Action.EVOLVE, evo_name = team2_current.get_poke_name())
                        


                    # attempts to retrieve a replacement for team 1's fainted pokemon
                    # if this fails then team 1 has no more pokemon
                    # so team 1 loses/team 2 wins
                    try:
                        team1_current = team1.retrieve_pokemon()
                        if self.verbose:
                            self.print_action_line(team1_current.get_poke_name(), Battle.Other_Action.INITIAL_DEPLOYED, team2.get_team_name())

                    except Exception:
                        self.end = True
                        result = 2

                # both pokemon have fainted
                else:
                    if self.verbose:
                        self.print_action_line(team1_current.get_poke_name(), Battle.Other_Action.FAINTED)
                        self.print_action_line(team2_current.get_poke_name(), Battle.Other_Action.FAINTED)

                    # both teams empty, game over
                    if team1.is_empty() and team2.is_empty():
                        self.end = True
                        self.result = 0

                    # both teams get new pokemon out
                    else:

                        # attempts to retrieve a replacement for team 1's fainted pokemon
                        # if this fails then team 1 has no more pokemon
                        # so team 1 loses/team 2 wins
                        try:
                            team1_current = team1.retrieve_pokemon()
                            if self.verbose:
                                self.print_action_line(team1_current.get_poke_name(), Battle.Other_Action.INITIAL_DEPLOYED, team1.get_team_name())

                        except Exception:
                            self.end = True
                            result = 2

                        # attempts to retrieve a replacement for team 2's fainted pokemon
                        # if this fails then team 2 has no more pokemon
                        # so team 2 loses/team 1 wins
                        try:
                            team2_current = team2.retrieve_pokemon()
                            if self.verbose:
                                self.print_action_line(team2_current.get_poke_name(), Battle.Other_Action.INITIAL_DEPLOYED, team1.get_team_name())

                        except Exception:

                            if self.end == True:
                                result = 1

        if team1_current is not None and team2_current is not None:
            if not team1_current.is_fainted() and team2_current.is_fainted():
                team1.return_pokemon(team1_current)
            else:
                team2.return_pokemon(team2_current)

        if team1_current is not None and team2_current is not None:
            if team1_current.is_fainted():
                team1.return_pokemon(team1_current)
            if team2_current.is_fainted():
                team2.return_pokemon(team2_current)

        self.reset()
        # returns battle result
        return result

    #---------------------------------------------------------------------------------------------------------------
    # THIS FUNCTION (print_action_line) IS MEANT FOR THE OPTIONAL VERBOSITY ARGUMENT, HOWEVER IT IS NOT COMPATIBLE WITH GRADESCOPE
    # TESTS... UNCOMMENT THIS FUNCTION TO VIEW A MORE DETAILED SUMMARY OF THE BATTLE, AS WELL AS THE PRINTING OF
    # THE POKEMON BATTLE
    #---------------------------------------------------------------------------------------------------------------
    # def print_action_line(self, poke_name: str, action: Action|Other_Action, team_name: str = "Trainer", evo_name: str = "", other_poke: str = "", dmg: int = -10) -> None:
    #     """
    #     Prints strings corresponding to a provided action.

    #     Args:
    #         poke_name : str
    #             name of main pokemon executing action
    #         action : Action|Other_Action
    #             the action being printed
    #         team_name : str
    #             name of team executing action
    #         evo_name : str
    #             name of the evolution of a pokemon that is evolving
    #         other_poke : str
    #             name of a defending pokemon
    #         dmg : int
    #             damage points taken/dealt

    #     Preconditions:
    #       -

    #     Returns:
    #         -

    #     Time Complexity:
    #       Best Case:
    #         O(1)
    #       Worst Case:
    #         O(1)
    #     """
    #     if not self.verbose:
    #         raise Exception("Verbosity is off!")

    #     if action in Action or action in Battle.Other_Action:
    #         print(Battle.ACTION_STRINGS[action].format(poke_name = poke_name, team_name = team_name, evo_name = evo_name, other_poke = other_poke, dmg = dmg))
    #     else:
    #         raise Exception("Invalid action.")
        
    def execute_choice(self, attacker: PokemonBase, defender: PokemonBase, attacker_team: PokeTeam, action: Action) -> PokemonBase:
        """
        Executes the action selected by a PokeTeam.

        Args:
            attacker : PokemonBase
                main pokemon attacking/executing an action
            defender : PokemonBase
                defending pokemon during the attacking routine
            attacker_team : PokeTeam
                team of the attacker pokemon
            action : Action
                the action executed by attacker

        Preconditions:
          -

        Returns:
            return_pokemon : PokemonBase
                the current attacker pokemon (can change after SWAP or SPECIAL)

        Time Complexity:
          Best Case:
            O(1) when both the PokeTeams are in battle mode 0, where the ADT implementation only uses constant O(1)
            operations.
          Worst Case:
            O(log n) when both the PokeTeams are in battle mode 2, where the function has to use the ArraySortedList
            ADT's .add() and _index_to_add() methods, that use a binary search to find the index to add.
        """

        # prints text describing action
        if self.verbose:
            self.print_action_line(attacker.get_poke_name(), action)

        # if action.name == ATTACK, attacker pokemon attacks defender
        if action.name == "ATTACK":
            atk_status = attacker.get_status_inflicted()
            attack_res = attacker.attack(defender)  # (attacker, defender, abs dmg, status effect damage)

            if attacker.can_evolve() and attacker.should_evolve():
                non_evo_name = attacker.get_poke_name()
                attacker = attacker.get_evolved_version()


            if self.verbose:
                try:
                    status = Battle.STATUS_OBJECT[atk_status]
                except KeyError:
                    status = "free"

                if attack_res[0] == attack_res[1] and status == Battle.Other_Action.CONFUSE:
                    self.print_action_line(attacker.get_poke_name(), status)
                    self.print_action_line(attacker.get_poke_name(), Battle.Other_Action.HURTITSELF)
                    self.print_action_line(attacker.get_poke_name(), Battle.Other_Action.LOSE_HP, dmg = attack_res[2])

                elif status != "free" and status != Battle.Other_Action.SLEEP:
                    self.print_action_line(attacker.get_poke_name(), Battle.Other_Action.DEAL_DMG, dmg = attack_res[2], other_poke = defender.get_poke_name()) # deals x hp
                    self.print_action_line(attacker.get_poke_name(), status) # status effect
                    if attack_res[3] > 0:
                        self.print_action_line(attacker.get_poke_name(), Battle.Other_Action.LOSE_HP, dmg =attack_res[3]) # loses x hp

                elif status == Battle.Other_Action.SLEEP:
                    self.print_action_line(attacker.get_poke_name(), status)
                
                else: 
                    self.print_action_line(attacker.get_poke_name(), Battle.Other_Action.DEAL_DMG, dmg = attack_res[2], other_poke = defender.get_poke_name()) # deals x hp
                    

            return_pokemon = attacker

        # if action.name == SWAP, the current pokemon is swapped for a new one
        if action.name == "SWAP":
            # returns attacker to the pokemon team and retrieves a new pokemon
            attacker_team.return_pokemon(attacker)
            return_pokemon = attacker_team.retrieve_pokemon()

            # Evolution check
            if return_pokemon.can_evolve() and return_pokemon.should_evolve():
                # non_evo_name = return_pokemon.get_poke_name()
                return_pokemon = return_pokemon.get_evolved_version()

            if self.verbose:
                self.print_action_line(attacker.get_poke_name(), Battle.Other_Action.RETURNED)
                self.print_action_line(return_pokemon.get_poke_name(), Battle.Other_Action.DEPLOYED)

        # if action.name == HEAL, the current pokemon is healed
        elif action.name == "HEAL":
            # if the heal count is 3, the game ends
            # otherwise the pokemon is healed
            if attacker_team.get_heal_count() == 3:
                self.end = True
                if self.verbose:
                    self.print_action_line(attacker.get_poke_name(), Battle.Other_Action.HEAL_FAILED)
            else:
                attacker.heal()
                attacker_team.increment_heal_count()
            
            return_pokemon = attacker

        # if action.name == SPECIAL, current pokemon is returned and
        # team lineup is shuffled based on battle mode
        elif action.name == "SPECIAL":
            # returns attacker to the pokemon team
            # runs the special associated with the team's battle mode
            # and retrieves a new pokemon
            attacker_team.return_pokemon(attacker)
            attacker_team.special()
            return_pokemon = attacker_team.retrieve_pokemon()

            # Evolution check
            if return_pokemon.can_evolve() and return_pokemon.should_evolve():
                # non_evo_name = return_pokemon.get_poke_name()
                return_pokemon = return_pokemon.get_evolved_version()

            if self.verbose:
                self.print_action_line(attacker.get_poke_name(), Battle.Other_Action.RETURNED)
                self.print_action_line(return_pokemon.get_poke_name(), Battle.Other_Action.DEPLOYED)

        return return_pokemon
