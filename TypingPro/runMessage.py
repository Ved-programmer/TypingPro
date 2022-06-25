import pygame
import pygame.freetype
import time
import utility
import texts
class line:
    def __init__(self, data, hu):
        self.data = data
        self.currentLetter = 0
        self.y = hu*300


def splitScreenMsg(msg, hu):
    cur = []
    strings = []
    words = msg.split(" ")
    for i in words:
        if len(" ".join(cur)) + len(i) >= 35:
            strings.append(line(" ".join(cur), hu))
            cur = []
        cur.append(i)
    if cur != []:strings.append(line(" ".join(cur), hu))
    return strings


def otherStuff(screen, WIDTH, HEIGHT, wu, hu, wpm, accuracy):
    font = pygame.font.SysFont(None, 70)
    text1 = font.render(f"accuracy: {accuracy}", True, (0, 0, 255))
    text2 = font.render(f"wpm: {wpm}", True, (0, 0, 255))
    text_rect1 = text1.get_rect(center=(WIDTH/2, HEIGHT/2-75*hu))
    text_rect2 = text2.get_rect(center=(WIDTH/2, HEIGHT/2+75*hu))
    screen.blit(text1, text_rect1)
    screen.blit(text2, text_rect2)



def calculateDetails(start, gotWrong, length):
    timeTaken = (time.time() - start) / 60
    words = length / 5
    wpm = words // timeTaken
    accuracy = 100 - round(gotWrong / length, 2)
    return [wpm, accuracy]

def showResults(screen, start, gotWrong, length, backgroundScreen, backgroundText, 
                foregroundText, WIDTH, HEIGHT, wu, hu):
    screen.fill(backgroundScreen)


    wpm, accuracy = calculateDetails(start, gotWrong, length)

    font = pygame.font.SysFont(None, 50)
    text1 = font.render(f"Your avergage WPM is {wpm}", True, (0, 0, 0))
    text2 = font.render(f"Your avergage accuracy is {accuracy}%", True, (0, 0, 0))
    text_rect1 = text1.get_rect(center=(WIDTH/2, HEIGHT/4))
    text_rect2 = text2.get_rect(center=(WIDTH/2, HEIGHT/3))
    

    backButton = utility.button((0, 0, 255), wu*100, HEIGHT/2, wu*300, 
                                hu*100, wu, hu, "Go Back", 40)

    runAgainButton = utility.button((0, 0, 255), wu*600, HEIGHT/2, wu*300, 
                                hu*100, wu, hu, "Run Again", 40)

    buttons = [backButton, runAgainButton]

    pygame.display.update()

    while True:
        for i in pygame.event.get():
            pos = pygame.mouse.get_pos()
            utility.changeButtonColor(buttons, pos)
            if i.type == pygame.QUIT:
                return
            if i.type == pygame.KEYDOWN:
                if i.unicode == "b":
                    return gotWrong
                if i.key == pygame.K_RETURN:
                    return runMessage(screen, texts.getText(),
                    backgroundScreen, backgroundText, foregroundText, WIDTH, HEIGHT, wu, hu)

            elif i.type == pygame.MOUSEBUTTONDOWN:

                if backButton.isOver(pos):
                    return gotWrong
            
                if runAgainButton.isOver(pos):
                    return runMessage(screen, texts.getText(),
                    backgroundScreen, backgroundText, foregroundText, WIDTH, HEIGHT, wu, hu)
                
            
        screen.fill(backgroundScreen)
        utility.drawButtons(buttons, screen)
        screen.blit(text1, text_rect1);screen.blit(text2, text_rect2)
        pygame.display.update()


def runMessage(screen, dataToShow, backgroundScreen, backgroundText, foregroundText, 
                WIDTH, HEIGHT, wu, hu):
    lines = splitScreenMsg(dataToShow, hu)
    #print(lines)
    
    currentLineIdx = 0
    currentLine = lines[currentLineIdx]
    
    font = pygame.freetype.Font(None, 35)
    font.origin = True

    M_ADV_X = 4
    text_surf_rect = font.get_rect(currentLine.data)
    
    baseline = text_surf_rect.y + hu*20
    
    text_surf = pygame.Surface((text_surf_rect.size[0] + wu*30, text_surf_rect[1] + hu*80))
    text_surf_rect.center = screen.get_rect().center
    text_surf_rect.y -= currentLine.y
    colour = foregroundText
  
    metrics = font.get_metrics(currentLine.data)
    gotWrong = 0
    length = 0
    start = 0
    wpm, accuracy = calculateDetails(start, gotWrong, 1)
    cur = 0

    backButton = utility.button((0, 0, 255), WIDTH/2-200*wu, HEIGHT/2 + 200*hu, wu*400, 
                                hu*200, wu, hu, "Go Back", 40)

    while True:
        if time.time() - cur > 1.5 and length > 1:
            wpm, accuracy = calculateDetails(start, gotWrong, length)
            cur = time.time()
        events = pygame.event.get()

        for e in events:
            pos = pygame.mouse.get_pos()
            utility.changeButtonColor([backButton], pos)
            if e.type == pygame.QUIT:
                return
            if e.type == pygame.KEYDOWN:
                if e.unicode == currentLine.data[currentLine.currentLetter]:
                    if not start:start = time.time()
                    colour = foregroundText
                    currentLine.currentLetter += 1
                    length += 1
                    if currentLine.currentLetter >= len(currentLine.data):
                        currentLineIdx += 1
                        if currentLineIdx >= len(lines):return showResults(screen, start, 
                                                                        gotWrong, length, 
                        backgroundScreen, backgroundText, foregroundText, WIDTH, HEIGHT, wu, hu)
                        currentLine = lines[currentLineIdx]
                        text_surf_rect = font.get_rect(currentLine.data)
                        baseline = text_surf_rect.y + hu*20
                        text_surf = pygame.Surface((text_surf_rect.size[0] + wu*30, 
                                                    text_surf_rect[1] + hu*80))
                        text_surf_rect.center = screen.get_rect().center
                        text_surf_rect.y -= currentLine.y
                        colour = foregroundText
                        metrics = font.get_metrics(currentLine.data)

                elif len(e.unicode) == 1:
                    #print(e.unicode, gotWrong)
                    if not start:start = time.time()
                    colour = 'red'
                    gotWrong += 1
                
            elif e.type == pygame.MOUSEBUTTONDOWN:
                if backButton.isOver(pos):
                    return gotWrong
                               
        screen.fill(backgroundScreen)
        text_surf.fill(backgroundText)
        otherStuff(screen, WIDTH, HEIGHT, wu, hu, wpm, accuracy)
        x = 0
       
        for (idx, (letter, metric)) in enumerate(zip(currentLine.data, metrics)):
            if idx == currentLine.currentLetter:color = colour
            elif idx < currentLine.currentLetter:color = 'lightgrey'
            else:color = 'black'
            
            font.render_to(text_surf, (x, baseline), letter, color)
            x += metric[M_ADV_X]
          
        screen.blit(text_surf, text_surf_rect)
        utility.drawButtons([backButton], screen)
        pygame.display.flip()
