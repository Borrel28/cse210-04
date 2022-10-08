from email import message
from multiprocessing.sharedctypes import Value
import random
import Die



# TODO: Implement the Die class as follows...
class Actor:
    """A person who plays the game. 
    
    The responsibility of a Actor is to rol the game of play.

    Attributes:
        player (List[Die]): A list of Die instances.
        points (boolean): Whether or not the game is being played.
        value (int): The points for one round of play.
        total_value (int): The the points for the entire game.
    """
    
    def __init__(self):
        super().__init__()
        this_message = " "   
    def get_message(self):
        return self.get_message
    def set_message(self, message):
        self._message = message
    
# 1) Add the class declaration. Use the following class comment.
    """A small cube with a different number of spots on each of its six sides.
    
    The responsibility of Die is to keep track of the side facing up and calculate the points for 
    it.
   
    Attributes:
        value (int): The number of spots on the side facing up.
        points (int): The number of points the die is worth.
    """
class player():
    def __init__(self):
        super().__init__(self)
        self.player = []
        self.is_playing = True
        self.value = 0
        self.total_value = 0
            
        for i in range(5):
            die = Die()
            self.is_playing.append(die)
        
# 2) Create the class constructor. Use the following method comment.
        """Constructs a new instance of Die with a value and points attribute.

        Args:
            self (Die): An instance of Die.
        """
    
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
            
            gems = object
            rock = stone
            object = 1
            stone = -1
            
# 3) Create the roll(self) method. Use the following method comment.
        """Generates a new random value and calculates the points.
        
        Args:
            self (Die): An instance of Die.
        """
        print("Random integers between 0 and 9: ")
        for i in range(1, 99):
            gems.random.int(1, 79)
            stone.ramdon.int(1, 20)
            
    def run_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        roll_dice = input("Roll dice? [y/n] ")
        self.is_playing = (roll_dice == "y")
       
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 

        for i in range(len(self.dice)):
            die = self.dice[i]
            die.roll()
            self.score += die.points 
        self.total_score += self.score

    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        values = ""
        for i in range(len(self.dice)):
            die = self.dice[i]
            values += f"{die.value} "
            
        print(f"You rolled: {values}")
        print(f"Your score is: {self.total_score}\n")
        self.is_playing == (self.score > 0)