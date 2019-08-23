import pygame,sys
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 24)
walkRight=[pygame.image.load('Mario derecha/Mario 10.png'),pygame.image.load('Mario derecha\Mario 9.png'),pygame.image.load('Mario derecha\Mario 8.png'),pygame.image.load('Mario derecha\Mario 7.png'),pygame.image.load('Mario derecha\Mario 11.png'),pygame.image.load('Mario derecha\Mario 10.png')]
walkLeft=[pygame.image.load('Mario derecha\Mario 10.png'),pygame.image.load('Mario derecha\Mario 9.png'),pygame.image.load('Mario derecha\Mario 8.png'),pygame.image.load('Mario derecha\Mario 7.png'),pygame.image.load('Mario derecha\Mario 11.png'),pygame.image.load('Mario derecha\Mario 10.png')]
walkBack=[pygame.image.load('Mario frente\Mario 13.png'),pygame.image.load('Mario frente\Mario 14.png'),pygame.image.load('Mario frente\Mario 17.png'),pygame.image.load('Mario frente\Mario 15.png'),pygame.image.load('Mario frente\Mario 19.png'),pygame.image.load('Mario frente\Mario 13.png')]
walkFront=[pygame.image.load('Mario espalda\Mario 1.png'),pygame.image.load('Mario espalda\Mario 2.png'),pygame.image.load('Mario espalda\Mario 3.png'),pygame.image.load('Mario espalda\Mario 4.png'),pygame.image.load('Mario espalda\Mario 5.png'),pygame.image.load('Mario espalda\Mario 6.png')]


win = pygame.display.set_mode((32*20,32*15))
pygame.display.set_caption("Mario Bros")
clock = pygame.time.Clock()
ene = pygame.image.load('hola.png')
char = walkFront[1]
capi=pygame.image.load('gorro1.png')
k=0.1
k2=3
musica=pygame.mixer.music.load("songmario.mp3")
pygame.mixer.music.play(1, 0.0)

class fondo(object):
    def __init__(self,x,y,patronx,patrony,imagen):#self = fondo  patronx = 40, patrony = 150, 4736, 576 = 18 x 32
        self.patronx=patronx
        self.patrony=patrony
        self.x=x
        self.y=y
        self.velx=20*k*k2
        self.vely=135*k
        self.bg=pygame.image.load(imagen)
    def drawing(self,win):
        win.blit(self.bg,(self.x,self.y))

class player(object):
    def __init__(self,x,y,width,height):#self = mario
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velx = 18*k*k2
        self.vely = 13*k
        self.direction=[False, False,False,False,False]#Gorrito Derecha izquierda Arriba Abajo
        self.isJump = False
        self.jumpCount = 5
        self.walkCount = 0
        self.vidas=3
        self.comandantex=0
        self.comandantey=0
        self.collider=[self.x,self.y,self.x+self.width,self.y+self.height]#Derecha izquierda Arriba Abajo
        self.directionjump=-1
        self.status='vivito'
        
    def validate(self,k):
        self.direction[1]=False
        self.direction[2]=False
        self.direction[3]=False
        self.direction[4]=False
        if k<len(self.direction) and k>0:
            self.direction[k]=True
            global x
            x=k    
    def draw(self, win):
##        win.blit(char, (self.x,self.y))
        self.collider=[self.x,self.y,self.x+self.width,self.y+self.height]#Derecha izquierda Arriba Abajo
        if self.walkCount + 1 >= 18:
            self.walkCount = 0
        if self.direction[1]:
            win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        elif self.direction[4]:
            win.blit(walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount +=1
        elif self.direction[2]:
            win.blit(walkFront[self.walkCount//3], (self.x,self.y))
            self.walkCount +=1
        elif self.direction[3]:
            win.blit(walkBack[self.walkCount//3], (self.x,self.y))
            self.walkCount +=1
        else:win.blit(char, (self.x,self.y))        
class cap(object):
    def __init__(self,a,b,heigh,weigh): # self = gorro
        self.x=a
        self.y=b
        self.heigh=heigh
        self.weigh=weigh
        self.coun=0.05
        self.velx=10
        self.vely=10
        self.vel=5
        self.z=-1
        self.collider=[self.x,self.y,self.x+self.weigh,self.y+self.heigh]#Derecha izquierda Arriba Abajo


    def drew(self, win):
        win.blit(capi, (self.x,self.y))
        self.collider=[self.x,self.y,self.x+64,self.y+64]#Derecha izquierda Arriba Abajo
            
        
class plataforma(object):
    def __init__(self,a,b,heigh,weigh):#self=plataforma
         self.a=a
         self.b=b
         self.c=c
         self.heigh=heigh
         self.weigh=weigh    
         
    def brush(self,win):
        win.blit(pf, (self.a,self.b))
        
class enemy(object):
    def __init__(self,x,y,fin,width,height,vel,move,vidas):#self = enemigo
        self.x = (x*-1+20)*32
        self.y = (y*-1+15)*32
        self.restarx = (x*-1+20)*32
        self.restary = (y*-1+15)*32
        self.move=move
        if self.move == 1:
            self.ini = (fin*-1+20)*32
            self.fin=self.x
            self.rini = (fin*-1+20)*32
            self.rfin=self.x
        elif self.move==2:
            self.ini = (fin*-1+15)*32 #1=x, 2=y
            self.fin=self.y
            self.rini = (fin*-1+15)*32 #1=x, 2=y
            self.rfin=self.y
        self.move = move
        self.width = width
        self.height = height
        self.vel = vel
        self.status='nohit'
        self.direction=[False,False,False,False,False]#Nada Derecha izquierda Arriba Abajo
        self.walkCount = 0
        self.collider=[self.x,self.y,self.x+64,self.y+64]#Derecha izquierda Arriba Abajo
        self.vidas=vidas
        
    def drawn(self, win):
        win.blit(ene, (self.x,self.y))


    def movement (self):
        self.collider=[self.x,self.y,self.x+64,self.y+64]#Derecha izquierda Arriba Abajo
        if self.move==1:
            self.x+=1*self.vel
            if self.x>self.fin:self.move=-1
        elif self.move==-1:
            self.x-=1*self.vel
            if self.x<self.ini:self.move=1
        elif self.move==2:
            self.y+=1*self.vel
            if self.y>self.fin:self.move=-2
        elif self.move==-2:
            self.y-=1*self.vel
            if self.y<self.ini:self.move=2
    def fondo(self):
        if man.direction[1]:
            self.x += bg.velx
            if self.move==1 or self.move==-1:
                self.ini += bg.velx
                self.fin += bg.velx
        elif man.direction[4]:
            self.x -= bg.velx
            if self.move==1 or self.move==-1:
                self.ini -= bg.velx
                self.fin -= bg.velx
        elif man.direction[2]:
            self.y += bg.vely
            if self.move==2 or self.move==-2:
                self.ini += bg.vely
                self.fin += bg.vely
        elif man.direction[3]:
            self.y -= bg.vely
            if self.move==2 or self.move==-2:
                self.ini -= bg.vely
                self.fin -= bg.vely


            
def hit (name,a,b,weapon):
        if minihit(weapon.collider[a],name.collider[0], name.collider[2])=='hit':
            if minihit(weapon.collider[b],name.collider[1], name.collider[3])=='hit':
                return 'minimuerto'
def megahit(ene,weapon):
    if hit(ene,0,1,weapon)=='minimuerto':
        quitarvida(ene)
    elif hit(ene,2,1,weapon)=='minimuerto':
        quitarvida(ene)
    elif hit(ene,0,3,weapon)=='minimuerto':
        quitarvida(ene)
    elif hit(ene,2,3,weapon)=='minimuerto':
        quitarvida(ene)
        
def revive(ene,i=0):
    ene.x=576 #576 = 18 x 32
    ene.y=416
    bg.x=-640
    bg.y=-4320
    ene.comandantex=0
    ene.comandantey=0
    while i<len(Ldeenemigos):
        Ldeenemigos[i].x=Ldeenemigos[i].restarx
        Ldeenemigos[i].y=Ldeenemigos[i].restary
        Ldeenemigos[i].fin=Ldeenemigos[i].rfin
        Ldeenemigos[i].ini=Ldeenemigos[i].rini
        i+=1

def quitarvida(ene):
    ene.vidas-=1
    ene.status='hit'
                    
def minihit(a,x1,x2):
    if  a>x1 and a<x2:
        return "hit"
def enemigos (ene):
     ene.movement()
     megahit(man,ene)
     if ene.vidas!=0 and  keys[pygame.K_LSHIFT]:megahit(ene,gorro)
     ene.fondo()
        
def redrawGameWindow():
    bg.drawing(win)
    man.draw(win)#llama a la funcion draw para dibujar a mario
    gorro.drew(win)#dibujo el cap osea gorro lol
    i=0
    while i <len(Ldeenemigos):
        Ldeenemigos[i].drawn(win)
        i+=1

    textsurface = myfont.render(str(man.vidas), False, (255, 255, 255))
    win.blit(textsurface,(10,0))
    
    pygame.display.update()



#mainloop
bg=fondo(-640,-4320,40,150,'FONDO TILED.png')
man = player(576, 416,95,114)
gorro = cap(200,410,32,50)
Ldeenemigos=[enemy(3,7,7,34,34,6,1,1),enemy(2,19,12,64,64,5,1,1),enemy(13,29,35,34,34,5,2,1)]
#self,x,y,fin,width,height,vel,move,vidas
run = True
while run:
    clock.tick(18)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    if not keys[pygame.K_LSHIFT]:
        if keys[pygame.K_a] and  man.comandantex<38*32:
            man.x -= man.velx
            man.comandantex += man.velx+bg.velx
            bg.x += bg.velx
            man.validate(1)
        elif keys[pygame.K_d] and man.comandantex>0+32 :
            man.x += man.velx
            man.comandantex -= (man.velx+bg.velx)           
            bg.x -= bg.velx
            man.validate(4)
        elif keys[pygame.K_w] and  man.comandantey<148*32 :
            man.y -= man.vely
            man.comandantey += man.vely+bg.vely
            bg.y += bg.vely
            man.validate(2)
        elif keys[pygame.K_s]  and man.comandantey>0+32:
            man.y += man.vely
            man.comandantey-= (man.vely+bg.vely)
            bg.y -= bg.vely
            man.validate(3)
        else:
            man.validate(-1)
            man.walkCount = 0

    if keys[pygame.K_LSHIFT]:
        if x==4:
            gorro.x-=man.x*gorro.coun*-1
        elif x==1:
            gorro.x-=man.x*gorro.coun
        elif x==2:
            gorro.y-=man.y*gorro.coun*1
        elif x==3:
            gorro.y-=man.y*gorro.coun*-1

    else:
        gorro.x=man.x+25
        gorro.y=man.y-10
        
    

##    musicaSonando = not musicaSonando     
##    if not(man.isJump):
##        if keys[pygame.K_SPACE]:
##            man.isJump = True
##            man.right = False 
##            man.left = False 
##            man.walkCount = 0
##    else:
##        if man.jumpCount >= -5:
##            man.y -= (man.jumpCount * abs(man.jumpCount)) * 0.5
##            man.jumpCount -= 1
##        else: 
##            man.jumpCount = 5
##            man.isJump = False
    i=0
    while i<len(Ldeenemigos):
        enemigos(Ldeenemigos[i])
        if Ldeenemigos[i].vidas==0:lastdead=Ldeenemigos.pop(i)
        i+=1

    if man.status=='hit':
        revive(man)
        man.status='nohit'

    if man.vidas== 0 : run =False

    redrawGameWindow()

pygame.quit()
