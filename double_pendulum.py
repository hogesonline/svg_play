import math
'''
Appreciation to the coding train who inspired this experiment
https://www.youtube.com/watch?v=uWzPe_S-RVE
'''


#setup basics
#radii
r1 = 100
r2 = 100
#masses
m1 = 5
m2 = 10
#angles
a1 = math.pi/2
a2 = math.pi/4
#velocities
a1_v = 0
a2_v = 0
#accelerations
a1_a = 0
a2_a = 0
#gravity
g = 1

previous_x2 = None
previous_y2 = None


#draw a quarter of a square (symmetry coming)
HEIGHT = 600
WIDTH = 600
header = f'<svg viewBox="-300 -300 {WIDTH} {HEIGHT}" xmlns="http://www.w3.org/2000/svg" style="background-color: #000;">\n'

style = f'''<g>
        <defs>
			<filter id="glow">
				<fegaussianblur class="blur" result="coloredBlur" stddeviation="4"></fegaussianblur>
				<femerge>
					<femergenode in="coloredBlur"></femergenode>
                    <femergenode in="coloredBlur"></femergenode>
                    <femergenode in="coloredBlur"></femergenode>
					<femergenode in="SourceGraphic"></femergenode>
				</femerge>
			</filter>
		</defs>
        '''



def draw_circle(cx, cy, rad, color='black'):
    return f'<circle cx="{cx}" cy="{cy}" r="{rad}" fill="{color}" stroke-width="0"/>'

def draw_line(x_start, y_start, x_end, y_end, color='black'):
    return f'<line x1="{x_start}" y1="{y_start}" x2="{x_end}" y2="{y_end}" stroke="{color}"/>'

def first_point(x,y):
	return f'<path d="M {x}, {y} '

def add_point(x,y):
	return f'L{x}, {y}'

print(header)
print(style)

#make some lines
path = ""

for i in range(2000):
    #increment accelerations (funky formula time)
    num1 = -g * (2 * m1 + m2) * math.sin(a1)
    num2 = -m2 * g * math.sin(a1-2*a2)
    num3 = -2 * math.sin(a1 - a2) * m2
    num4 = a2_v * a2_v * r2 + a1_v * a1_v * r1 * math.cos(a1 - a2)
    den = r1 * (2 * m1 + m2 - m2 * math.cos(2 * a1 - 2 * a2))
    a1_a = (num1 + num2 + num3 * num4) / den /10
    #acceleration 2
    num1 = 2 * math.sin(a1 - a2)
    num2 = (a1_v * a1_v * r1 * (m1 + m2))
    num3 = g * (m1 + m2) * math.cos(a1)
    num4 = a2_v * a2_v * r2 * m2 * math.cos(a1 - a2)
    den = r2 * (2 * m1 + m2 - m2 * math.cos(2 * a1 - 2 * a2))
    a2_a = num1 * (num2 + num3 + num4) / den

    #first pendulum
    x1 = r1 * math.sin(a1)
    y1 = r1 * math.cos(a1)
    # print(draw_line(0, 0, x1, y1))
    # print(draw_circle(x1, y1, m1, color=f'hsl({i*20},100%, 50% )'))
    #second pendulum
    x2 = x1 + r2 * math.sin(a2)
    y2 = y1 + r2 * math.cos(a2)
    #draw the second pendulum
    # print(draw_line(x1, y1, x2, y2))
    # print(draw_circle(x2, y2, m2, color=f'hsl({i*20},50%, 50% )'))
    if previous_x2 == None:
        path += first_point(x2, y2)
    else:
        path += add_point(x2, y2)


    #increase velocity by accel
    a1_v += a1_a
    a2_v += a2_a

    #increase angle
    a1 = (a1 + a1_v) 
    a2 = (a2 + a2_v) 


    previous_x2 = x2
    previous_y2 = y2
    #print()
#end the path off with style
path+= '" style="fill-opacity: 0; stroke-width: 2; stroke: green; filter: url(#glow);"'


print(path)
footer = '</g></svg>'
print(footer)