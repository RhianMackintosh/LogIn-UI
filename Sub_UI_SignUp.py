#Pygame Signup
import pygame
pygame.init()

ScreenWidth = 800
ScreenHeight = 800
font = pygame.font.Font("freesansbold.ttf",50)
StartColour = (163,218,246)
StartColourD = (132,205,242)

LogIn = "Log In"
SignIn = "Sign In"

window = pygame.display.set_mode((ScreenWidth,ScreenHeight))
window.fill((255,255,255))
pygame.display.set_caption("Games")
pygame.display.update()


def button(StartColour,x,y,width,height,text,pos1,pos2):
    pygame.draw.rect(window,(StartColour),(x,y,width,height))
    Button2 = font.render(text,1,(0,0,0))
    window.blit(Button2,(pos1,pos2))
    

def LogOnUI():
    window.fill(255,255,255)

    #the log in text
    button(StartColour,)
    
    
