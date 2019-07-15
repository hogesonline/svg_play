import random

def drawRect(x,y,width, height, color='black'):
    return f'<rect x="{x}" y="{y}" width="{width}" height="{height}" fill="{color}" stroke-width="0.5" stroke="{color}"/>'

def drawMondrian(filename,height, width, colors, colornums, step=10):
    header = f'<svg viewBox="0 0 {WIDTH} {HEIGHT}" xmlns="http://www.w3.org/2000/svg">\n'
    footer = f'</svg>'
    sv = open(filename+".svg","w")
    sv.write(header)

    for y in range(0,height, step):
      x = 0
      while x < (width):
        col = random.choice(colors)
        numsq = random.choice(colornums[col])
        w = step*numsq
        if x + w >= width:
            w = width-x
        sv.write(drawSquare(x,y,w,step,col))
        x += w

    sv.write(footer)
    sv.close()

if __name__ == '__main__':
    #colourscheme
    COLORS = ['#f7352f', '#017bfc', '#fad000','black','white',]
    #markov chain like lookup based on mondrian image analysis
    COLORNUMS = {'#f7352f': [1, 2, 2, 1, 1, 1, 14, 7, 4, 2, 2, 1, 1, 2, 1, 1, 15, 1, 4, 11, 3, 1, 1, 12, 1, 2, 7, 1, 27, 1, 2, 8, 2, 14, 1, 15, 1, 7, 1, 2, 18, 2, 18, 2, 2, 2, 1, 2, 1, 14, 2, 1, 4, 2, 3, 2, 2, 5, 5], '#017bfc': [1, 1, 1, 1, 1, 2, 1, 1, 1, 8, 2, 8, 1, 13, 31, 1, 2, 28, 21, 1, 2, 11, 1, 23, 2, 4, 2, 2], '#fad000': [1, 1, 1, 1, 1, 1, 2, 7, 3, 3, 2, 1, 2, 7, 8, 2, 4, 8, 1, 7, 2, 1, 4, 3, 1, 14], 'black': [9, 12, 9, 7, 4, 10, 2, 5, 6, 4, 11, 3, 23, 4, 4, 2, 19, 3, 2, 9, 9, 2, 4, 3, 3, 6, 10, 3, 3, 2, 7, 2, 1, 2, 5, 3, 3, 3, 6, 7, 3, 3, 14, 2, 2, 5, 3, 1, 1, 2, 20, 11, 4, 7, 4, 2, 24, 1, 15, 3, 1, 2, 3, 5, 1, 3, 1, 2, 1, 12, 2, 1, 15, 1, 1, 2, 2, 1, 2, 4, 4, 5, 15, 3, 4, 2, 14, 6, 1, 1, 1, 1, 1, 12, 2, 6, 1, 1, 2, 2], 'white': [1, 3, 2, 1, 3, 2, 17, 2, 17, 1, 1, 1, 1, 2, 1, 9, 19, 1, 6, 1, 1, 4, 1, 5, 4, 1, 23, 2, 8, 1, 1, 5, 3, 1, 3, 1, 2, 2, 1, 2, 4, 2, 5, 3, 2, 1, 6, 1, 1, 8, 14, 2, 3, 5, 1, 2, 9, 1, 8, 1, 1, 3, 1, 3, 1, 13, 2, 1, 7, 7, 1, 25, 1, 1, 1, 11, 3, 10, 1, 12, 1, 1, 3, 14, 12, 1]}

    drawMondrian('Mondrian', 500, 500, COLORS, COLORNUMS)
