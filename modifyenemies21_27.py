##YOU'RE EDITING THIS ONE
import pygame,sys
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 24)
walkRight=[pygame.image.load('Mario derecha/Mario 10.png'),pygame.image.load('Mario derecha\Mario 9.png'),pygame.image.load('Mario derecha\Mario 8.png'),pygame.image.load('Mario derecha\Mario 7.png'),pygame.image.load('Mario derecha\Mario 11.png'),pygame.image.load('Mario derecha\Mario 10.png')]
standing=[pygame.image.load('Mario derecha/Mario 10.png'),pygame.image.load('Mario derecha\Mario 9.png'),pygame.image.load('Mario derecha\Mario 8.png'),pygame.image.load('Mario derecha\Mario 7.png'),pygame.image.load('Mario derecha\Mario 11.png'),pygame.image.load('Mario derecha\Mario 10.png')]
walkLeft=[pygame.image.load('Mario derecha\Mario 10.png'),pygame.image.load('Mario derecha\Mario 9.png'),pygame.image.load('Mario derecha\Mario 8.png'),pygame.image.load('Mario derecha\Mario 7.png'),pygame.image.load('Mario derecha\Mario 11.png'),pygame.image.load('Mario derecha\Mario 10.png')]
walkBack=[pygame.image.load('Mario frente\Mario 13.png'),pygame.image.load('Mario frente\Mario 14.png'),pygame.image.load('Mario frente\Mario 17.png'),pygame.image.load('Mario frente\Mario 15.png'),pygame.image.load('Mario frente\Mario 19.png'),pygame.image.load('Mario frente\Mario 13.png')]
walkFront=[pygame.image.load('Mario espalda\Mario 1.png'),pygame.image.load('Mario espalda\Mario 2.png'),pygame.image.load('Mario espalda\Mario 3.png'),pygame.image.load('Mario espalda\Mario 4.png'),pygame.image.load('Mario espalda\Mario 5.png'),pygame.image.load('Mario espalda\Mario 6.png')]
win = pygame.display.set_mode((32*20,32*15))
pygame.display.set_caption("Mario Bros")
clock = pygame.time.Clock()
char = walkFront[1]
capi=pygame.image.load('gorro1.png')
k=0.1
k2=3
musica=pygame.mixer.music.load("songmario.mp3")
pygame.mixer.music.play(1, 0.0)
#remplazaste fondo por nivel
class nivel(object):
    def __init__(self,patronx,patrony,imagen,obstacule,walls=[]):#self = fondo  patronx = 40, patrony = 150, 4736, 576 = 18 x 32
        self.patronx=patronx
        self.patrony=patrony
        self.walls=walls
        self.bg=pygame.image.load(imagen)
        self.obstacule=pygame.image.load(obstacule)
    def drawing(self,win):
        win.blit(self.bg,(0,0))

class Player(object):
    def __init__(self,x,y,width,height,actual=0):#self = mario
        self.rect = pygame.Rect(x,y,width,height)
        self.vel=5
        self.actual=actual
        self.status='nohit'
        self.direction=[False,False,False,False,False]#Standing Derecha izquierda Arriba Abajo
        self.walkCount = 0
        self.vidas=3
    def move(self, dx, dy):
        if dx != 0:self.move_single_axis(dx, 0)
        if dy != 0:self.move_single_axis(0, dy)
    def portal(self,dx,dy):
        if dx != 0:self.move_single(dx, 0)
        if dy != 0:self.move_single(0, dy)
    def move_single_axis(self, dx, dy):# Move the rect        
        self.rect.x += dx
        self.rect.y += dy
        # If you collide with a wall, move out based on velocity
        for wall in walls[self.actual]:
            if self.rect.colliderect(wall.rect):
                if dx > 0:self.rect.right = wall.rect.left# Moving right; Hit the left side of the wall
                if dx < 0:self.rect.left = wall.rect.right# Moving left; Hit the right side of the wall
                if dy > 0:self.rect.bottom = wall.rect.top# Moving down; Hit the top side of the wall
                if dy < 0:self.rect.top = wall.rect.bottom# Moving up; Hit the bottom side of the wall
    def move_single(self,dx,dy,x=0):
        for p in portal[self.actual]:
            if self.rect.colliderect(p.rect):
                self.actual=portalvalues[self.actual][x]
            x+=1
    def validate(self,k):
        self.direction[0]=False
        self.direction[1]=False
        self.direction[2]=False
        self.direction[3]=False
        self.direction[4]=False
        if k<len(self.direction) and k>=0:self.direction[k]=True
        else:self.direction[0]=True
           
    def draw(self, win):
####         win.blit(char, (self.rect.x,self.rect.y))
####         self.collider=[self.x,self.y,self.x+self.width,self.y+self.height]#Derecha izquierda Arriba Abajo
##        if self.walkCount + 1 >= 18:
##            self.walkCount = 0
##        if self.direction[1]:
##            win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
##        elif self.direction[4]:
##            win.blit(walkRight[self.walkCount//3], (self.x,self.y))
##        elif self.direction[2]:
##            win.blit(walkFront[self.walkCount//3], (self.x,self.y))
##        elif self.direction[3]:
##            win.blit(walkBack[self.walkCount//3], (self.x,self.y))
##        ##self.walkCount +=1
##        ##elif self.direction[0]:
##            win.blit(standing[self.walkCount//3], (self.x,self.y))
##        else:win.blit(char, (self.x,self.y))
class cap(object):
    def __init__(self,a,b,height,width,vel): # self = gorro
        self.rect = pygame.Rect(a,b,width,height)
        self.vel=vel
        #width, height
    def move(self, dx, dy):
        if dx != 0:self.move_single_axis(dx, 0)
        if dy != 0:self.move_single_axis(0, dy)
    def move_single_axis(self, dx, dy):# Move the rect        
        self.rect.x += dx
        self.rect.y += dy
        # If you collide with a wall, move out based on velocity
        for wall in walls[player.actual]:
            if self.rect.colliderect(wall.rect):
                if dx > 0:self.rect.right = wall.rect.left# Moving right; Hit the left side of the wall
                if dx < 0:self.rect.left = wall.rect.right# Moving left; Hit the right side of the wall
                if dy > 0:self.rect.bottom = wall.rect.top# Moving down; Hit the top side of the wall
                if dy < 0:self.rect.top = wall.rect.bottom# Moving up; Hit the bottom side of the wall

        
    def drew(self, win):
        win.blit(capi, (self.rect.x,self.rect.y))            
        
class enemy(object):
    def __init__(self,x,y,width,height,vel,moved,vidas,imagen):#self = enemigo
        self.rect=pygame.Rect(x,y,width,height)
        self.moved=moved
        self.vel = vel
        self.direction=[True,False,False,False,False]#Nada Derecha izquierda Arriba Abajo
        self.walkCount = 0
        self.vidas=vidas
        self.imagen=pygame.image.load(imagen)
        
    def drawn(self, win):
        win.blit(self.imagen, (self.rect.x,self.rect.y))
        
    def moven(self, dx, dy):
        if dx != 0:self.move_single_axis(dx, 0)
        if dy != 0:self.move_single_axis(0, dy)
    def move_single_axis(self, dx, dy):# Move the rect        
        self.rect.x += dx
        self.rect.y += dy
        for wall in walls[player.actual]:
            if self.rect.colliderect(wall.rect):
                if dx > 0:self.moved=1# Moving right; Hit the left side of the wall
                if dx < 0:self.moved=-1# Moving left; Hit the right side of the wall
                if dy > 0:self.moved=-2# Moving down; Hit the top side of the wall
                if dy < 0:self.moved=2# Moving up; Hit the bottom side of the wall            
    def movement (self):
        if self.moved==-1:self.moven(1*self.vel, 0)
        elif self.moved==1:self.moven(-1*self.vel, 0)
        elif self.moved==-2:self.moven(0,-1*self.vel)
        elif self.moved==2:self.moven(0,1*self.vel)

        
def revive(ene,i=0):
    ene.x=576 #576 = 18 x 32
    ene.y=416
    bg.x=-640
    bg.y=-4320
    ene.comandantex=0
    ene.comandantey=0

def quitarvida(ene):
    ene.vidas-=1
    ene.status='hit'


def redrawGameWindow():
    bg.drawing(win)
    player.draw(win)#llama a la funcion draw para dibujar a mario
    gorro.drew(win)#dibujo el cap osea gorro lol
    textsurface = myfont.render(str(player.vidas), False, (255, 255, 255))
    win.blit(textsurface,(10,0))
    for wall in walls[player.actual]:##CAMBIAR por mapa actual
        win.blit(bg.obstacule,wall.rect)
        #pygame.draw.rect(win, (255, 255, 255), wall.rect)#las dibuja
    for wall in portal[player.actual]:##CAMBIAR por mapa actual
        pygame.draw.rect(win, (255, 0, 0), wall.rect)
    if ene[player.actual].direction[0]:ene[player.actual].drawn(win)
    pygame.display.update()



#mainloop
bg=nivel(20,15,'Tierra.png','Arbustomario.png')##(self,patronx,patrony,imagen,walls=[])
player = Player(128,64,64,64)##(self,x,y,width,height,actual=0)
gorro = cap(200,410,32,32,5)##(self,a,b,height,width,vel)
ene=[enemy(32,64,64,64,2,-2,3,'hola.jpg'),enemy(128,64,64,64,4,-1,3,'hola.jpg')]##(self,x,y,fin,width,height,vel,moved,vidas,imagen)
walls = []
level = [[
"WWWWWWWWWWWWWWWWWWWW","WWWWWWWWWWWWWWWWWWWW",
"W  1             M  ","                 WWW",
"W         WWWWWW    ","     2  WWWWWW   WWW",
"W   WWWW       W    ","  WWWW       W   WWW",
"W   W        WWWW   ","  W        WWWW  WWW",
"W WWW  WWWW         ","WWW  WWWW        WWW",
"W   W     W W       ","  W     W W      WWW",
"W   W     W   WWW W ","  W     W   WWW WWWW",
"W   WWW WWW   W W   ","  WWW WWW   W W  WWW",
"W     W   W   W W   ","    W   W   W W  WWW"],[
"WWW   W   WWWWW W  W","W   W   WWWWW W  WWW",
"W W      WW         ","W      WW        WWW",
"W W   WWWW   WWW    ","W   WWWW   WWW   WWW",
"W     W        W    ","    W        W   WWW",
"W                   ","                 WWW",
"W                   ","                 WWW",
"W                   ","                 WWW",
"W         WWWWWW    ","        WWWWWW   WWW",
"W   WWWW       W    ","  WWWW       W   WWW",
"W   W        WWWW   ","  W        WWWW  WWW"],[
"W WWW  WWWW         ","WWW  WWWW        WWW",
"W   W     W W       ","  W     W W      WWW",
"W   W     W   WWW W ","  W     W   WWW WWWW",
"W   WWW WWW   W W   ","  WWW WWW   W W  WWW",
"W     W   W   W W   ","    W   W   W W  WWW",
"WWW   W   WWWWW W  W","W   W   WWWWW W  WWW",
"W W      WW         ","W      WW        WWW",
"W W   WWWW   WWW    ","W   WWWW   WWW   WWW",
"W     W        W    ","    W        W   WWW",
"WWWWWWWWWWWWWWWWWWWW","WWWWWWWWWWWWWWWWWWWW"]
]
portal=[]
portalvalues=[]
#portalvalues=[[1,2], [], []]#llenar manualmente
mstartpoints=[]#llenar manualmente
#for food in level:portalvalues.append([])
for food in level:
    walls.append([])
    portal.append([])
    portalvalues.append([])
    mstartpoints.append([])
class Wall(object):
    def __init__(self, pos,position,walls,col=-1,another=[]):
        walls[position].append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
        if col!=-1:
            portalvalues[position].append(int(col))
        elif len(another)>0:
            mstartpoints[position].remove(self)
            mstartpoints[position].append(another)
            print(mstartpoints[position])


liststrnumeros=[]
for numer in range(len(level)):liststrnumeros.append(str(numer))
def actualmaze(independent,m,x=0,y=0):
    for row in independent:#Pasa por todas as posiciones para crear una lista de walls
        for col in row:
            if col == "W":
                Wall((x, y),m,walls)
            elif liststrnumeros.count(col)>0:
                Wall((x, y),m,portal,col)
            elif col=="M":
                Wall((x, y),m,mstartpoints,-1,[y//32,x//32])
##            elif col==' ':print('buu')#no hace nada ni debe hacer algo
##            else:
##                print('listo para crear obstáculos')
            x += 32
        y += 32
        x = 0
m=0            
for independent in level:
    actualmaze(independent,m)
    m+=1

run = True
while run:#AQUÍ
    clock.tick(18)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    
    if not keys[pygame.K_LSHIFT]:
        if keys[pygame.K_LEFT]:
            player.move(-1*player.vel, 0)
            player.portal(-1*player.vel, 0)
            player.validate(1)
            
        if keys[pygame.K_RIGHT]:
            player.move(1*player.vel, 0)
            player.portal(1*player.vel, 0)
            player.validate(4)
            
        if keys[pygame.K_UP]:
            player.move(0, -1*player.vel)
            player.portal(0, -1*player.vel)
            player.validate(2)
            
        if keys[pygame.K_DOWN]:
            player.move(0, 1*player.vel)
            player.portal(0, 1*player.vel)
            player.validate(3)

        else:
            #player.validate(-1)
            player.walkCount = 0

    if keys[pygame.K_LSHIFT]:
        x=player.direction.index(True)
        if x==4:
            gorro.move(gorro.vel, 0)
        elif x==1:
            gorro.move(-1*gorro.vel, 0)
        elif x==2:
            gorro.move(0,-1*gorro.vel)
        elif x==3:
            gorro.move(0,1*gorro.vel)
    else:
        gorro.rect.x=player.rect.x
        gorro.rect.y=player.rect.y
        

##    musicaSonando = not musicaSonando     

    if player.status=='hit':
        revive(man)
        player.status='nohit'

    if player.vidas== 0 : run =False
    ##AQUÍ
    ene[player.actual].movement()
    redrawGameWindow()

pygame.quit()
