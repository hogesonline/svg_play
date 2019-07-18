#rewrite to make it all built out of diagonal lines.
import random

def drawLine(x, y, length, pos, size, sections, topLeftX, topLeftY, sw, sym=False, color='black'):
    '''returns the svg xml for the line
    Params:
    x - starting x value
    y - starting y value
    length - number of squares across and down
    pos - whether the gradient is positive or negative
    size - the size of each square in the grid
    topleftX - the starting point for the tile x value
    topleftY - the starting point for the tile y value
    sw - strokewidth
    sym - whether this is the symmtrical duplicate of another line
    color of the stroke
    '''
    if sym:
        length = -length
    x2 = x + length
    if pos:
        y2 = y - length
    else:
        
        y2 = y + length

    if x2 < 0:
        y2 = y2 + x2
        x2 = 0
    if y2 < 0:
        x2 = x2 + y2
        y2 = 0
    #don't actually know why I need this -- dumb computers
    if sym and pos:
        temp = x2
        x2 = y2
        y2 = temp

    #depending on all the above conditions output the format for the line
    return f'<line x1="{topLeftX + x * size}" y1="{topLeftY + y * size}" x2="{topLeftX + x2 * size}" y2="{topLeftY + y2 * size}" stroke-linecap="square" stroke-width="{sw}" stroke="{color}" />'
    #return f'<line x1="{x * size + topLeftX}" y1="{y * size + topLeftY}" x2="{x2 * size + topLeftX}" y2="{y2 * size + topLeftY}" stroke-linecap="square" stroke-width="{sw}" stroke="{color}" />'


def createLines(sections):
    #Make lines (not actually unique) in the bottom right diagonal half
    #of the bottom quadrant and then repeats in all the places 
    numLines = random.randint(sections // 2, int(sections * 1.5))
    pointSet = set()
    lines = []
    neg = True
    #repeats ignoring duplicate points
    while len(lines) < numLines:
        #get a random even number for x adn y
        x = random.randint(0, sections // 2 - 1) * 2
        y = random.randint(0, x // 2) * 2

        #calculate the maximum length
        top = sections - x - y if x == y and x == 2 else sections-x
        #pick a random length between 1 and the maximum
        length = random.randint(1, top)
        #alternate the positivity of the gradient depending on starting point
        pos = (x in (2, 4)and y in (2, 4))

        if (x, y) not in pointSet:
            lines.append((x, y, length, pos))
            pointSet.add((x, y))
    return lines

def makeTiles(size, tiles ,imageSize, sw=1):
    #takes number of sections in each quadrant (indicates intricacy)
    #tiles is the number of repetitions across and down
    #imagesize is number of pixels across and down but it also affects
    #the relative stroke width --> sw is stroke width
    imagePad = 50
    header = f'<svg viewBox="-{imagePad} -{imagePad} {imageSize + 2 * imagePad} {imageSize + 2 * imagePad}" xmlns="http://www.w3.org/2000/svg">\n'
    print(header)
    tileSize = imageSize / tiles
    padding = imageSize / tiles / 2
    padding = 40
    sections = size
    for row in range(tiles):
        for column in range(tiles):
            #cutting off at the border is not working

            #make a tile quadrant group (without <g> wrapping just yet)
            group = ''
            topLeftX = column * tileSize + padding / 2
            topLeftY = row * tileSize + padding / 2
            #print(topLeftX, topLeftY)
            squareSize = ((tileSize - padding) / size) / 2
            lines= createLines(sections)
            for line in lines:
                #do the same thing (ish) in the four different quadrants
                x,y,length,pos = line
                x1 = x
                y1 = y
                
                #print(x1,y1,length,pos,a,b)
                l = drawLine(x1, y1, length, pos, squareSize, sections, topLeftX, topLeftY, sw)
                group+=l +'\n'
                #x, y, length, pos, size, sections, topLeftX, topLeftY, sw, sym=False, color='black'
                if x != y or pos:
                    x1 = y
                    y1 = x
                    l2 = drawLine(x1, y1, -length, pos, squareSize, sections, topLeftX, topLeftY, sw, sym = True)
                    #x, y, length, pos, size, sections, topLeftX, topLeftY, sw, sym=False, color='black'
                    group+=l2 +'\n'
                    
            #repeat this quadrant 3 more times
            for quad in range(4):
                #convert quad to binary for positioning
                rotation = quad * 90
                rotationX = topLeftX + (tileSize - padding) / 2
                rotationY = topLeftY + (tileSize - padding) / 2
                print(f'<g transform="rotate({rotation} {rotationX} {rotationY})">{group}</g>')



    footer = f'</svg>'                
    print(footer)
    
if __name__ == "__main__":
    #main(7,15,1500)
    makeTiles(10, 10 ,1000, sw=2)

        
