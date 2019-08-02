import math, random

def draw_line(x, y, x2,  y2, color=(0, 100, 0), sw=1):
    return f'<line x1="{x}" y1="{y}" x2="{x2}" y2="{y2}" \
    style="stroke:hsl({str(color[0])+","+str(color[1])+"%,"+str(color[2])+"%"});\
    stroke-width:{sw}" />'

def draw_tree(x1, y1, angle, depth, col):
    '''
    Makes a recursive randomised tree
    Params:
    x1 - the starting x
    y1 - the starting y
    angle - the direction from the vertial - allows for rotation around an origin
    depth - how many iterations
    col - colour
    '''
    if depth:
        x2 = x1 + int(math.cos(math.radians(angle)) * depth * 10.0)
        y2 = y1 + int(math.sin(math.radians(angle)) * depth * 10.0)
        print(draw_line(x1, y1, x2, y2, color=(col)))
        diffA = random.randint(-5, 5) * 3
        diffB = random.randint(-5, 5) * 3
        draw_tree(x2, y2, angle - diffA, depth - 1, (col[0], col[1], col[2] + 5))
        draw_tree(x2, y2, angle + diffB, depth - 1, (col[0], col[1], col[2] + 5))

def make_tree_circle(width, color):
    '''Makes a circle full of randomised recursively drawn trees in a particular colour

    Params:
    width - the diameter fo the resulting circle
    color: the hsl values of the centre colour as a tuple
    '''
    header = f'<svg viewBox="0 0 {width} {width}" xmlns="http://www.w3.org/2000/svg">\n'
    print(header)

    for angle in range(0, 360, 10):

        #draw_tree(600, 600, angle, 10, (212,100,30))
        draw_tree(width // 2, width // 2, angle, 10, color)
    footer = f'</svg>'
    print(footer)

if __name__ == '__main__':
    make_tree_circle(1200, (267, 93, 42))

