import pygame
from snake import Snake

pygame.init()

#Create a screen
width = 800
height = 600 

#Create the Snake
length = 30
color = (57,255,20)
snake = Snake(length, color)
snake_speed = snake.get_snake_speed()
x_speed = snake_speed 
y_speed = 0

screen = pygame.display.set_mode([width, height])
clock = pygame.time.Clock()

#done 
done = False 

while not done:
    # events; tracks keyboard, mouse clicks
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        #snake; up, down, left, right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left")
                x_speed = snake_speed * -1 
                y_speed = 0

            if event.key == pygame.K_RIGHT:
                print("Right")
                x_speed = snake_speed 
                y_speed = 0

            if event.key == pygame.K_UP:
                print("Up")
                x_speed = 0
                y_speed = snake_speed * -1

            if event.key == pygame.K_DOWN:
                print("Down")
                x_speed = 0 
                y_speed = snake_speed 

    snake.change_direction(x_speed, y_speed)

    #Draw
    screen.fill((0,0,0))
    snake.get_snake().draw(screen)
    pygame.display.flip()

    clock.tick(15)
            


