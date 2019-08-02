#draw a quarter of a square (symmetry coming)
import random

class Curve:
    def __init__(self,num,x,y,r,stroke,large_a_f=0,small_a_f=0,end_x=0,end_y=0):
        self.stroke = stroke
        self.start_x=x
        self.start_y=y
        self.r=r
        self.large_a_f = large_a_f
        self.small_a_f = small_a_f
        self.end_x = end_x
        self.end_y = end_y

    def get_path(self):
        return f'<path d="M {self.start_x} {self.start_y}\
            A {self.r} {self.r} 0 {self.large_a_f} {self.small_a_f} \
            {self.end_x} {self.end_y}" fill="none" stroke="black" \
            stroke-width="{self.stroke}"/>'
           
def main(num,imageSize):
    header = f'<svg viewBox="0 0 {imageSize} {imageSize}" xmlns="http://www.w3.org/2000/svg">\n'
    footer = f'</svg>'
    grid = {}
    c_size = imageSize/num
    print(header)
    for r in range(num):
        for c in range(num):
            n = random.randint(0,4)
            s = 4
            rad = c_size/2
            twos = n//2
            ones = n%2

            x = c * c_size + (rad * int(twos != ones))
            y = r * c_size + rad + (rad * twos) - (rad * ones)	
            end_x=c * c_size + rad + (rad * int(twos != ones))
            end_y=r * c_size + (rad * int(ones)) + (rad * int(twos))
            large_a_f = 1
            small_a_f = 1 * twos
            
              
            curve = Curve(n,x,y,rad,s,large_a_f,small_a_f,end_x,end_y)
            grid[(r,c)] =curve
            print(curve.get_path())
    
        
    print(footer)

if __name__ == '__main__':
    main(10,400)


