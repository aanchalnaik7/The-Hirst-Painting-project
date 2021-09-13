###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##

#
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colour = (r, g, b)
#     rgb_colors.append(new_colour)
#
# print(rgb_colors)

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

colour_list = [(217, 227, 244), (232, 225, 211), (220, 235, 230), (237, 223, 232), (189, 158, 130), (133, 90, 68), (138, 168, 182), (189, 147, 158), (217, 204, 142), (59, 112, 133),
(142, 74, 91), (144, 171, 160), (183, 94, 110), (70, 111, 91), (185, 100, 87), (12, 39, 62), (67, 34, 22), (216, 177, 188), (18, 54, 34), (63, 24, 42), (147, 141, 87),
(218, 179, 173), (86, 144, 157), (106, 42, 64), (107, 46, 38), (174, 203, 189), (164, 201, 210), (100, 143, 125), (29, 85, 60), (185, 189, 207)]

tim.setheading(255)
tim.forward(300)
tim.setheading(0)
num_of_dots = 100

for dot_count in range(1, num_of_dots + 1):
    tim.dot(20, random.choice(colour_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()