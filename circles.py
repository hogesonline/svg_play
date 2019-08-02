import numpy as np
import random

#original source https://scipython.com/blog/packing-circles-in-a-circle/

class Circle:
    """A little class representing an SVG circle."""

    def __init__(self, cx, cy, r, maxrings=6, icolour=None):
        """Initialize the circle with its centre, (cx,cy) and radius, r.

        icolour is the index of the circle's colour.

        """
        self.cx, self.cy, self.r = cx, cy, r
        self.rings = random.randint(2,maxrings)
        self.icolour = icolour

    def overlap_with(self, cx, cy, r):
        """Does the circle overlap with another of radius r at (cx, cy)?"""

        d = np.hypot(cx-self.cx, cy-self.cy)
        return d < r + self.r

    def draw_circle(self):
        """Write the circle's SVG to the output stream"""
        for _ in range(self.rings-1):
            num = random.randint(1,self.rings)
            gap = self.r/(self.rings+1)
            rad = gap*num
            sw = random.choice([1,1,1,2,2,3])
            print(f'<circle cx="{self.cx}" cy="{self.cy}" r="{rad}" stroke-width="{sw}" class="c{self.icolour}"/>')            
        sw = random.choice([1,1,1,2,2,3])
        print(f'<circle cx="{self.cx}" cy="{self.cy}" r="{self.r}" stroke-width="{sw}" class="c{self.icolour}"/>')

class Circles:
    """A class for drawing circles-inside-a-circle."""

    def __init__(self, width=600, height=600, R=250, n=600, rho_min=0.04,
                 rho_max=0.1, colours=None):
        """Initialize the Circles object.

        width, height are the SVG canvas dimensions
        R is the radius of the large circle within which the small circles are
        to fit.
        n is the maximum number of circles to pack inside the large circle.
        rho_min is rmin/R, giving the minimum packing circle radius.
        rho_max is rmax/R, giving the maximum packing circle radius.
        colours is a list of SVG fill colour specifiers to be referenced by
            the class identifiers c<i>. If None, a default palette is set.

        """

        self.width, self.height = width, height
        self.R, self.n = R, n
        # The centre of the canvas
        self.CX, self.CY = self.width // 2, self.height // 2
        self.rmin, self.rmax = R * rho_min, R * rho_max
        self.colours = colours or ['none']

    def preamble(self):
        """The usual SVG preamble, including the image size."""

        print('<?xml version="1.0" encoding="utf-8"?>\n\n'
        f'<svg xmlns="http://www.w3.org/2000/svg"\n xmlns:xlink="http://www.w3.org/1999/xlink" width="{self.width}" height="{self.height}" >')

    def defs_decorator(func):
        """For convenience, wrap the CSS styles with the needed SVG tags."""

        def wrapper(self):
            print("""
            <defs>
            <style type="text/css"><![CDATA[""")

            func(self)

            print("""]]></style>
            </defs>""")
        return wrapper

    @defs_decorator
    def svg_styles(self):
        """Set the SVG styles: circles are coloured with no border."""

        print('circle {stroke: black;}')
        for i, c in enumerate(self.colours):
            print(f'.c{i} {{fill: {c}; }}')

    def make_svg(self, *args, **kwargs):
        """Create the image as an SVG file with name filename."""

        self.preamble()
        self.svg_styles()
        for circle in self.circles:
            circle.draw_circle()
        print('</svg>')

    def _place_circle(self, r):
        # The guard number: if we don't place a circle within this number
        # of trials, we give up.
        guard = 500
        while guard:
            # Pick a random position, uniformly on the larger circle's interior
            cr, cphi = ( self.R * np.sqrt(np.random.random()),
                         2*np.pi * np.random.random() )
            cx, cy = cr * np.cos(cphi), cr * np.sin(cphi)
            if cr+r < self.R:
            # The circle fits inside the larger circle.
                if not any(circle.overlap_with(self.CX+cx, self.CY+cy, r)
                                    for circle in self.circles):
                    # The circle doesn't overlap any other circle: place it.
                    circle = Circle(cx+self.CX, cy+self.CY, r,
                                icolour=np.random.randint(len(self.colours)))
                    self.circles.append(circle)
                    return
            guard -= 1
        # Warn that we reached the guard number of attempts and gave up for
        # for this circle.
        #print('guard reached.')

    def make_circles(self):
        """Place the little circles inside the big one."""

        # First choose a set of n random radii and sort them. We use
        # random.random() * random.random() to favour small circles.
        self.circles = []
        r = self.rmin + (self.rmax - self.rmin) * np.random.random(
                                self.n) * np.random.random(self.n)
        r[::-1].sort()
        # Do our best to place the circles, larger ones first.
        for i in range(self.n):
            self._place_circle(r[i])

circles = Circles(n=2000)
circles.make_circles()
circles.make_svg()
