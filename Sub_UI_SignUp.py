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
    typeFirst = ""
    typeLast = ""
    typeUser = ""
    typePass = ""
    typeConfirm = ""
    typeAnswer = ""
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
    
    pygame.mouse.set_pos([0,0])
    
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

        if mousex >= 350 and mousex <= 620 and mousey >= 180 and mousey <= 220:
            button(StartColourD,140,170,500,60,"",small,170,185)
            button(StartColour,160,180,180,40,"First Name",small,170,185)
            button(white,350,180,270,40,"",small,170,185)
            button(white,350,180,270,40,typeFirst,small,360,185)
            pygame.display.update()

            finished = False
            
            while finished == False: 
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.unicode.isalpha():
                            typeFirst += event.unicode
                        elif event.unicode.isdigit():
                            typeFirst += event.unicode
                        elif event.key == pygame.K_BACKSPACE:
                            typeFirst = typeUser[:-1]
                        elif event.key == pygame.K_RETURN:
                            finished = True
                            pygame.mouse.set_pos([0,0])
                            
                    print(typeFirst)
                    button(white,350,180,270,40,typeFirst,small,360,185)
                    pygame.display.update()
            
        elif mousex >= 350 and mousex <= 620 and mousey >= 275 and mousey <= 315:
            button(StartColourD,140,265,500,60,"",small,170,280)
            button(StartColour,160,275,180,40,"Last Name",small,170,280)
            button(white,350,275,270,40,"",small,170,280)
            button(white,350,275,270,40,typeLast,small,360,280)
            pygame.display.update()

            finished = False
            
            while finished == False: 
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.unicode.isalpha():
                            typeLast += event.unicode
                        elif event.unicode.isdigit():
                            typeLast += event.unicode
                        elif event.key == pygame.K_BACKSPACE:
                            typeLast = typeUser[:-1]
                        elif event.key == pygame.K_RETURN:
                            finished = True
                            pygame.mouse.set_pos([0,0])
                            
                    print(typeLast)
                    button(white,350,275,270,40,typeLast,small,360,280)
                    pygame.display.update()

        elif mousex >= 350 and mousex <= 620 and mousey >= 375 and mousey <= 415:
            button(StartColourD,140,365,500,60,"",small,170,280)
            button(StartColour,160,375,180,40,"Username",small,170,380)
            button(white,350,375,270,40,"",small,170,380)
            button(white,350,375,270,40,typeUser,small,360,380)
            pygame.display.update()

            finished = False
            
            while finished == False: 
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.unicode.isalpha():
                            typeUser += event.unicode
                        elif event.unicode.isdigit():
                            typeUser+= event.unicode
                        elif event.key == pygame.K_BACKSPACE:
                            typeUser = typeUser[:-1]
                        elif event.key == pygame.K_RETURN:
                            finished = True
                            pygame.mouse.set_pos([0,0])
                            
                    print(typeUser)
                    button(white,350,375,270,40,typeUser,small,360,380)
                    pygame.display.update()

        elif mousex >= 350 and mousex <= 620 and mousey >= 475 and mousey <= 515:
            button(StartColourD,140,465,500,60,"",small,170,280)
            button(StartColour,160,475,180,40,"Password",small,170,480)
            button(white,350,475,270,40,"",small,170,480)
            button(white,350,475,270,40,typePass,small,360,480)
            pygame.display.update()

            finished = False
            
            while finished == False: 
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.unicode.isalpha():
                            typePass += event.unicode
                        elif event.unicode.isdigit():
                            typePass += event.unicode
                        elif event.key == pygame.K_BACKSPACE:
                            typePass = typeUser[:-1]
                        elif event.key == pygame.K_RETURN:
                            finished = True
                            pygame.mouse.set_pos([0,0])
                            
                    print(typePass)
                    button(white,350,475,270,40,typePass,small,360,480)
                    pygame.display.update()

        elif mousex >= 350 and mousex <= 620 and mousey >= 575 and mousey <= 615:
            button(StartColourD,140,565,500,60,"",small,170,280)
            button(StartColour,160,575,180,40,"Confirm",small,170,580)
            button(white,350,575,270,40,"",small,170,580)
            button(white,350,575,270,40,typePass,small,360,385)
            pygame.display.update()

            finished = False
            
            while finished == False: 
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.unicode.isalpha():
                            typeConfirm += event.unicode
                        elif event.unicode.isdigit():
                            typeConfirm += event.unicode
                        elif event.key == pygame.K_BACKSPACE:
                            typeConfirm = typeUser[:-1]
                        elif event.key == pygame.K_RETURN:
                            finished = True
                            pygame.mouse.set_pos([0,0])
                            
                    print(typeConfirm)
                    button(white,350,575,270,40,typeConfirm,small,360,580)
                    pygame.display.update()

        elif mousex >= 350 and mousex <= 620 and mousey >= 720 and mousey <= 760:
            button(StartColourD,140,710,500,60,"",small,170,280)
            button(StartColour,160,720,180,40,"Answer",small,190,725)
            button(white,350,720,270,40,"",small,170,725)
            button(white,350,720,270,40,typeAnswer,small,360,725)
            pygame.display.update()

            finished = False
            
            while finished == False: 
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.unicode.isalpha():
                            typeAnswer += event.unicode
                        elif event.unicode.isdigit():
                            typeAnswer += event.unicode
                        elif event.key == pygame.K_BACKSPACE:
                            typeAnswer = typeUser[:-1]
                        elif event.key == pygame.K_RETURN:
                            finished = True
                            pygame.mouse.set_pos([0,0])
                            
                    print(typeAnswer)
                    button(white,350,720,270,40,typeAnswer,small,360,725)
                    pygame.display.update()
            

        else:
            button(backGC,130,150,520,650,"",small,0,0)
            
            #title button
            button(StartColourD,260,40,310,80,"Sign Up",big,310,55)
            button(StartColour,250,30,310,80,"Sign Up",big,310,45)

            #name button
            button(StartColour,160,180,180,40,"First Name",small,170,185)
            button(white,350,180,270,40,typeFirst,small,360,185)

            #surname button
            button(StartColour,160,275,180,40,"Last Name",small,170,280)
            button(white,350,275,270,40,typeLast,small,360,280)

            #username button
            button(StartColour,160,375,180,40,"Username",small,170,380)
            button(white,350,375,270,40,typeUser,small,360,380)

            #upassword button
            button(StartColour,160,475,180,40,"Password",small,170,480)
            button(white,350,475,270,40,typePass,small,360,480)

            #password check button
            button(StartColour,160,575,180,40,"Confirm",small,170,580)
            button(white,350,575,270,40,typeConfirm,small,360,580)

            #security question button
            button(backGC,60,685,180,10,"Security Question: What is your mothers maiden name",tiny,120,685)
            button(StartColour,160,720,180,40,"Answer",small,190,725)
            button(white,350,720,270,40,typeAnswer,small,360,725)

            pygame.display.update()
            


        

        
    
    
    
