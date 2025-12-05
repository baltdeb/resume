'''
Deborah Baltazar-Zuniga

I have attempt to make barbie pink house with a BEAUTIFUL night time scenery!

'''

from turtle import *

# loads the Turtle graphics module, which is a built-in library in Python
import turtle
import math

def setup_turtle():
    """Initialize turtle with standard settings"""
    t = turtle.Turtle()
    t.speed(10)  # Fastest speed
    screen = turtle.Screen()
    screen.title("Turtle Graphics Assignment")
    return t, screen


def draw_rectangle(t, width, height, fill_color=None):
    """Draw a rectangle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    if fill_color:
        t.end_fill()

def draw_square(t, size, fill_color=None):
    """Draw a square with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    if fill_color:
        t.end_fill()


def draw_triangle(t, size, fill_color=None):
    """Draw an equilateral triangle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    if fill_color:
        t.end_fill()


def draw_circle(t, radius, fill_color=None):
    """Draw a circle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    t.circle(radius)
    if fill_color:
        t.end_fill()


def draw_polygon(t, sides, size, fill_color=None):
    """Draw a regular polygon with given number of sides"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    angle = 360 / sides
    for _ in range(sides):
        t.forward(size)
        t.right(angle)
    if fill_color:
        t.end_fill()

def draw_curve(t, length, curve_factor, segments=10, fill_color=None):
    """
    Draw a curved line using small line segments
    
    Parameters:
    - t: turtle object
    - length: total length of the curve
    - curve_factor: positive for upward curve, negative for downward curve
    - segments: number of segments (higher = smoother curve)
    - fill_color: optional color to fill if creating a closed shape
    """
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
        
    segment_length = length / segments
    # Save the original heading
    original_heading = t.heading()
    
    for i in range(segments):
        # Calculate the angle for this segment
        angle = curve_factor * math.sin(math.pi * i / segments)
        t.right(angle)
        t.forward(segment_length)
        t.left(angle)  # Reset the angle for the next segment
    
    # Reset to original heading
    t.setheading(original_heading)
    
    if fill_color:
        t.end_fill()
        
def jump_to(t, x, y):
    """Move turtle without drawing"""
    t.penup()
    t.goto(x, y)
    t.pendown()



def draw_house(t,scale=1.0, x=None, y=None): 
        """Draw the house scaled by `scale` anchored at (x,y).
        If x,y are None the current turtle position is used as the house origin."""
        # remember current position to restore later
        orig_x, orig_y = t.position()
        # choose origin
        if x is None or y is None:
            x0, y0 = orig_x, orig_y
        else:
            x0, y0 = x, y

        # draw scaled base (same anchor as original)
        jump_to(t, x0, y0)
        draw_rectangle(t, 350 * scale, 300 * scale, "deeppink1")

        # draw scaled roof using same anchor so placement matches original
        jump_to(t, x0, y0)
        draw_triangle(t, 350 * scale, "pink")

        # restore turtle position
        jump_to(t, orig_x, orig_y)

def draw_tree(t, x, y, scale=1.0, trunk_color="brown", foliage_color="orange"):
        # trunk top-left at (x,y)
        jump_to(t, x, y)
        draw_rectangle(t, 40 * scale, 200 * scale, trunk_color)
        # foliage centered horizontally above trunk top; ensure circle's bottom touches trunk top
        fx = x + (40 * scale) / 2
        # When calling turtle.circle(radius) from point P, the circle's bottommost point is at P.y.
        # So start the circle at (fx, y) so the circle's bottom touches the trunk top (y) with no gap.
        orig_heading = t.heading()
        t.setheading(0)
        jump_to(t, fx, y)
        draw_circle(t, 57 * scale, foliage_color)
        t.setheading(orig_heading)

def draw_stars(t, star_list, double=False, offset_y=20):
        """Draw stars given list of (x, y, size, color).
        If double is True, draw a second row offset by offset_y above the originals."""
        for x, y, size, color in star_list:
            jump_to(t, x, y)
            draw_circle(t, size, color)
        if double:
            for x, y, size, color in star_list:
                jump_to(t, x, y + offset_y)
                draw_circle(t, size, color)

    # original star positions/sizes/colors
stars = [
        (-250, 270, 3, "white"),
        (-200, 270, 2, "light yellow"),
        (50, 260, 4, "white"),
        (200, 300, 3, "light yellow"),
        (280, 290, 2, "white"),
    ]

def rects_overlap(a, b):
        """Return True if rect a and b overlap. Rect format: (min_x, min_y, max_x, max_y)."""
        return not (a[2] <= b[0] or a[0] >= b[2] or a[3] <= b[1] or a[1] >= b[3])

def flower_bbox(t, x, y, petal_size):
        """Approximate flower bounding box from center and petal_size."""
        r = petal_size + petal_size * 0.5  # margin for petals
        return (x - r, y - r, x + r, y + r)

def draw_flower(t, x, y, petal_count=6, petal_size=20, petal_color="pink", center_color="yellow"):
        """Draw one flower centered at (x,y). Restores turtle heading/position."""
        orig_x, orig_y = t.position()
        orig_heading = t.heading()

        jump_to(t, x, y)
        for i in range(petal_count):
            draw_polygon(t, 6, petal_size, petal_color)
            t.right(360 / petal_count)

        jump_to(t, x, y - (petal_size * 0.3))
        draw_circle(t, petal_size * 0.33, center_color)

        jump_to(t, orig_x, orig_y)
        t.setheading(orig_heading)

def plant_flower_field(t, count=5, petal_size=20, spacing_x=90, spacing_y=70, search_bounds=(-340, -260, 340, 40)):
        """
        Plant up to `count` flowers (max 5) in free space inside search_bounds,
        avoiding overlap with main scene objects (house, trees, moon).
        search_bounds: (min_x, min_y, max_x, max_y)
        """
        count = max(0, min(count, 5))

        # conservative occupied regions (min_x, min_y, max_x, max_y)
        occupied = []
        # House: large conservative rectangle around the house+roof
        occupied.append((-30, -350, 400, 220))
        # Tree 1 trunk and foliage (from draw_tree(-250,150), scale 1)
        occupied.append((-287, 104, -173, 218))  # foliage
        occupied.append((-250, -50, -210, 150))  # trunk
        # Tree 2 (draw_tree(-120,130, scale=0.5))
        # trunk: (-120,130) width 20 height 100 -> x [-120,-100], y [30,130]
        occupied.append((-138.5, 106.5, -81.5, 164))  # foliage (center -110,135.5 radius ~28.5)
        occupied.append((-120, 30, -100, 130))        # trunk
        # Moon at (-50,200) radius 80
        occupied.append((-130, 120, 30, 280))

        placed = 0
        min_x, min_y, max_x, max_y = search_bounds

        # generate grid positions attempting to place flowers in available free spaces
        y = max_y - petal_size  # start near top of search area and go downward
        while y >= min_y and placed < count:
            x = min_x + petal_size
            while x <= max_x - petal_size and placed < count:
                fb = flower_bbox(t, x, y, petal_size)
                # check overlap with any occupied region
                if not any(rects_overlap(fb, occ) for occ in occupied):
                    # place flower
                    petal_col = "light pink" if (placed % 2 == 0) else "pink"
                    draw_flower(t, x, y, petal_count=6, petal_size=petal_size, petal_color=petal_col)
                    placed += 1
                x += spacing_x
            y -= spacing_y


#YOU MUST add function calls in this draw_scence function defintion
# to create your scence (No statements outside of function definiions)
def draw_scene(t):
    """Draw a colorful scene with various shapes"""
    # Set background color
    screen = t.getscreen()
    screen.bgcolor("midnight blue")
    # " making a barbie house"
    # draw default-sized house at the original location
    draw_house(t, scale=1.0)

    
    # helper to draw a tree so we can place multiple copies


    # original tree (keeps existing placement)
    draw_tree(t, -250, 150, scale=1.0)

    # second tree moved to a different location (smaller example)
    draw_tree(t, -120, 130, scale=0.5)

    jump_to(t, -50, 200)
    #moon 
    draw_circle(t, 80, "white")

    # making stars

    # draw stars and double them on top
    draw_stars(t, stars, double=True, offset_y=25)

    # reusable flower & field helpers (avoid overlapping important scene objects)
   

    # plant up to 5 flowers using free space (search bounds chosen to avoid house, moon, trees)
    plant_flower_field(t, count=5, petal_size=18, spacing_x=100, spacing_y=70,
                       search_bounds=(-340, -260, -40, 0))

def new_func(t):
    draw_rectangle(t,40, 200, "brown")
    jump_to(t,-230,150)
    draw_circle(t, 57, "orange")


    



    
    

# This is the main() function that starts off the execution
def main():
    t, screen = setup_turtle()
    draw_scene(t)
    screen.mainloop()

# if this script is executed, call the main() function
# meaning when is file is run directly
if __name__ == "__main__":
    main()