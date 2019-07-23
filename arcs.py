#draw a quarter of a square (symmetry coming)
import random

class Curve:
    def __init__(self,num,x,y,r,stroke,largeAF=0,sF=0,endX=0,endY=0):
        self.stroke = stroke
        if num == 0:
            self.circle = True
            self.cx=x
            self.cy=y
            self.r=r
        else:
            self.circle = False
            self.startx=x
            self.starty=y
            self.r=r
            self.largeAF = largeAF
            self.sF = sF
            self.endX = endX
            self.endY = endY

    def getPath(self):
        if self.circle:
            return f'<circle cx="{self.cx}" cy="{self.cy}" r="{self.r}" fill="none" stroke="black" stroke-width="{self.stroke}"/>'
        else:
            return f'<path d="M {self.startx} {self.starty}A {self.r} {self.r} 0 {self.largeAF} {self.sF} {self.endX} {self.endY}" fill="none" stroke="black" stroke-width="{self.stroke}"/>'
           
        


def main(num,imageSize):
    header = f'<svg viewBox="0 0 {imageSize} {imageSize}" xmlns="http://www.w3.org/2000/svg">\n'
    footer = f'</svg>'
    grid = {}
    cSize = imageSize/num
    sv = open("genart5.svg","w")
    sv.write(header)
    for r in range(num):
        for c in range(num):
            n = random.randint(5,8)
            s = 4
            rad = cSize/2
            if n == 0:
                #circle
                cx = c*cSize+cSize/2
                cy = r*cSize+cSize/2
                curve = Curve(n,cx,cy,rad,s)
                print(n,cx,cy,rad,s)
            else:
                if n == 1:
                    #top left arc
                    x = c*cSize
                    y = r*cSize+cSize/2
                    endX=c*cSize+cSize/2
                    endY=r*cSize
                    largeAF=0
                    sF=1
                elif n==2:
                    #top right arc
                    x = c*cSize+cSize/2
                    y = r*cSize
                    endX=c*cSize+cSize
                    endY=r*cSize+cSize/2
                    largeAF=0
                    sF=1
                elif n==3:
                    #botom right arc
                    x = c*cSize+cSize/2
                    y = r*cSize+cSize
                    endX=c*cSize+cSize
                    endY=r*cSize+cSize/2
                    largeAF=0
                    sF=0
                elif n==4:
                    #botom left arc
                    x = c*cSize
                    y = r*cSize+cSize/2
                    endX=c*cSize+cSize/2
                    endY=r*cSize+cSize
                    largeAF=0
                    sF=0
                if n == 5:
                    #top left arc
                    x = c*cSize
                    y = r*cSize+cSize/2
                    endX=c*cSize+cSize/2
                    endY=r*cSize
                    largeAF=1
                    sF=0
                elif n==6:
                    #top right arc
                    x = c*cSize+cSize/2
                    y = r*cSize
                    endX=c*cSize+cSize
                    endY=r*cSize+cSize/2
                    largeAF=1
                    sF=0
                elif n==7:
                    #botom right arc
                    x = c*cSize+cSize/2
                    y = r*cSize+cSize
                    endX=c*cSize+cSize
                    endY=r*cSize+cSize/2
                    largeAF=1
                    sF=1
                elif n==8:
                    #botom left arc
                    x = c*cSize
                    y = r*cSize+cSize/2
                    endX=c*cSize+cSize/2
                    endY=r*cSize+cSize
                    largeAF=1
                    sF=1
                elif n==9:
                    x = c*cSize
                    y = r*cSize+cSize/2
                    endX=c*cSize+cSize
                    endY=r*cSize+cSize/2
                    largeAF=1
                    sF=1
                elif n==10:
                    x = c*cSize
                    y = r*cSize+cSize/2
                    endX=c*cSize+cSize
                    endY=r*cSize+cSize/2
                    largeAF=0
                    sF=0
                elif n==11:
                    x = c*cSize+cSize/2
                    y = r*cSize
                    endX=c*cSize+cSize/2
                    endY=r*cSize+cSize
                    largeAF=0
                    sF=0
                elif n==12:
                    x = c*cSize+cSize/2
                    y = r*cSize
                    endX=c*cSize+cSize/2
                    endY=r*cSize+cSize
                    largeAF=1
                    sF=1
              
                curve = Curve(n,x,y,rad,s,largeAF,sF,endX,endY)
                print(n,x,y,rad,s,1,1,endX,endY)
            grid[(r,c)] =curve
            sv.write(curve.getPath())
    
        
    sv.write(footer)
    sv.close()


if __name__ == '__main__':
    main(4,400)


