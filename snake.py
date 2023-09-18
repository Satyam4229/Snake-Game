import pygame
import random

pygame.init()  # for initializing the pygame

# Defining colors
white = (255, 255, 255)
yellow = (255, 215, 0)
black = (0, 0, 0)
red = (222, 50, 99)
blue = (0, 0, 255)
green = (15, 255, 80)

# Creating Display
dis_width = 800
dis_height = 600

# Setting display and caption
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake game by Satyam Pandey')

# Setting clock for maintaining the time
clock = pygame.time.Clock()

# Initializing the initial speed and size of snake
snake_block = 10
snake_speed = 5

# Setting font style and size
font_style = pygame.font.SysFont("cambria", 35)
score_font = pygame.font.SysFont("cambria", 30)


# Function for printing score
def your_score(score):
    value = score_font.render(" Your Score : " + str(score) + " ", True, yellow, black)
    dis.blit(value, [0, 0])


# Function for creating our snake
def our_snake(snake, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake, snake])


# Function for printing ending message
def message(msg, color, m, n):
    msg = font_style.render(msg, True, color, white)
    dis.blit(msg, [dis_width / m, dis_height / n])


# Function for game loop
def gameLoop():

    game_over = False    # Defining game over and game close
    game_close = False

    x1 = dis_width / 2  # Positioning of snake
    y1 = dis_height / 2

    x1_change = 0  # change in position
    y1_change = 0

    snake_List = []   # Array for storing the length of snake
    Length_of_snake = 1

    # Co-ordinates of food for snake which is random
    foodx = round(random.randrange(1, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(1, dis_height - snake_block) / 10.0) * 10.0

    # loop for start the game
    while not game_over:

        while game_close:

            # Background color filling
            dis.fill(blue)

            # Messages which prints in ending
            message('    You Lost !!!    ', black, 2.8, 3)
            message('     Press Q - Quit       ', red, 3.13, 2.2)
            message(' Press C - Play Again ', red, 3.2, 1.8)

            # Printing of score
            your_score(Length_of_snake - 1)

            pygame.display.update()

            # Setting up the key for close and restart the game
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:   # pressing q will quit the game
                        game_close = False
                        game_over = True
                    if event.key == pygame.K_c:   # pressing c will restart the game
                        gameLoop()

        # Creating keys to play the game
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Creating borders to game over
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        # adding co-ordinates to move the snake
        x1 += x1_change
        y1 += y1_change

        dis.fill(blue)

        # Creating food for snake
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        # Adding Snake size
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)

        # Deleting previous element from list
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Striking of snake with itself
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)   # Initializing snake
        your_score(Length_of_snake - 1)   # Initializing score

        pygame.display.update()

        # eating and increasing of snake
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        # Generating fps or increasing snake speed
        clock.tick(snake_speed + Length_of_snake / 2)

    pygame.quit()
    quit()


gameLoop()
