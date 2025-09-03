# importin turtel
import turtle
# faces coorfinates
face_one = [
  [(-40, 120), (-70, 260), (-130, 230), (-170, 200), (-170, 100), (-160, 40), (-170, 10), (-150, -10), (-140, 10),(-40, -20), (0, -20)],

  [(0, -20), (40, -20), (140, 10), (150, -10), (170, 10), (160, 40), (170, 100), (170, 200), (130, 230), (70, 260),(40, 120), (0, 120)]
]

face_two = [
  [(-40, -30), (-50, -40), (-100, -46), (-130, -40), (-176, 0), (-186, -30), (-186, -40), (-120, -170), (-110, -210),(-80, -230), (-64, -210), (0, -210)],
  
  [(0, -210), (64, -210), (80, -230), (110, -210), (120, -170), (186, -40), (186, -30), (176, 0), (130, -40),(100, -46), (50, -40), (40, -30), (0, -30)]
]

face_three = [
  [(-60, -220), (-80, -240), (-110, -220), (-120, -250), (-90, -280), (-60, -260), (-30, -260), (-20, -250),(0, -250)],
  
  [(0, -250), (20, -250), (30, -260), (60, -260), (90, -280), (120, -250), (110, -220), (80, -240), (60, -220),(0,-220)]
]
# hide the cursor
turtle.hideturtle()
# make the back ground red
turtle.bgcolor("#ff3100")
# set up the window's width and hight in pixels 
turtle.setup(500,600)
# the draw speed 
turtle.speed(3)

face_one_start=(0,120)
face_two_start=(0,-30)
face_three_start=(0,-220)


def draw_faces(face_details_list,starting_point):
  #Pull the pen up – no drawing when moving. 
  turtle.penup()
  # go to the starting point 
  turtle.goto(starting_point)
  #Pull the pen down – drawing when moving.
  turtle.pendown()
  # choose the color font
  turtle.color("#FFC000")
  #To be called just before drawing a shape to be filled.
  turtle.begin_fill()



  # for loob to match the coordinate points together 
  for i in range(len(face_details_list[0])):
    x,y=face_details_list[0][i]  # x,y = (-40, 120) => x =-40 , y = 120
    turtle.goto(x,y)
  for i in range(len(face_details_list[1])):
    x,y=face_details_list[1][i]  # x,y = (-40, 120) => x =-40 , y = 120
    turtle.goto(x,y)
  # fill the shape 
  turtle.end_fill()

def main():
  draw_faces(face_one,face_one_start)
  draw_faces(face_two,face_two_start)
  draw_faces(face_three,face_three_start)


if __name__=="__main__":
  main()