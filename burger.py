import tkinter as tk
from PIL import Image, ImageTk
import random
import pathlib

# -------------------- CONFIGURATION --------------------
WIDTH, HEIGHT = 640, 480
IMG_FILE = "burger.png"
STEP_RANGE = (-5, 5)
BURGER_SIZE = 100

# -------------------- SETUP WINDOW ---------------------
root = tk.Tk()
root.title("Bouncing Burger Activity")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#87ceeb")  # Light sky blue
canvas.pack()

# -------------------- LOAD IMAGE -----------------------
img_path = pathlib.Path(__file__).with_name(IMG_FILE)
if not img_path.exists():
    raise FileNotFoundError(f"Image '{IMG_FILE}' not found.")

raw_img = Image.open(img_path).resize((BURGER_SIZE, BURGER_SIZE))
burger_img = ImageTk.PhotoImage(raw_img)

# -------------------- DRAW ELEMENTS --------------------
burger = canvas.create_image(50, 50, image=burger_img, anchor=tk.NW)

# -------------------- ANIMATION VARIABLES --------------
dx = random.choice([i for i in range(*STEP_RANGE) if i != 0])
dy = random.choice([i for i in range(*STEP_RANGE) if i != 0])
paused = False
bg_colors = ["#87ceeb", "#f5c542", "#ff6961", "#77dd77", "#cfcfcf"]

# -------------------- FUNCTIONS ------------------------
def animate():
    global dx, dy
    if paused:
        canvas.after(16, animate)
        return

    x, y = canvas.coords(burger)
    right, bottom = x + BURGER_SIZE, y + BURGER_SIZE

    # Bounce detection with color feedback
    bounced = False
    if x + dx < 0 or right + dx > WIDTH:
        dx *= -1
        bounced = True
    if y + dy < 0 or bottom + dy > HEIGHT:
        dy *= -1
        bounced = True
    if bounced:
        canvas.config(bg=random.choice(bg_colors))  # Change background color

    canvas.move(burger, dx, dy)
    canvas.after(16, animate)

def toggle_pause(event=None):
    global paused
    paused = not paused
    canvas.itemconfig( text="Paused" if paused else "Press SPACE to pause/resume")

# -------------------- EVENT BINDINGS -------------------
root.bind("<space>", toggle_pause)

# -------------------- START ----------------------------
animate()
root.mainloop()
