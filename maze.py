import random

def drawDiag(x,y,x2,y2,color='black'):
    return f'<line x1="{x}" y1="{y}" x2="{x2}" y2="{y2}" stroke="{color}" />'

def makeMaze(num, filename, colour = "black" , height = 500):
    width = height
    header = f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">\n'
    footer = f'</svg>'
    step=height//num
    sv = open(filename,"w")
    sv.write(header)

    for x in range(0,width, step):
      for y in range(0,height, step):
        #sv.write(drawDiag(x, y, x+step, y+step))
        if random.choice([0,1])==0:
            sv.write(drawDiag(x, y, x+step, y+step, colour))
        else:
            sv.write(drawDiag(x+step, y, x, y+step, colour))    

    sv.write(footer)
    sv.close()

if __name__ == "__main__":
    makeMaze(50, "maze.svg")
