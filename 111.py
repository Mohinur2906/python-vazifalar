import turtle

# Ekran sozlamalari
ekran = turtle.Screen()
ekran.bgcolor("lightyellow")
ekran.title("Chiroyli qizcha Malika")
ekran.setup(width=700, height=700)

t = turtle.Turtle()
t.speed(6)
t.hideturtle()

def doira_chiz(x, y, radius, rang):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.color(rang)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# --- SOCH (orqa qism, yuzdan kattaroq) ---
doira_chiz(0, 190, 75, "saddlebrown")

# --- YUZ ---
doira_chiz(0, 190, 55, "peachpuff")

# --- SOCH TOLALARI (ikki tomonda, kokillar) ---
t.penup()
t.goto(-70, 150)
t.pendown()
t.color("saddlebrown")
t.begin_fill()
t.goto(-100, 90)
t.goto(-80, 60)
t.goto(-55, 120)
t.goto(-70, 150)
t.end_fill()

t.penup()
t.goto(70, 150)
t.pendown()
t.begin_fill()
t.goto(100, 90)
t.goto(80, 60)
t.goto(55, 120)
t.goto(70, 150)
t.end_fill()

# --- KOKIL BANTLARI (ikkita rangli bant) ---
def bant_chiz(x, y, rang):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(rang)
    t.begin_fill()
    for _ in range(2):
        t.forward(25)
        t.left(150)
        t.forward(25)
        t.left(30)
    t.end_fill()

bant_chiz(-100, 95, "hotpink")
bant_chiz(80, 95, "hotpink")

# --- KO'ZLAR ---
doira_chiz(-20, 195, 8, "white")
doira_chiz(20, 195, 8, "white")
doira_chiz(-20, 195, 4, "black")
doira_chiz(20, 195, 4, "black")

# --- QOSHLAR ---
t.penup()
t.goto(-30, 210)
t.pendown()
t.color("saddlebrown")
t.pensize(3)
t.setheading(20)
t.forward(18)

t.penup()
t.goto(30, 210)
t.pendown()
t.setheading(160)
t.forward(18)
t.pensize(1)

# --- LUNJLAR (pushti) ---
doira_chiz(-35, 170, 8, "lightpink")
doira_chiz(35, 170, 8, "lightpink")

# --- OG'IZ (tabassum) ---
t.penup()
t.goto(-15, 165)
t.pendown()
t.color("red")
t.pensize(3)
t.setheading(-60)
t.circle(15, 120)
t.pensize(1)

# --- BO'YIN ---
t.penup()
t.goto(-12, 135)
t.pendown()
t.color("peachpuff")
t.begin_fill()
t.goto(12, 135)
t.goto(12, 110)
t.goto(-12, 110)
t.goto(-12, 135)
t.end_fill()

# --- KO'YLAK (ko'ylak, pushti rangli, uchburchak shaklida) ---
t.penup()
t.goto(-15, 110)
t.pendown()
t.color("deeppink")
t.begin_fill()
t.goto(15, 110)
t.goto(70, -60)
t.goto(-70, -60)
t.goto(-15, 110)
t.end_fill()

# --- KO'YLAK NAQSHI (yulduzchalar) ---
def kichik_yulduz(x, y, rang):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(rang)
    t.begin_fill()
    for _ in range(5):
        t.forward(10)
        t.right(144)
    t.end_fill()

kichik_yulduz(-30, 20, "white")
kichik_yulduz(20, -10, "white")
kichik_yulduz(-10, -35, "white")

# --- QO'LLAR ---
t.penup()
t.goto(-15, 90)
t.pendown()
t.color("peachpuff")
t.pensize(10)
t.goto(-60, 20)

t.penup()
t.goto(15, 90)
t.pendown()
t.goto(60, 20)
t.pensize(1)

# --- OYOQLAR ---
t.penup()
t.goto(-25, -60)
t.pendown()
t.color("peachpuff")
t.pensize(12)
t.goto(-25, -130)

t.penup()
t.goto(25, -60)
t.pendown()
t.goto(25, -130)

# --- TUFLI (poyabzal) ---
t.color("white")
t.penup()
t.goto(-25, -130)
t.pendown()
t.goto(-25, -145)

t.penup()
t.goto(25, -130)
t.pendown()
t.goto(25, -145)
t.pensize(1)


t.penup()
t.goto(0, -200)
t.pendown()
t.color("deeppink")
t.write("MALIKA", align="center", font=("Comic Sans MS", 26, "bold"))

ekran.exitonclick()