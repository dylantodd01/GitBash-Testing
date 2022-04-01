import sys, pygame, time, random
pygame.init()

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

size = width, height = 600, 600
black = (0, 0, 0)
blue = (0, 100, 200)
white = (255, 255, 255)

piEstimate = "0"
insideCircleCounter = 0
outsideCircleCounter = 0

def throwDart():
    pos = (random.randint(0, 600), random.randint(0, 600))
    pygame.draw.circle(screen, white, pos, 1)
    return pos

def dartCounter(pos, insideCircleCounter, outsideCircleCounter):
    distanceToCentre = ((abs(pos[0] - 300))**2 + (abs(pos[1] - 300))**2)**0.5
    if distanceToCentre <= 300:
        insideCircleCounter += 1
    else:
        outsideCircleCounter += 1
    return insideCircleCounter, outsideCircleCounter

def calculatePi(insideCircleCounter, outsideCircleCounter):
    piEstimate = (insideCircleCounter/(insideCircleCounter+outsideCircleCounter))*4
    return str(piEstimate)

screen = pygame.display.set_mode(size)
screen.fill(black)
pygame.draw.circle(screen, blue, (300,300), 300)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

    print(piEstimate)
    #textsurface = myfont.render(piEstimate, False, (255, 0, 0))
    #screen.blit(textsurface,(0,0))
    pygame.display.flip()

    #time.sleep(0.0001)

    pos = throwDart()
    insideCircleCounter, outsideCircleCounter = dartCounter(pos, insideCircleCounter, outsideCircleCounter)
    piEstimate = calculatePi(insideCircleCounter, outsideCircleCounter)
    
    
