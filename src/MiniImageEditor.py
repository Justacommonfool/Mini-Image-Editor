import random
import PIL
from PIL.Image import Image
from PIL.ImageDraw import ImageDraw
from PIL import ImageTk
from tkinter import *
from tkinter import filedialog, messagebox
import os
import pkg_resources.py2_warn

global main_file
global col
global crop_rotate_root

"""-----------------------------------------------------------------PIL Class---------------------------------------------------------------- """


class Images:

    def __init__(self, file_name):  # initializing image
        """

        :type file_name: str
        """
        self.filename = file_name
        self.image = PIL.Image.open(self.filename)
        self.pix = self.image.load()

    def checker(self, arg):
        """

        :type arg: str
        """
        co = arg
        color = arg
        randoms = False

        # Setting the argument to RGB and coloring every other pixel.
        if color == 'dark':
            color = (192, 192, 192)
        elif color == 'random':
            randoms = True
        elif color == 'maroon':
            color = (256, 0, 0)
        elif color == 'white':
            color = (256, 256, 256)

        pix = self.pix
        image = self.image
        for i in range(image.size[0]):  # for every pixel:
            for j in range(image.size[1]):
                if i % 2 == 0 and j % 2 == 0:
                    # change to black if not red
                    pix[i, j] = color if not randoms else (
                        random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
        x = image.copy()
        x.save(f'Icons\\{co}.png')

    # The next couple of __color functions shade the image to that color
    def __red(self, intensity):
        image = self.image
        pix = self.pix
        x = image.convert('RGB')
        # looping every pixel
        for i in range(image.size[0]):
            for j in range(image.size[1]):
                r = x.getpixel((i, j))[0]
                pix[i, j] = r * intensity, r, r

        x = image.copy()
        x.save('Icons\\red.png')

    def __green(self, intensity):
        image = self.image
        pix = self.pix
        x = image.convert('RGB')
        for i in range(image.size[0]):
            for j in range(image.size[1]):
                r = x.getpixel((i, j))[0]
                pix[i, j] = r, r * intensity, r
        x = image.copy()
        x.save('Icons\\green.png')

    def __teal(self, intensity):
        image = self.image
        pix = self.pix
        x = image.convert('RGB')
        for i in range(image.size[0]):
            for j in range(image.size[1]):
                r = x.getpixel((i, j))[0]
                pix[i, j] = r, r * intensity, r * intensity
        x = image.copy()
        x.save('Icons\\teal.png')

    def __white(self, intensity):
        image = self.image
        pix = self.pix
        x = image.convert('RGB')
        for i in range(image.size[0]):
            for j in range(image.size[1]):
                r = x.getpixel((i, j))[0]
                pix[i, j] = r * intensity, r * intensity, r * intensity
        x = image.copy()
        x.save('Icons\\white.png')

    def __pinkple(self, intensity):
        image = self.image
        pix = self.pix
        x = image.convert('RGB')
        for i in range(image.size[0]):
            for j in range(image.size[1]):
                r = x.getpixel((i, j))[0]
                pix[i, j] = r * intensity, r, r * intensity
        x = image.copy()
        x.save('Icons\\pinkple.png')

    def __yellow(self, intensity):
        image = self.image
        pix = self.pix
        x = image.convert('RGB')
        for i in range(image.size[0]):
            for j in range(image.size[1]):
                r = x.getpixel((i, j))[0]
                pix[i, j] = r * intensity, r * intensity, r
        x = image.copy()
        x.save('Icons\\yellow.png')

    def __blue(self, intensity):
        image = self.image
        pix = self.pix
        x = image.convert('RGB')
        for i in range(image.size[0]):
            for j in range(image.size[1]):
                r = x.getpixel((i, j))[0]
                pix[i, j] = r, r, r * intensity
        x = image.copy()
        x.save('Icons\\blue.png')

    def __gray(self):
        image = self.image
        pix = self.pix
        x = image.convert("RGB")
        for i in range(image.size[0]):
            for j in range(image.size[1]):
                r = x.getpixel((i, j))[0]
                pix[i, j] = r, r, r  # Gray only occurs when each value is the same

        x = image.copy()
        x.save('Icons\\grey.png')

    def shade(self, color: str, intensity: int = 10000):
        # Combining the previous functions into one function
        if color.lower().strip() == 'red':
            self.__red(intensity)
        elif color.lower().strip() == 'green':
            self.__green(intensity)
        elif color.lower().strip() == 'teal':
            self.__teal(intensity)
        elif color.lower().strip() == 'blue':
            self.__blue(intensity)
        elif color.lower().strip() == 'white':
            x = self.image.copy()
            x.save('Icons\\white.png')
        elif color.lower().strip() == 'grey':
            self.__gray()
        elif color.lower().strip() == 'pinkple':
            self.__pinkple(intensity)
        elif color.lower().strip() == 'yellow':
            self.__yellow(intensity)

    def square_crop(self, x_coord_list: list, y_coord_list: list):
        image = self.image

        try:
            image.save('C:\\ShrihanCoding\\PycharmProjectsSourceCode\\.Pong GUI\\Icons\\normal.png')
            cropped_im = image.crop((min(x_coord_list), min(y_coord_list), max(x_coord_list), max(y_coord_list)))

        except:
            raise SystemError(
                f'Tile not inside picture. This is the dimensions of the picture: ({image.size}). This is the input: {(min(x_coord_list), min(y_coord_list), max(x_coord_list), max(y_coord_list))}')

        copier = cropped_im.copy()
        try:
            copier.save('C:\\ShrihanCoding\\PycharmProjectsSourceCode\\.Pong GUI\\Icons\\cropped.png')
        except SystemError as e:
            print(e)
            print('Accepted coords:' + str(image.size[0]) + str(image.size[1]))
            print((min(x_coord_list), max(y_coord_list), max(x_coord_list), min(y_coord_list)))
            return

    # Function for coloring pixels
    def markup(self, i, j, color, opacity):

        image = self.image
        rgb = image.convert('RGB')
        x = ImageDraw(image)
        # When opacity==0, simplifying the code leads to better performance
        if opacity == 0:
            x.point((i, j), fill=color)
        else:
            # To mix the colors, I added and dived the RGB values between the current color and the desired one

            try:
                pixel = rgb.getpixel((i, j))
            except IndexError:
                return

            try:
                index0 = (color[0] * opacity) + (pixel[0] * (100 - opacity))
                index1 = (color[1] * opacity) + (pixel[1] * (100 - opacity))
                index2 = (color[2] * opacity) + (pixel[2] * (100 - opacity))
                x.point((i, j), fill=(int(index0 / 100), int(index1 / 100), int(index2 / 100)))
            except ZeroDivisionError:
                pass
        copied_im = image.copy()
        copied_im.save('C:\\ShrihanCoding\\PycharmProjectsSourceCode\\.Pong GUI\\Icons\\markup.png')

    def rotate(self, degree):
        image = self.image
        rotated = image.rotate(degree)
        copy_it = rotated.copy()
        copy_it.save('Icons\\rotated.png')

    def resizing(self, width, height):
        image = self.image
        resized = image.resize((width, height))
        copy = resized.copy()
        copy.save('Icons\\resized.png')


"""------------------------------------------Tkinter-------------------------------------------------------------------------------"""

# starting Tk() in the middle of file to import performance
root = Tk()
root.title('Mini Image Editor')
root.configure(bg='#1a001a', width=1000, height=1000)
root.iconbitmap('Icons\\logo (1).ico')
root.resizable(0, 0)


# Since root.bind() returns something, I have to add an unused argument
def save_image(event):
    # Opens Windows File Explorer on Ctrl-S Click
    filedialog.asksaveasfilename(initialdir='C:\\', title='Name your file',
                                 filetypes=(('Image Files', '*.png*'), ('*.jpeg*', '*.pdf*')))


root.bind('<Control-s>', save_image)

filename = 'Icons\\searchIcon.png'  # Setting default main image as search icon


# Function for the 'find image' button
def browseFiles(file):
    filter_button.configure(state=NORMAL)
    global editing_img
    global markup_btn

    try:
        global main_file
        filename = file
        main_file = filename
        fil_pic = PIL.Image.open(os.path.abspath(main_file))
        if fil_pic.size[0] < 400 or fil_pic.size[1] < 400:
            pass
        else:
            fil_pic = fil_pic.resize((round(int(fil_pic.size[0]) / (int(fil_pic.size[0]) / 400)),
                                      round(int(fil_pic.size[1]) / (int(fil_pic.size[1]) / 400))))

        fil_pic.save(main_file)
        img_holder = ImageTk.PhotoImage(fil_pic)
        editing_img.grid_forget()
        editing_img = Label(root, image=img_holder)
        editing_img.image = img_holder
        editing_img.grid(row=0, column=0, rowspan=3, columnspan=3)

        markup_btn.grid_forget()
        markup_btn = Button(root, text='M\na\nr\nk\nu\np', command=markup, font=32, height=10, width=5)
        markup_btn.grid(row=0, column=4, rowspan=3, columnspan=2, padx=5)





    except PermissionError:
        pass
    except PIL.UnidentifiedImageError:
        pass


def markup():

    try:
      reset = PIL.Image.open(main_file)
    except NameError:
        return
    reset.save('Icons\\markup.png')

    def color(colour):
        # setting the color for the markup function
        global set_color
        set_color = colour

    def coords(event):
        # Function for finding mouse coordinates calling Images\Markup function
        get_opacity = int(opacity.get())
        x = Images('Icons\\markup.png')

        try:
            x.markup(event.x, event.y, set_color, get_opacity)
        except NameError:
            # Default color 'white' if other color is not set
            x.markup(event.x, event.y, (256, 256, 256), get_opacity)

        new_img = ImageTk.PhotoImage(PIL.Image.open(
            os.path.abspath('Icons\\markup.png')))
        markup_editor = Label(markup_root, image=new_img)
        markup_editor.image = new_img
        markup_editor.grid_forget()
        markup_editor.grid(row=0, column=0)

    def revert():
        new_img = ImageTk.PhotoImage(PIL.Image.open(
            os.path.abspath('Icons\\normal.png')))
        markup_editor = Label(markup_root, image=new_img)
        markup_editor.image = new_img
        markup_editor.grid_forget()
        markup_editor.grid(row=0, column=0)
        reset = PIL.Image.open(main_file)
        reset.save('Icons\\markup.png')

    markup_root = Toplevel()
    markup_root.title('Mini Image Editor- Markup')
    markup_root.configure(bg='#1a001a')
    markup_root.iconbitmap('Icons\\logo (1).ico')
    markup_image = PIL.Image.open(os.path.abspath(main_file))
    markup_image.save('Icons\\normal.png')

    def im_save():
        browseFiles('Icons\\markup.png')
        markup_root.destroy()

    if markup_image.size[0] < 500 and markup_image.size[1] < 500:
        # resizing image if too big
        width = markup_image.size[0]
        height = markup_image.size[1]
        markup_image.resize((int(width / (500 / width)), int(height / (500 / height))))
        marup_monkey = ImageTk.PhotoImage(markup_image)
    else:
        marup_monkey = ImageTk.PhotoImage(markup_image)

    markup_editor = Label(markup_root, image=marup_monkey)
    markup_editor.image = marup_monkey
    markup_editor.grid(row=0, column=0)
    markup_root.bind('<B1-Motion>', coords)
    markup_root.bind('<Control-s>', save_image)

    # Creating Scale and Color elements for markup window

    frame = LabelFrame(markup_root, text='Markup Controls', fg='white', width=90, height=markup_image.size[1],
                       bg='#1a001a')
    frame.grid(row=0, column=1, padx=20, pady=20)

    red_dot = Button(frame, text='RED', fg='red', borderwidth=0, command=lambda: color((256, 0, 0)))
    red_dot.grid(row=0, column=0, padx=10, pady=10)

    blue_dot = Button(frame, text='BLUE', fg='blue', borderwidth=0, command=lambda: color((0, 0, 256)))
    blue_dot.grid(row=0, column=1, padx=10, pady=10)

    green_dot = Button(frame, text='GREEN', fg='green', borderwidth=0, command=lambda: color((0, 255, 0)))
    green_dot.grid(row=1, column=0, padx=10, pady=10)

    black_dot = Button(frame, text='BLACK', fg='black', borderwidth=0, command=lambda: color((0, 0, 0)))
    black_dot.grid(row=1, column=1, padx=10, pady=10)

    white_dot = Button(frame, text='WHITE', fg='#adb0ab', borderwidth=0, command=lambda: color((255, 255, 255)))
    white_dot.grid(row=2, column=0, padx=10, pady=10)

    yellow_dot = Button(frame, text='YELLOW', fg='#dbd9a0', borderwidth=0)
    yellow_dot.grid(row=2, column=1, padx=10, pady=10)

    revert_button = Button(frame, text='REVERT', fg='red', bg='#1a001a', borderwidth=5, command=revert)
    revert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    save_button = Button(frame, text='SAVE', fg='green', bg='#1a001a', borderwidth=5, command=im_save)
    save_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    opacity = Scale(frame, from_=0, to=100, label='Opacity', tickinterval=50, bg='#1a001a', fg='white')
    opacity.grid(row=0, column=3, rowspan=3, padx=10, pady=10)


# Function for 'Photoshop' Button
def crop():
    global crop_image
    crop_root = Toplevel()
    crop_root.title('Mini Image Editor- Crop')
    crop_root.iconbitmap('Icons\\logo (1).ico')
    try:
        crop_file = ImageTk.PhotoImage(PIL.Image.open(main_file))
    except NameError:
        return
    crop_image = Label(crop_root, image=crop_file)
    crop_image.image = crop_file
    crop_image.grid(row=1, column=0)
    try:
        crop_instance = Images(main_file)
    except NameError:
        return
    coordinates_list = []
    coordinates_list2 = []

    def crop_size(event):
        coordinates_list.append(event.x)
        coordinates_list2.append(event.y)

        if len(coordinates_list) == 4:
            crop_instance.square_crop(coordinates_list, coordinates_list2)
            coordinates_list.clear()
            coordinates_list2.clear()

            crop_file = ImageTk.PhotoImage(PIL.Image.open('Icons\\cropped.png'))
            crop_image2 = Label(crop_root, image=crop_file)
            crop_image2.grid(row=1, column=0)
            crop_image.image = crop_file

    def save_cropped(event):
        try:
            browseFiles('Icons\\cropped.png')
        except FileNotFoundError as e:
            messagebox.showerror(FileNotFoundError, 'You have not cropped anything')
        crop_root.destroy()

    crop_root.bind('<Return>', crop_size)
    crop_root.bind('<Control-s>', save_cropped)


def rotate():
    global main_file
    rotate_root = Toplevel()
    rotate_root.title('Mini Image Editor- Rotate')
    rotate_root.iconbitmap('Icons\\logo (1).ico')
    try:
        rotate_instance = Images(main_file)
    except NameError:
        return

    def slider_detect(event):
        degrees = rotate_slider.get()
        rotate_instance.rotate(degrees)
        rotate_file = ImageTk.PhotoImage(PIL.Image.open('Icons\\rotated.png'))
        rotate_image = Label(rotate_root, image=rotate_file)
        rotate_image.image = rotate_file
        rotate_image.grid(row=0, column=0)

    def save_rotation():
        browseFiles('Icons\\rotated.png')
        rotate_root.destroy()

    rotate_file = ImageTk.PhotoImage(PIL.Image.open(main_file))
    rotate_image = Label(rotate_root, image=rotate_file, padx=20, pady=20)
    rotate_image.image = rotate_file
    rotate_image.grid(row=0, column=0)

    rotate_slider = Scale(rotate_root, label='Rotation', bg='teal', fg='white', from_=-180, to=180, tickinterval=90,
                          length=200)
    rotate_slider.grid(row=0, column=1, padx=40)
    rotate_root.bind('<B1-Motion>', slider_detect)
    rotate_root.bind('<Control-s>', save_rotation)

    save_button = Button(rotate_root, text='Save Image', fg='green', bg='white', command=save_rotation)
    save_button.grid(row=0, column=2)


def resize():
    global resized_img
    resize_root = Toplevel()
    resize_root.title('Mini Image Editor- Resize')
    resize_root.iconbitmap('Icons\\logo (1).ico')
    resize_root.configure(bg='#1a001a')
    try:
        resize_instance = Images(main_file)
    except NameError:
        return

    pic = main_file
    photo = ImageTk.PhotoImage(PIL.Image.open(pic))
    resized_img = Label(resize_root, image=photo)
    resized_img.image = photo
    resized_img.grid(row=0, column=0, columnspan=2, rowspan=2)

    def sliders(event=None):
        global resized_img

        try:
            resize_instance.resizing(x_axis.get(), y_axis.get())
        except ValueError:
            return

        pic = 'Icons\\resized.png'
        photo = ImageTk.PhotoImage(PIL.Image.open(pic))
        resized_img.destroy()
        resized_img = Label(resize_root, image=photo)
        resized_img.image = photo
        resized_img.grid(row=0, column=0, columnspan=2, rowspan=2)

    def save(event=None):
        browseFiles('Icons\\resized.png')
        resize_root.destroy()

    x_axis = Scale(resize_root, from_=int(photo.height()), to=1, orient=HORIZONTAL, tickinterval=100, length=300)
    x_axis.set(int(photo.width()))
    y_axis = Scale(resize_root, from_=int(photo.width()), to=1, orient=HORIZONTAL, tickinterval=100, length=300)
    y_axis.set(int(photo.height()))
    width = Label(resize_root, text='Width: ')
    width.grid(row=0, column=3, padx=10, sticky='W')

    height = Label(resize_root, text='Height: ')
    height.grid(row=1, column=3, padx=20, sticky='W')

    x_axis.grid(row=0, column=4, padx=10)
    y_axis.grid(row=1, column=4, padx=10)

    save_button = Button(resize_root, text='SAVE', fg='white', bg='green', command=save)
    save_button.grid(row=0, column=5, columnspan=2)

    resize_root.bind('<B1-ButtonRelease>', sliders)
    resize_root.bind('<Control-s>', save)


def crop_rotate_main():
    global crop_rotate_root
    crop_rotate = Toplevel()
    crop_rotate.title('Mini Image Editor- Crop and Rotate Menu')
    crop_rotate.iconbitmap('Icons\\logo (1).ico')
    crop_rotate.configure(bg='#1a001a')
    # Makes a direction menu

    direction_label = Label(crop_rotate, text='Directions to crop: hover mouse over corner you want to crop \nand then '
                                              'click ENTER. Repeat for 4 corners.', bg='#1a001a', font=32, fg='white')
    direction_label.grid(row=0, column=0)

    crop_button = Button(crop_rotate, text='Crop', borderwidth=1, command=crop, width=30, font=10)
    crop_button.grid(row=1, column=0, padx=20, pady=10)

    direction_label_2 = Label(crop_rotate,
                              text='Directions to rotate: Change slider value to rotate the image x degrees.',
                              bg='#1a001a', font=32, fg='white')
    direction_label_2.grid(row=2, column=0)

    rotate_button = Button(crop_rotate, text='Rotate', borderwidth=1, command=rotate, width=30, font=10)
    rotate_button.grid(row=3, column=0, padx=20, pady=10)

    direction_label_3 = Label(crop_rotate,
                              text='Directions to resize: Enter width or height.',
                              bg='#1a001a', font=32, fg='white')
    direction_label_3.grid(row=4, column=0)

    resize_button = Button(crop_rotate, text='Resize', borderwidth=1, command=resize, width=30, font=10)
    resize_button.grid(row=5, column=0, padx=20, pady=10)


# Function for finding and creating filters
def filter():
    global Picture

    # List to loop and call the Images\Shade and Images\Checker functions
    col_list = ['red', 'green', 'teal', 'pinkple', 'white', 'grey', 'yellow', 'blue']
    checker_list = ['maroon', 'random', 'white', 'dark']

    anoth_root = Toplevel()
    anoth_root.title('Mini Image Editor-Filters')
    anoth_root.iconbitmap('Icons\\logo (1).ico')

    row_num = 0
    col_num = 0
    assign = -1

    # Loop for Shade function
    for col in col_list:
        # Assigning rows and columns based on what cycle the loop is on
        assign += 1
        if assign == 0:
            row_num = 1
            col_num = 0
        elif assign == 1:
            row_num = 1
            col_num = 1
        elif assign == 2:
            row_num = 1
            col_num = 2
        elif assign == 3:
            row_num = 1
            col_num = 3
        elif assign == 4:
            row_num = 2
            col_num = 0
        elif assign == 5:
            row_num = 2
            col_num = 1
        elif assign == 6:
            row_num = 2
            col_num = 2
        elif assign == 7:
            row_num = 2
            col_num = 3
        elif assign == 8:
            row_num = 2
            col_num = 4
        try:
            xo = Images(main_file)
        except NameError:
            return

        try:
            # Calling shade function
            xo.shade(col)
        except TypeError:
            # If application does not accept image, filter button will be disabled until new image is added
            filter_button.configure(state=DISABLED)
            return

        Picture = Entry(anoth_root, width=250)
        Picture.grid(row=0, column=0, columnspan=4)
        Picture.insert(0, '🔍 Select a filter')
        col_list_find = {}
        fil_pic = PIL.Image.open(f'Icons\\{col}.png')
        fil_holder = ImageTk.PhotoImage(fil_pic)
        fil_img = (Label(anoth_root, image=fil_holder, text=col, borderwidth=10))
        fil_img.image = fil_holder
        fil_img.text = col
        fil_img.grid(row=row_num, column=col_num)
        col_list_find.update({fil_img.text: fil_img.image})

    num = 0
    check_list_find = {}

    # Loop for Images\Checker function
    for check in checker_list:
        # Assigning rows and columns below the shade images
        num += 1
        if num == 1:
            row_num = 3
            col_num = 0
        elif num == 2:
            row_num = 3
            col_num = 1
        elif num == 3:
            row_num = 3
            col_num = 2
        elif num == 4:
            row_num = 3
            col_num = 3

        check_instance = Images(main_file)
        check_instance.checker(check)
        check_pic = ImageTk.PhotoImage(PIL.Image.open(f'Icons\\{check}.png'))
        check_img = Label(anoth_root, image=check_pic, borderwidth=10, text=check)
        check_img.image = check_pic
        check_img.text = check
        check_list_find.update({check_img.text: check_img.image})
        check_img.grid(row=row_num, column=col_num)

    def change(money):
        # Function for moving selected image to main root
        """

        :type money: object
        """
        global main_file
        global editing_img

        text = Picture.get()
        for each in col_list_find.keys():
            global main_file
            if each == str(text).strip().lower():
                browseFiles(f'Icons\\{each}.png')
                anoth_root.destroy()
                break
            else:
                pass

        for each in check_list_find.keys():
            text = Picture.get()
            if each == str(text).strip().lower():
                browseFiles(f'Icons\\{each}.png')
                anoth_root.destroy()
                break
            else:
                pass

    anoth_root.configure(bg='#1a001a')
    anoth_root.bind('<Return>', change)


# Default Widgets for default window

img_holder = ImageTk.PhotoImage(PIL.Image.open(os.path.abspath(filename)))
editing_img = Label(root, image=img_holder)
editing_img.image = img_holder
editing_img.grid(row=0, column=0, columnspan=3, rowspan=3)

find_img = Button(root, text='Find Image', bg='white', borderwidth=5, fg='#1a001a',
                  command=lambda: browseFiles(filedialog.askopenfilename(initialdir="/", title="Select a File",
                                                                         filetypes=(("Image Files", '*.png*'),
                                                                                    ("*.jpeg*", "*.jfif*")))))
find_img.grid(row=6, column=1)

filter_button = Button(root, text='Filters', borderwidth=5, bg='white', fg='#1a001a', command=filter)
filter_button.grid(row=6, column=0)

markup_btn = Button(root, text='M\na\nr\nk\nu\np', font=32, command=markup, width=5, height=10)
markup_btn.grid(row=0, column=4, rowspan=3, columnspan=2, padx=5)

crop_rotate_button = Button(root, text='Crop/Rotate', fg='#1a001a', bg='white', borderwidth=5, command=crop_rotate_main)
crop_rotate_button.grid(row=6, column=2)

root.mainloop()
