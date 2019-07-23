from PIL import Image


class Circle:
    def __init__(self,cx,cy,pixels, topL):
        '''Attributes:
            self.topL - top Left
            self.cx - centre x value
            self.cy - centre y value
            self.rad  - radius of the circle
            self.pixels - this is a PIL image that contains just the pixels relevant to this circle
            self.avg_col - calls a function to get the average pixel colour for the pixels
            self.colour - stores the colour of the centre pixel in pixels
            self.pixelDiff - calls a function that finds the difference between the average colour for the image and the centre colour

        '''

        self.topL = topL
        self.cx = cx
        self.cy = cy
        self.rad = pixels.width/2
        self.pixels = pixels
        self.avg_col = self.getAvgCol()
        self.colour = pixels.getpixel((pixels.width//2, pixels.height//2))
        self.pixelDiff = self.getDiff()
        
        #print(self.colour)

    def getDiff(self):
        #Gets the difference between 2 colours. 
        #Does this by finding the difference between red, blue and green values and adding them
        r,g,b = self.avg_col
        r1,g1,b1 = self.colour
        
        return abs(r-r1)+abs(g-g1)+abs(b-b1)

    def getAvgCol(self):
        #finds the average colour for a set of pixels by adding them to 3 different lists and averaging red, green and blue separately
        red = []
        green = []
        blue = []
        for y in range(self.pixels.height):
            for x in range(self.pixels.width):
                pixel = self.pixels.getpixel((x, y))
                r, g, b = pixel
                red.append(r)
                green.append(g)
                blue.append(b)
        if len(red) ==0:
            return 0
        return sum(red)/len(red),sum(green)/len(green),sum(blue)/len(blue)


def drawCircle(cx,cy,radius, colour):
    return f'<circle cx="{cx}" cy="{cy}" r="{radius}" fill="rgb{colour}" stroke-width="0"/>'

def getMax(circles):
    #find the circle with the largest difference between colour and average colour. It will be the next circle to be split
    #I think there must be a better way to do this, As the circles get smaller, on things like stripes the difference between
    #centre pixel and average pixel color gets bigger again
     
    maxDiff = None
    index = 0
    temp=[]
    for i in range(len(circles)):
        pD = circles[i].pixelDiff
        temp.append(str(pD))
        if maxDiff is None or pD>maxDiff:
            maxDiff = pD
            index = i
    return maxDiff,index

def analysePic(im):
    #this should definitely be recursive
    #biggest circle
    topL = (0,0)
    cx = im.width//2
    cy = im.height//2
    pixels = im.crop((0,0,im.width, im.height))
    circles = [Circle(cx,cy,pixels,topL)]
    #set up the first 4 quadrants
    radius = im.width//2
    index = 0
    #split the new circle
    newCircle = circles.pop(index)
    maxDiff = newCircle.pixelDiff
    #repeat until the radius gets to 5
    while radius >2:
        old_topL = newCircle.topL
        topLx, topLy = old_topL
        im = newCircle.pixels
        radius = im.width//4
        #c1
        topL1 = old_topL
        cx = im.width//4
        cy = im.height//4
        im1 = im.crop((0,0,im.width//2, im.height//2))
        circles.append(Circle(cx,cy,im1,topL1))
        #c2
        #topL2 = old_topL[0]+radius*2,old_topL[1]
        topL2 = topLx+im.width//2,topLy
        cx = im.width//4
        cy = im.height//4
        im2 = im.crop((im.width//2,0,im.width, im.height//2))
        circles.append(Circle(cx,cy,im2,topL2))
        #c3
        #topL3 = old_topL[0],old_topL[1]+radius*2
        topL3 = topLx,topLy+im.height//2
        cx = im.width//4
        cy = im.height//4
        im3 = im.crop((0,im.height//2,im.width//2,im.height ))
        circles.append(Circle(cx,cy,im3,topL3))
        #c4
        topL4 = topLx+im.width//2,topLy+im.height//2
        cx = im.width//4
        cy = im.height//4
        im4 = im.crop((im.width//2,im.height//2,im.width, im.height))
        circles.append(Circle(cx,cy,im4,topL4))
        maxDiff, index = getMax(circles)
        #split the new circle
        newCircle = circles.pop(index)
    #put the final circle back
    circles.append(newCircle)
    return circles
    
    

def picCircles(image, filename):
    im = Image.open(image)
    width = im.width
    height = im.height
    header = f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">\n'
    footer = f'</svg>'
    
    sv = open(filename+".svg","w")
    sv.write(header)
    circles = analysePic(im)
    
    for circle in circles:
        topLx,topLy = circle.topL
        sv.write(drawCircle(circle.cx+topLx, circle.cy+topLy, circle.rad, circle.colour))
    sv.write(footer)
    sv.close

if __name__ == '__main__':
    picCircles("gerberas.jpeg",'flower')
    picCircles("rose2.jpg",'rose')
    picCircles("zebra.jpg",'zebra')

