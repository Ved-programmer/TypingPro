import pygame


class button():


    def __init__(self, color, x,y,width,height, wu, hu, text = "", font = 60):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.wu = wu
        self.hu = hu
        self.font = font


    def draw(self,win):
        #Call this method to draw the button on the screen

        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height))
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', int(self.wu*self.hu*self.font))
            text = font.render(self.text, 1, (0,255,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + 
                    (self.height/2 - text.get_height()/2)))


    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False
