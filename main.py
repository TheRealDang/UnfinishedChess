import pyglet
import pyglet.window as win
import pyglet.app as app
import pyglet.sprite as spr
import pyglet.image as img
import pyglet.graphics as grc
import pyglet.window.mouse as mou
import os
import time

os.system("cls")

def pth(p):
    return "/".join(__file__.split("\\")[0:len(__file__.split("\\"))-1])+"/"+p

bth = grc.Batch()
scr = win.Window(caption="Chess",resizable=True)

class ins():
    def __init__(self,iga,x=0,y=0,bah=bth,hei=-1,wid=-1,typ='spr'):
        self.ima = img.load(pth(iga))
        self.ima.anchor_x = self.ima.width // 2
        self.ima.anchor_y = self.ima.height // 2
        self.spr=spr.Sprite(self.ima,x,y,batch=bah)
        if hei!=-1:
            self.spr.height=hei
        if wid!=-1:
            self.spr.width=wid
        self.type = typ
    def det(self):
        self.spr.delete()
        self.type="deleted"

def pie(name='pawn',color='w',b =True):
    a = ins(f'ast/{color}_{name}.png',typ = 'pic')
    a.p = name
    a.c = color
    a.f = True
    a.sc = a.spr.width / a.spr.height
    a.cos = False
    a.w = False
    if b:
        p.append(a)
    else:
        return a

c = []
p = []
e = []
pl = ['pawn','rook','knight','bishop','queen','king']
ct = 0

class msi:
    x = 0
    y = 0

for i in range(8):
    for j in range(8):
        ct = (i*8)+(j)
        if (i+j)%2 == 0:
            c.append(ins("ast/bd.png",hei=scr.height/8,wid=scr.height/8,y=scr.height/8*i,typ='brd',x=scr.height/8*j))
        else:
            c.append(ins("ast/bl.png",hei=scr.height/8,wid=scr.height/8,y=scr.height/8*i,typ='brd',x=scr.height/8*j))
        if ct<8:
            if ct < 4:
                pie(pl[ct+1])
            elif ct==4:
                pie(pl[5])
            else:
                pie(pl[8-ct])
        elif ct>55:
            if ct < 60:
                pie(pl[ct-55],'b')
            elif ct==60:
                pie(pl[5],'b')
            else:
                pie(pl[64-ct],'b')
        elif 32<ct<56:
            pie(color='b')
        else:
            pie()
        if 15 < ct < 48:
            p[ct].det()
            p[ct] = 'deleted'

def upc(lst):
    for i in range(len(lst)):
        if lst[i] != 'deleted' and lst[i] != 'deleted_c':
            if lst[i] == 'deleted_c':
                lst[i] = 'deleted'
            else:
                if lst[i].type == 'dia':
                    lst[i].spr.height = scr.height/1.5
                    lst[i].spr.width = scr.height*1.2
                    lst[i].spr.x = scr.width/2
                    lst[i].spr.y = scr.height/2
                elif lst[i].type[0:2] == 'ot':
                    if lst[i].type[2] == '1':
                        lst[i].spr.height = scr.height/150
                        lst[i].spr.width = scr.height*1.2
                        lst[i].spr.x = scr.width/2
                        lst[i].spr.y = scr.height/1.2-scr.height/300
                    if lst[i].type[2] == '2':
                        lst[i].spr.height = scr.height/1.5
                        lst[i].spr.width = scr.height/150
                        lst[i].spr.x = (scr.width - scr.height*1.2)/2+scr.height/300
                        lst[i].spr.y = scr.height/2
                    if lst[i].type[2] == '3':
                        lst[i].spr.height = scr.height/150
                        lst[i].spr.width = scr.height*1.2
                        lst[i].spr.x = scr.width/2
                        lst[i].spr.y = (scr.height-scr.height/1.5)/2+scr.height/300
                    if lst[i].type[2] == '4':
                        lst[i].spr.height = scr.height/1.5
                        lst[i].spr.width = scr.height/150
                        lst[i].spr.x = scr.width-(scr.width-scr.height*1.2)/2-scr.height/300
                        lst[i].spr.y = scr.height/2
                else:
                    if lst[i].type == 'brd':
                        lst[i].spr.height = scr.height/8
                        lst[i].spr.width = scr.height/8
                    elif lst[i].type == 'pic':
                        lst[i].spr.height = scr.height/9
                        lst[i].spr.width = scr.height/9*lst[i].sc
                    lst[i].spr.x = scr.height/8*(i%8)+scr.height/16+(scr.width-scr.height)/2
                    lst[i].spr.y = scr.height/8*(i//8)+scr.height/16

class s:
    c1 = ins('ast/sl.png',typ='brd')
    c2 = ins('ast/sl.png',typ='brd')
    c1.spr.opacity = 255/2.2
    c2.spr.visible = False
    p.append(c1)
    p.append(c2)

class dia:
    #d = ins('ast/dlg.png',typ='dia')
    l1 = ins('ast/dut.png',typ='ot1')
    l2 = ins('ast/dut.png',typ='ot2')
    l3 = ins('ast/dut.png',typ='ot3')
    l4 = ins('ast/dut.png',typ='ot4')
#    e.append(d)
#    e.append(l1)
#    e.append(l2)
#    e.append(l3)
#    e.append(l4)

class g:
    x = 0
    y = 0
    chs = 0
    wrn = True
    class ing:
        mv = []
        x = 0
        y = 0
        cx = 0
        cy = 0
        boo = False
        omov = []

def chk(x,y):
    if -1<x<8 and -1<y<8 and type(p[(x)+y*8]) != type(str()):
        if (p[(x)+y*8].c=='b' and g.wrn) or (p[(x)+y*8].c=='w' and not g.wrn):
            return True
        else:
            return False
    else:
        return False
    
def chl(x,y):
    if -1<x<8 and -1<y<8:
        if type(p[(x)+y*8]) != type(str()):
            return (p[(x)+y*8].c=='b' and g.wrn) or (p[(x)+y*8].c=='w' and not g.wrn)

def mov(name,color,x,y):
    mo = []
    sp = ''
    spl = []
    i = 0
    if name == 'pawn':
        if color == 'w':
            if y == 1:
                for i in range(2):
                    if -1<y+i+1<8 and p[x+(y+i+1)*8] == 'deleted':
                        mo.append(x+(y+i+1)*8)
                    else:
                        break
            else:
                mo.append(x+(y+1)*8)
                if y+i+1 > 7 or p[x+(y+i+1)*8] != 'deleted':
                    mo.pop(-1)
            if chl(x+1,y+1):
                mo.append(x+1+(y+1)*8)
            if chl(x-1,y+1):
                mo.append(x-1+(y+1)*8)
        if color == 'b':
            if y == 6:
                for i in range(2):
                    mo.append(x+(y-i-1)*8)
                    if y-i-1 < 0 or p[x+(y-i-1)*8] != 'deleted':
                        mo.pop(-1)
                        break
            else:
                mo.append(x+(y-1)*8)
                if y-i-1 < 0 or p[x+(y-1)*8] != 'deleted':
                    mo.pop(-1)
            if chl(x+1,y-1):
                mo.append(x+1+(y-1)*8)
            if chl(x-1,y-1):
                mo.append(x-1+(y-1)*8)
    if name == 'rook':
        while x+1+i < 8 and p[(x+i+1)+y*8] == "deleted":
            mo.append((x+i+1)+y*8)
            i+=1
        if chk(x+1+i,y):
            mo.append((x+i+1)+y*8)
        i=0
        while x-1-i > -1 and p[(x-i-1)+y*8] == "deleted":
            mo.append((x-i-1)+y*8)
            i+=1
        if chk(x-1-i,y):
            mo.append((x-i-1)+y*8)
        i=0
        while y+1+i < 8 and p[x+(y+1+i)*8] == "deleted":
            mo.append(x+(y+1+i)*8)
            i+=1
        if chk(x,y+i+1):
            mo.append(x+(y+i+1)*8)
        i=0
        while y-1-i > -1 and p[x+(y-1-i)*8] == "deleted":
            mo.append(x+(y-1-i)*8)
            i+=1
        if chk(x,y-i-1):
            mo.append(x+(y-i-1)*8)
    if name == 'knight':
        if x+1<8 and y+2<8 and p[(x+1)+(y+2)*8] == 'deleted':
                mo.append((x+1)+(y+2)*8)
        if chk(x+1,y+2):
            mo.append((x+1)+(y+2)*8)

        if x-1>-1 and y+2<8 and p[(x-1)+(y+2)*8] == 'deleted':
                mo.append((x-1)+(y+2)*8)
        if chk(x-1,y+2):
            mo.append((x-1)+(y+2)*8)
        
        if x+1<8 and y-2>-1 and p[(x+1)+(y-2)*8] == 'deleted':
                mo.append((x+1)+(y-2)*8)
        if chk(x+1,y-2):
            mo.append((x+1)+(y-2)*8)

        if x-1>-1 and y-2>-1 and p[(x-1)+(y-2)*8] == 'deleted':
                mo.append((x-1)+(y-2)*8)
        if chk(x-1,y-2):
            mo.append((x-1)+(y-2)*8)

        if x+2<8 and y+1<8 and p[(x+2)+(y+1)*8] == 'deleted':
                mo.append((x+2)+(y+1)*8)
        if chk(x+2,y+1):
            mo.append((x+2)+(y+1)*8)

        if x+2<8 and y-1>-1 and p[(x+2)+(y-1)*8] == 'deleted':
                mo.append((x+2)+(y-1)*8)
        if chk(x+2,y-1):
            mo.append((x+2)+(y-1)*8)

        if x-2>-1 and y+1<8 and p[(x-2)+(y+1)*8] == 'deleted':
                mo.append((x-2)+(y+1)*8)
        if chk(x-2,y+1):
            mo.append((x-2)+(y+1)*8)

        if x-2>-1 and y-1>-1 and p[(x-2)+(y-1)*8] == 'deleted':
                mo.append((x-2)+(y-1)*8)
        if chk(x-2,y-1):
            mo.append((x-2)+(y-1)*8)
    if name == 'bishop':
        while x+1+i<8 and y+1+i<8 and p[(x+1+i)+(y+1+i)*8] == 'deleted':
            mo.append((x+1+i)+(y+1+i)*8)
            i += 1
        if chk(x+i+1,y+i+1):
            mo.append((x+i+1)+(y+i+1)*8)
        i=0     
        while x-1-i>-1 and y+1+i<8 and p[(x-1-i)+(y+1+i)*8] == 'deleted':
            mo.append((x-1-i)+(y+1+i)*8)
            i += 1
        if chk(x-i-1,y+i+1):
            mo.append((x-i-1)+(y+i+1)*8)
        i=0
        while x+1+i<8 and y-1-i>-1 and p[(x+1+i)+(y-1-i)*8] == 'deleted':
            mo.append((x+1+i)+(y-1-i)*8)
            i += 1
        if chk(x+i+1,y-i-1):
            mo.append((x+i+1)+(y-i-1)*8)
        i=0
        while x-1-i>-1 and y-1-i>-1 and p[(x-1-i)+(y-1-i)*8] == 'deleted':
            mo.append((x-1-i)+(y-1-i)*8)
            i += 1
        if chk(x-i-1,y-i-1):
            mo.append((x-i-1)+(y-i-1)*8)
        i=0
    if name == 'queen':
        while x+1+i<8 and y+1+i<8 and p[(x+1+i)+(y+1+i)*8] == 'deleted':
            mo.append((x+1+i)+(y+1+i)*8)
            i += 1
        if chk(x+i+1,y+i+1):
            mo.append((x+i+1)+(y+i+1)*8)
        i=0     
        while x-1-i>-1 and y+1+i<8 and p[(x-1-i)+(y+1+i)*8] == 'deleted':
            mo.append((x-1-i)+(y+1+i)*8)
            i += 1
        if chk(x-i-1,y+i+1):
            mo.append((x-i-1)+(y+i+1)*8)
        i=0
        while x+1+i<8 and y-1-i>-1 and p[(x+1+i)+(y-1-i)*8] == 'deleted':
            mo.append((x+1+i)+(y-1-i)*8)
            i += 1
        if chk(x+i+1,y-i-1):
            mo.append((x+i+1)+(y-i-1)*8)
        i=0
        while x-1-i>-1 and y-1-i>-1 and p[(x-1-i)+(y-1-i)*8] == 'deleted':
            mo.append((x-1-i)+(y-1-i)*8)
            i += 1
        if chk(x-i-1,y-i-1):
            mo.append((x-i-1)+(y-i-1)*8)
        i=0
        while x+1+i < 8 and p[(x+i+1)+y*8] == "deleted":
            mo.append((x+i+1)+y*8)
            i+=1
        if chk(x+1+i,y):
            mo.append((x+i+1)+y*8)
        i=0
        while x-1-i > -1 and p[(x-i-1)+y*8] == "deleted":
            mo.append((x-i-1)+y*8)
            i+=1
        if chk(x-1-i,y):
            mo.append((x-i-1)+y*8)
        i=0
        while y+1+i < 8 and p[x+(y+1+i)*8] == "deleted":
            mo.append(x+(y+1+i)*8)
            i+=1
        if chk(x,y+i+1):
            mo.append(x+(y+i+1)*8)
        i=0
        while y-1-i > -1 and p[x+(y-1-i)*8] == "deleted":
            mo.append(x+(y-1-i)*8)
            i+=1
        if chk(x,y-i-1):
            mo.append(x+(y-i-1)*8)
    if name == 'king':
        if x+1 < 8 and y+1 < 8 and p[(x+1)+(y+1)*8] == 'deleted':
            mo.append((x+1)+(y+1)*8)
        if chk(x+1,y+1):
            mo.append((x+1)+(y+1)*8)
        if y+1 < 8 and (p[(x)+(y+1)*8] == 'deleted' or chk(x,y+1)):
            mo.append((x)+(y+1)*8)
        if x-1 > -1 and y+1 < 8 and p[(x-1)+(y+1)*8] == 'deleted':
            mo.append((x-1)+(y+1)*8)
        if chk(x-1,y+1):
            mo.append((x-1)+(y+1)*8)
        if x-1 > -1 and (p[(x-1)+(y)*8] == 'deleted' or chk(x-1,y)):
            mo.append((x-1)+(y)*8)
        if x-1 > -1 and y-1 > -1 and p[(x-1)+(y-1)*8] == 'deleted':
            mo.append((x-1)+(y-1)*8)
        if chk(x-1,y-1):
            mo.append((x-1)+(y-1)*8)
        if y-1 > -1 and (p[(x)+(y-1)*8] == 'deleted' or chk(x,y-1)):
            mo.append((x)+(y-1)*8)
        if x+1 < 8 and y-1 > -1 and p[(x+1)+(y-1)*8] == 'deleted':
            mo.append((x+1)+(y-1)*8)
        if chk(x+1,y-1):
            mo.append((x+1)+(y-1)*8)
        if x+1 < 8 and (p[(x+1)+(y)*8] == 'deleted' or chk(x+1,y)):
            mo.append((x+1)+(y)*8)
        if x== 4 and y == 0 and p[(x+2)+y*8] == 'deleted' and p[(x+1)+y*8] == 'deleted' and type(p[(x+3)+y*8]) != type(str()) and p[(x+3)+y*8].p == 'rook':
            if p[x+y*8].f == True and p[(x+3)+y*8].f == True:
                mo.append((x+2)+y*8)
                sp = 'catw'
                spl.append((x+2)+y*8)
        if x== 4 and y == 0 and p[(x-3)+y*8] == 'deleted' and p[(x-2)+y*8] == 'deleted' and p[(x-1)+y*8] == 'deleted' and type(p[(x-4)+y*8]) != type(str()) and p[(x-4)+y*8].p == 'rook':
            if p[x+y*8].f == True and p[(x-4)+y*8].f == True:
                mo.append((x-2)+y*8)
                sp = 'catw'
                spl.append((x-2)+y*8)
        if x== 4 and y == 7 and p[(x+2)+y*8] == 'deleted' and p[(x+1)+y*8] == 'deleted' and type(p[(x+3)+y*8]) != type(str()) and p[(x+3)+y*8].p == 'rook':
            if p[x+y*8].f == True and p[(x+3)+y*8].f == True:
                mo.append((x+2)+y*8)
                sp = 'catb'
                spl.append((x+2)+y*8)
        if x== 4 and y == 7 and p[(x-3)+y*8] == 'deleted' and p[(x-2)+y*8] == 'deleted' and p[(x-1)+y*8] == 'deleted' and type(p[(x-4)+y*8]) != type(str()) and p[(x-4)+y*8].p == 'rook':
            if p[x+y*8].f == True and p[(x-4)+y*8].f == True:
                mo.append((x-2)+y*8)
                sp = 'catb'
                spl.append((x-2)+y*8)
    print([mo,sp,spl])
    return [mo,sp,spl]

def cow(x,b=120,o=True,l=None):
    x = x[0]
    for i in range(len(x)):
        c[x[i]].spr.color = (b,b,b)
        if l != x[i]:
            if o and p[x[i]] == 'deleted':
                p[x[i]]+='_c'
            elif p[x[i]] == 'deleted_c':
                p[x[i]]='deleted'
            else:
                p[x[i]].w = True
        if not o:
            g.ing.mv = [[],'',[]]

@scr.event
def on_draw():
    g.ing.cx = scr.height/8*(g.ing.x)+scr.height/16+(scr.width-scr.height)/2
    g.ing.cy = scr.height/8*(g.ing.y)+scr.height/16
    scr.set_minimum_size(scr.height+scr.height//2, 1)
    upc(e)
    upc(c)
    upc(p)
    g.x = int((msi.x-(scr.width-scr.height)/2)//(scr.height/8))
    g.y = int(msi.y//(scr.height/8))
    g.chs = int(g.x+g.y*8)
    s.c1.spr.x = ((msi.x-(scr.width-scr.height)/2)//(scr.height/8))*scr.height/8+scr.height/16+(scr.width-scr.height)/2
    s.c1.spr.y = (msi.y//(scr.height/8))*scr.height/8+scr.height/16
    s.c2.spr.x = g.ing.cx
    s.c2.spr.y = g.ing.cy
    g.x = int((msi.x-(scr.width-scr.height)/2)//(scr.height/8))
    g.y = int(msi.y//(scr.height/8))
    if g.x > 8:
        g.x = 8
    if g.y > 7:
        g.y = 7
    g.chs = int(g.x+g.y*8)
    if -1 < g.x < 8 and p[g.chs] != 'deleted':
        if p[g.chs] == 'deleted_c':
            s.c1.spr.visible=True
        elif not((p[g.chs].c == "b" and g.wrn) or (p[g.chs].c == "w" and not g.wrn)):
            s.c1.spr.visible=True
        elif g.ing.mv == []:
            s.c1.spr.visible=False
        elif g.chs in g.ing.mv[0]:
            s.c1.spr.visible=True
        else:
            s.c1.spr.visible=False
    else:
        s.c1.spr.visible=False
    scr.clear()
    bth.draw()

@scr.event
def on_mouse_motion(x, y, dx, dy):
    msi.x = x
    msi.y = y

@scr.event
def on_mouse_press(x,y,button,modifiers):
    if g.ing.boo:
        if g.x<0 or g.x > 7:
            g.ing.boo = False
            cow(g.ing.omov,255,False)
        elif g.x == g.ing.x and g.y == g.ing.y:
            g.ing.boo = False
            cow(g.ing.omov,255,False)
        elif p[g.chs] == 'deleted':
            g.ing.boo = False
            cow(g.ing.omov,255,False)
        elif p[g.chs] == 'deleted_c' or g.chs in g.ing.mv[0]:
            p[g.chs] = pie(p[g.ing.x+g.ing.y*8].p,p[g.ing.x+g.ing.y*8].c,False)
            p[g.chs].f = False
            p[g.ing.x+g.ing.y*8] = 'deleted'
            if g.ing.omov[1] == 'catw' and g.chs in g.ing.omov[2]:
                if g.chs > 4:
                    p[5] = pie('rook',b=False)
                    p[5].f = False
                    p[7] = 'deleted'
                else:
                    p[3] = pie('rook',b=False)
                    p[3].f = False
                    p[0] = 'deleted'
            if g.ing.omov[1] == 'catb' and g.chs in g.ing.omov[2]:
                if g.chs > 60:
                    p[61] = pie('rook','b',b=False)
                    p[61].f = False
                    p[63] = 'deleted'
                else:
                    p[59] = pie('rook','b',b=False)
                    p[59].f = False
                    p[56] = 'deleted'
            upc(p)
            g.ing.boo = False
            cow(g.ing.omov,255,False,g.chs)
            if g.wrn:
                g.wrn = False
            else:
                g.wrn = True
        else:
            if not((p[g.chs].c == "b" and g.wrn) or (p[g.chs].c == "w" and not g.wrn)):
                g.ing.x = g.x
                g.ing.y = g.y
                cow(g.ing.omov,255,False)
                g.ing.omov = mov(p[g.chs].p,p[g.chs].c,g.ing.x,g.ing.y)
                cow(g.ing.omov)
                g.ing.mv = g.ing.omov
            else:
                g.ing.boo = False
                cow(g.ing.omov,255,False)
    elif p[g.chs] != 'deleted' and p[g.chs] != 'deleted_c' and g.x>-1 and g.x<8:
        if not((p[g.chs].c == "b" and g.wrn) or (p[g.chs].c == "w" and not g.wrn)):
            g.ing.x = g.x
            g.ing.y = g.y
            g.ing.boo = True
            g.ing.omov = mov(p[g.chs].p,p[g.chs].c,g.ing.x,g.ing.y)
            cow(g.ing.omov)
            g.ing.mv = g.ing.omov
    s.c2.spr.visible = g.ing.boo

app.run()