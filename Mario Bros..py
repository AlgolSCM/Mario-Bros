##YOU'RE EDITING THIS ONE
import pygame,sys
from tkinter import *
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 24)
walkRight=[pygame.image.load('Mario derecha/Mario 10.png'),pygame.image.load('Mario derecha\Mario 9.png'),pygame.image.load('Mario derecha\Mario 8.png'),pygame.image.load('Mario derecha\Mario 7.png'),pygame.image.load('Mario derecha\Mario 11.png'),pygame.image.load('Mario derecha\Mario 10.png')]
standing=[pygame.image.load('Mario derecha/Mario 10.png'),pygame.image.load('Mario derecha\Mario 9.png'),pygame.image.load('Mario derecha\Mario 8.png'),pygame.image.load('Mario derecha\Mario 7.png'),pygame.image.load('Mario derecha\Mario 11.png'),pygame.image.load('Mario derecha\Mario 10.png')]
walkLeft=[pygame.image.load('Mario Izquierda\Mario 33.png'),pygame.image.load('Mario Izquierda\Mario 38.png'),pygame.image.load('Mario Izquierda\Mario 37.png'),pygame.image.load('Mario Izquierda\Mario 36.png'),pygame.image.load('Mario Izquierda\Mario 35.png'),pygame.image.load('Mario Izquierda\Mario 34.png')]
walkBack=[pygame.image.load('Mario frente\Mario 13.png'),pygame.image.load('Mario frente\Mario 14.png'),pygame.image.load('Mario frente\Mario 17.png'),pygame.image.load('Mario frente\Mario 15.png'),pygame.image.load('Mario frente\Mario 19.png'),pygame.image.load('Mario frente\Mario 13.png')]
walkFront=[pygame.image.load('Mario espalda\Mario 1.png'),pygame.image.load('Mario espalda\Mario 2.png'),pygame.image.load('Mario espalda\Mario 3.png'),pygame.image.load('Mario espalda\Mario 4.png'),pygame.image.load('Mario espalda\Mario 5.png'),pygame.image.load('Mario espalda\Mario 6.png')]
win = pygame.display.set_mode((32*20+32*8,32*15))
pygame.display.set_caption("Mario Bros")
clock = pygame.time.Clock()
char =walkFront[1]
capi=pygame.image.load('gorro1.png')
portal,portalvalues,aliadosfree,mstartpoints,obstaculitos=[],[],[],[],[]
keysdowns=[True,False,False,False]#para intercalar entre que se mueva Mario,aliado,gorro,aliadoX2
count=0
nivelnumero=1
gemas=[]
gema=0

musica=pygame.mixer.music.load("songmario.mp3")
pygame.mixer.music.play(-1)

gameover = pygame.image.load ('Mariogameover.png')
##inicio = pygame.image.load ('Marioinicio.png')
pausa = pygame.image.load ('Mariopausa.png')
meta = pygame.image.load ('Meta.png')
jugando = True
#remplazaste fondo por nivel

##menuestatico(self,imagenes,textos,txtposition,bg,value='toconvert',fuente=['Comic Sans Ms',24],color=[0,100,0],i=0,j=0)
def changetool(herramienta):
    if herramienta==0:
        aliados[keysdowns.index(True)].tool.tipo=1
    elif herramienta==1:
        aliados[keysdowns.index(True)].tool.tipo=2
def keypress(persona):
    if not keys[pygame.K_LSHIFT]:
        if keys[pygame.K_LEFT]:
            persona.move(-1*player.vel, 0)
            validate(persona.direction,1,4)
        if keys[pygame.K_RIGHT]:
            persona.move(1*player.vel, 0)
            validate(persona.direction,4,4)
        if keys[pygame.K_UP]:
            persona.move(0, -1*player.vel)
            validate(persona.direction,2,4)
        if keys[pygame.K_DOWN]:
            persona.move(0, 1*player.vel)
            validate(persona.direction,3,4)
####        if keys[pygame.K_h]:
####            if keysdowns.index(True)==1:
##                if len(aliados)>0:
####                     if keys[pygame.K_h]:
##                          w = Tk()
##                          img=PhotoImage(file='mision.gif')
##                          img2=PhotoImage(file='mision.gif')
##                          def a():
##                              Bo3= Button(w,image=img,height=53,width=40,command =b).place(x=70,y=50)
##                              Bo4= Button(w,image=img2,height=53,width=40,command =d).place(x=190,y=50)
##                              lblmision1=Label(text='Herramienta roja',font=('Book Antiqua',8)).place(x=50,y=130)
##                              lblmision2=Label(text='Herramienta azul',font=('Book Antiqua',8)).place(x=170,y=130)
##                          def b():
##                              changetool(0)
##                          def d():
##                              changetool(1)
##                          w.geometry('300x180')
##                          w.title("Aliados")
##                          Bo = Button(w,text="Acciones de Aliados",command = a).place(x=100,y=10)
##                          w.mainloop()
##            elif keysdowns.index(True)==2:
##                if len(aliados)>1:
####                     if keys[pygame.K_h]:
##                          w = Tk()
##                          img=PhotoImage(file='mision.gif')
##                          img2=PhotoImage(file='mision.gif')
##                          def a():
##                              Bo3= Button(w,image=img,height=53,width=40,command =b).place(x=70,y=50)
##                              Bo4= Button(w,image=img2,height=53,width=40,command =d).place(x=190,y=50)
##                              lblmision1=Label(text='Herramienta roja',font=('Book Antiqua',8)).place(x=50,y=130)
##                              lblmision2=Label(text='Herramienta azul',font=('Book Antiqua',8)).place(x=170,y=130)
##                          def b():
##                             changetool(0)
##                          def d():
##                               changetool(1)
##                          w.geometry('300x180')
##                          w.title("Aliados")
##                          Bo = Button(w,text="Acciones de Aliados",command = a).place(x=100,y=10)
##                          w.mainloop()   
        else:
            player.walkCount = 0

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
        self.direction=[False,False,False,False,False,True]#Standing Derecha izquierda Arriba Abajo AGREGASTE AQUÍ
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
        for wall in walls[self.actual]:
            if self.rect.colliderect(wall.rect):
                if dx > 0:self.rect.right = wall.rect.left# Moving right; Hit the left side of the wall
                if dx < 0:self.rect.left = wall.rect.right# Moving left; Hit the right side of the wall
                if dy > 0:self.rect.bottom = wall.rect.top# Moving down; Hit the top side of the wall
                if dy < 0:self.rect.top = wall.rect.bottom# Moving up; Hit the bottom side of the wall
        for wall in obstaculitos[self.actual]:
            if self.rect.colliderect(wall.rect):
                if dx > 0:self.rect.right = wall.rect.left# Moving right; Hit the left side of the wall
                if dx < 0:self.rect.left = wall.rect.right# Moving left; Hit the right side of the wall
                if dy > 0:self.rect.bottom = wall.rect.top# Moving down; Hit the top side of the wall
                if dy < 0:self.rect.top = wall.rect.bottom# Moving up; Hit the bottom side of the wall

           
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
        if self.rect.x > 20*32-self.rect.height:self.moved=1# Moving right; Hit the left side of the wall
        elif self.rect.x < 0:self.moved=-1# Moving left; Hit the right side of the wall
        if self.rect.y > 15*32-self.rect.width:self.moved=-2# Moving down; Hit the top side of the wall
        elif self.rect.y < 0:self.moved=2
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
    def __init__(self,x,y,tipo,imagen):
        self.rect=pygame.Rect(x,y,32,32)
        self.tipo = tipo#1 ó 2
        self.image = pygame.image.load(imagen)
    def draw(self):
        win.blit(self.image,(self.rect.x,self.rect.y))
class gemin(object):
    def __init__(self,x,y,imagen):
        self.rect=pygame.Rect(x,y,32,32)
        self.image = pygame.image.load(imagen)
        self.value=True
    def draw(self):
        win.blit(self.image,(self.rect.x,self.rect.y))                  
class allies(object):
    def __init__(self,x,y,width,height,distance,name,images,avatar,tool,estado,askmark):
        self.distance = distance#lista de valores para indicar cuan separado de Mario esta en x y y
        self.rect = pygame.Rect(x,y,width,height)
        self.name = name
        self.vel=5
        self.image = pygame.image.load(images)
        self.avatar = pygame.image.load(avatar)
        self.tool=tool
        self.estado=estado
        self.direction=[True,False,False,False,False]
        self.askmark=pygame.image.load('askmark.png')
        #Estados siguiendo(sigue a Mario), mision(los manda a alguna parte del mapa y le trae herramientos),
##        returning(volviendo a Mario), recovering(llenan vida),mapa(estáticos)
        self.tiempo=0
    def estatico(self):
        win.blit(self.image,(self.rect.x,self.rect.y))
    def siguiendo(self):
        self.rect.x=player.rect.x+self.distance[0]
        self.rect.y=player.rect.y+self.distance[1]
        win.blit(self.image,(self.rect.x,self.rect.y))
    def mision(self):
        print('misionero')
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
##        if dx != 0:self.move_single_axis(dx, 0)
##        if dy != 0:self.move_single_axis(0, dy)
##    def move_single_axis(self, dx, dy):# Move the rect        
##        self.rect.x += dx
##        self.rect.y += dy
aliados=[]        
##CUIDADO desde aquí
def validate(self,k,l):
    for i in range(l):
        self[i]=False
        if k<len(self) and k>=0:self[k]=True
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
    def __init__(self,imagenes,textos,txtposition,bg,value='toconvert',fuente=['Comic Sans Ms',18],color=[0,100,0],i=0,j=0):
        self.fuente=pygame.font.SysFont(fuente[0], fuente[1])#en fuente se mandará fuente y tamaño
        self.textos=textos
        self.txtposition=txtposition
        self.color=color
        self.bg=bg#lista con color, rect para usar como fondo
        self.imagenes=imagenes#lista con este tipo de elementos[imagen.jpg,x,y]
        while j<len(self.imagenes)and value=='toconvert':
            self.imagenes[j][0] = pygame.image.load(self.imagenes[j][0])
            j+=1
        while i<len(self.textos):
            self.textos[i] = self.fuente.render(self.textos[i], False, (self.color))#cuidado con el self.fuente
            i+=1
    def write(self,win=win,i=0,j=0,k=0):
        pygame.draw.rect(win, self.bg[0],(self.bg[1]))
        while k<len(self.imagenes):
            win.blit(self.imagenes[k][0], (self.imagenes[k][1],self.imagenes[k][2]))
            k+=1
        while i<len(self.textos):
            win.blit(self.textos[i],(self.txtposition[j],self.txtposition[j+1]))
            i,j=i+1,j+2

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
def pause ():
    paused = True
    while paused:
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if keys[pygame.K_r]:
                    paused = False
      
def redrawGameWindow():
    bg.drawing(win)
    player.draw(win)#llama a la funcion draw para dibujar a mario
    gorro.drew(win)#dibujo el cap osea gorro lol
##    textsurface = myfont.render(str(player.vidas), False, (255, 255, 255))
##    win.blit(textsurface,(64,64))
    keys = pygame.key.get_pressed()
    for wall in walls[player.actual]:##CAMBIA por mapa actual
        win.blit(bg.obstacule,wall.rect)
        #pygame.draw.rect(win, (255, 255, 255), wall.rect)#las dibuja
    for wall in portal[player.actual]:##CAMBIAR por mapa actual
        pygame.draw.rect(win, (255, 0, 0), wall.rect)
    if ene[player.actual].direction[0]:ene[player.actual].drawn(win)#Si esta vivo lo dibuja
    if keysdowns[1] or keysdowns[2]:
        for thing in obstaculitos[player.actual]:thing.draw()
    for allie in aliados:
        if allie.estado=='Siguiendo':allie.siguiendo()
        elif allie.estado=='Misionero':allie.estatico()
    if gemas[player.actual].value:gemas[player.actual].draw()    
    for allie in aliadosfree[player.actual]:
        allie.estatico()
        if player.rect.colliderect(allie.rect):
            win.blit(allie.askmark,allie.rect)
            if keys[pygame.K_j]:
                allie.estado='Siguiendo'
                aliados.append(aliadosfree[player.actual].pop())    
    leftbar.write()
    for i in range(len(dinamicmenus)):
        if menustates[i]:
            staticmenus[i].write()
            dinamicmenus[i].onscreen()
            dinamicmenus[i].run()
   
    if keys[pygame.K_p]==True: win.blit(pausa,(0,0))
    if jugando == False: win.blit(gameover,(0,0))
    if gema==9: win.blit(meta,(0,0))
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
herramientas=[tools(1,1,'trebol.png',5),tools(2,1,'corazon.png',5),tools(3,1,'coco.png',5),tools(4,1,'espada.png',5)]


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
    


bg=nivel(20,15,'Tierra.png','Arbustomario.png')##(self,patronx,patrony,imagen,walls=[])
player = Player(128,64,64,64)##(self,x,y,width,height,actual=0)
gorro = cap(200,410,32,32,5)##(self,a,b,height,width,vel)

Uciaproducciones=[[['W A   M  BWWWWWWWWWWWWWW'
                    ,'W  AA   T   WBB  W '
                    ,'W   AAA   BB   W     W '
                    ,'W           W  AA   '
                    ,'W Y      W  BB   '
                    ,'W  AA  W    W    BB '
                    ,'W  AA  W    W  BB   '
                    ,'W  AA  WB  WWWWWWWW '
                    ,'W AA   W   WW   BB  '
                    ,'W  AA  W   BB       '
                    ,'W  AA  W G   BB    '
                    ,'W  AA  W       BB    '
                    ,'W  AA  WWWWWWWWWWBB '
                    ,'W    AAM  BB   W   '
                    ,'W   0    AA     W  BB '],
                    ## AA  BB
                    ['W  AAA   X    M  W   '
                    ,'W        BBB    W   '
                    ,'WWWWWWWWWWWW    W   '
                    ,'A A  W  A  W  B W B '
                    ,'A  A W  A  W B  W B '
                    ,'A  A W G A W  B WWWW'
                    ,'A A  W  A  W    BBB  '
                    ,'W A  W  A  W  BB    '
                    ,'W  A W   A W   BB   '
                    ,'W    WAA   W   1BB  '
                    ,'W    W     WWWWWWWWW'
                    ,'W M W   A W    B  '
                    ,'W  A W  A  W   BB   '
                    ,'W    W  A  W B  Y   '
                    ,'W    W A   W    BB     '],
                    ##   AB
                    ['W  A W     W  B W   '
                    ,'W    W  A  W  B W   '
                    ,'W A  W   X W B  W   ','W    W      AA  W   '
                    ,'W    W   BB M   W   '
                    ,'W B  W    AA    W   '
                    ,'W  A W      BB  W   '
                    ,'W    WWWWWWWWWWWW   '
                    ,'W G  BB   W M   '
                    ,'W    2    W   AA    '
                    ,'W    AA   W     BB  '
                    ,'W   AA    W  BB     '
                    ,'WWWWWW A  WWWWWWWWWW'
                    ,'W B  W    W  B W    '
                    ,'W    W    W    W  A Y  '],
                    ##    BB
                    ['W  A W    W B  W    '
                    ,'W  A W    W  B W X  '
                    ,'W A  W M  W    W  B '
                    ,'W A  W    W  B W    '
                    ,'W    W  A W  M W  B '
                    ,'W A  W    W 3  W  B '
                    ,'W    W  A W    W  B '
                    ,'W    A    W  G W  B '
                    ,'W    AA I W B  W A  '
                    ,'W  BB     W    W A  '
                    ,'W    BB   W    W   A '
                    ,'W    WWWWWW A  W  A '
                    ,'W      AA   B  W B  '
                    ,'W     Y   AA   W  B '
                    ,'W       AA     W   BB  '],
                    ##    AB
                    ['W         AB        '
                    ,'W    W    W    AA   '
                    ,'W B  W    W   B X   '
                    ,'W    W    W   AA    '
                    ,'W    W  B WWWWWWWWWW'
                    ,'W    W       AA     '
                    ,'W    W  G    BB     '
                    ,'W A  W   B  M   AA  '
                    ,'W    W     Y    BB  '
                    ,'W    WWWWWWW    AA  ',
                    'W   BB     W    WWWW'
                    ,'W     AA   W   BB   '
                    ,'W   AA     W  B  4  '
                    ,'W    A     W    BB  '
                    ,'W AA  W    W     BB    '],
##                       AB
                   ['W     W  A W    W B '
                    ,'W   A W    W    W B '
                    ,'W     W A  W    W B '
                    ,'W   A W    W    W B '
                    ,'W  A  W    W    W B '
                    ,'W  A  W G  W  B W   '
                    ,'W     W  A W    WWWW'
                    ,'W   B W    W   AA   '
                    ,'W  B  W    W   A    '
                    ,'W     W    W   BB   '
                    ,'W       A  W   B    '
                    ,'W    X   A WWWWWWWWW'
                    ,'W  M        BB      '
                    ,'W        AA      5  '
                    ,'W   WWW       Y    BB  '],
                             ['W     W         AA  '
                    ,'W     W    WWWWWWWWW'
                    ,'W     W      BB     '
                    ,'W     W      X      '
                    ,'W     W   G   AA    '
                    ,'W     W      BB     '
                    ,'W   A WWWWWWWWWWWWWW'
                    ,'W       BB      6   '
                    ,'W         AAA       '
                    ,'W    A  M       B   '
                    ,'W    AA             '
                    ,'WWWWWWW    WWW  B W '
                    ,'W  AA W    W  BB  W '
                    ,'W     W   AA      W '
                    ,'W     W    Y   B  W    '],
##                      BB
                   ['W     W   M   AA  W '
                    ,'W     W  B  X     W '
                    ,'W  AA W   B  WWWWWW '
                    ,'W       AAB         '
                    ,'W   ABB             '
                    ,'W         ABBA       '
                    ,'W      AA    WWWWWWW'
                    ,'W    WWW     BB  W  '
                    ,'W AA   W     BB  W  '
                    ,'W   B  W   AA    W  '
                    ,'W  BB  WWWWWWWW  W  '
                    ,'W  AA  W 7   W   W  '
                    ,'W B  WWW  B  W   W  '
                    ,'W  A   W   Y W   W  '
                    ,'W  BB  W G  AAA  W     '],
##                       BB
                   ['W      W   AA    W  '
                    ,'W BB   W  M WWWWWW  '
                    ,'W  B   W    AA   W  '
                    ,'W   A  W    AA   W  '
                    ,'W  BB  W   B     W  '
                    ,'W   AA W     X   W  '
                    ,'W      WWWWWW  B WWW'
                    ,'W      W   AA    W  '
                    ,'W  B   W     AA  W  '
                    ,'W   B  W  G BB   W  '
                    ,'W   A  W    AA   W  ','WWWWWWWWWWWWW    W  '
                    ,'W    W      ABBA     '
                    ,'W    W      Y  BB   '
                    ,'W    W  8      AAA     '],
##                       BB
                   ['W    W        AA    '
                    ,'W 0  W    BB  X  A  '
                    ,'W    W    WWWWWW  B '
                    ,'W A  W    W  B W    '
                    ,'W    W  A W    W B M'
                    ,'W  A W    W B  W    '
                    ,'W    W A  W    W  B '
                    ,'W A  W    W  B W    '
                    ,'W    W A  W    W  B '
                    ,'W A  W    W    W B  '
                    ,'W    W  A W    W  B '
                    ,'W    Y A  W G B   M  '
                    ,'W   AA    W     BB  '
                    ,'W  ABB     W    AAB     '
                    ,'W    AA   W     AA     ']
],[['W A X M  BWWWWWWWWWWWWWW'
                    ,'W  AA   T   WBB  W '
                    ,'W   AAA   BB   W     W '
                    ,'W           W  AA   '
                    ,'W           W  BB   '
                    ,'W  AA  W    W    BB '
                    ,'W  AA  W    W  BB   '
                    ,'W  AA  WB  WWWWWWWW '
                    ,'W AA   W   WW   BB  '
                    ,'W  AA  W   BB       '
                    ,'W  AA  W G M  BB    '
                    ,'W  AA  W      BB    '
                    ,'W  AA  WWWWWWWWWWBB '
                    ,'W    AA    BB   W   '
                    ,'W   0    AA     W  BB '],
                    ## AA  BB
                    ['W  AAA   X    M  W   '
                    ,'W        BBB    W   '
                    ,'WWWWWWWWWWWW    W   '
                    ,'W A  W  A  W  B W B '
                    ,'W  A W  A  W B  W B '
                    ,'W  A W G A W  B WWWW'
                    ,'W A  W  A  W    BBB  '
                    ,'W A  W  A  W  BB    '
                    ,'W  A W   A W   BB   '
                    ,'W    WAA   W   1BB  '
                    ,'W    W     WWWWWWWWW'
                    ,'W M W   A W    B  '
                    ,'W  A W  A  W   BB   '
                    ,'W    W  A  W B  Y   '
                    ,'W    W A   W    BB     '],
                    ##   AB
                    ['W  A W     W  B W   '
                    ,'W    W  A  W  B W   '
                    ,'W A  W   X W B  W   ','W    W      AA  W   '
                    ,'W    W   BB M   W   '
                    ,'W B  W    AA    W   '
                    ,'W  A W      BB  W   '
                    ,'W    WWWWWWWWWWWW   '
                    ,'W G  BB   W M   '
                    ,'W    2    W   AA    '
                    ,'W    AA   W     BB  '
                    ,'W   AA    W  BB     '
                    ,'WWWWWW A  WWWWWWWWWW'
                    ,'W B  W    W  B W    '
                    ,'W    W    W    W  A Y  '],
                    ##    BB
                    ['W  A W    W B  W    '
                    ,'W  A W    W  B W X  '
                    ,'W A  W M  W    W  B '
                    ,'W A  W    W  B W    '
                    ,'W    W  A W  M W  B '
                    ,'W A  W    W 3  W  B '
                    ,'W    W  A W    W  B '
                    ,'W    A    W  G W  B '
                    ,'W    AA I W B  W A  '
                    ,'W  BB     W    W A  '
                    ,'W    BB   W    W   A '
                    ,'W    WWWWWW A  W  A '
                    ,'W      AA   B  W B  '
                    ,'W     Y   AA   W  B '
                    ,'W       AA     W   BB  '],
                    ##    AB
                    ['W         AB        '
                    ,'W    W    W    AA   '
                    ,'W B  W    W   B X   '
                    ,'W    W    W   AA    '
                    ,'W    W  B WWWWWWWWWW'
                    ,'W    W       AA     '
                    ,'W    W  G    BB     '
                    ,'W A  W   B  M   AA  '
                    ,'W    W     Y    BB  '
                    ,'W    WWWWWWW    AA  ',
                    'W   BB     W    WWWW'
                    ,'W     AA   W   BB   '
                    ,'W   AA     W  B  4  '
                    ,'W    A     W    BB  '
                    ,'W AA  W    W     BB    '],
##                       AB
                   ['W     W  A W    W B '
                    ,'W   A W    W    W B '
                    ,'W     W A  W    W B '
                    ,'W   A W    W    W B '
                    ,'W  A  W    W    W B '
                    ,'W  A  W G  W  B W   '
                    ,'W     W  A W    WWWW'
                    ,'W   B W    W   AA   '
                    ,'W  B  W    W   A    '
                    ,'W     W    W   BB   '
                    ,'W       A  W   B    '
                    ,'W    X   A WWWWWWWWW'
                    ,'W  M        BB      '
                    ,'W        AA      5  '
                    ,'W   WWW       Y    BB  '],
                             ['W     W         AA  '
                    ,'W     W    WWWWWWWWW'
                    ,'W     W      BB     '
                    ,'W     W      X      '
                    ,'W     W   G   AA    '
                    ,'W     W      BB     '
                    ,'W   A WWWWWWWWWWWWWW'
                    ,'W       BB      6   '
                    ,'W         AAA       '
                    ,'W    A  M       B   '
                    ,'W    AA             '
                    ,'WWWWWWW    WWW  B W '
                    ,'W  AA W    W  BB  W '
                    ,'W     W   AA      W '
                    ,'W     W    Y   B  W    '],
##                      BB
                   ['W     W   M   AA  W '
                    ,'W     W  B  X     W '
                    ,'W  AA W   B  WWWWWW '
                    ,'W       AAB         '
                    ,'W   ABB             '
                    ,'W         ABBA       '
                    ,'W      AA    WWWWWWW'
                    ,'W    WWW     BB  W  '
                    ,'W AA   W     BB  W  '
                    ,'W   B  W   AA    W  '
                    ,'W  BB  WWWWWWWW  W  '
                    ,'W  AA  W 7   W   W  '
                    ,'W B  WWW  B  W   W  '
                    ,'W  A   W   Y W   W  '
                    ,'W  BB  W G  AAA  W     '],
##                       BB
                   ['W      W   AA    W  '
                    ,'W BB   W  M WWWWWW  '
                    ,'W  B   W    AA   W  '
                    ,'W   A  W    AA   W  '
                    ,'W  BB  W   B     W  '
                    ,'W   AA W     X   W  '
                    ,'W      WWWWWW  B WWW'
                    ,'W      W   AA    W  '
                    ,'W  B   W     AA  W  '
                    ,'W   B  W  G BB   W  '
                    ,'W   A  W    AA   W  ','WWWWWWWWWWWWW    W  '
                    ,'W    W      ABBA     '
                    ,'W    W      Y  BB   '
                    ,'W    W  8      AAA     '],
##                       BB
                   ['W    W        AA    '
                    ,'W 0  W    BB  X  A  '
                    ,'W    W    WWWWWW  B '
                    ,'W A  W    W  B W    '
                    ,'W    W  A W    W B M'
                    ,'W  A W    W B  W    '
                    ,'W    W A  W    W  B '
                    ,'W A  W    W  B W    '
                    ,'W    W A  W    W  B '
                    ,'W A  W    W    W B  '
                    ,'W    W  A W    W  B '
                    ,'W    Y A  W G B   M  '
                    ,'W   AA    W     BB  '
                    ,'W  ABB     W    AAB     '
                    ,'W    AA   W     AA     ']
],[[' WWW WWWWWWWWWWWWWWWW',
'  I AAA     BBB   W',
'AA      M  BB      W',
' AAAA        BBB  W',
'  X      ABBA      W',
'     AAA      WBB  W',
'  0    BBB   W AA W',
'  WWWWWWWWWWWW  A W',
'  W   AA     BBB  W',
'  W     AAA   B   W',
'  W   BBB   ABA   W',
'  WBA  WWWWWW AB  W',
'  W A  W    W   B W',
'WWW A  W A  W  YB W',
'  W BB W    A   W'],

['   W    W    ABBA   W',
'B W A  W    AAB   W',
'  W AB W   ABB    W',
'  W B  W A  W  B  W',
'  W    W    W     W',
'WWWW AB W  A W BB  W',
'   X   W AA W ABA W',
'  AAA  W AB W BA  W',
'  ABA  W  1 W BB  W',
'  AAA  W    W BA  W',
'WWWWWWWWW B  W  BB W',
'  AA   M A  W B   W',
' BB    AAA  W  AA W',
' AA   BBB   W  Y  W',
'       ABA  W AA  W'],

[' WWWWWWWW A  WABBA W',
'W   AA W    W BAB W',
'W   X  W AA W BB  W',
'W ABA  W  ABAB    W',
'W  AB  W    ABB   W',
'W   BB W    AAA   W',
'W   A W    ABA    W',
'W BB WWW     AAB  W',
'W    BB    W    A W',
'W  ABBA 2   W B   W',
'W B  M  AA  W AA  W',
'W    BBB    W  A  W',
'WWWWWWWWWWWWWW AB  W',
'W        ABB W A Y W',
'W    BAA     W AA  W'],

['W       BB   W AA  W',
'W X   BBB    W  AB W',
'W AB WWWWWWWWW AA  W',
'W Y  W   BB  W  BA W',
'W BB W   AA  W AA  W',
'W  A W  BBB  W  M  W',
'W AA W  ABBA W BB  W',
'W B  W 3  WWWW  BB W',
'W  A W B  W  AAA  W',
'W BB W  A W  BB   W',
'W A  W A  W X  BB  W',
'W  B W  B W   AA   W',
'W Y  W BB W   AA   W',
'W  A W A  WBB  WWWWW',
'W    W  A W AB W B W'],

['   ABB    W AA W B W',
'  ABB    W  A W B W',
'  BBA    W  A W A W',
'    BBA  W  A W B W',
'WWWWWWWWWWW A  W A W',
'     BB    X  W   W',
'      AA      W   W',
'     M   BB   W   W',
'  AAA     4   W   W',
'    BBB Y     W   W',
'WWWWWWWWWWWWWWWW   W',
'W           ABBA  W',
'W   ABBA          W',
'W         BABA    W',
'W     BA         W'],

[' W A  W  B WWWW B  W',
'W  A W  BBB  W AA W',
'  AB W   BA  W    W',
'  A  W   B   W BA  W',
'  A  W  B    W A  W',
' B   W    B  W  A W',
'WWWWWWWWWW  B W    W',
' 5          BBB   W',
'     AAAA         W',
'    X      BBB    W',
'  BB    AA        W',
'WWWWWWWWWWWWWW  BB W',
'     AAA    W     W',
'      AA    W Y M W',
'     BB     W AA  W'],

['      AA     W  BB W',
'WWWWWWWWWWWWWW  B  W',
'   AA       W AB  W',
'   BAB  6   W AA  W',
'   AAA      W BB  W',
'       ABA  W  AA  W',
'WWWWWWWWW  A W AA  W',
'    BB W  A W BB  W',
'   AAA  W B W M A W',
'X  BB  W A  W  B  W',
'   AB  W B  W BA  W',
'  W  A W  A W BB  W',
'A W    W AB W ABB W',
'  W BB W A  W A Y W',
'  W AA W  A W BB  W'],

[' A W AB  W BB W AA  W',
'  W BB W BA W  A  W',
'B W  B W  A W A   W',
'7 W BB W  B W  AA W',
'  W AA W    W  BB W',
'  W B W   A W AA  W',
'WWWW X  W  BBW  A  W',
' BBA   W      AA  W',
'  ABB  W     AA   W',
' BAB   W M  BBB   W',
'   ABB W  BB   A  W',
' W  AA WWWWWWWWWWWW',
' W     W  BB W  A W',
' W AAA W  Y  W B  W',
' W  BB W AA  W    W'],

['  W AA  W     W B  W',
' W  A WW BB  W AA W',
' W  AA    AABB    W',
' W AA   BB    AA  W',
' W AA    AAB 8    W',
' W   AAA      BB  W',
'WWWWWWWWWWWWWW  A  W',
'   B   W    AAA   W',
'X  BAB W    BAB   W',
'   AA  W  BABA   WW',
'        BABAB      W',
' W BBB      AAA   W',
' W   M  BB  AAA   W',
' W   BBB    Y  B  W',
' WWWWWWWWWWWWWWWWWW'],

['  AA  W       BBB    W',
' AAA W    AA  A    W',
'BB   W  ABA    0   W',
'  AA W      BBB    W',
'W BB W  B WWWWW  A W',
'W  X W   A W   BB  W',
'W AA W  W AAA B  W',
'W B  W AA W    BA  W',
'W  A W A  W  BAB   W',
'W AA W  A W    AA  W',
'W A  W BB W   BB   W',
'W   AAAA  W   BB   W',
'W   ABAB  W    BBA W',
'W M  ABA  W  A Y   W',
'W    ABA  W   ABAA  W'],


]]
level=Uciaproducciones[nivelnumero-1]
ene,walls,portal,portalvalues,aliadosfree,mstartpoints,obstaculitos,liststrnumeros=[],[],[],[],[],[],[],[]
def restartlists():
    ene,walls,portal,portalvalues,aliadosfree,mstartpoints,obstaculitos,liststrnumeros=[],[],[],[],[],[],[],[]
    for i in range(len(level)):
        walls.append([])
        portal.append([])
        portalvalues.append([])
        mstartpoints.append([])
        aliadosfree.append([])
        obstaculitos.append([])
    for i in range(len(level)):liststrnumeros.append(str(i))
    return ene,walls,portal,portalvalues,aliadosfree,mstartpoints,obstaculitos,liststrnumeros

ene,walls,portal,portalvalues,aliadosfree,mstartpoints,obstaculitos,liststrnumeros=restartlists()
##for food in level:
##    walls.append([])
##    portal.append([])
##    portalvalues.append([])
##    mstartpoints.append([])
##    aliadosfree.append([])
##    obstaculitos.append([])
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

##liststrnumeros=[]
##for numer in range(len(level)):liststrnumeros.append(str(numer))
def actualmaze(independent,m,x=0,y=0):
    for row in independent:#Pasa por todas as posiciones para crear una lista de walls
        for col in row:
            if col == "W":Wall((x, y),m,walls)
            elif liststrnumeros.count(col)>0:Wall((x, y),m,portal,col)
            elif col=="A":obstaculitos[m].append(obstaculo(x,y,1,'red.jpeg'))
            elif col=="B":obstaculitos[m].append(obstaculo(x,y,1,'red.jpeg'))
            elif col=="X":ene.append(enemy(x,y,64,64,5,-1,1,'Goomba.png'))#(self,x,y,width,height,vel,moved,vidas,imagen,estatus='vivo')
            elif col=="Y":ene.append(enemy(x,y,64,64,5,-2,1,'Goomba.png'))
            elif col=="G":gemas.append(gemin(x,y,'gemas.png'))
            elif col=="M":Wall((x, y),m,mstartpoints,-1,(y,x))
            elif col=="T":aliadosfree[m].append(allies(x,y,64,64,[64,0],'toad','fantasmita1.png','fantasmita1.png',herramientas[0],'Estatico','askmark.png'))
            elif col=="I":aliadosfree[m].append(allies(x,y,64,64,[0,64],'toad','fantasmita2.png','fantasmita2.png',herramientas[0],'Estatico','askmark.png'))            
    ##obstaculo(self,x,y,tipo,imagen)

            x += 32
        y += 32
        x = 0
##m=0            
##for independent in level:
##    actualmaze(independent,m)
##    m+=1           
def paramaze(m=0):
    for independent in level:
        actualmaze(independent,m)
        m+=1
paramaze()               
run = True
while run:#AQUÍ
    clock.tick(18)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    
    leftbar=menuestatico([['sidebar.jpeg',32*20+10,0]],
                     ['Nivel',str(nivelnumero),'Vidas',str(player.vidas),
                      'Gemas',str(gema),'¿Necesitas ayuda?','Presiona "A"','Créditos:','Cuarteto Dinámico',
                      'P luego R para Pausar','D ver obstaculos y cambiar','entre aliado/jugador','J para ser aliados'],
                     [32*20+30,225,32*20+120,225,
                      32*20+30,250,32*20+120,250,32*20+30,275,32*20+120,275,
                      32*20+30,325,32*20+30,350,32*20+30,400,32*20+30,425,
                      32*20+30,175,32*20+30,125,32*20+30,150,32*20+30,100],
                     [(229, 37, 33),(32*20+0,0,32*20+10,32*15)])        
    if keysdowns[0]:
        if len(aliados)>0:aliados[0].estado='Siguiendo'
        if len(aliados)>1:aliados[1].estado='Siguiendo'
        keypress(player)
    if keysdowns[1]:
        if len(aliados)>0:
            aliados[0].estado='Misionero'
            keypress(aliados[0])
            for obstaculo in obstaculitos[player.actual]:
                if aliados[0].rect.colliderect(obstaculo.rect) and aliados[0].tool.tipo==obstaculo.tipo:
                    obstaculitos[player.actual].remove(obstaculo)
        else:
            validate(keysdowns,0,len(keysdowns))
    if keysdowns[2]:
        if len(aliados)>1:
            aliados[1].estado='Misionero'
            keypress(aliados[1])
            for obstaculo in obstaculitos[player.actual]:
                if aliados[1].rect.colliderect(obstaculo.rect) and aliados[1].tool.tipo==obstaculo.tipo:
                    obstaculitos[player.actual].remove(obstaculo)
        else:
            validate(keysdowns,0,len(keysdowns))
        
    if keys[pygame.K_d]:count +=1
        
    if keys[pygame.K_LSHIFT]:
        validate(keysdowns,3,len(keysdowns))#Mario,aliado,gorro
        x=player.direction.index(True)
        if x==4:gorro.move(gorro.vel, 0)
        elif x==1:gorro.move(-1*gorro.vel, 0)
        elif x==2:gorro.move(0,-1*gorro.vel)
        elif x==3:gorro.move(0,1*gorro.vel)
    else:
        validate(keysdowns,count%3,len(keysdowns))
        gorro.rect.x=player.rect.x+10
        gorro.rect.y=player.rect.y-4
    if keys[pygame.K_p]:
        pause()
        
        

    if player.rect.colliderect(ene[player.actual].rect) and ene[player.actual].direction[0]:
        player.vidas-=1
        player.rect.x=mstartpoints[player.actual][0]
        player.rect.y=mstartpoints[player.actual][1]
    elif gorro.rect.colliderect(ene[player.actual].rect):ene[player.actual].direction[0]=False#hace que no se muestre y que no pueda matar
##    for allie in aliadosfree[player.actual]:
##        if player.rect.colliderect(allie.rect) and allie.estado=='Estatico':print('paraSaol')
    if gorro.rect.colliderect(gemas[player.actual].rect) and (gemas[player.actual].value):
        gema+=1
        gemas[player.actual].value=False
    if gema==9:
        nivelnumero+=1
        level=Uciaproducciones[nivelnumero-1]
        ene,walls,portal,portalvalues,aliadosfree,mstartpoints,obstaculitos,liststrnumeros=restartlists()
        gemas=[]
        player.actual=0
        paramaze()
        player.rect.x=mstartpoints[player.actual][0]
        player.rect.y=mstartpoints[player.actual][1]
        gema=0
    player.teleport()
    if keys[pygame.K_a]:
        window = Tk()
        def f():
               lblEntrada2=Label(text='Seguro que no puedes salir del nivel',font=('Register',8)).place(x=10,y=50)
               en2=StringVar()
               txtEntrada2=Entry(window,textvariable=en2).place(x=10,y=70)
               B2 = Button(window,text="Enviar",command = g).place(x=200,y=70)
##               B2.pack()
        def g():
              lblEntrada3=Label(text='Debes encontrar las 9 gemas ',font=('Register',8)).place(x=10,y=90)
              en3=StringVar()
              txtEntrada3=Entry(window,textvariable=en3).place(x=10,y=110)
              B3 = Button(window,text="Enviar",command = h).place(x=200,y=110)
##              B3.pack()
                
        def h():
             lblEntrada4=Label(text='Fue un gusto ayudarte',font=('Register',8)).place(x=10,y=130)
             en4=StringVar()

        window.geometry('500x350')
        window.title("Aliados")
        lblEntrada=Label(text='Hola, soy tu Aliado y estoy aqui para ayudarte',font=('Register',8)).place(x=10,y=10)
        enE=StringVar()
        
        txtEntrada=Entry(window,textvariable=enE).place(x=10,y=30)

        B = Button(window,text="Enviar",command = f).place(x=200,y=30)

    ##    B.pack()
        window.mainloop() 
          
    if player.vidas== 0 :
        jugando = False
        if jugando == False :
            pygame.mixer.music.stop()
            for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                if keys[pygame.K_q]:
                    pygame.quit()
                    quit()

        
##                if keys[pygame.K_e]:
##                    gameover = False
##                    man.vidas = 3
##                    revive(man)
##                    jugando = True
##                    pygame.mixer.music.play(-1)
    ##AQUÍ
    ene[player.actual].movement()
   
                    
                        
  #  print (mstartpoints)
    redrawGameWindow()

pygame.quit()
