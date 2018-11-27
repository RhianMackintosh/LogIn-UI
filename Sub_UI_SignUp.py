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

    button(StartColourD,260,40,310,80,"Sign Up",big,310,55)
    button(StartColour,250,30,310,80,"Sign Up",big,310,45)

    #name button
    button(StartColour,160,180,180,40,"First Name",small,170,185)
    button(white,350,180,270,40,"",small,170,185)

    #surname button
    button(StartColour,160,275,180,40,"Last Name",small,170,280)
    button(white,350,275,270,40,"",small,170,280)

    #username button
    button(StartColour,160,375,180,40,"Username",small,170,380)
    button(white,350,375,270,40,"",small,170,380)

    #upassword button
    button(StartColour,160,475,180,40,"Password",small,170,480)
    button(white,350,475,270,40,"",small,170,480)

    #password check button
    button(StartColour,160,575,180,40,"Confirm",small,170,580)
    button(white,350,575,270,40,"",small,170,580)

    #security question button
    button(backGC,60,685,180,10,"Security Question: What is your mothers maiden name",tiny,120,685)
    button(StartColour,160,720,180,40,"Answer",small,190,725)
    button(white,350,720,270,40,"",small,170,725)

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


        

        
    
    
    
