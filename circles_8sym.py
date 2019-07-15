import random, sys 
footer = f'</svg>'
randColors = [1,  0]
colours = {0:'black',
           1:'white'}

def drawCirc(x,y,width, height, color='black'):
    r = height/2
    cx = x+(r)
    cy = y+(r)
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}" stroke-width="0"/>'

def createTile(size):
    invader = []
    #only do the first n//2 rows (treating the first n//2 cols first)
    for r in range(size//2+1):
        tempRow = []
        #needed to flip black and white circles
        wasBlack = 0
        for c in range(size//2+1):
            #if on the horizontal or vertical centre or on the diagonal
            #try not to make it too heavy on the black
            if wasBlack>2:
                tempRow.append(1)
                wasBlack = 0
            else:
                if r==c or c==size//2+1 or r==size//2+1 or r<c:
                    col = random.choice(randColors)
                    tempRow.append(col)
                    if col ==0:
                        wasBlack +=1
                    else:
                        wasBlack = 0
                #bottom of diag
                elif r>c:
                    tempRow.append(invader[c][r])
        for c in range(size//2,-1,-1):
            tempRow.append(tempRow[c])
        invader.append(tempRow)
    for r in range(size//2,-1,-1):
        invader.append(invader[r])
    return invader
    
def makeCircleTiles(size, tiles ,imageSize, filename):
    #size is number of sections per tile, tiles is number of tiles, imageSize is
    #how big the image is in pixels
    sv = open(filename+".svg","w")
    header = f'<svg viewBox="0 0 {imageSize} {imageSize}" xmlns="http://www.w3.org/2000/svg">\n'
    sv.write(header)
    tileSize = imageSize/tiles
    padding = 40
    for x in range(tiles):
        for y in range(tiles):
            topLeftX = x*tileSize + padding/2
            topLeftY = y*tileSize + padding/2
            botRightX = topLeftX + tileSize - padding
            botRightY = topLeftY + tileSize - padding
            squareSize = (botRightX-topLeftX)/size
            tile = createTile(size)
            for r in range(len(tile)):
                for c in range(len(tile)):
                    col = tile[r][c]
                    topLeftXTil = c*squareSize + topLeftX
                    topLeftYTil = r*squareSize + topLeftY
                    botRightXTil = topLeftXTil + squareSize
                    botRightYTil = topLeftYTil + squareSize

                    line = drawCirc(topLeftXTil, topLeftYTil, squareSize, squareSize, colours[col])
                    sv.write(line)
    sv.write(footer)
    sv.close()
    
                
   
if __name__ == "__main__":
    #main(7,15,1500)
    makeCircleTiles(17 , 4 ,500, "circleTiles")


        
