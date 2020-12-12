import pygame
import utility
import webbrowser


def showCreators(screen, WIDTH, HEIGHT, wu, hu):
    onThisScreen = True
    screen.fill([0, 0, 0])
    font = pygame.font.Font(None, int(wu*hu*55))
    text1 = font.render("This game was made by Ved Rathi in 2020", True, [255, 255, 255])
    text2 = font.render("assisted by Navdeep Kante", True, [255, 255, 255])
    text_rect1 = text1.get_rect(center = [WIDTH/2, HEIGHT/8])
    text_rect2 = text2.get_rect(center = [WIDTH/2, HEIGHT/4])

    screen.blit(text1, text_rect1)
    screen.blit(text2, text_rect2)
    backButton = utility.button((0, 0, 255), WIDTH/2 - wu*300, HEIGHT/2 - hu*170, wu*600, 
                                hu*375, wu, hu, "Go Back")

    repositoryButton = utility.button((0, 0, 255), WIDTH/2 - wu*150, HEIGHT/2 + hu*250, wu*300, 
                                hu*100, wu, hu, "view on Github", 40)

    vedGithubButton = utility.button((0, 0, 255), wu*10, HEIGHT/2 + hu*250, wu*300, 
                                hu*100, wu, hu, "Ved's Github", 40)

    navdeepGithubButton = utility.button((0, 0, 255), wu*690, HEIGHT/2 + hu*250, wu*300, 
                                hu*100, wu, hu, "Navdeep's Github", 40)
        
    buttons = [backButton, repositoryButton, vedGithubButton, navdeepGithubButton]

    utility.drawButtons(buttons, screen)
    pygame.display.update()

    while onThisScreen:
        for e in pygame.event.get():
            pos = pygame.mouse.get_pos()
            utility.changeButtonColor(buttons, pos)
            
            if e.type == pygame.QUIT:
                return pygame.QUIT

            elif e.type == pygame.MOUSEBUTTONDOWN:
                if backButton.isOver(pos):
                    return 
                
                if repositoryButton.isOver(pos):
                    webbrowser.open("https://github.com/Ved-programmer/TypingPro")

                elif vedGithubButton.isOver(pos):
                    webbrowser.open("https://github.com/Ved-programmer")

                elif navdeepGithubButton.isOver(pos):
                    webbrowser.open("https://github.com/smartnavdeep")


        utility.drawButtons(buttons, screen)
        pygame.display.update()

