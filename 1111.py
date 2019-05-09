#coding=utf-8
import time 
import copy as copy

#舞台所有方块，默认为全部空
stageWidth = 6
stageHeight = 6

#方块横条
block1 =[[1,1,1,1],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
block1_1 =[[0,0,0,1],[0,0,0,1],[0,0,0,1],[0,0,0,1]]
block1_2 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[1,1,1,1]]
block1_3 = [[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]]

#方块右L
block2 = [[1,0,0,0],[1,0,0,0],[1,1,0,0],[0,0,0,0]]
block2_1 = [[0,1,1,1],[0,1,0,0],[0,0,0,0],[0,0,0,0]]
block2_2 = [[0,0,0,0],[0,0,1,1],[0,0,0,1],[0,0,0,1]]
block2_3 = [[0,0,0,0],[0,0,0,0],[0,0,1,0],[1,1,1,0]]

#方块左L
block3 = [[0,1,0,0],[0,1,0,0],[1,1,0,0],[0,0,0,0]]
block3_1 = [[0,1,0,0],[0,1,1,1],[0,0,0,0],[0,0,0,0]]
block3_2 = [[0,0,0,0],[0,0,1,1],[0,0,1,0],[0,0,1,0]]
block3_3 = [[0,0,0,0],[0,0,0,0],[1,1,1,0],[0,0,1,0]]

#方块田
block4 = [[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]]
block4_1 =[[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]]
block4_2 =[[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]]
block4_3 =[[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]]

#方块T
block5 = [[1,1,1,0],[0,1,0,0],[0,0,0,0],[0,0,0,0]]
block5_1 = [[0,0,0,1],[0,0,1,1],[0,0,0,1],[0,0,0,0]]
block5_2 = [[0,0,0,0],[0,0,0,0],[0,0,1,0],[0,1,1,1]]
block5_3 = [[0,0,0,0],[1,0,0,0],[1,1,0,0],[1,0,0,0]]

#方块Z
block6 = [[1,1,0,0],[0,1,1,0],[0,0,0,0],[0,0,0,0]]
block6_1 = [[0,0,0,1],[0,0,1,1],[0,0,1,0],[0,0,0,0]]
block6_2 = [[0,0,0,0],[0,0,0,0],[0,1,1,0],[0,0,1,1]]
block6_3 = [[0,0,0,0],[0,1,0,0],[1,1,0,0],[1,0,0,0]]

#方块反Z
block7 = [[0,1,1,0],[1,1,0,0],[0,0,0,0],[0,0,0,0]]
block7_1 = [[0,0,1,0],[0,0,1,1],[0,0,0,1],[0,0,0,0]]
block7_2 = [[0,0,0,0],[0,0,0,0],[0,0,1,1],[0,1,1,0]]
block7_3 = [[0,0,0,0],[1,0,0,0],[1,1,0,0],[0,1,0,0]]

#所有方块方向组合
b1 = [block1,block1_1,block1_2,block1_3]
b2 = [block2,block2_1,block2_2,block2_3]
b3 = [block3,block3_1,block3_2,block3_3]
b4 = [block4,block4_1,block4_2,block4_3]
b5 = [block5,block5_1,block5_2,block5_3]
b6 = [block6,block6_1,block6_2,block6_3]
b7 = [block7,block7_1,block7_2,block7_3]

class Point(object):
    """docstring for Point"""
    def __init__(self, x,y):
        super(Point, self).__init__()
        self.x = x
        self.y = y

    def getX():
        return self.x
    def setX(self,x):
        self.x = x

    def getY():
        return self.y
    def setY(self,y):
        self.y = y

    def printXY(self):
        print "X:"+str(self.x)+",Y:"+str(self.y)

class BlockSprite(object):
    """docstring for BlockSprite"""
    def __init__(self, block,point):
        super(BlockSprite, self).__init__()
        self.block = block
        self.point = point

def lmin(block):
    l_min = None
    for i in range(0, len(block)):
        for j in range (0, 4):
            #print "j:"+str(j)+",i:"+str(i)
            #print block[j][i]
            if block[j][i] == 1:
                #print "左横坐标i:",i
                l_min = i
                break
        if l_min != None:
            break
    #print "l_min:",l_min
    return l_min

def rmax(block):
    b = copy.deepcopy(block)
    for i in range(0,len(b)):
        b[i].reverse()
    #print block
    l_min = lmin(b)
    r_max = 3-l_min
    #print "r_max:",r_max
    return r_max

def bottomMin(block):
    b = copy.deepcopy(block)
    b.reverse()
    bottom_min = None
    for i in range(0, len(b)):
        for j in range (0, 4):
            if b[i][j] == 1:
                bottom_min = i
                break
        if bottom_min != None:
            break
    bottom_min = 3-bottom_min
    #print "bottom_min:",bottom_min
    return bottom_min

def checkIsBump(sprite,stage):
    nowStage = copy.deepcopy(stage)
    x = sprite.point.x
    y = sprite.point.y
    print "x",x
    print "y",y
    x1 = rmax(sprite.block)
    print "x1",x1
    for i in range(0,len(sprite.block)):
        b = sprite.block[i]
        print "b:",b
        n = 0
        for j in range (x, x1):
            # print "b[n]",b[n]
            # print "y",y
            print "j",j
            # print "stage[y][j]",stage[y][j]
            if b[n] == 1 and stage[y][j] == 2:
                print "固定方块会碰撞"
                return True
            else:
                nowStage[y][j]=b[n]
                #在下一个方块出现之前让下落方块编程固定方块
            n = n+1
        y = y-1
    print "nowStage:",nowStage
    return False

def createStage(stageWidth,stageHeight):
    stage = []
    for y in range (0,stageHeight):
        x_l = []
        for x in range(0, stageWidth):
            x_l.append(0)
        stage.append(x_l)
    return stage

#在做updateStage之前要重新createStage       
def updateStage(sprite):
    nowStage = copy.deepcopy(stage)
    x = sprite.point.x
    y = sprite.point.y
    '''
    这部分是对下落的方块进行更新
    '''
    for i in range(0,len(sprite.block)):
        b = sprite.block[i]
        n = 0
        for j in range (x, x+4):
            if b[n] == 1:
                nowStage[y][j]=b[n]
            n = n+1
        y = y-1
    print "nowStage:",nowStage

def checkIsLeftBump(sprite):
    l_min = lmin(sprite.block)
    if sprite.point.x + l_min > 0:
        return False
    else:
        print "左撞墙"
        return True

def checkIsRightBump(sprite):
    r_max= rmax(sprite.block)
    t = sprite.point.x +r_max
    if t < stageWidth-1:
        return False
    else:
        print "右撞墙"
        return True

def checkIsBottomBump(sprite):
    bottom_min = bottomMin(sprite.block)
    t = sprite.point.y-bottom_min
    if t >= 0:
        return False
    else:
        print "底部撞墙"
        return True

#左键被执行,以0～7表示宽度，从左到右
def letfEvent(sprite,stage):
    shadowSprite = copy.deepcopy(sprite)
    if checkIsLeftBump(sprite):
        print "Bump!"
        return True
    else:
        shadowSprite.point.x = shadowSprite.point.x - 1
        if checkIsBump(shadowSprite, stage):
            print "Bump!"
            return True
        else:
            print "Move to left!"
            sprite.point.x = sprite.point.x - 1
            return False

#右键被执行
def rightEvent(sprite, stage):
    shadowSprite = copy.deepcopy(sprite)
    if checkIsRightBump(sprite):
        print "Bump!"
        return True
    else:
        shadowSprite.point.x = shadowSprite.point.x + 1
        if checkIsBump(shadowSprite, stage):
            print "Bump!"
            return True
        else:
            print "Move to right!"
            sprite.point.x = sprite.point.x + 1
            return False

#下降被执行，从下到上表示高度，从0开始
def downEvent(sprite,stage):
    shadowSprite = copy.deepcopy(sprite)
    if checkIsBottomBump(sprite):
    shadowSprite.point.y = shadowSprite.point.y - 1
    if checkIsBump(shadowSprite, stage) or checkIsBottomBump(sprite):
        print "Bump!"
        return True
    else:
        print "Move to down!"
        sprite.point.y = sprite.point.y - 1
        return False


def setTopBlock(block):
    b = copy.deepcopy(block)
    for i in range(0, len(b)):
        isum = 0
        for j in range(0, 4):
            #print "i:"+str(i)+",j:"+str(j)
            isum = isum + b[i][j]
        #print isum 
        if isum == 0:
            block.remove(b[i]) 
    #print block 
    if len(block) >0 and len(block) <4:      
        for i in range(0, 4-len(block)):
            b = []
            for j in range (0, 4):
                b.append(0)
            block.append(b)
    #print block
    return block

#旋转事件？？？从0开始计数,这个方法不好，原因是
def upEvent(blocklist,count):
    count = count % 4
    print "count:",count
    block = blocklist[count]
    count = count +1
    print block
    return count


def getGroundHeight(stage):
    h = 0
    for i in range(0, len(stage)):
        #print stage[i]
        for j in range(0, len(stage[i])):
            #print stage[i][j]
            if stage[i][j] == 2:
                h = i+1
                #print "h:",h
                break
        if h != 0:
            break
    return h


#假设方块不能变化,假设方块一直位于中间，则横条所在区域的正方形的角坐标,则应该替换stage里的对应位置
x1y1 = [(stageWidth - 4)/2,stageHeight-1]
x2y2 = [(stageWidth - 4)/2 + 3,stageHeight-1]
x3y3 = [(stageWidth - 4)/2,stageHeight-4]
x4y4 = [(stageWidth - 4)/2 + 3,stageHeight-4]

# print x1y1
# print x2y2
# print x3y3
# print x4y4

stage = createStage(stageWidth, stageHeight)
# print stage

block = setTopBlock(b7[0])
print block

p1 = Point((stageWidth - 4)/2,stageHeight-1)



sprite = BlockSprite(block, p1)
print sprite.block
print sprite.point.x
print sprite.point.y

print "set"
sprite.point.y = 2
#print bottomMin(sprite.block)
#如果发现方块的位置和舞台固定方块的位置重合，那肯定就不能放了

stage[0][0] = 2
stage[0][1] = 2
stage[1][0] = 2
# stage[0][2] = 2
# stage[1][1] = 2
#print "stage:",stage
#updateStage(sprite)

print "sprite.point.x:",sprite.point.x
print "sprite.point.y:",sprite.point.y
# letfEvent(sprite, stage)
# letfEvent(sprite, stage)
# letfEvent(sprite, stage)
# downEvent(sprite, stage)
# downEvent(sprite, stage)
rightEvent(sprite, stage)
rightEvent(sprite, stage)
# rightEvent(sprite, stage)
print "sprite.point.x:",sprite.point.x
print "sprite.point.y:",sprite.point.y



















    




    












