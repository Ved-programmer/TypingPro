import pygame
import pygame.freetype
import time
import random


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
        cur.append(i)
        if len(" ".join(cur)) >= 30:
            strings.append(line(" ".join(cur), hu))
            cur = []
    if cur != []:strings.append(line(" ".join(cur), hu))
    return strings


def otherStuff(screen, WIDTH, HEIGHT, wu, hu, wpm, accuracy):
    font = pygame.font.SysFont(None, 150)
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

    font = pygame.font.SysFont(None, int(wu*hu*60))
    text1 = font.render(f"Your avergage WPM is {wpm}", True, (0, 0, 0))
    text2 = font.render(f"Your avergage accuracy is {accuracy}%", True, (0, 0, 0))
    text_rect1 = text1.get_rect(center=(WIDTH/2, HEIGHT/4))
    text_rect2 = text2.get_rect(center=(WIDTH/2, HEIGHT/3))
    screen.blit(text1, text_rect1)
    screen.blit(text2, text_rect2)

    text = font.render("Press b to go back and enter to run again.", True, (0, 0, 0))
    text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
    screen.blit(text, text_rect)

    pygame.display.update()

    while True:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                return
            if i.type == pygame.KEYDOWN:
                if i.unicode == "b":
                    return gotWrong
                if i.key == pygame.K_RETURN:
                    with open("text.txt") as f:
                        lines = f.readlines()
                    return runMessage(screen, random.choice(lines).removesuffix("\n"),
                    backgroundScreen, backgroundText, foregroundText, WIDTH, HEIGHT, wu, hu)


def runMessage(screen, dataToShow, backgroundScreen, backgroundText, foregroundText, 
                WIDTH, HEIGHT, wu, hu):
    lines = splitScreenMsg(dataToShow, hu)
    #print(lines)
    
    currentLineIdx = 0
    currentLine = lines[currentLineIdx]
    
    font = pygame.freetype.Font(None, int(wu*hu*50))
    font.origin = True
    #font_height = font.get_sized_height()

    M_ADV_X = 4
    text_surf_rect = font.get_rect(currentLine.data)
    
    baseline = text_surf_rect.y + hu*20
    text_surf = pygame.Surface((text_surf_rect.size[0] + wu*30, text_surf_rect[1] + hu*80))
    text_surf_rect.center = screen.get_rect().center
    text_surf_rect.y -= currentLine.y
    text_surf_rect.h += currentLine.y
    colour = foregroundText
  
    metrics = font.get_metrics(currentLine.data)
    gotWrong = 0
    length = 0
    start = 0
    wpm, accuracy = calculateDetails(start, gotWrong, 1)
    cur = 0

    while True:
        if time.time() - cur > 1 and length > 0:
            wpm, accuracy = calculateDetails(start, gotWrong, length)
            cur = time.time()
        events = pygame.event.get()

        for e in events:
            if e.type == pygame.QUIT:
                return
            if e.type == pygame.KEYDOWN:
                if not start:start = time.time()
                if e.unicode == currentLine.data[currentLine.currentLetter]:
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
                        text_surf_rect.h += currentLine.y
                        colour = foregroundText
                        metrics = font.get_metrics(currentLine.data)

                elif len(e.unicode) == 1:
                    #print(e.unicode, gotWrong)
                    colour = 'red'
                    gotWrong += 1
                               
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
        pygame.display.flip()
    screen.fill(backgroundScreen)
    pygame.display.flip()

    


if __name__ == '__main__':
    """
    pygame.init()
    screen = pygame.display.set_mode((800, 400))
    green = [0, 255, 0]
    yellow = [255, 255, 0]
    purple = [125, 25, 200]

    screen.fill(green)
    pygame.display.update()
    with open("text.txt") as f:
        val = f.readlines()[0].removesuffix("\n")
        #print(val)
        returnVal = runMessage(screen, val, green, yellow, purple)
    print(returnVal)

    """
