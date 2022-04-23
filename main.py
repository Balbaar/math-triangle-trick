import pygame
import math
import random

count = 0  # Keeps count
dot_size = 1

triangle = input("1: Symmetrical Triangle & 2: 90 Degree Triangle ")
dots = int(input("Amount of dots per click: "))

#Starting Points | Symmetrical
if triangle == "1":
    dotA = [400, 100]  # 0
    dotB = [700, 200 + math.sqrt(150000)]  # 1
    dotC = [100, 200 + math.sqrt(150000)]  # 2

#Starting Points | 90 degree triangle
if triangle == "2":
    dotA = [100, 100]
    dotB = [700, 700]
    dotC = [100, 700]

#Draw starting points
screen = pygame.display.set_mode([800, 800])
pygame.draw.circle(screen, (250, 0, 0), [dotA[0], dotA[1]], 5)
pygame.draw.circle(screen, (250, 0, 0), [dotB[0], dotB[1]], 5)
pygame.draw.circle(screen, (250, 0, 0), [dotC[0], dotC[1]], 5)
pygame.display.update()

pygame.display.set_caption("Math Triangle Trick")


#Dots
start_dots = [dotA, dotB, dotC]
new_dots = []


#Calculate first middle dot
def calc_first_dot():
    dotX = start_dots[1]
    dotY = start_dots[0]
    x = abs((dotX[0] - dotY[0]) / 2)
    y = abs((dotX[1] - dotY[1]) / 2)
    print(f"Dot: {count} : {x}, {y}")
    return [min(dotX[0], dotY[0]) + x, min(dotX[1], dotY[1]) + y]


#Calculate new dot | in the middle of last one and a random starting dot
def calc_dot(dotY):
    dotX = start_dots[random.randint(0, 2)]
    x = abs((dotX[0] - dotY[0]) / 2)
    y = abs((dotX[1] - dotY[1]) / 2)
    print(f"Dot: {count} : {x}, {y}")
    return [min(dotX[0], dotY[0]) + x, min(dotX[1], dotY[1]) + y]


#Draw screen
def draw_screen(coord):
    pygame.draw.circle(screen, (0, 0, 255), [coord[0], coord[1]], dot_size)
    pygame.display.update()


first = 1
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if count == 0:
                new_dots.append(calc_first_dot())
                draw_screen(new_dots[-1])
                count += 1
            else:
                for i in range(dots - first):
                    #time.sleep(0.05)
                    count += 1
                    new_dots.append(calc_dot(new_dots[-1]))
                    draw_screen(new_dots[-1])
                first = 0
