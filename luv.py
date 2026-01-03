from turtle import*
import math

def heart(t):
    # Adjusted parametric formula for a bigger and smoother heart
    return (16 * math.sin(t) ** 3,
            13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t))

speed(0)
bgcolor("black")
color("red")
pensize(2)
up()
scale = 18    # Increased scale for a bigger heart
goto(0, -scale * 13)  # Start at bottom center of the heart
down()
begin_fill()
for t in range(0, 361):
    x, y = heart(math.radians(t))
    goto(x * scale, y * scale)
end_fill()
up()
# Center the text inside the heart
goto(0, scale * 2)   # Empirically chosen offset for the heart center
color("white")
write("VIKRAM", align="center", font=("Arial", 30, "bold"))
hideturtle()
done()
