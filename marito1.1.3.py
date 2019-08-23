import pygame,sys
import random
import os
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 24)
walkRight=[pygame.image.load('Mario derecha/Mario 10.png'),pygame.image.load('Mario derecha\Mario 9.png'),pygame.image.load('Mario derecha\Mario 8.png'),pygame.image.load('Mario derecha\Mario 7.png'),pygame.image.load('Mario derecha\Mario 11.png'),pygame.image.load('Mario derecha\Mario 10.png')]
walkLeft=[pygame.image.load('Mario derecha\Mario 10.png'),pygame.image.load('Mario derecha\Mario 9.png'),pygame.image.load('Mario derecha\Mario 8.png'),pygame.image.load('Mario derecha\Mario 7.png'),pygame.image.load('Mario derecha\Mario 11.png'),pygame.image.load('Mario derecha\Mario 10.png')]
walkBack=[pygame.image.load('Mario frente\Mario 13.png'),pygame.image.load('Mario frente\Mario 14.png'),pygame.image.load('Mario frente\Mario 17.png'),pygame.image.load('Mario frente\Mario 15.png'),pygame.image.load('Mario frente\Mario 19.png'),pygame.image.load('Mario frente\Mario 13.png')]
walkFront=[pygame.image.load('Mario espalda\Mario 1.png'),pygame.image.load('Mario espalda\Mario 2.png'),pygame.image.load('Mario espalda\Mario 3.png'),pygame.image.load('Mario espalda\Mario 4.png'),pygame.image.load('Mario espalda\Mario 5.png'),pygame.image.load('Mario espalda\Mario 6.png')]

arbusto=pygame.image.load('Arbustomario.png')
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


total=['W            W W W W W W W W W W W W W W W W W  W W W W W W W W W W W W W W W W', 'W                       W           W                                         W', 'W                       W           W                                         W', 'W                       W                                                     W', 'W                       W                                                     W', 'W             W         W                                           W         W', 'W             W         W                                           W         W', 'W             W       W W W W W W W W         W W W W W W W W W W W W         W', 'W             W       W W                     W                               W', 'W             W                               W                               W', 'W             W                               W                               W', 'W             W                               W         W W W W W W           W', 'W             W W W W W W W W W W             W         W         W           W', 'W                               W         W W W         W         W           W', 'W                               W             W         W                     W', 'W                               W             W         W                     W', 'W                               W             W         W                     W', 'W W W W W W W W W W W W         W             W         W                     W', 'W         W           W         W             W         W         W           W', 'W         W           W         W             W         W         W           W', 'W         W           W         W W W W W W W W         W         W           W', 'W         W           W                                 W         W           W', 'W         W           W                                 W         W           W', 'W         W           W                                 W         W           W', 'W         W           W                                 W         W           W', 'W         W           W W W W W W W W W W W W W W W W W W         W           W', 'W         W           W                                           W           W', 'W         W           W                                           W           W', 'W         W           W                                           W           W', 'W         W           W                                           W           W', 'W         W           W         W         W W W W W W W W         W           W', 'W         W           W         W         W             W         W           W', 'W         W           W         W         W             W         W           W', 'W         W                     W         W             W                     W', 'W         W                     W         W             W                     W', 'W         W                     W         W             W                     W', 'W         W                     W         W             W                     W', 'W         W W W W W W W W W W W W         W         W W W                     W', 'W                   W                     W                       W           W', 'W                   W                     W                       W           W', 'W                   W                     W                       W           W', 'W                   W                     W                       W           W', 'W W W W W W         W W W W W W W W W W W W W W W W W W W W W W W W           W', 'W         W         W         W         W                         W           W', 'W         W         W         W         W                         W           W', 'W         W         W         W         W                         W           W', 'W         W         W         W         W                         W           W', 'W         W         W         W         W         W W W W W W W W W           W', 'W         W         W         W         W         W               W           W', 'W         W         W         W         W         W               W           W', 'W         W         W         W         W         W               W           W', 'W         W         W         W         W         W               W           W', 'W                   W         W         W         W         W W W W           W', 'W                   W         W         W         W         W                 W', 'W                   W         W         W         W         W                 W', 'W                   W         W         W         W         W                 W', 'W         W W W W W W         W         W         W         W                 W', 'W                             W         W         W         W                 W', 'W                             W         W         W         W         W W W W W', 'W                             W         W         W         W         W       W', 'W                                                           W         W       W', 'W         W         W                                       W         W       W', 'W         W         W                                       W         W       W', 'W         W         W                                       W         W       W', 'W         W         W W W W W W W W W W W W W W W W W W W W W         W       W', 'W         W                                                           W       W', 'W         W                                                           W       W', 'W         W                                                           W       W', 'W         W                                                           W       W', 'W         W W W W W W W                                               W       W', 'W                     W         W W W W W W W W W W W W W W W W W W W W       W', 'W                     W                   W                                   W', 'W                     W                   W                                   W', 'W                     W                   W                                   W', 'W           W         W                   W                                   W', 'W           W         W         W         W         W         W W W W         W', 'W           W         W         W         W         W               W         W', 'W           W         W         W                   W               W         W', 'W           W         W         W                   W               W         W', 'W           W         W         W                   W               W         W', 'W           W         W         W                   W               W         W', 'W           W         W         W W W W W W W W W W W W W W         W         W', 'W           W         W                                                       W', 'W           W         W                                                       W', 'W           W         W                                                       W', 'W                     W                                                       W', 'W                     W W W W W W W W W W W W W W W W W W W W W W W           W', 'W                                                                 W           W', 'W                                                                 W           W', 'W       W W W                                                     W           W', 'W           W                                                     W           W', 'W           W         W W W W W W W W W W W W W W W W W W         W           W', 'W           W                                           W         W           W', 'W           W                                           W         W           W', 'W           W                                           W         W           W', 'W           W                                           W         W           W', 'W           W W W W W W W W W W W W W W W W W W         W         W           W', 'W                                             W         W         W           W', 'W                                             W         W         W           W', 'W                                             W         W         W           W', 'W                                             W         W         W           W', 'W W W W W W W         W W W         W         W         W         W           W', 'W           W         W             W         W         W         W           W', 'W           W                       W         W         W         W           W', 'W           W                       W         W         W         W           W', 'W           W                       W         W         W         W           W', 'W           W                       W         W         W         W           W', 'W           W             W W W W W W         W         W         W           W', 'W                                             W         W         W           W', 'W                                             W         W         W           W', 'W                                             W         W         W           W', 'W                         W W W W W W W W W W W         W         W           W', 'W         W W W                   W                     W                     W', 'W             W                   W                     W                     W', 'W             W                   W                     W                     W', 'W             W W W W W W W W     W                     W                     W', 'W             W           W       W         W           W W W W W W W W W W W W', 'W         W W W           W       W         W           W           W         W', 'W             W           W       W         W           W           W         W', 'W             W                   W         W           W           W         W', 'W             W                   W         W           W           W         W', 'W             W         W W W W W W         W         W W           W         W', 'W             W                   W         W                                 W', 'W             W                   W         W                                 W', 'W             W                   W         W                                 W', 'W             W                   W         W                                 W', 'W             W W W W W W         W W W W W W W W W W W W W W W W W           W', 'W             W                   W                     W                     W', 'W             W                   W                     W                     W', 'W             W                   W                     W                   W W', 'W             W                   W                                           W', 'W W W W W W W W W W W W W         W         W                                 W', 'W         W                                 W                                 W', 'W         W                                 W                                 W', 'W         W                                 W W W W W W W W W W W W W W W W W W', 'W         W                                       W                           W', 'W         W                                       W                           W', 'W         W         W W W W W W                   W                           W', 'W         W         W         W                   W                           W', 'W         W         W         W         W         W         W W W W W         W', 'W         W         W         W         W         W         W                 W', 'W         W         W         W         W         W         W                 W', 'W         W         W         W         W         W         W                 W', 'W         W         W         W         W         W         W                 W', 'W         W         W         W         W         W         W                 W', 'W         W         W         W         W         W         W                 W', 'W                   W                   W                   W                 W', 'W                   W                   W                   W                 W', 'W                   W                   W                   W                 W', 'W                   W                   W                   W                 W']
walls = [] # List to hold the walls

# Nice class to hold a wall rect
class Wall(object):
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
        
##file= open ('FONDITO 2.txt', 'r')
##i=0
##for line in file:
##    currentline=line.split(",")
##    total.append(currentline)
##    i+=1
##file.close()
##print(total)

# Parse the level string above. W = wall, E = exit
x = y = 0
for row in total:
    for col in row:
        if col == "W":
            Wall((x, y))
        x += 16
    y += 32
    x = 0


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
        self.rect = pygame.Rect(self.x, self.y, self.width,self.height)  #crea un rectángulo alrededor de Mario
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
    def move(self, dx, dy):
        if self.move_single_axis(dx,dy)!='hit':
            self.rect = pygame.Rect(self.x, self.y, self.width,self.height)
            # Move each axis separately. Note that this checks for collisions both times.
            if dx != 0:
                self.move_single_axis(dx, 0)
            if dy != 0:
                self.move_single_axis(0, dy)
    
    def move_single_axis(self, dx, dy):
        
        # Move the rect
        self.x += dx
        self.y += dy
        # If you collide with a wall, move out based on velocity
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                    return 'hit'
                if dx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                    return 'hit'
                if dy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                    return 'hit'
                if dy < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom
                    return 'hit'
        
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
     megahit(man.rect,ene)
     if ene.vidas!=0 and  keys[pygame.K_LSHIFT]:megahit(ene,gorro)
     ene.fondo()

class obstaculo(object):
    def __init__(self,tipo,vida,imagen):
        self.tipo = tipo
        self.poder = poder
        self.usos = 10
        self.image = pygame.image.load(imagen)
    #al igual que herramientas se lleva la cuenta en una lista con una lista de [x,y] y una lista que tenga cada tipo      
class tools(object):
    #imagen,tipo(contra que es valido)1,2,3,4,poder(1,2 tiempo que se demora representado por rectangulo que se llena),
    #usos(05), precio,bloqueado o desbloqueado
    def __init__(self,tipo,poder,imagen,precio,cantidad=0):
        self.tipo = tipo
        self.poder = poder
        self.usos = 10*cantidad
        self.image = pygame.image.load(imagen)
        self.precio = precio
        #se lleva la cuenta en una lista con la cantidad de items y una lista que tenga cada tipo
        #los tipos son:tréboles,cocos,corazones y espadas útiles contra Tierra,Aire,Agua,Fuego
class allies(object):
    def __init__(self,x,y,distance,name,images,avatar,vida,ataque,defensa,tool,estado):
        self.x = x
        self.y = y
        self.distance = distance#lista de valores para indicar cuan separado de Mario esta en x y y
        self.rect = 'para collider'
        self.name = name
        self.image = pygame.image.load(images)
        #Falta funicon para transformarlas y que se puedan mover,tambien las imagenes
        self.avatar = pygame.image.load(avatar)
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.exp=0
        self.tool=tool
        self.estado=estado#Estados siguiendo(sigue a Mario), mision(los manda a alguna parte del mapa y les trae info), returning(volviendo a Mario), recovering(llenan vida)
        self.tiempo=0
        self.walkCount=0
##    def walking(self):
##        self.direction = man.direction
##        if self.walkCount + 1 >= 18:self.walkCount = 0
##            ##if self.direction[1]:win.blit(image[1][self.walkCount//3], (self.x,self.y))
##            ##elif self.direction[4]:win.blit(image[2][self.walkCount//3], (self.x,self.y))
##            ##elif self.direction[2]:win.blit(image[3][self.walkCount//3], (self.x,self.y))
##            ##elif self.direction[3]:win.blit(image[4][self.walkCount//3], (self.x,self.y))
##        else:win.blit(self.image, (self.x,self.y))
##        self.walkCount += 1
##            ##avatar podría ser una lista, posicion 0 la imagen y los otros 2 x y y
##            ##images lista de 5 listas con los nombres de la imagenes para standing,right,left,up,down
##            ##cuatro tipo de herramientas (basados en cartas) efectivas entre 4 tipos de obstaculos que tienen una velocidad
        def changetool(self,cursor):
            self.tool=herramientas[cursor]
def getalliesimages(x=40,y=60,i=0,L=[]):
    while i<len(aliados):
        L.append([aliados[i].avatar,x,y+100*i])
        L.append([aliados[i].tool.image,x+280,y+20+100*i])
        i+=1
    return L
def gettoolsimages(x=60,y=60,i=0,L=[]):#lo mismo que la anterior pero para las herramientas
    while i<len(herramientas):
        L.append([herramientas[i].image,x,y+100*i])
        i+=1
    return L
class menuestatico(object):
    def __init__(self,imagenes,textos,txtposition,bg,value='toconvert',fuente=['Comic Sans Ms',24],color=[0,100,0],i=0,j=0):
        self.fuente=pygame.font.SysFont(fuente[0], fuente[1])#en fuente se mandará fuente y tamaño
        self.textos=textos
        self.txtposition=txtposition
        self.color=color
        self.bg=bg#lista con color, rect para usar como fondo
        self.imagenes=imagenes#lista con este tipo de elementos[imagen.jpg,x,y]
        while i<len(self.textos):
            self.textos[i] = self.fuente.render(self.textos[i], False, (self.color))#cuidado con el self.fuente
            i+=1
        while j<len(self.imagenes)and value=='toconvert':
            self.imagenes[j][0] = pygame.image.load(self.imagenes[j][0])
            j+=1
    def write(self,win=win,i=0,j=0,k=0):
        pygame.draw.rect(win, self.bg[0],(self.bg[1]))
        while i<len(self.textos):
            win.blit(self.textos[i],(self.txtposition[j],self.txtposition[j+1]))
            i,j=i+1,j+2
        while k<len(self.imagenes):
            win.blit(self.imagenes[k][0], (self.imagenes[k][1],self.imagenes[k][2]))
            k+=1
class menudinamico(object):
    #VAS A DIVIDIRLO EN DOS CAPAS: dinámico y estático
    def __init__(self,con,coff,menuactions,recs,cursor=0):
        self.menuactions=menuactions#lista de funciones que llamará
        self.con=con#color de boton encendido
        self.coff=coff
        self.recs=recs#lista de rects # Rect(left, top, width, height)
        self.cursor=cursor#posicion en lista
    def onscreen(self,win=win,i=0):#dibuja todos los rectángulos de linea en linea
        while i<len(self.recs):
            if i!=self.cursor:pygame.draw.rect(win, self.coff,(self.recs[i]))
            else:pygame.draw.rect(win, self.con,(self.recs[i]))    
            i+=1            
    def run(self):#permite que se mueva entre las opciones(cambia color y cuando pone enter ejecuta una funcion) lista de listas
        if keys[pygame.K_UP] and self.cursor>0:self.cursor-=1
        elif keys[pygame.K_DOWN] and self.cursor<len(self.menuactions)-1:self.cursor+=1
        if keys[pygame.K_RETURN]:
            print(exec(self.menuactions[self.cursor]))

#Para determinar si un menu esta en true
def menutrue(i=0):
    while i<len(menustates):
        if menustates[i]:return True
        i+=1
        return False
        
def redrawGameWindow(i=0,j=0,n=0):
    bg.drawing(win)
    man.draw(win)#llama a la funcion draw para dibujar a mario
    gorro.drew(win)#dibujo el cap osea gorro lol
    for wall in walls:
        win.blit(arbusto,wall.rect)
    pygame.draw.rect(win, (255, 0, 0), man.rect)
    while n <len(Ldeenemigos):
        Ldeenemigos[n].drawn(win)
        n+=1

    textsurface = myfont.render(str(man.vidas), False, (255, 255, 255))
    win.blit(textsurface,(10,0))
    while i<len(dinamicmenus):
        if menustates[i]:
            staticmenus[i].write()
            dinamicmenus[i].onscreen()
            dinamicmenus[i].run()
        i+=1
    while j<len(aliados):
##        if aliados[j].estado=='Siguiendo':aliados[j].walking()
        j+=1
    pygame.display.update()

herramientas=[tools(1,1,'trebol.png',5),tools(1,2,'trebol.png',10),
              tools(2,1,'corazon.png',5),tools(2,2,'corazon.png',10),
              tools(3,1,'coco.png',5),tools(3,2,'coco.png',10),
              tools(4,1,'espada.png',5),tools(4,2,'espada.png',10)]
herramientascant=[1,1,1,1,1,1,1,1]#cantidad de herramientas
aliados=[allies(0,0,[64,64],'Trebol','persona.png','toad.png',10,2,2,herramientas[0],'Siguiendo'),
         allies(0,0,[0,64],'York','persona.png','toad.png',10,2,2,herramientas[2],'Siguiendo'),
         allies(0,0,[0,64],'Tom','persona.png','toad.png',10,2,2,herramientas[4],'Siguiendo'),
         allies(0,0,[0,64],'Jerry','persona.png','toad.png',10,2,2,herramientas[6],'Siguiendo')]
menustates=[True,False]
#self,con,coff,menuactions,recs,cursor=0
dinamicmenus=[menudinamico((255,69,0),(255,215,0),
                           ['print(aliados[dinamicmenus[0].cursor])',2,3,4,5,6,7,8],
                           [[530,65,60,30],[530,105,60,30],[530,165,60,30],[530,205,60,30],[530,265,60,30],[530,305,60,30],[530,365,60,30],[530,405,60,30]]),
              menudinamico((255,69,0),(255,215,0),
                           ['',2,3,4,5,6,7,8],
                           [[530,65,60,30],[530,105,60,30],[530,165,60,30],[530,205,60,30],[530,265,60,30],[530,305,60,30],[530,365,60,30],[530,405,60,30]])
              ]
#imagenes,textos,txtposition,bg,fuente=['Comic Sans Ms',24],color=[0,100,0]
staticmenus=[menuestatico(getalliesimages(),#imagenes,x,y
                          ['a','b','c','d'],#textos
                          [5,5,5,5,5,5,5,5],#x,y
                          [(240,230,140),(20,40,600,420)],#rectángulo de fondo
                          'novalue'#para que no convierta las imagenes
                          ),
             menuestatico(gettoolsimages(),#imagenes,x,y
                          ['a','b','c','d'],#textos
                          [5,5,5,5,5,5,5,5],#x,y
                          [(240,230,140),(20,40,600,420)],#rectángulo de fondo
                          'novalue'#para que no convierta las imagenes
                          )
             ]

    


#mainloop
bg=fondo(-640,-4320,40,150,'Tierra.png')
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

##    if not keys[pygame.K_LSHIFT]:
##        if keys[pygame.K_a] and  man.comandantex<38*32:
##            man.x -= man.velx
##            man.comandantex += man.velx+bg.velx
##            bg.x += bg.velx
##            man.validate(1)
##        elif keys[pygame.K_d] and man.comandantex>0+32 :
##            man.x += man.velx
##            man.comandantex -= (man.velx+bg.velx)           
##            bg.x -= bg.velx
##            man.validate(4)
##        elif keys[pygame.K_w] and  man.comandantey<148*32 :
##            man.y -= man.vely
##            man.comandantey += man.vely+bg.vely
##            bg.y += bg.vely
##            man.validate(2)
##        elif keys[pygame.K_s]  and man.comandantey>0+32:
##            man.y += man.vely
##            man.comandantey-= (man.vely+bg.vely)
##            bg.y -= bg.vely
##            man.validate(3)
##        else:
##            man.validate(-1)
##            man.walkCount = 0

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

     # Move the player if an arrow key is pressed
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        man.move(-2*man.velx, 0)
    if key[pygame.K_d]:
        man.move(2*man.velx, 0)
    if key[pygame.K_w]:
        man.move(0, -2*man.vely)
    if key[pygame.K_s]:
        man.move(0, 2*man.vely)
    
    pygame.display.flip()
        
    

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
