#draw a quarter of a square (symmetry coming)
import random

class Quadrilateral:
    def __init__(self, x1, x2, y1, y2, col):
        '''
        Attributes:
        self.xTL x value of the top left
        self.xBL x value of the bottom left
        self.xTR x value of the top right
        self.xBR x value of the bottom right
        self.yTL y value of the top left
        self.yTR y value of the bottom left
        self.yBL y value of the top right
        self.yBR y value of the bottom right
        self.col color
        '''
        self.xTL = x1
        self.xBL = x1
        self.xTR = x2
        self.xBR = x2
        self.yTL = y1
        self.yTR = y1
        self.yBL = y2
        self.yBR = y2
        self.col = col


        

def draw_quad(quad):
##    M = moveto
##    L = lineto
    return f'<path d="M{quad.xTL} {quad.yTL} \
            L{quad.xTR} {quad.yTR} \
            L{quad.xBR} {quad.yBR} \
            L{quad.xBL} {quad.yBL}Z" stroke="black" fill="{quad.col}"/>'

def make_quadrilaterals(num, imageSize, colors = ('#044BD9', '#0583F2', '#05AFF2', '#05DBF2', '#fa7f70')):
    header = f'<svg viewBox="0 0 {imageSize} {imageSize}" xmlns="http://www.w3.org/2000/svg">\n'
    grid = {}
    quad_size = imageSize/num
    print(header)
    for r in range(num):
        for c in range(num):
            q = None
            q = Quadrilateral(
                            c * quad_size, c * quad_size + quad_size, r * quad_size, 
                            r * quad_size + quad_size, random.choice(colors))
            grid[(r, c)] = q

    #shifting stuff
    for r in range(1, num):
        for c in range(1, num):
            diffx = random.randint(0, quad_size // 2) - quad_size // 4                             
            diffy = random.randint(0, quad_size // 2) - quad_size // 4
            q = grid[(r, c)]
            qUpLeft = grid[(r - 1, c - 1)]
            qUp = grid[(r - 1, c)]
            qLeft = grid[(r, c - 1)]

            #update all 4 quads for the square I'm working with's top left
            q.xTL += diffx
            q.yTL += diffy
            qUpLeft.xBR += diffx
            qUpLeft.yBR += diffy
            qUp.xBL += diffx
            qUp.yBL += diffy
            qLeft.xTR += diffx
            qLeft.yTR += diffy
            print(draw_quad(qUpLeft) )

        print(draw_quad(qUp) )
        
    for c in range(num):
        q = grid[(r, c)]
        print(draw_quad(q) )
    footer = f'</svg>'
    print(footer)


if __name__ == '__main__':
    make_quadrilaterals(30,450)


