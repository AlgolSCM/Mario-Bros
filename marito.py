##matar al enemigo (eliminar el elemento de la clase)
import pygame,sys
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 15)


win = pygame.display.set_mode((32*20,32*15))
pygame.display.set_caption("Mario Bros")

##walkRight=[pygame.image.load('l0_hambur04.png'),pygame.image.load('l0_hambur01.png'),pygame.image.load('l0_hambur02.png'),pygame.image.load('l0_hambur03.png')]
##walkLeft=[pygame.image.load('l0_hambur08.png'),pygame.image.load('l0_hambur05.png'),pygame.image.load('l0_hambur06.png'),pygame.image.load('l0_hambur07.png')]
##walkFront=[pygame.image.load('l0_hambur12.png'),pygame.image.load('l0_hambur09.png'),pygame.image.load('l0_hambur10.png'),pygame.image.load('l0_hambur11.png')]
##walkBack=[pygame.image.load('l0_hambur16.png'),pygame.image.load('l0_hambur13.png'),pygame.image.load('l0_hambur14.png'),pygame.image.load('l0_hambur15.png')]
clock = pygame.time.Clock()
ene = pygame.image.load('hola.jpg')
bg = pygame.image.load('FONDO TILED.png')
char = pygame.image.load('marito.jpg')
capi=pygame.image.load('gorro.jpg')
x=0

class player(object):
    def __init__(self,x,y,width,height):#self = mario
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 15
        self.direction=[False, False,False,False,False]#Gorrito Derecha izquierda Arriba Abajo
        self.isJump = False
        self.jumpCount = 10
        self.walkCount = 0
        self.vida=3
        self.revivex=x
        self.revivey=y
        self.collider=[self.x,self.y,self.x+self.width,self.y+self.height]#Derecha izquierda Arriba Abajo
        self.directionjump=-1
        self.status='vivito'
        self.z=100
        
    def validate(self,k):
        self.direction[1]=False
        self.direction[2]=False
        self.direction[3]=False
        self.direction[4]=False
        if k<len(self.direction) and k>0:
            self.direction[k]=True
            global x
            x=k
            ##pone verdadero a la direccion que apunta
    
    def draw(self, win):
        win.blit(char, (self.x,self.y))
        self.collider=[self.x,self.y,self.x+self.width,self.y+self.height]#Derecha izquierda Arriba Abajo
       
##        if self.walkCount + 1 >= 12:
##            self.walkCount = 0
##        if self.direction[1]:
##            win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
##            self.walkCount += 1
##        elif self.direction[4]:
##            win.blit(walkRight[self.walkCount//3], (self.x,self.y))
##            self.walkCount +=1
##        elif self.direction[2]:
##            win.blit(walkFront[self.walkCount//3], (self.x,self.y))
##            self.walkCount +=1
##        elif self.direction[3]:
##            win.blit(walkBack[self.walkCount//3], (self.x,self.y))
##            self.walkCount +=1
##        else:win.blit(char, (self.x,self.y))
            
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
    def __init__(self,x,y,width,height,vel,fin,move):#self = enemigo
        self.x = x
        self.y = y
        if move == 1:
            self.fin = fin*32+self.x
            self.ini=x
        elif move==2:
            self.fin = fin*32+self.y #1=x, 2=y
            self.ini=y
        self.move = move
        self.width = width
        self.height = height
        self.vel = vel
        self.direction=[False,False,False,False,False]#Nada Derecha izquierda Arriba Abajo
        self.walkCount = 0
        self.collider=[self.x,self.y,self.x+64,self.y+64]#Derecha izquierda Arriba Abajo
        self.status='vivito y coleando'
    def drawn(self, win):
        if self.status=='vivito y coleando':win.blit(ene, (self.x,self.y))


    def movement (self):
        self.collider=[self.x,self.y,self.x+64,self.y+64]#Derecha izquierda Arriba Abajo

        if self.move==1:
            self.x+=1*self.vel
            if self.x>self.fin:
                self.move=-1
        elif self.move==-1:
            self.x-=1*self.vel
            if self.x<self.ini:
                self.move=1
        elif self.move==2:
            self.y+=1*self.vel
            if self.y>self.fin:
                self.move=-2
        elif self.move==-2:
            self.y-=1*self.vel
            if self.y<self.ini:
                self.move=2
        
def hit (name,a,b,weapon):
        if minihit(weapon.collider[a],name.collider[0], name.collider[2])=='hit':
            if minihit(weapon.collider[b],name.collider[1], name.collider[3])=='hit':
                return 'minimuerto'
def megahit(ene,weapon):
    if hit(ene,0,1,weapon)=='minimuerto':ene.status='muerto'
    elif hit(ene,2,1,weapon)=='minimuerto':ene.status='muerto'
    elif hit(ene,0,3,weapon)=='minimuerto':ene.status='muerto'
    elif hit(ene,2,3,weapon)=='minimuerto':ene.status='muerto'
                
def minihit(a,x1,x2):
    if  a>x1 and a<x2:
        return "hit"
def enemigos (ene):
     ene.movement()
     megahit(man,ene)
     if ene.status=='vivito y coleando'and  keys[pygame.K_LSHIFT]:megahit(ene,gorro)

        
def redrawGameWindow():
    win.blit(bg,(-0*32,32*-135))# fondo
    man.draw(win)#llama a la funcion draw para dibujar a mario
    gorro.drew(win)#dibujo el cap osea gorro lol
    i=0
    while i <len(Ldeenemigos):
        Ldeenemigos[i].drawn(win)
        i+=1

    textsurface = myfont.render(str(man.vida), False, (0, 0, 0))
    win.blit(textsurface,(0,0))
    pygame.display.update()



#mainloop
man = player(200, 410, 64,64)
gorro = cap(200,410,32,32)
Ldeenemigos=[enemy(64,64,64,64,10,5,1), enemy(80,64,64,64,10,5,2)]
run = True
while run:
    clock.tick(12)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if not keys[pygame.K_LSHIFT]:
        if keys[pygame.K_a] and man.x > man.vel:
            man.x -= man.vel
            man.validate(1)
        elif keys[pygame.K_d] and man.x < 640 - man.width - man.vel:
            man.x += man.vel
            man.validate(4)
        elif keys[pygame.K_w] and man.y > 0:
            man.y -= man.vel
            man.validate(2)
        elif keys[pygame.K_s] and man.y < 460 - man.height - man.vel:
            man.y += man.vel
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
        gorro.x=man.x
        gorro.y=man.y
        
    if not(man.isJump):
        if keys[pygame.K_SPACE]:
            man.isJump = True
            man.right = False 
            man.left = False 
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            man.y -= (man.jumpCount * abs(man.jumpCount)) * 0.5
            man.jumpCount -= 1
        else: 
            man.jumpCount = 10
            man.isJump = False
    i=0
    while i<len(Ldeenemigos):
        enemigos(Ldeenemigos[i])
        i+=1

    if man.status=='muerto':
        man.vida=man.vida-1
        man.status='vivito y coleando'
        man.x=man.revivex
        man.y=man.revivey

    if man.vida== 0 : run =False

    redrawGameWindow()

pygame.quit()
