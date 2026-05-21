import pygame,random
pygame.init()

#Constants
WIDTH=360
HEIGHT=440
PI=3.141592654

screen=pygame.display.set_mode((WIDTH,HEIGHT))
#Colours
EMERALD=(20, 255, 141)
BLUE=(0, 76, 207)
SKY=(145, 186, 255)
ORANGE=(255, 201, 92)
BLACK=(0)
WHITE=(255,255,255)
ORANGE=(255, 102, 0)
BROWN=(196, 120, 4)
LIME=(20, 255, 83)
SKIN=(240, 234, 132)
DARKBROWN=(79, 66, 41)
ONEBLUE=(0, 0,255)
TWOGREEN=(0,255,0)
THREERED=(255,0,0)
FOURPURPLE=(208, 0, 255)
FIVEYELLOW=(255, 255, 0)
SIXORANGE=(255, 183, 0)
SEVENGREY=(107, 107, 107)
EIGHTBLACK=(0)
#Variables
def variable():
    global isGameOver,firstClick,sizePF,sizeLB,isWin,hasStop,hasloopLose,startRGB,numLB,mineR,mineG,mineB
    isGameOver=False
    firstClick=True
    sizePF=40
    sizeLB=15
    isWin=False
    hasStop=False
    hasloopLose=False
    startRGB=40
    numLB=10
    mineR=0
    mineG=0
    mineB=0
variable()

#Initualize lists
def initLifeBouy():
    global listLifeBouy
    listLifeBouy=[]
    for i in range(9):
        listLifeBouy.append([])
        for j in range(9):
            listLifeBouy[i].append(False)
def initBoard():
    global boardList
    boardList=[]
    for i in range(9):
        boardList.append([])
        for j in range(9):
            boardList[i].append("E")

#Text
def text(message,size,colour,cord):
    font=pygame.font.Font(None,size)
    line=font.render(str(message),True,colour)
    screen.blit(line,cord)

#Draw board
def draw():
    global numLB
    for i in range(9):
        for j in range(9):
            if listLifeBouy[i][j]==True and "_"  in boardList[i][j]:
                listLifeBouy[i][j]=False
                numLB+=1
            if j%2==0:
                    if i%2!=0:
                        pygame.draw.rect(screen,SKY,(j*40,i*40+80,40,40))
                    if i%2==0:
                        pygame.draw.rect(screen,BLUE,(j*40,i*40+80,40,40))
            if j%2!=0:
                    if i%2==0:
                        pygame.draw.rect(screen,SKY,(j*40,i*40+80,40,40))
                    if i%2!=0:
                        pygame.draw.rect(screen,BLUE,(j*40,i*40+80,40,40))

            if "_" in boardList[i][j] and type(int(boardList[i][j][1]))==int:
                platform(sizePF,j*40,i*40+80)
                if int(boardList[i][j][1])!=0:
                    if int(boardList[i][j][1])==1:
                        text(boardList[i][j][1],50,ONEBLUE,(j*40+10,i*40+80+5))
                    if int(boardList[i][j][1])==2:
                        text(boardList[i][j][1],50,TWOGREEN,(j*40+10,i*40+80+5))
                    if int(boardList[i][j][1])==3:
                        text(boardList[i][j][1],50,THREERED,(j*40+10,i*40+80+5))
                    if int(boardList[i][j][1])==4:
                        text(boardList[i][j][1],50,FOURPURPLE,(j*40+10,i*40+80+5))
                    if int(boardList[i][j][1])==5:
                        text(boardList[i][j][1],50,FIVEYELLOW,(j*40+10,i*40+80+5))
                    if int(boardList[i][j][1])==6:
                        text(boardList[i][j][1],50,SIXORANGE,(j*40+10,i*40+80+5))
                    if int(boardList[i][j][1])==7:
                        text(boardList[i][j][1],50,SEVENGREY,(j*40+10,i*40+80+5))
                    if int(boardList[i][j][1])==8:
                        text(boardList[i][j][1],50,EIGHTBLACK,(j*40+10,i*40+80+5))
            if  listLifeBouy[i][j]==True and "_" not in boardList[i][j] :
                lifeBouy(sizeLB,(j*40+20,i*40+20+80),7)
         
#Draw objects   
def cross(x,y):
    pygame.draw.line(screen,THREERED,(x+5,y+5),(x+40-5,y+40-5),5)
    pygame.draw.line(screen,THREERED,(x+40-5,y+5),(x+5,y+40-5),5)   
def lifeBouy(size,cord,width):
    for i in range(4):
        pygame.draw.arc(screen,ORANGE,(cord[0]-size,cord[1]-size,2*size,2*size),i*PI/2,PI*i/2+PI/4,width)
        pygame.draw.arc(screen,WHITE,(cord[0]-size,cord[1]-size,2*size,2*size),i*PI/2+PI/4,(i+1)*PI/2,width)
def platform(size,x,y):
    pygame.draw.rect(screen,SKIN,(x,y,size,size),0)  
    pygame.draw.rect(screen,BROWN,(x,y,size,size),2)
    pygame.draw.rect(screen,DARKBROWN,(x+7,y+5,size/4,size/16),0)
    pygame.draw.rect(screen,DARKBROWN,(x+25,y+17,size/4,size/16),0)
    pygame.draw.rect(screen,DARKBROWN,(x+10,y+28,size/4,size/16),0)

#Random mine
def minesInit(firtMove):
    global boardList
    i=0
    while i<10:
        mineX=random.randint(0,8)
        mineY=random.randint(0,8)
        if boardList[mineY][mineX]=="M" or firtMove==(mineY,mineX):
            continue
        else:
            boardList[mineY][mineX]="M"
            i+=1

#Check empty space around
def checkEmpty():
    global boardList
    for k in range(9):
        for i in range(9):
            for j in range(9):
                
                if boardList[i][j]=="_0":
                    if i>0 and j>0:
                        if "_" not in boardList[i-1][j-1]:
                            boardList[i-1][j-1]="_"+boardList[i-1][j-1]
                    if i>0 and j>=0:
                        if "_" not in boardList[i-1][j]:
                            boardList[i-1][j]="_"+boardList[i-1][j]
                    if i>=0 and j>0:
                        if "_" not in boardList[i][j-1]:
                            boardList[i][j-1]="_"+boardList[i][j-1]
                    if i<8 and j<8:
                        if "_" not in boardList[i+1][j+1]:
                            boardList[i+1][j+1]="_"+boardList[i+1][j+1]
                    if i<8 and j<=8:
                        if "_" not in boardList[i+1][j]:
                            boardList[i+1][j]="_"+boardList[i+1][j]
                    if i<=8 and j<8:
                        if "_" not in boardList[i][j+1]:
                            boardList[i][j+1]="_"+boardList[i][j+1]
                    if i>0 and j<8:
                        if "_" not in boardList[i-1][j+1]:
                            boardList[i-1][j+1]="_"+boardList[i-1][j+1]
                    if i<8 and j>0:
                        if "_" not in boardList[i+1][j-1]:
                            boardList[i+1][j-1]="_"+boardList[i+1][j-1]

                elif "_" in boardList[i][j] and type(int(boardList[i][j][1]))==int and int(boardList[i][j][1])!=0:
                    
                    if i>0 and j>0:
                        if i>0 and j>0:
                            if boardList[i-1][j-1]=="0":
                                boardList[i-1][j-1]="_"+boardList[i-1][j-1]
                        if i>0 and j>=0:
                            if boardList[i-1][j]=="0":
                                boardList[i-1][j]="_"+boardList[i-1][j]
                        if i>=0 and j>0:
                            if boardList[i][j-1]=="0":
                                boardList[i][j-1]="_"+boardList[i][j-1]
                        if i<8 and j<8:
                            if boardList[i+1][j+1]=="0":
                                boardList[i+1][j+1]="_"+boardList[i+1][j+1]
                        if i<8 and j<=8:
                           if boardList[i+1][j]=="0":
                                boardList[i+1][j]="_"+boardList[i+1][j]
                        if i<=8 and j<8:
                            if boardList[i][j+1]=="0":
                                boardList[i][j+1]="_"+boardList[i][j+1]
                        if i>0 and j<8:
                            if boardList[i-1][j+1]=="0":
                                boardList[i-1][j+1]="_"+boardList[i-1][j+1]
                        if i<8 and j>0:
                            if boardList[i+1][j-1]=="0":
                                boardList[i+1][j-1]="_"+boardList[i+1][j-1]
                       
#Check mine around
def checkMine():
    global boardList
    for i in range(9):
        for j in range(9):
            mineCount=0
            
            if boardList[i][j]!="M":
                if i>0 and j>0:
                    if boardList[i-1][j-1]=="M":
                        mineCount+=1
                if i>0 and j>=0:
                    if boardList[i-1][j]=="M":
                        mineCount+=1
                if i>=0 and j>0:
                    if boardList[i][j-1]=="M":
                        mineCount+=1
                if i<8 and j<8:
                    if boardList[i+1][j+1]=="M":
                        mineCount+=1
                if i<8 and j<=8:
                    if boardList[i+1][j]=="M":
                        mineCount+=1
                if i<=8 and j<8:
                    if boardList[i][j+1]=="M":
                        mineCount+=1
                if i>0 and j<8:
                    if boardList[i-1][j+1]=="M":
                        mineCount+=1
                if i<8 and j>0:
                    if boardList[i+1][j-1]=="M":
                        mineCount+=1

                # print(mineCount,end=",")
                boardList[i][j]=str(mineCount)
        # print()

#Game Over
def checkWin():
    
    foundCount=0
    for i in range(9):
        for j in range(9):
            if "_" in boardList[i][j]:
                foundCount+=1
    
    if foundCount==71:
        return True 
def caseOver():
    global timeTaken,hasStop,stop
    
    pygame.draw.rect(screen,EMERALD,(0,0,WIDTH,40))
    if hasStop==False:
                stop=pygame.time.get_ticks()
                hasStop=True
    timeTaken=round(time(start,stop))
    if isWin==True:
            text("Victory",50,ORANGE,(WIDTH/2-60,0))
            ifWin()
    else:
            text("DEFEAT",50,SEVENGREY,(WIDTH/2-65,0))
            ifLose()
    text("Space to play again",50,(BLACK),(10,HEIGHT-40))
def ifLose():
    global hasloopLose,r,g,b
    if not hasloopLose:
                for i in range(9):
                    for j in range(9):
                        if boardList[i][j]=="M":
                            r,g,b=random.randint(startRGB,255),random.randint(startRGB,255),random.randint(startRGB,255)
                            pygame.draw.rect(screen,(r,g,b),(j*40,i*40+80,40,40))
                            pygame.draw.circle(screen,((r-startRGB),(g-startRGB),(b-startRGB)),(j*40+20,i*40+20+80),15,0)
                        else:
                            if listLifeBouy[i][j]==True:
                                cross(j*40,i*40+80)
                hasloopLose=True
def ifWin():
    global mineR,mineG,mineB,bestTime,timeTaken
    if bestTime=="--" or "" or int(bestTime)>timeTaken:
                file=open("bestTime.txt","w")
                file.write(str(timeTaken))
                file.close()
    file=open("bestTime.txt","r")
    bestTime=file.read()
    file.close()
    for i in range(9):
                    for j in range(9):
                        if boardList[i][j]=="M":
                            pygame.draw.rect(screen,(round(mineR),round(mineG),round(mineB)),(j*40,i*40+80,40,40))
                            
                            if mineR<255:
                                mineR+=0.05
                                mineG+=0.05
                                mineB+=0.05

#Display
def basicDisplay():
    global bestTime,timeTaken,stop,start
    if firstClick:
            start=0
            stop=0
    timeTaken=round(time(start,stop))
    stop=pygame.time.get_ticks()
        
    file=open("bestTime.txt","r")
    bestTime=file.read()
    file.close()
    text((f"{numLB}"),50,BLUE,(WIDTH/2-18*len(f"{numLB}"),4))
    lifeBouy(sizeLB,(WIDTH/2+20,sizeLB+5),7)
    text("Time: "+str(timeTaken)+"s",40,BLUE,(10,40))
    text("Best: "+str(bestTime)+"s",40,BLUE,(230,40))
    draw()

#Time
def time(start,stop):
    sec=(stop-start)/1000
    return sec
initBoard()
initLifeBouy()

#Events
def events():
    global firstClick,start,isGameOver,boardList,listLifeBouy,numLB
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE and isGameOver==True:
                variable()
                initBoard()
                initLifeBouy()
        if event.type==pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if firstClick:
                    posX,posY=pygame.mouse.get_pos()
                    gridX,gridY=posX//40,(posY-80)//40
                    minesInit((gridY,gridX))
                    checkMine()
                    checkEmpty()
                    firstClick=False
                    start=pygame.time.get_ticks()
                    # print(boardList)
                
                posX,posY=pygame.mouse.get_pos()
                gridX,gridY=posX//40,(posY-80)//40
                if boardList[gridY][gridX]=="M":
                    isGameOver=True
                    continue
                if "_" not in boardList[gridY][gridX]:
                    boardList[gridY][gridX]="_"+boardList[gridY][gridX]
                checkEmpty()
            if pygame.mouse.get_pressed()[2]:
                if firstClick:
                    pass
                else:
                    posX,posY=pygame.mouse.get_pos()
                    gridX,gridY=posX//40,(posY-80)//40
                    if listLifeBouy[gridY][gridX]==False:
                        listLifeBouy[gridY][gridX]=True
                        numLB-=1
                    else:
                        listLifeBouy[gridY][gridX]=False
                        numLB+=1
while True:    
    events()
    if isGameOver:
        caseOver()
        
    else:
        screen.fill(EMERALD)
        basicDisplay()
        
        
        if checkWin():
            isWin=True
            isGameOver=True
    
    pygame.display.update()