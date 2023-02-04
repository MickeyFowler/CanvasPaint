from create_canvas import Create_canvas
from square_or_rectangle import Rectangle, Square

canvas_width = int(input("Please enter the canvas width you want: "))
canvas_height = int(input("Please enter canvas height you want: "))
colors = {"white": (255, 255, 255), "black": (0, 0, 0)}
canvas_color = input("Please enter the canvas color you want. (white or black): ")
canvas = Create_canvas(height=canvas_height, width=canvas_width, color=colors[canvas_color])

while True:
    shape_type = input("What shape do you want to draw? (rectangle or square) Enter q to quit. ")
    if shape_type.lower() == "rectangle":
        rec_x = int(input("Please enter x of the rectangle: "))
        rec_y = int(input("Please enter y of the rectangle: "))
        rec_width = int(input("Please enter width of the rectangle: "))
        rec_height = int(input("Please enter height of the rectangle: "))
        red = int(input("How much red should this rectangle have? "))
        green = int(input("How much green should this rectangle have? "))
        blue = int(input("How much blue should this rectangle have? "))
        r1 = Rectangle(x=rec_x, y=rec_y, height=rec_height, width=rec_width, color=(red, green, blue))
        r1.draw(canvas)

    if shape_type.lower() == "square":
        sqr_x = int(input("Please enter x of the square: "))
        sqr_y = int(input("Please enter y of the square: "))
        sqr_side = int(input("Please enter side length of the square: "))
        red = int(input("How much red should this square have? "))
        green = int(input("How much green should this square have? "))
        blue = int(input("How much blue should this square have? "))
        s1 = Square(x=sqr_x, y=sqr_y, side=sqr_side, color=(red, green, blue))
        s1.draw(canvas)

    if shape_type == 'q':
        break

canvas.make('canvas.png')
