import tkinter as tk
import customtkinter as ctk
import os
from PIL import Image, ImageTk


# Asset path
ASSET_PATH = os.path.join(os.getcwd(), 'assets')

# Constant definition
BG_COLOR = '#ffbd59'
TEXTBOX = '#ffd48c'


class Entries:
    def __init__(self):
        self.textbox = ctk.CTkEntry(master=app,
                        placeholder_text="Type in your tweet...",
                        placeholder_text_color=("#3b3b39"),
                        width=526,
                        height=165,
                        border_width=0,
                        corner_radius=40,
                        fg_color=TEXTBOX,
                        text_font=('Aileron Bold', 14, "bold"),
                        justify=tk.CENTER)


    def get_textbox_entry(self, event):
        value = self.textbox.get()
        print(value)


class Images:
    def __init__(self):
        self.green_stain_img = tk.PhotoImage(file=f'{ASSET_PATH}/plama_zielona_png.png')


class Buttons:
    def __init__(self, app, image_handler, entry_handler):
        self.entry_handler = entry_handler
        self.green_stain = tk.Button(app, image=image_handler.green_stain_img,
                                borderwidth=0,
                                background=BG_COLOR,
                                activebackground=BG_COLOR,
                                command=self.clear_text)
    
    def clear_text(self):
        self.entry_handler.textbox.delete(0, tk.END)
        self.entry_handler.textbox.insert(0, "")

# Necessary obejcts creation
app = ctk.CTk()
image_handler = Images()
entry_handler = Entries()
button_handler = Buttons(app, image_handler, entry_handler)


# App configuration
app.title('Moody')
app.geometry("1280x720")
app.configure(bg=(BG_COLOR, TEXTBOX))
ctk.set_appearance_mode("system") #choose value from tuples: system -> default, dark -> second_value
# app.overrideredirect(True)

# Title bar
# title_bar = tk.Frame(app, bg='black', relief="raised")
# title_bar.pack(expand=1, fill=tk.X)
# title_label = tk.Label(title_bar, text='Moody', bg="black", fg="white")
# title_label.pack(side=tk.LEFT, pady=2)

# Elements placement
# Textbox
entry_handler.textbox.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Buttons
button_handler.green_stain.place(relx=0.55, rely=0.05)

# Utility function
def close_win(e):
    app.destroy()

# KEYS THAT ARE USED IN THE APP
app.bind('<Return>', entry_handler.get_textbox_entry)
# app.bind('b', entry_handler.clear_text)
app.bind('<Escape>', lambda e: close_win(e))


# print(font.families())
app.mainloop()




