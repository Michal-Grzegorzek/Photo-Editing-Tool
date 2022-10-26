from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename,asksaveasfilename
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps
import os



my_w = Tk()
my_w.geometry("1000x1000")  # Size of the window
my_w.title('Photo Editing Tool')


img = None
img_path = None


def upload_image():
    global img_path, img
    img_path = filedialog.askopenfilename(initialdir=os.getcwd())
    img = Image.open(img_path)
    img.thumbnail((350, 350))
    photo_img = ImageTk.PhotoImage(img)
    canvas2.create_image(300, 210, image=photo_img)
    canvas2.image = photo_img


def rotate_image(func):
    global img
    img = img.rotate(int(rotate_combo.get()))
    photo_img = ImageTk.PhotoImage(img)
    canvas2.create_image(300, 210, image=photo_img)
    canvas2.image = photo_img


def blur():
    global img
    img = img.filter(ImageFilter.BLUR)
    photo_image = ImageTk.PhotoImage(img)
    canvas2.create_image(300, 210, image=photo_image)
    canvas2.image = photo_image


def emboss():
    global img
    img = img.filter(ImageFilter.EMBOSS)
    photo_image = ImageTk.PhotoImage(img)
    canvas2.create_image(300, 210, image=photo_image)
    canvas2.image = photo_image


def sharpen():
    global img
    img = img.filter(ImageFilter.SHARPEN)
    photo_image = ImageTk.PhotoImage(img)
    canvas2.create_image(300, 210, image=photo_image)
    canvas2.image = photo_image


def find_edges():
    global img
    img = img.filter(ImageFilter.FIND_EDGES)
    photo_image = ImageTk.PhotoImage(img)
    canvas2.create_image(300, 210, image=photo_image)
    canvas2.image = photo_image


def invert_colors():
    global img
    img= ImageOps.invert(img)
    # img = ImageOps.posterize(img, 2)
    photo_image = ImageTk.PhotoImage(img)
    canvas2.create_image(300, 210, image=photo_image)
    canvas2.image = photo_image


def solarize(func):
    global img
    for m in range(0, v1.get() + 1):
        img = ImageOps.solarize(img, threshold=m)
        photo_image = ImageTk.PhotoImage(img)
        canvas2.create_image(300, 210, image=photo_image)
        canvas2.image = photo_image


def postersize(func):
    global img
    m = v2.get()
    img = ImageOps.posterize(img, m)
    photo_image = ImageTk.PhotoImage(img)
    canvas2.create_image(300, 210, image=photo_image)
    canvas2.image = photo_image


def gray_scale():
    global img
    img = ImageOps.grayscale(img)
    photo_image = ImageTk.PhotoImage(img)
    canvas2.create_image(300, 210, image=photo_image)
    canvas2.image = photo_image


def flip_img(event):
    global img
    if flip_combo.get() == "FLIP LEFT TO RIGHT":
        img = img.transpose(Image.FLIP_LEFT_RIGHT)
    elif flip_combo.get() == "FLIP TOP TO BOTTOM":
        img = img.transpose(Image.FLIP_TOP_BOTTOM)
    photo_image = ImageTk.PhotoImage(img)
    canvas2.create_image(300, 210, image=photo_image)
    canvas2.image = photo_image

def crop_img():
    global img
    pixels = 30
    img = ImageOps.crop(img, pixels)
    photo_image = ImageTk.PhotoImage(img)
    canvas2.create_image(300, 210, image=photo_image)
    canvas2.image = photo_image

# create canvas to display image
canvas2 = Canvas(my_w, width="600", height="420", relief=RIDGE, bd=2)
canvas2.place(x=350, y=40)

title = Label(my_w, text="Photo Editing Tool", font="ariel 17 bold", width=15, anchor='e')
title.place(x=550, y=10)

settings_label = Label(my_w, text="Settings", font="ariel 14 bold", width=15, anchor='e')
settings_label.place(x=40, y=50)

colors_label = Label(my_w, text="Edit colors", font="ariel 12 bold", anchor='e', fg='#3D8361')
colors_label.place(x=40, y=90)

filter_label = Label(my_w, text="Filters", font="ariel 12 bold", anchor='e', fg='#8758FF')
filter_label.place(x=40, y=240)

layout_label = Label(my_w, text="Layout", font="ariel 12 bold", anchor='e', fg='#FA7070')
layout_label.place(x=40, y=370)


btn_select = Button(my_w, text="Select Image", bg='#4649FF', fg='black',
              font=('ariel 15 bold'), relief=GROOVE, command=upload_image)
btn_select.place(x=400, y=495)

btn_gray = Button(my_w, text="Gray-scale", bg='#3D8361', fg='black', width=10,
                    font=('ariel 12 bold'), relief=GROOVE, command=gray_scale)
btn_gray.place(x=40, y=120)

btn_invert = Button(my_w, text="Invert image", bg='#3D8361', fg='black', width=10,
                    font='ariel 12 bold', relief=GROOVE, command=invert_colors)
btn_invert.place(x=180, y=120)

btn_blur = Button(my_w, text="Blur", bg='#8758FF',fg='black',
                    font='ariel 12 bold', relief=GROOVE, command=blur, width=10)
btn_blur.place(x=40, y=270)

btn_emboss = Button(my_w, text="Emboss", bg='#8758FF',fg='black',
                    font='ariel 12 bold', relief=GROOVE, command=emboss, width=10)
btn_emboss.place(x=180, y=270)

btn_sharpen = Button(my_w, text="Sharpen", bg='#8758FF',fg='black',
                    font='ariel 12 bold', relief=GROOVE, command=sharpen, width=10)
btn_sharpen.place(x=40, y=320)

btn_find_edges = Button(my_w, text="Edges", bg='#8758FF',fg='black',
                    font='ariel 12 bold', relief=GROOVE, command=find_edges, width=10)
btn_find_edges.place(x=180, y=320)




rotate = Label(my_w, text="Rotate:", font="ariel 12 bold")
rotate.place(x=40, y=400)
values = [0, 90, 180, 270, 360]
rotate_combo = ttk.Combobox(my_w, values=values, font='ariel 10 bold')
rotate_combo.place(x=100, y=400)
rotate_combo.bind("<<ComboboxSelected>>", rotate_image)


flip = Label(my_w, text="Flip:", font="ariel 12 bold")
flip.place(x=40, y=430)
opt_flip = ['FLIP LEFT TO RIGHT', 'FLIP TOP TO BOTTOM']
flip_combo = ttk.Combobox(my_w, values=opt_flip, font=('ariel 10 bold'))
flip_combo.place(x=100, y=430)
flip_combo.bind("<<ComboboxSelected>>", flip_img)

btn_crop = Button(my_w, text="Crop", bg='#8758FF',fg='black',
                    font='ariel 12 bold', relief=GROOVE, command=crop_img, width=10)
btn_crop.place(x=40, y=620)


solarize_label = Label(my_w, text="Solarize:", font=("ariel 13 bold"), width=9, anchor='e')
solarize_label.place(x=15, y=170)
v1 = IntVar()
scale1 = ttk.Scale(my_w, from_=0, to=255, variable=v1,
                   orient=HORIZONTAL, command=solarize)
scale1.place(x=130, y=170)

postersize_label = Label(my_w, text="Postersize:", font=("ariel 13 bold"), width=9, anchor='e')
postersize_label.place(x=15, y=200)
v2 = IntVar()
scale2 = ttk.Scale(my_w, from_=1, to=5, variable=v2,
                   orient=HORIZONTAL, command=postersize)
scale2.place(x=130, y=200)

my_w.mainloop()