import pygame
from snake_pixel import Snake
from Food import Food


class GameEnvironment:
    """
        Class that models the environment in which the game is played.
        instance variables: screen : the pygame display
                            surface : the pygame surface
                            snake : A list of Snake objects
                            fps : The speed of the game
                            dir_change_location : A dictionary of coordinates
                             pointing to directions to be followed at those
                             coordinates
                            food : A Food object
                            status : States whether the game is running or over
                            It is 1 if game is running, 0 if game is over.
        """
    def __init__(self):
        pygame.init()
        self.status = 1
        self.screen = pygame.display
        self.surface = self.screen.set_mode((800, 600))
        self.snake = [Snake(200, 200, 'r')]
        self.fps = 100
        self.dir_change_location = {}
        self.food = Food()
        self.food.generate_food()

    def events(self):
        """
                Contains the event loop for the pygame window.Rectangle
                images for the snake and the Circle images for food are created
                in this event loop. Calls to other GameEnvironment methods are
                made from here.
                :return: None
        """
        done = False
        clock = pygame.time.Clock()
        while not done:  # start of the event loop
            for event in pygame.event.get():  # piping out the events
                if event.type == pygame.QUIT:
                    self.status = 0
                    done = True
            self.food.set_level()  # getting the food level set for the game
            self.fps = (self.food.level * 10) + 100
            # setting the speed of the game according the food level
            self.check_wall()  # checking if the snake has banged into the wall
            self.check_suicide()  # checking if the snake has turned into itself
            if self.status == 0:  # checking if the snake is supposed to dead.
                done = True
            self.check_food()  # checking if the snake has eaten food.
            pressed = pygame.key.get_pressed()
            self.update_position(pressed, self.snake[0].x_coord,
                                 self.snake[0].y_coord)
            # updating the position of the snake according to input direction
            self.surface.fill((0, 0, 0))
            for i in range(len(self.food.x)):  # loop to display all food.
                pygame.draw.circle(self.surface, (255, 255, 255),
                                   (self.food.x[i], self.food.y[i]), 10)
            for i in range(len(self.snake)):  # loop to display entire snake
                pygame.draw.rect(self.surface, (55, 255, 55),
                                 pygame.Rect(self.snake[i].get_position()[0],
                                             self.snake[i].get_position()[1],
                                             20, 20))

            self.screen.flip()
            clock.tick(self.fps)

    def update_position(self, pressed, x_coord, y_coord):
        """
        Method to make sure that all snake objects change direction at given
        point
        :param pressed: A pygame key object
        :param x_coord: The x coordinate where the change in direction happens
        :param y_coord: The y coordinate where the change in direction happens
        :return: None
        """
        dir = ''  # String to represent the input direction
        if pressed[pygame.K_LEFT]:  # Condition when left arrow key is pressed
            dir = 'l'
        elif pressed[pygame.K_UP]:  # Condition when up arrow key is pressed
            dir = 'u'
        elif pressed[pygame.K_DOWN]:  # Condition when down arrow key is pressed
            dir = 'd'
        elif pressed[pygame.K_RIGHT]:  # Condition for right arrow key press
            dir = 'r'
        if dir != '':  # when there is no input, continue in original direction
            self.dir_change_location[(x_coord, y_coord)] = dir
        for i in range(len(self.snake)):
            if (self.snake[i].x_coord, self.snake[i].y_coord) in \
                    self.dir_change_location.keys():
                # checking if a snake node has reached a point where it has to
                # change direction.
                old_x = self.snake[i].x_coord
                old_y = self.snake[i].y_coord
                self.snake[i].move(
                    self.dir_change_location[(self.snake[i].x_coord,
                                              self.snake[i].y_coord)])
                # moving that snake object in the direction it has to go in at
                # that point. The direction is given by the dictionary.
                if i == len(self.snake) - 1:
                    del self.dir_change_location[(old_x, old_y)]
                    # once the last snake node passes a point, get rid of that
                    # point in the dictionary to prevent the snake from
                    # following old instructions
            else:
                self.snake[i].move(self.snake[i].direction)


    def check_wall(self):
        """
        Method to check if the snake's head has hit the wall. Ends the game if
        this happens.
        :return: None
        """
        head = self.snake[0]
        x = head.get_position()[0]
        y = head.get_position()[1]
        if x > 800 or y > 600 or x < 0 or y < 0:
            # checking if the head of the snake collides with a wall.
            self.status = 0  # killing the snake

    def check_food(self):
        """
        Checks if the snake has passed a food object. The length of the snake
        increases if this happens. Makes appropriate changes to the food object
        too.
        :return:
        """
        for i in range(len(self.food.x)): # iterating through all food on screen
            x = self.food.x[i]
            y = self.food.y[i]
            if pygame.Rect(self.snake[i].get_position()[0],
                           self.snake[i].get_position()[1],
                           20, 20).collidepoint(x, y):
                # checking if the food snake's head collides with a food object
                self.snake.append(
                    self.snake[len(self.snake) - 1].get_next_snake())
                # making the snake longer.
                self.food.get_eaten(i)
                # recording that food was eaten for scoring purposes
                break

    def check_suicide(self):
        """
        Checks if the snake turns into itself. Ends the game if this happens
        :return: None
        """
        head = pygame.Rect(self.snake[0].get_position()[0],
                           self.snake[0].get_position()[1],
                           20, 20)
        for snake in self.snake[1:]:
            body = pygame.Rect(snake.get_position()[0],
                               snake.get_position()[1],
                               20, 20)
            if head.collidepoint(body.centerx, body.centery):
                # checking if the center of the snake's head is in the center of
                # a part of its body
                self.status = 0  # killing the snake
                break
