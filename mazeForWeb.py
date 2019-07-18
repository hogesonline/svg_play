import random

def drawDiag(x,y,x2,y2,color='black'):
    return f'<line x1="{x}" y1="{y}" x2="{x2}" y2="{y2}" stroke="{color}" />'

def makeMaze(num, color = "black" , height = 500):
    svgOut = ''
    width = height
    header = f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">\n'
    step = height // num
    svgOut += header

    for x in range(0, width, step):
      for y in range(0, height, step):
        
        if random.choice([0,1]) == 0:
            svgOut += drawDiag(x, y, x + step, y + step, color) + '\n'
        else:
            svgOut += drawDiag(x + step, y, x, y + step, color) + '\n'
  

    footer = f'</svg>'
    svgOut += footer
    return svgOut

if __name__ == "__main__":
    makeMaze(50)
