import pygame 

class Snake:
	def __init__(self,length, color, width=15, height=15):
		self.width = width
		self.height = height
		self.margin = 3

		self.speed = self.width + self.margin
		self.x_speed = self.speed
		self.y_speed = 0

		self.length = length
		self.color = color

		self.snake_body = []
		self.snake = pygame.sprite.Group()

		self.make_snake()

	# Create an initial snake
	def make_snake(self):
		for i in range(self.length):
		    x = 250 - (self.width + self.margin) * i
		    y = 30

		    body = SnakeBody(x, y, self.color, self.width, self.height)
		    self.snake_body.append(body)
		    self.snake.add(body)

	def change_direction(self,x,y):
		self.x_speed = x
		self.y_speed = y
		
		head = self.snake_body.pop()
		self.snake.remove(head)
	 
		x = self.snake_body[0].rect.x + self.x_speed
		y = self.snake_body[0].rect.y + self.y_speed
		body = SnakeBody(x, y, self.color, self.width, self.height)

		self.snake_body.insert(0, body)
		self.snake.add(body)

	def get_snake(self):
		return self.snake

	def get_snake_speed(self):
		return self.speed



class SnakeBody(pygame.sprite.Sprite):
	def __init__(self, x, y, color, width, height):
		super().__init__()
 		
		self.image = pygame.Surface([width, height])
		self.image.fill(color)

		# Make our top-left corner the passed-in location.
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y