#rewrite to make it all built out of diagonal lines.
import random

def drawLine(x, y, length, pos, size, sections, quad, topLeftX, topLeftY, sym=False, color='black', sw=1):
    #this is a bit of a mess. I need to work out the maths for the symmetry
    #so that I can get rid of the if statements
    #this stuff is icky
    pos = (not pos) if (quad//2==0 or quad %2==0)and not(quad//2==0 and quad %2==0) else pos
    length = (-length) if quad%2==0 else length
    if sym and not pos:
        length = -length
    x2 = x+length
    if pos:
        y2 = y-length
    else:
        y2 = y+length
    #this section is to cut off the lines that are too long for the square border
    #if the second x point or y point is outside the bounding box remove the extra
    #but also remove the same amount from the other value in the pair. 
    if (quad//2==0 or quad %2==0)and not(quad//2==0 and quad %2==0):
        if x2>sections*2:
            y2 = y2+(sections*2-x2)
            x2 = sections*2
        elif x2<0:
            y2 = y2-(x2)
            x2 = 0
        if y2>sections*2:
            x2 = x2+(sections*2-y2)
            y2 = sections*2
        elif y2<0:
            x2 = x2-(y2)
            y2 = 0
    else:
        if x2>sections*2:
            y2 = y2-(sections*2-x2)
            x2 = sections*2
        elif x2<0:
            y2 = y2+(x2)
            x2 = 0
        if y2>sections*2:
            x2 = x2-(sections*2-y2)
            y2 = sections*2
        elif y2<0:
            x2 = x2+(y2)
            y2 = 0
    #depending on all the above conditions output the format for the line
    return f'<line x1="{x*size+topLeftX}" y1="{y*size+topLeftY}" x2="{(x2)*size+topLeftX}" y2="{(y2)*size+topLeftY}" stroke-linecap="square" stroke-width="{sw}" stroke="{color}" />'

def createLines(sections):
    #Make lines (not actually unique) in the bottom right diagonal half
    #of the bottom quadrant and then repeats in all the places 
    numLines = random.randint(sections//2,int(sections*1.5))
    pointSet = set()
    lines = []
    neg = True
    #repeats ignoring duplicate points
    while len(lines)<numLines:
        x = random.randint(0,sections//2-1)*2
        y = random.randint(0,x//2)*2
        top = sections-x-y if x==y==2 else sections-x
        length = random.randint(1,top)
        pos = (x in (2,4)and y in (2,4))
        if (x,y) not in pointSet:
            lines.append((x,y,length,pos))
            pointSet.add((x,y))
    return lines

def makeTiles(size, tiles ,imageSize, filename, sw=1):
    #takes number of sections in each quadrant (indicates intricacy)
    #tiles is the number of repetitions across and down
    #imagesize is number of pixels across and down but it also affects
    #the relative stroke width --> sw is stroke width
    sv = open(filename,"w")
    header = f'<svg viewBox="-50 -50 {imageSize+100} {imageSize+100}" xmlns="http://www.w3.org/2000/svg">\n'
    footer = f'</svg>'
    sv.write(header)
    tileSize = imageSize/tiles
    padding = imageSize/tiles/2
    sections = size
    for row in range(tiles):
        for column in range(tiles):
            #cutting off at the border is not working
            topLeftX = column*tileSize + padding/2
            topLeftY = row *tileSize + padding/2
            #print(topLeftX, topLeftY)
            squareSize = ((tileSize - padding)/size)/2
            lines= createLines(sections)
            for quad in range(4):
                for line in lines:
                    a = int(quad//2==0)
                    b = int(quad%2==0)
                    #do the same thing (ish) in the four different quadrants
                    x,y,length,pos = line
                    x1 = abs(sections*2*b-x)
                    y1 = abs(sections*2*a-y)
                    
                    #print(x1,y1,length,pos,a,b)
                    l = drawLine(x1,y1,length,pos, squareSize, sections, quad, topLeftX, topLeftY, sw=sw)
                    sv.write(l)
                    if not (x==y and not pos):
                        x1 = abs(sections*2*a-y)
                        y1 = abs(sections*2*b-x)
                        l2 = drawLine(x1,y1,-length,pos, squareSize, sections, quad, topLeftX, topLeftY, sym = True, sw=sw)
                        sv.write(l2)
                        #print(l2)
                
    sv.write(footer)
    sv.close()
    
if __name__ == "__main__":
    #main(7,15,1500)
    makeTiles(10, 10 ,1000,'diagTiles.svg', sw=2)

        
