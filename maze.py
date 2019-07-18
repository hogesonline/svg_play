import random

def drawDiag(x, y, x2, y2, color='black'):
	#format a line for svg 
    return f'<line x1="{x}" y1="{y}" x2="{x2}" y2="{y2}" stroke="{color}" />'

def makeMaze(num, color = "black" , height = 500):
	#num is the number of diagonals across and down
	#filename is the output file name
    width = height
    header = f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">\n'
    
    step=height // num
    sv = open(filename, "w")
    #write the header for the file
    print(header)
    #loop through 
    for row in range(0, height, step):
      for col in range(0, width, step):
        #choose a random direction for the diagonal line
        if random.choice([0, 1]) == 0:
        	#write the line
            print(drawDiag(col, row, col + step, row + step, color))
        else:
        	#write the line
            print(drawDiag(col + step, row, col, row + step, color))    
    #write the footer
    footer = f'</svg>'
    print(footer)

if __name__ == "__main__":
    makeMaze(50, color="darkviolet" )
