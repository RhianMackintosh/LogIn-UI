#Pygame Signup
import pygame
pygame.init()
    

def SignUpUI():
    def button(StartColour,x,y,width,height,text,fontC,pos1,pos2):
        pygame.draw.rect(window,(StartColour),(x,y,width,height))
        Button2 = fontC.render(text,1,(0,0,0))
        window.blit(Button2,(pos1,pos2))

    #------------------------------------------------------------------------------
    white = (255,255,255)
    backGC = (217, 240, 252)
    StartColour = (163,218,246)
    StartColourD = (132,205,242)
    ScreenWidth = 800
    ScreenHeight = 800
    typeUser = ""
    typePass = ""
    big = pygame.font.Font("freesansbold.ttf",50)
    small = pygame.font.Font("freesansbold.ttf",30)
    tiny = pygame.font.Font("freesansbold.ttf",20)
    window = pygame.display.set_mode((ScreenWidth,ScreenHeight))
    window.fill((backGC))
    pygame.display.update()
    #------------------------------------------------------------------------------

    button(StartColourD,260,100,310,80,"Sign Up",big,310,110)
    button(StartColour,250,90,310,80,"Sign Up",big,310,110)

    #name button
    button(StartColour,160,250,180,40,"First Name",small,170,255)
    button(white,350,250,270,40,"",small,170,255)

    #surname button
    button(StartColour,160,350,180,40,"Last Name",small,170,355)
    button(white,350,350,270,40,"",small,170,355)

    #username button
    button(StartColour,160,450,180,40,"Username",small,170,455)
    button(white,350,450,270,40,"",small,170,455)

    #security question button
    button(backGC,60,535,180,10,"Security Question: What is your mothers maiden name",tiny,120,535)
    button(StartColour,160,570,180,40,"Answer",small,190,575)
    button(white,350,570,270,40,"",small,170,575)

    pygame.display.update()

    selec = False
    while selec == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEMOTION:
                print(event.pos)

    mousex,mousey = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if mousex >= 350 and mousex <= 620 and mousey >= 250 and mousey <= 290:
        print("hi")
        

    elif mousex >= 350 and mousex <= 620 and mousey >= 350 and mousey <= 390:
        print("hi")

    elif mousex >= 350 and mousex <= 620 and mousey >= 450 and mousey <= 490:
        print("hi")

    elif mousex >= 350 and mousex <= 620 and mousey >= 550 and mousey <= 590:
        print("hi")

    elif click[0] == 1:
        print("clicked submit")
        selec = True
        name = "hi"
        surname,= "hello"
        Nuser = "hiya"
        Nsecurity = "hellllo"
        return name,surname,Nuser,Nsecurity


        

        
    
    
    
