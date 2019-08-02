import pandas as pd, numpy as np, matplotlib.pyplot as plt
import IPython.display as display

''' 
Full credit to Geoff Boeing whose code I borrowed to form the data frame
https://geoffboeing.com/2015/03/chaos-theory-logistic-map/
'''

class Circle:
    def __init__(self, cx, cy, r, color='black'):
        """Initialize the circle with its centre, (cx,cy) and radius, r.

        icolour is the index of the circle's colour.

        """
        self.cx, self.cy, self.radius = cx, cy, r
        self.color = color


def logistic_model(generations=20, 
                   growth_rate_min=0.5, 
                   growth_rate_max=4.0, 
                   growth_rate_steps=7, 
                   pop_initial=0.5):
    """
    returns a pandas dataframe with columns for each growth rate, row labels for each time step,
    and population values computed by the logistic model: pop[t + 1] = pop[t] * rate * (1 - pop[t])
    
    generations = number of iterations to run the model
    growth_rate_min = the first growth rate for the model, between 0 and 4
    growth_rate_max = the last growth rate for the model, between 0 and 4
    growth_rate_steps = how many growth rates between min (inclusive) and max (exclusive) to run the model on
    pop_initial = starting population when you run the model, between 0 and 1
    """
    
    # convert the growth rate min and max values to floats so we can divide them
    growth_rate_min = float(growth_rate_min)
    growth_rate_max = float(growth_rate_max)
    
    # calculate the size of each step
    growth_rate_step = (growth_rate_max - growth_rate_min) / growth_rate_steps
    
    # we want to go up to but not including the growth_rate_max
    growth_rate_max -= 0.0000000001
    
    # get a range of values to represent each growth rate we're modeling - these will be our columns
    growth_rates = np.arange(growth_rate_min, growth_rate_max, growth_rate_step)
    
    # create a new dataframe with one column for each growth rate and one row for each timestep (aka generation)
    pops = pd.DataFrame(columns=growth_rates, index=range(generations))
    pops.iloc[0] = pop_initial
    
    # for each column (aka growth rate) in the dataframe
    for rate in pops.columns:
        
        # pop is a copy of the pandas series of this column in the dataframe
        pop = pops[rate]
        
        # for each timestep in the number of iterations to run
        for t in range(generations - 1):
            
            # update the dataframe values by running this timestep of the logistic model
            pop[t + 1] = pop[t] * rate * (1 - pop[t])
    
    return pops

def get_bifurcation_points(pops, discard_gens):
    """
    convert a dataframe of values from the logistic model into a set of xy points that
    you can plot as a bifurcation diagram
    
    pops = population data output from the model
    discard_gens = number of rows to discard before keeping points to plot
    """
    
    # create a new dataframe to contain our xy points
    points = pd.DataFrame(columns=['x', 'y'])
    
    # drop the initial rows of the populations data, if specified by the argument
    if discard_gens > 0:
        discard_gens = np.arange(0, discard_gens)
        pops = pops.drop(labels=pops.index[discard_gens])
    
    # for each column in the logistic populations dataframe
    for rate in pops.columns:
        # append the growth rate as the x column and all the population values as the y column
        points = points.append(pd.DataFrame({'x':rate, 'y':pops[rate]}))
    
    # reset the index and drop the old index before returning the xy point data
    points = points.reset_index().drop(labels='index', axis=1)
    return points

def bifurcation_plot(pops, discard_gens=1, xmin=0, xmax=4, ymin=0, ymax=1, height=6, width=10):
    """
    plot the results of the logistic model as a bifurcation diagram
    
    pops = population data output from the model
    discard_gens = number of rows to discard before keeping points to plot
    xmin = minimum value on the x axis
    xmax = maximum value on the x axis
    ymin = minimum value on the y axis
    ymax = maximum value on the y axis
    height = the height of the figure to plot, in inches
    width = the width of the figure to plot, in inches
    """
    
    # first get the xy points to plot
    points = get_bifurcation_points(pops, discard_gens)
    circles = []
    for row in points.itertuples():
        circles.append(Circle(row.x, row.y,2))
        
    return circles

def drawCircle(cx, cy, radius, color):
    return f'<circle cx="{cx}" cy="{cy}" r="{radius}" fill="{color}" stroke-width="0"/>'

def drawStuff(circles, width, mult, color="black"):
    header = f'<svg viewBox="-50 -50 {width} {width}" xmlns="http://www.w3.org/2000/svg">\n'
    print(header)
    for c in circles:
        print(drawCircle(c.cy * mult, c.cx * mult - 3 * mult, c.radius, color))
    footer = f'</svg>'
    print(footer)


if __name__ == "__main__":
    pops = logistic_model(generations=300, growth_rate_min=2.99, growth_rate_max=4, growth_rate_steps=1000)
    circles = bifurcation_plot(pops, discard_gens=200, xmin=2.8, xmax=4)
    drawStuff(circles, 1000, 1000, color='rgb(0,102,0)')

