import pygame
import runMessage
import creators
import utility
import texts


pygame.init()
screen_info = pygame.display.Info()

WIDTH, HEIGHT = screen_info.current_w//2, screen_info.current_h//2

# WIDTH, HEIGHT = 1000, 800
wu = WIDTH / 1000
hu = HEIGHT / 1000

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Typing Pro")

#RGB color values
white = (255, 255, 255)
green = [0, 255, 0]
yellow = [255, 255, 0]
purple = [125, 25, 200]

screen.fill(green)
pygame.display.update()

gameOn = True
messageRunningButton = utility.button((0, 0, 255), WIDTH/2 - wu*300, hu*100, wu*600, hu*350,
                        wu, hu, "Start Typing")

aboutMe = utility.button((0, 0, 255), WIDTH/2 - wu*300, hu*550, wu*600, hu*350,
                        wu, hu, "Get to know the creators")

messageRunning = lambda : runMessage.runMessage(screen, texts.getText(),
                                                green, yellow, purple, WIDTH, HEIGHT, wu, hu)

pygame.display.update()

buttons = [aboutMe, messageRunningButton]

while gameOn:
    for e in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if e.type == pygame.QUIT:
            gameOn = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RETURN:
                gotWrong = messageRunning()
                if gotWrong == None:gameOn = False
                

        elif e.type == pygame.MOUSEBUTTONDOWN:
            if aboutMe.isOver(pos):
                if creators.showCreators(screen, WIDTH, HEIGHT, wu, hu) == pygame.QUIT:
                    gameOn = False
            
            if messageRunningButton.isOver(pos):
                gotWrong = messageRunning()
                if gotWrong == None:gameOn = False

        utility.changeButtonColor(buttons, pos)
    
    screen.fill(green)
    
    utility.drawButtons(buttons, screen)
    pygame.display.update()
        
pygame.quit()

# <-- LICENCE info -->
'''
TypingPro
Copyright Ved Rathi
Licensed under MIT (https://github.com/Ved-Programmer/TypingPro/blob/master/LICENSE)
'''

