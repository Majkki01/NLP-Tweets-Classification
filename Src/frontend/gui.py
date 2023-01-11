import tkinter as tk
import customtkinter as ctk
import os
import sys
from PIL import Image, ImageTk
import time
sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'model'))
from predict_sentiment import predict_sentiment
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
                        justify=tk.CENTER,
                        state="normal")


    def get_textbox_entry(self):
        value = self.textbox.get()
        print(value)


class Images:
    def __init__(self, app):
        # image import
        self.exit_button_img = tk.PhotoImage(file=f'{ASSET_PATH}/exit_button.png')
        self.analyse_sentiment_img = tk.PhotoImage(file=f'{ASSET_PATH}/analyse_sentiment_button.png')
        self.how_does_it_work_img = tk.PhotoImage(file=f'{ASSET_PATH}/how_does_it_work_button.png')
        self.about_us_img = tk.PhotoImage(file=f'{ASSET_PATH}/about_us_button.png')
        self.clear_textbox_img = tk.PhotoImage(file=f'{ASSET_PATH}/clear_textbox_button.png')
        self.happy_emote_img = tk.PhotoImage(file=f'{ASSET_PATH}/happy_emote.png')
        self.angry_emote_img = tk.PhotoImage(file=f'{ASSET_PATH}/angry_emote.png')
        self.confused_emote_img = tk.PhotoImage(file=f'{ASSET_PATH}/confused_emote.png')
        self.sad_emote_img = tk.PhotoImage(file=f'{ASSET_PATH}/sad_emote2.png')
        self.moody_app_text_img = tk.PhotoImage(file=f'{ASSET_PATH}/moody_app_text.png')


        # creating display boxes for images
        self.happy_emote = ctk.CTkLabel(master=app, 
                                        width=10, height=120, 
                                        image=self.happy_emote_img) 
        self.angry_emote = ctk.CTkLabel(master=app, 
                                        width=10, height=120, 
                                        image=self.angry_emote_img) 
        self.confused_emote = ctk.CTkLabel(master=app, 
                                        width=10, height=120, 
                                        image=self.confused_emote_img) 
        self.sad_emote = ctk.CTkLabel(master=app, 
                                        width=10, height=120, 
                                        image=self.sad_emote_img) 
        self.moody_app_text = ctk.CTkLabel(master=app,
                                            width=10, height=1,
                                            image=self.moody_app_text_img)


class Buttons:
    def __init__(self, app, image_handler, entry_handler):
        self.entry_handler = entry_handler
        self.authors_count = 0
        self.what_is_it_about_count = 0
        self.exit_button = tk.Button(app, image=image_handler.exit_button_img,
                                borderwidth=0,
                                background=(BG_COLOR),
                                activebackground=(BG_COLOR),
                                command=self.exit_application)
        self.analyse_sentiment_button = tk.Button(app, image=image_handler.analyse_sentiment_img,
                                borderwidth=0,
                                background=(BG_COLOR),
                                activebackground=(BG_COLOR),
                                command=self.analyse_sentiment)
        self.how_does_it_work_button = tk.Button(app, image=image_handler.how_does_it_work_img,
                                borderwidth=0,
                                background=(BG_COLOR),
                                activebackground=(BG_COLOR),
                                command=self.how_does_it_work)
        self.about_us_button = tk.Button(app, image=image_handler.about_us_img,
                                borderwidth=0,
                                background=(BG_COLOR),
                                activebackground=(BG_COLOR),
                                command=self.about_us)
        self.clear_textbox_button = tk.Button(app, image=image_handler.clear_textbox_img,
                                borderwidth=0,
                                background=(BG_COLOR),
                                activebackground=(BG_COLOR),
                                command=self.clear_text)


    def clear_text(self):
        self.entry_handler.textbox.insert(0, "")
        self.entry_handler.textbox.delete(0, tk.END)


    def about_us(self):
        authors_list = ["Authors:", "Tomasz Kuczynski", "Marta Frackowiak", "Jakub Sochacki", "Maciej Swietlik", "Michal Rejmak", "Lilianna Czaniecka"]
        if self.authors_count < len(authors_list):
            self.entry_handler.textbox.delete(0, tk.END)
            self.entry_handler.textbox.insert(0, authors_list[self.authors_count])
            self.authors_count += 1
            app.after(1000, self.about_us)
        else:
            self.authors_count = 0
            self.entry_handler.textbox.delete(0, tk.END)
        

    def how_does_it_work(self):
        display_list = ["It is pretty simple...", "You type in a tweet",
                        "Click analyse sentiment button", "Observe the emotes", "Done!" ]
        if self.what_is_it_about_count < len(display_list):
            self.entry_handler.textbox.delete(0, tk.END)
            self.entry_handler.textbox.insert(0, display_list[self.what_is_it_about_count])
            self.what_is_it_about_count += 1
            app.after(1500, self.how_does_it_work)
        else:
            self.what_is_it_about_count = 0
            self.entry_handler.textbox.delete(0, tk.END)


    def analyse_sentiment(self, event=None):
        tweet = entry_handler.get_textbox_entry()
        predict_sentiment(tweet) 


    def exit_application(self):
        app.destroy()


# Necessary obejcts creation
app = ctk.CTk()
image_handler = Images(app)
entry_handler = Entries()
button_handler = Buttons(app, image_handler, entry_handler)


# App configuration
app.title('Moody')
app.geometry("1280x720")
app.configure(bg=(BG_COLOR))
ctk.set_appearance_mode("system") #choose value from tuples: system -> default, dark -> second_value
# app.overrideredirect(True)


# Textbox
entry_handler.textbox.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


# Buttons
button_handler.exit_button.place(relx=0.1, rely=0.4)
button_handler.analyse_sentiment_button.place(relx=0.3, rely=0.1)
button_handler.how_does_it_work_button.place(relx=0.5, rely=0.1)
button_handler.about_us_button.place(relx=0.70, rely=0.18)
button_handler.clear_textbox_button.place(relx=0.80, rely=0.45)


# Images
image_handler.happy_emote.place(relx=0.15, rely=0.7)
image_handler.angry_emote.place(relx=0.35, rely=0.7)
image_handler.confused_emote.place(relx=0.55, rely=0.7)
image_handler.sad_emote.place(relx=0.75, rely=0.7)
image_handler.moody_app_text.place(relx=.04, rely=.06)


# Utility function
def close_win(e):
    app.destroy()


# KEYS THAT ARE USED IN THE APP
app.bind('<Return>', button_handler.analyse_sentiment)
app.bind('<Escape>', lambda e: close_win(e))


app.mainloop()



