##YOU'RE EDITING THIS ONE
import pygame,sys
from tkinter import *
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
musica=pygame.mixer.music.load("songmario.mp3")
pygame.mixer.music.play(-1)
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
    def teleport(self,x=0):
        
        for p in portal[self.actual]:
            if self.rect.colliderect(p.rect):
                self.actual=portalvalues[self.actual][x]
                self.rect.x=mstartpoints[self.actual][0]
                self.rect.y=mstartpoints[self.actual][1]
            x+=1
    def move(self, dx, dy):
        if dx != 0:self.move_single_axis(dx, 0)
        if dy != 0:self.move_single_axis(0, dy)
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

    def validate(self,k):
##        self.direction[0]=False
        self.direction[1]=False
        self.direction[2]=False
        self.direction[3]=False
        self.direction[4]=False
        if k<len(self.direction) and k>=0:self.direction[k]=True
##        else:self.direction[0]=True
           
    def draw(self, win):
##        win.blit(char, (self.rect.x,self.rect.y))
##        self.walkCount +=1
        if self.walkCount + 1 >= 18:
            self.walkCount = 0
        if self.direction[1]:
            win.blit(walkLeft[self.walkCount//3], (self.rect.x,self.rect.y))
            self.walkCount +=1
        elif self.direction[4]:
            win.blit(walkRight[self.walkCount//3], (self.rect.x,self.rect.y))
            self.walkCount +=1
        elif self.direction[2]:
            win.blit(walkFront[self.walkCount//3], (self.rect.x,self.rect.y))
            self.walkCount +=1
        elif self.direction[3]:
            win.blit(walkBack[self.walkCount//3], (self.rect.x,self.rect.y))
            self.walkCount +=1
        ##elif self.direction[0]:
##            win.blit(standing[self.walkCount//3], (self.rect.x,self.rect.y))
        else:win.blit(char, (self.rect.x,self.rect.y))        
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
    def __init__(self,x,y,width,height,vel,moved,vidas,imagen,estatus='vivo'):#self = enemigo
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

class obstaculo(object):
    def __init__(self,tipo,vida,imagen):
        self.tipo = tipo
        self.poder = poder
        self.usos = 10
        self.image = pygame.image.load(imagen)

class allies(object):
    def __init__(self,x,y,width,height,distance,name,images,avatar,tool,estado):
        self.distance = distance#lista de valores para indicar cuan separado de Mario esta en x y y
        self.rect = pygame.Rect(x,y,width,height)
        self.name = name
        self.image = pygame.image.load(images)
        self.avatar = pygame.image.load(avatar)
        self.tool=tool
        self.estado=estado
        #Estados siguiendo(sigue a Mario), mision(los manda a alguna parte del mapa y le trae herramientos),
##        returning(volviendo a Mario), recovering(llenan vida),mapa(estáticos)
        self.tiempo=0
    def estatico(self):
        win.blit(self.image,(self.rect.x,self.rect.y))
    def siguiendo(self):
        self.rect.x=player.rect.x+self.distance[0]
        self.rect.y=player.rect.y+self.distance[1]
        
##CUIDADO desde aquí
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
##DANGER HASTA AQUÍ

        
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
    for allie in aliados:
        if allie.estado=='Siguiendo':allie.siguiendo()
        if allie.estado=='Estatico':allie.estatico()
    for i in range(len(dinamicmenus)):
        if menustates[i]:
            staticmenus[i].write()
            dinamicmenus[i].onscreen()
            dinamicmenus[i].run()
    pygame.display.update()

##DANGER
class tools(object):
    #imagen,tipo(contra que es valido)1,2,3,4,poder(1,2 tiempo que se demora representado por rectangulo que se llena),
    #usos(05), precio,bloqueado o desbloqueado
    def __init__(self,tipo,poder,imagen,precio,cantidad=0):
        self.tipo = tipo
        self.poder = poder
        self.usos = 10*cantidad
        self.image = pygame.image.load(imagen)
        self.precio = precio
herramientas=[tools(1,1,'trebol.png',5),tools(1,2,'trebol.png',10),
              tools(2,1,'corazon.png',5),tools(2,2,'corazon.png',10),
              tools(3,1,'coco.png',5),tools(3,2,'coco.png',10),
              tools(4,1,'espada.png',5),tools(4,2,'espada.png',10)]
herramientascant=[1,1,1,1,1,1,1,1]#cantidad de herramientas
aliados=[allies(0,0,64,64,[64,64],'Trebol','persona.png','toad.png',herramientas[0],'Siguiendo'),
         allies(0,0,64,64,[0,64],'York','persona.png','toad.png',herramientas[2],'Estatico'),
         allies(0,0,64,64,[0,64],'Tom','persona.png','toad.png',herramientas[4],'Siguiendo'),
         allies(0,0,64,64,[0,64],'Jerry','persona.png','toad.png',herramientas[6],'Siguiendo')]
menustates=[False,False]
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
##HASTA AQUI 
    

#mainloop
bg=nivel(20,15,'Tierra.png','Arbustomario.png')##(self,patronx,patrony,imagen,walls=[])
player = Player(128,64,64,64)##(self,x,y,width,height,actual=0)
gorro = cap(200,410,32,32,5)##(self,a,b,height,width,vel)
ene=[enemy(32,64,64,64,2,-2,3,'hola.png'),enemy(64,128,64,64,4,-2,3,'hola.png'),enemy(128,64,64,64,4,-1,3,'hola.png')]##(self,x,y,fin,width,height,vel,moved,vidas,imagen)
walls = []
level = [['W       WWWWWWWWWWWWWW','W           W     W ','W           W     W ','W           W       ','W           W       ','W      W    W       ','W      W    W       ','W      W   WWWWWWWW ','W      W   WW       ','W      W            ','W      W   M        ','W      W            ','W      WWWWWWWWWW   ','W               W   ','W   0           W     '],
         ['W               W   ','W               W   ','WWWWWWWWWWWW    W   ','W    W     W    W   ','W    W     W    W   ','W    W     W    WWWW','W    W     W        ','W    W     W        ','W    W     W        ','W    W     W   1    ','W    W     WWWWWWWWW','W M W     W        ','W    W     W        ','W    W     W        ','W    W     W           '],
         ['W    W     W    W   ','W    W     W    W   ','W    W     W    W   ','W    W          W   ','W    W          W   ','W    W          W   ','W    W          W   ','W    WWWWWWWWWWWW   ','W         W M   ','W    2    W         ','W         W         ','W         W         ','WWWWWW    WWWWWWWWWW','W    W    W    W    ','W    W    W    W       '],
         ['W    W    W    W    ','W    W    W    W    ','W    W M  W    W    ','W    W    W    W    ','W    W    W    W    ','W    W    W 3  W    ','W    W    W    W    ','W         W    W    ','W         W    W    ','W         W    W    ','W         W    W    ','W    WWWWWW    W    ','W              W    ','W              W    ','W              W       '],
         ['W                   ','W    W    W         ','W    W    W         ','W    W    W         ','W    W    WWWWWWWWWW','W    W              ','W    W              ','W    W      M       ','W    W              ','W    WWWWWWW        ','W          W    WWWW','W          W        ','W          W     4  ','W          W        ','W     W    W           '],
         ['W     W    W    W   ','W     W    W    W   ','W     W    W    W   ','W     W    W    W   ','W     W    W    W   ','W     W    W    W   ','W     W    W    WWWW','W     W    W        ','W     W    W        ','W     W    W        ','W          W        ','W          WWWWWWWWW','W  M                ','W                5  ','W   WWW                '],
         ['W     W             ','W     W    WWWWWWWWW','W     W             ','W     W             ','W     W             ','W     W             ','W     WWWWWWWWWWWWWW','W               6   ','W                   ','W       M           ','W                   ','WWWWWWW    WWW    W ','W     W    W      W ','W     W           W ','W     W           W    '],
         ['W     W   M       W ','W     W           W ','W     W      WWWWWW ','W                   ','W                   ','W                   ','W            WWWWWWW','W    WWW         W  ','W      W         W  ','W      W         W  ','W      WWWWWWWW  W  ','W      W 7   W   W  ','W    WWW     W   W  ','W      W     W   W  ','W      W         W     '],
         ['W      W         W  ','W      W  M WWWWWW  ','W      W         W  ','W      W         W  ','W      W         W  ','W      W         W  ','W      WWWWWW    WWW','W      W         W  ','W      W         W  ','W      W         W  ','W      W         W  ','WWWWWWWWWWWWW    W  ','W    W              ','W    W              ','W    W  8              '],
         ['W    W              ','W 0  W              ','W    W    WWWWWW    ','W    W    W    W    ','W    W    W    W   M','W    W    W    W    ','W    W    W    W    ','W    W    W    W    ','W    W    W    W    ','W    W    W    W    ','W    W    W    W    ','W         W         ','W         W         ','W         W         ','W         W            ']
]
portal=[]
portalvalues=[]
aliadosfree=[] 
#portalvalues=[[1,2], [], []]#llenar manualmente
mstartpoints=[]#llenar manualmente
#for food in level:portalvalues.append([])
for food in level:
    walls.append([])
    portal.append([])
    portalvalues.append([])
    mstartpoints.append([])
    aliadosfree.append([])
class Wall(object):
    def __init__(self, pos,position,walls,col=-1,another=[]):
        walls[position].append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
        if col!=-1:
            portalvalues[position].append(int(col)+1)
        elif len(another)>0:
            mstartpoints[position].remove(self)
            mstartpoints[position].append(another[0])
            mstartpoints[position].append(another[1])


          
liststrnumeros=[]
for numer in range(len(level)):liststrnumeros.append(str(numer))
def actualmaze(independent,m,x=0,y=0):
    for row in independent:#Pasa por todas as posiciones para crear una lista de walls
        for col in row:
            if col == "W":Wall((x, y),m,walls)
            elif liststrnumeros.count(col)>0:Wall((x, y),m,portal,col)
            elif col=="M":Wall((x, y),m,mstartpoints,-1,(y,x))
            #elif col=="T":aliadosfree[m].append(allies(x,y,64,64,[64,0],'toad','Toad.png','Toad.png',herramientas[0],'estático'))
                ##self,x,y,width,height,distance,name,images,avatar,tool,estado)

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
            player.validate(1)
            
        if keys[pygame.K_RIGHT]:
            player.move(1*player.vel, 0)
            player.validate(4)
            
        if keys[pygame.K_UP]:
            player.move(0, -1*player.vel)
            player.validate(2)
            
        if keys[pygame.K_DOWN]:
            player.move(0, 1*player.vel)
            player.validate(3)

        else:
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
        

    if player.rect.colliderect(ene[player.actual].rect) and ene[player.actual].direction[0]:
        print('que mario reinicie y le quite vida')
        player.vidas-=1
        player.rect.x=mstartpoints[self.actual][0]
        player.rect.y=mstartpoints[self.actual][1]
    elif gorro.rect.colliderect(ene[player.actual].rect):ene[player.actual].direction[0]=False#hace que no se muestre y que no pueda matar
    for allie in aliados:
        if player.rect.colliderect(allie.rect) and allie.estado=='Estatico':print('paraSaol')
    player.teleport()
    if keys[pygame.K_a]:
        window = Tk()
        def f():
               lblEntrada2=Label(text='Seguro que no puedes salir del nivel',font=('Register',8)).place(x=10,y=50)
               en2=StringVar()
               txtEntrada2=Entry(window,textvariable=en2).place(x=10,y=70)
               B2 = Button(window,text="Enviar",command = g).place(x=200,y=70)
##               B2.pack() player.rect.colliderect(aliados[1].rect):
        def g():
              lblEntrada3=Label(text='Para pasar al siguiente nivel debes encontrar 4 letras y un numero',font=('Register',8)).place(x=10,y=90)
              en3=StringVar()
              txtEntrada3=Entry(window,textvariable=en3).place(x=10,y=110)
              B3 = Button(window,text="Enviar",command = h).place(x=200,y=110)
##              B3.pack()
                
        def h():
             lblEntrada4=Label(text='Fue un gusto ayudarte',font=('Register',8)).place(x=10,y=130)
             en4=StringVar()
##    txtEntrada4=Entry(window,textvariable=en4).place(x=10,y=150)
##    B4 = Button(window,text="Enviar",command = h).place(x=200,y=150)
##    B4.pack()
##    print('quetal')
        window.geometry('500x350')
        window.title("Aliados")
        lblEntrada=Label(text='Hola, soy tu Aliado y estoy aqui para ayudarte',font=('Register',8)).place(x=10,y=10)
        enE=StringVar()
        ##enE.set('Hola')
        txtEntrada=Entry(window,textvariable=enE).place(x=10,y=30)

        B = Button(window,text="Enviar",command = f).place(x=200,y=30)

    ##    B.pack()
        window.mainloop() 
          
    if player.vidas== 0 : run =False
    ##AQUÍ
    ene[player.actual].movement()
  #  print (mstartpoints)
    redrawGameWindow()

pygame.quit()
