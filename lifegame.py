from turtle import*
import random
import time

life = [[0 for i in range(3)]for j in range(3)]
newlife = [[0 for i in range(3)]for j in range(3)]

def init():
    for r in range(3):
        for c in range(3):
            if random.randint(1,2) == 1:
                life[r][c] = 1
            else:
                life[r][c] = 0
def n(r,c) :
    s = 0
    if life[r][c] == 1:
        s -= 1
    for x in [-1,0,1]:
        for y in [-1,0,1]:
            if ( r+x != -1) and ( r+x != 3) and ( c+y != -1) and ( c+y != 3):
                if life[r+x][c+y] == 1:
                    s += 1
    return s

def newn(r,c) :
    t = 0
    if newlife[r][c] == 1:
        t -= 1
    for x in [-1,0,1]:
        for y in [-1,0,1]:
            if ( r+x != -1) and ( r+x != 3) and ( c+y != -1) and ( c+y != 3):
                if newlife[r+x][c+y] == 1:
                    t += 1
    return t

def updatelife():
    for r in range(3):
        for c in range(3):
            if life[r][c] == 1:
                if n(r,c) == 2 or n(r,c) == 3:
                    newlife[r][c] = 1
                else:
                    newlife[r][c] = 0
            elif life[r][c] == 0:
                if n(r,c) == 3:
                    newlife[r][c] = 1
                else:
                    newlife[r][c] = 0
def updatenewlife():
    for r in range(3):
        for c in range(3):
            if newlife[r][c] == 1:
                if newn(r,c) == 2 or newn(r,c) == 3:
                    life[r][c] = 1
                else:
                    life[r][c] = 0
            elif newlife[r][c] == 0:
                if newn(r,c) == 3:
                    life[r][c] = 1
                else:
                    life[r][c] = 0


def draw():
    for a in[0,20,40]:
        for b in [0,-20,-40]:
            grid = Turtle()
            grid.shape("square")
            
            if a == 0:
                c = 0
            elif a == 20:
                c = 1
            elif a == 40:
                c = 2
                
            if b == 0:
                r = 0
            elif b == -20:
                r = 1
            elif b == -40:
                r = 2
                
            if life[r][c] == 1:
                grid.color("black","black")
            else:
                grid.color("black","white")
                
            grid.shapesize(stretch_wid=1,stretch_len=1)
            grid.penup()
            grid.goto(0+a,0+b)

def newdraw():
    for a in[0,20,40]:
        for b in [0,-20,-40]:
            grid = Turtle()
            grid.shape("square")
            
            if a == 0:
                c = 0
            elif a == 20:
                c = 1
            elif a == 40:
                c = 2
                
            if b == 0:
                r = 0
            elif b == -20:
                r = 1
            elif b == -40:
                r = 2
                
            if newlife[r][c] == 1:
                grid.color("black","black")
            else:
                grid.color("black","white")
                
            grid.shapesize(stretch_wid = 1,stretch_len = 1)
            grid.penup()
            grid.goto(0+a,0+b)


init()
life.append(init())                 #打印出 初始life

draw()                              #畫出life
print(life[0])
print(life[1])
print(life[2])
print("new round")
updatelife()                         
newlife.append(updatelife())        #用 life 去更新 updatelife
time.sleep(0.5)

newdraw()                           #畫出newlife
print(newlife[0])                   #打印出 newlife
print(newlife[1])
print(newlife[2])
time.sleep(0.5)

x = 0
while x <= 1 :                      #迴圈(設定要run幾次生命遊戲)
    print("new round")
    updatenewlife()             
    life.append(updatenewlife())    #用 updatelife 去更新 life
    draw()                          #畫出life
    print(life[0])                  #打印出 life
    print(life[1])
    print(life[2])
    print("new round")
    updatelife()                
    newlife.append(updatelife())    #用 life 去更新 updatelife
    time.sleep(0.5)
    newdraw()                       #畫出newlife
    print(newlife[0])               #打印出 updatelife
    print(newlife[1])
    print(newlife[2])
    time.sleep(0.5)
    x += 1

#心得:
#好像大部分情況下細胞都會死光，這或許就代表 "末日終會降臨吧?"
#但有時候細胞會聚集成某種永遠不會被摧毀的聚落，這一定暗示了我們，人類若是要面對即將到來的某種威脅，那就必須要團結一致，才能克服困難