from game_environment import GameEnvironment
import pygame


class Game:
    """
       Class to represent a single game.
       instance variables:
       int level = The difficulty level of the game. This is obtained from the
        food in the environment
       int score = The score the user has scored.
       environment = The game environment object in which this game is player
       """

    def __init__(self):

        self.score = 0
        self.environment = GameEnvironment()
        self.level = self.environment.food.level

    def set_level(self, level):
        """
        Sets the initial difficulty level of the game. Changes the food levels
        in the environment accordingly and changes the fps of the environment.
        :param level: The initial level of the game.
        :return: None

        >>> game_object = Game()
        >>> game_object.set_level(3)
        >>> print(game_object.level)
        3
        >>> game_object.set_level(4)
        >>> print(game_object.level)
        4
        """
        self.level = level
        self.environment.food.level = self.level
        self.environment.fps += 5

    def run_game(self):
        """
        Calls the events method on this game's environment and then calls
        end_game_display when the game ends
        :return: None
        """
        self.environment.events()
        if self.environment.status == 0:
            pygame.quit()
            self.end_game_display()

    def end_game_display(self):
        """
        This method creates and displays a pygame window with the appropriate
        message displayed
        """
        pygame.init()
        end_screen = True

        while end_screen:
            red_font = (255, 0, 0)
            white_font = (255, 255, 255)
            screen = pygame.display
            surface = screen.set_mode((800, 600))
            pygame.display.set_caption('Sorry! You Lost.')

            # Creates text for end screen, when snake dies
            large_text = pygame.font.Font('freesansbold.ttf', 90)
            text_surf = large_text.render('Sorry! You Died.', True, red_font)
            text_rect = text_surf.get_rect()
            text_rect.center = (400, 300)
            surface.blit(text_surf, text_rect)

            # Creates two rectangles, which will act as buttons
            pygame.draw.rect(surface, red_font, (150, 450, 100, 50))
            pygame.draw.rect(surface, red_font, (550, 450, 100, 50))

            # Creates the text for the restart button
            small_text = pygame.font.Font('freesansbold.ttf', 25)
            button_restart_text = small_text.render('Restart', True, white_font)
            button_restart_rect = text_surf.get_rect()
            button_restart_rect.center = (504, 510)
            surface.blit(button_restart_text, button_restart_rect)

            # Creates text for te quit button
            button_quit_text = small_text.render('Quit', True, white_font)
            button_quit_rect = text_surf.get_rect()
            button_quit_rect.center = (920, 510)
            surface.blit(button_quit_text, button_quit_rect)
            screen.flip()

            mouse_pos = pygame.mouse.get_pos()

            # If the mouse positions are in the area of the restart or quit buttons, carry out the appropriate action
            if 250 > mouse_pos[0] > 150 and 500 > mouse_pos[1] > 450:
                pygame.quit()
                end_screen = False
                new_game = Game()
                new_game.run_game()
            if 550 + 100 > mouse_pos[0] > 550 and 450 + 50 > mouse_pos[1] > 450:
                end_screen = False
                pygame.quit()



def get_score(game_object):
    """
    Returns the score scored in given game. The score is calculated using the
    level and amount eaten.
    :param game_object: Game object
    :return: int

    >>> game = Game()
    >>> print(game.score)
    0
    >>> get_score(game)
    0

    """
    game_object.score = game_object.level * game_object.environment.food.eaten
    return game_object.score


def get_final_score(game_object):
    """
    Implementation yet to decided.
    :param game_object:
    :return:
    """


if __name__ == '__main__':
    game = Game()
    game.run_game()
