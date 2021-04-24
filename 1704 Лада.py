import pygame
import random
from circle import Circle

pygame.init()
screen = pygame.display.set_mode((800, 600))
black = (0, 0, 0)
white = (255, 255, 255)
red = (184, 15, 10)
lime = (180, 255, 100)
running = True
moments = []
g = 0
fps = pygame.time.Clock()
all_circles = []
c = 0
a = 2
b = 2
rad = 5
flag = True

# class Circle:
#     def __init__(self, x, y, color, radius, thickness, direction):
#         self.x = x
#         self.y = y
#         self.radius = radius
#         self.thickness = thickness
#         self.color = color
#         self.direction = direction
#     def make_circle(self, screen):
#         pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, self.thickness)
#     def move(self):
#         if self.direction == 'right':
#             self.x += 1
#             if (self.x + self.radius) == 800:
#                 self.direction = 'left'
#         if self.direction == 'left':
#             self.x -= 1
#             if (self.x - self.radius) == 0:
#                 self.direction = 'right'

        
for i in range(100):
        boop = Circle(i , i * 5, random.choices(range(0,255), k = 3), i + 10, 5, 'right')
        all_circles.append(boop)
          
while running:
    print('here')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()  
    screen.fill(black)
    
    for i in all_circles:
        i.make_circle(screen)  
        i.move()
    
    fps.tick(100000)
    pygame.display.update()