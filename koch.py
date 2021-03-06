""" 
Koch curve drawing program.

    File name: koch.py
    Author: Stanik
    Email: stanik@tuta.io
    GitHub: https://github.com/stanik120
    License: GPL 3
    Python Version: 3.9.1
    
"""
import arcade
import math

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
# number of iteration
ITERATION = 4
# number of side in polygon
POLYGON = 4

def create_line_width_angle(start_x: float, start_y: float, end_x: float, end_y: float, rotation_point_x: float, rotation_point_y: float, angle: float = 0, color: arcade.Color = arcade.csscolor.WHITE, line_width: float = 1) -> arcade.Shape:
    """
    Create a line to be rendered later with additional parameters to set the angle and rotation point of the line.

    :param float start_x:
    :param float start_y:
    :param float end_x:
    :param float end_y:
    :param float rotation_point_x: rotation point of the line
    :param float rotation_point_y: rotation point of the line
    :param float angle:
    :param Color color:
    :param float line_width:
    :param arcade.Color color:

    :Returns arcade.Shape:
    """
    shape = arcade.create_line(
        start_x = rotation_point_x + (start_x - rotation_point_x) * math.cos(math.radians(angle)) - (start_y - rotation_point_y) * math.sin(math.radians(angle)),
        start_y = rotation_point_y + (start_x - rotation_point_x) * math.sin(math.radians(angle)) + (start_y - rotation_point_y) * math.cos(math.radians(angle)),
        end_x = rotation_point_x + (end_x - rotation_point_x) * math.cos(math.radians(angle)) - (end_y - rotation_point_y) * math.sin(math.radians(angle)),
        end_y = rotation_point_y + (end_x - rotation_point_x) * math.sin(math.radians(angle)) + (end_y - rotation_point_y) * math.cos(math.radians(angle)),
        color = color,
        line_width = line_width
    )
    return shape

def create_koch_curve(start_x: float, start_y: float, width: float, angle: float = 0, iteration: int = 2, count: int = 0, line_width: float = 1, color: arcade.Color = arcade.csscolor.WHITE) -> arcade.ShapeElementList:
    """ 
    Create a Koch curve to be rendered later. 
    :param float start_x:
    :param float start_y:
    :param float width:
    :param float angle:
    :param int iteration: how many times to repeat the process
    :param int count: repetition counter
    :param float line_width:
    :param arcade.Color color:

    :Returns arcade.ShapeElementList:
    """
    # make a list to hold the line in the curve
    line_list = arcade.ShapeElementList()
    # length of a single line in the curve
    line_length = width / 3
    # repetition counter
    count += 1
    # if the repetition count is less than or the same as the iteration number create new curve on all line in curent curve
    if count <= iteration:
        # create new curve on line a-b
        koch = create_koch_curve(
            start_x = start_x,
            start_y = start_y,
            width = line_length,
            angle = angle,
            iteration = iteration,
            count = count,
            line_width = line_width,
            color = color
        )
        for line in koch:
            line_list.append(line)
        # create new curve on line b-c
        koch = create_koch_curve(
            start_x = start_x + (start_x - start_x + line_length) * math.cos(math.radians(angle)) - (start_y - start_y) * math.sin(math.radians(angle)),
            start_y = start_y + (start_x - start_x + line_length) * math.sin(math.radians(angle)) + (start_y - start_y) * math.cos(math.radians(angle)),
            width = line_length,
            angle = angle + 60,
            iteration = iteration,
            count = count,
            line_width = line_width,
            color = color
        )
        for line in koch:
            line_list.append(line)
        # create new curve on line c-d
        koch = create_koch_curve(
            start_x = start_x + (start_x - start_x + line_length + line_length / 2) * math.cos(math.radians(angle)) - (start_y - start_y + (line_length * math.sqrt(3) / 2)) * math.sin(math.radians(angle)),
            start_y = start_y + (start_x - start_x + line_length + line_length / 2) * math.sin(math.radians(angle)) + (start_y - start_y + (line_length * math.sqrt(3) / 2)) * math.cos(math.radians(angle)),
            width = line_length,
            angle = angle - 60,
            iteration = iteration,
            count = count,
            line_width = line_width,
            color = color
        )
        for line in koch:
            line_list.append(line)
        # create new curve on line d-e
        koch = create_koch_curve(
            start_x = start_x + (start_x - start_x + line_length * 2) * math.cos(math.radians(angle)) - (start_y - start_y) * math.sin(math.radians(angle)),
            start_y = start_y + (start_x - start_x + line_length * 2) * math.sin(math.radians(angle)) + (start_y - start_y) * math.cos(math.radians(angle)),
            width = line_length,
            angle = angle,
            iteration = iteration,
            count = count,
            line_width = line_width,
            color = color
        )
        for line in koch:
            line_list.append(line)
    # if you in last iteration create line
    else:
        # create line a-b
        line = create_line_width_angle(
            start_x = start_x,
            start_y = start_y,
            end_x = start_x + line_length,
            end_y = start_y,
            rotation_point_x = start_x,
            rotation_point_y = start_y,
            angle = angle,
            line_width = line_width,
            color = color,
        )
        line_list.append(line)
        # create line b-c
        line = create_line_width_angle(
            start_x = start_x + line_length,
            start_y = start_y,
            end_x = start_x + line_length + line_length / 2,
            end_y = start_y + (line_length * math.sqrt(3) / 2),
            rotation_point_x = start_x,
            rotation_point_y = start_y,
            angle = angle,
            line_width = line_width,
            color = color,
        )
        line_list.append(line)
        # create line c-d
        line = create_line_width_angle(
            start_x = start_x + line_length + line_length / 2,
            start_y = start_y + (line_length * math.sqrt(3) / 2),
            end_x = start_x + line_length * 2,
            end_y = start_y,
            rotation_point_x = start_x,
            rotation_point_y = start_y,
            angle = angle,
            line_width = line_width,
            color = color,
        )
        line_list.append(line)
        # create line d-e
        line = create_line_width_angle(
            start_x = start_x + line_length * 2,
            start_y = start_y,
            end_x = start_x + line_length * 3,
            end_y = start_y,
            rotation_point_x = start_x,
            rotation_point_y = start_y,
            angle = angle,
            line_width = line_width,
            color = color,
        )
        line_list.append(line)

    return line_list

class KochSnowflake(list):
    """ 
    Create a Koch curve on the faces of a regular polygon with the given number of faces 
    :param float center_x: center of a snowflake
    :param float center_y: center of a snowflake
    :param float radius: radius of a snowflake
    :param int polygon: number of faces
    :param int iteration: how many times to repeat the process
    :param float line_width:
    :param arcade.Color color:
    """
    def __init__(self, center_x: float, center_y: float, radius: float, polygon: int = 6, iteration: int = 2, line_width: float = 1, color: arcade.Color = arcade.csscolor.WHITE):
        super().__init__()
        self.radius = radius
        self.center_x = center_x
        self.center_y = center_y
        self.polygon = polygon
        self.iteration = iteration
        self.line_width = line_width
        self.color = color

        self.update()

    def update(self):
        """ call this method if you change something in object """
        # clear list of line in snowflake when update
        self.clear()
        # calculate side_width a = 2r tan(??/n) = 2R sin(??/n)
        side_width = 2 * self.radius * math.sin(math.pi / self.polygon)
        # calculate inradius r = (1/2)a cot(??/n) = R cos(??/n) 
        inradius = self.radius * math.cos(math.pi / self.polygon)
        # calculate start_x and start_y for the first curve
        start_x = self.center_x - side_width / 2
        start_y = self.center_y + inradius
        # create new curve for all wall in polygon
        for i in range(self.polygon):
            angle = (360 - (360 / self.polygon)) * i
            # create new curve
            koch = create_koch_curve(
                start_x = start_x,
                start_y = start_y,
                width = side_width,
                angle = angle,
                iteration = self.iteration,
                count = 0,
                line_width = self.line_width,
                color = self.color
            )
            for line in koch:
                self.append(line)
            # calculate start_x and start_y for the next curve
            rotation_point_x = start_x
            rotation_point_y = start_y
            end_x = start_x + side_width
            end_y = start_y
            start_x = rotation_point_x + (end_x - rotation_point_x) * math.cos(math.radians(angle)) - (end_y - rotation_point_y) * math.sin(math.radians(angle))
            start_y = rotation_point_y + (end_x - rotation_point_x) * math.sin(math.radians(angle)) + (end_y - rotation_point_y) * math.cos(math.radians(angle))

    def draw(self):
        """ draw method """
        for line in self:
            line.draw()

class Window(arcade.Window):
    """ main class """
    def __init__(self, width: int, height: int, title: str):
        super().__init__(width=width, height=height, title=title)
        # create Koch curve object
        self.koch = KochSnowflake(
            center_x = WINDOW_WIDTH / 2,
            center_y = WINDOW_HEIGHT / 2,
            radius = WINDOW_WIDTH * .4,
            polygon = POLYGON,
            iteration = ITERATION
        )

    def on_key_press(self, symbol: int, modifiers: int):
        """ change number of iteration or number of faces in polygon when you press the button """
        # change number of iteration
        if symbol == arcade.key.UP:
            self.koch.iteration += 1
        if symbol == arcade.key.DOWN and self.koch.iteration > 0:
            self.koch.iteration -= 1
        # change number of faces in polygon
        if symbol == arcade.key.RIGHT:
            self.koch.polygon += 1
        if symbol == arcade.key.LEFT and self.koch.polygon > 2:
            self.koch.polygon -= 1
        self.koch.update()
        
    def on_draw(self):
        arcade.start_render()
        # draw Koch curve
        self.koch.draw()
        # draw text 
        arcade.draw_text(f"number of faces in polygon: {self.koch.polygon}", 0, WINDOW_HEIGHT - 20, arcade.csscolor.WHITE)
        arcade.draw_text(f"number of iteration: {self.koch.iteration}", 0, WINDOW_HEIGHT - 40, arcade.csscolor.WHITE)

def main():
    """ main function """
    window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, "Koch Curve")
    arcade.run()

if __name__ == "__main__":
    main()