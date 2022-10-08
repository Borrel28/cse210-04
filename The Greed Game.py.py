from unicodedata import name
from xml.dom.minidom import ProcessingInstruction


class Person:
    "intoducing of the class for the greed game"
    def __init__(self, name) -> None:
        self.name = name
        
    def get_name(self):
        return self._name
        
class Player(Person):
    def __init__(self, name) -> None:
        super().__init__(name)
#The game play and game over messages
    def start_game(self):
        self.player
        
        
        
        # the rules of the game
        Gems = 1
        Rock = -1
        player_touches = sum 
        sum = (Gems + Rock)
        # player instructions
        """if the Player touche the Gems he earns points otherwise looses points
        parameter
        gems = +1 
        Rock = -1
        """
        # Gems & Rock randomly appear and fall from the top of the screen.
        for i in range(1, 99):
            Gems.random.int(1, 79)
            Rock.ramdon.int(1, 20)
        #) can move left or right along the bottom of the screen.
        player_touches = sum # they earn
        
        if Rock < Gems:
            print("you gained much point {sum}")
            print("You Win")
        else: # game over
            print("you lost much point {sum}")
            print("Game Over")

        for playertouches in range(len(self.player)):
            touches = self.player[i]
            player_touches.roll()
            self.score += touches.points 
        self.total_score += self.touches

#Your program must also meet the following requirements.

#The program must have a README file.
#The program must have at least eight classes.
#Each module, class and method must have a corresponding comment.
#The game must remain generally true to the order of play described earlier.
#Have Some Fun
#Make the game your own by enhancing it any way you like. Here are a few ideas.

#Enhanced player movement (up and down in a limited range)

#Enhanced gem, rock and player representation (colors or better symbols)Gems (*) and rocks (o) randomly appear and fall from the top of the screen.The player (#) can move left or right along the bottom of the screen.
#If the player touches a gem they earn a point.
#If the player touches a rock they lose a point.
#Gems and rocks are removed when the player touches them.
#The game continues until the player closes the window.
#Enhanced player movement (up and down in a limited range)
#Enhanced game play and game over messages.
#Enhanced gem, rock and player representation (colors or better symbols)

        
        
        
        
        