'''
TO DO:
Displaying the evolution chain of the Pokémon, their abilities, moves, and stats
'''

import tkinter
import requests  # for API
from tkinter import *  # for GUI
from PIL import Image, ImageTk  # This is to show the image in the same window
import os  # Sprite in the terminal
import io

# Assign window
w = Tk()
w.title('Pokemon App')
w.geometry('500x500')

# Make window appear in the middle of the screen
# Get user screen width and height
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()

# Calculate position x and y coordinates
x = (screen_width / 2) - (500 / 2)
y = (screen_height / 2) - (500 / 2)


# This is to show the sprite, if the user wants
def show_sprite():
    pokemonInput = inputtxt.get(1.0, 'end-1c')
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemonInput}/'
    response = requests.get(url)
    responseJSN = response.json()
    sprite_url = responseJSN['sprites']['front_default']
    sprite_response = requests.get(sprite_url)
    # API will return binary data for the sprite, this just makes it an image object that can be used by the PIL
    # library.
    image_data = io.BytesIO(sprite_response.content)
    image = Image.open(image_data)
    photo = ImageTk.PhotoImage(image)

    sprite_label.config(image=photo)
    sprite_label.image = photo


# When button is clicked (after text)
def clicked():
    # Get user input
    pokemonInput = inputtxt.get(1.0, 'end-1c')
    # API call
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemonInput}/'

    # Get a response from API call and store it as JSON
    response = requests.get(url)
    responseJSN = response.json()

    # Output attributes given Pokemon name (can be changed later btw)
    base_experience = responseJSN['base_experience']
    height = responseJSN['height']
    weight = responseJSN['weight']

    # Output those JSN stuff above
    output_label.config(text="Output: " + '\n' + f'Base experience: {base_experience}' + '\n' + f'Height: {height}' +
                             '\n' + f'Weight: {weight}')

    # I want the 'Enter' button to disappear after it is pressed and the information is there, looks better that way :)
    btn.pack_forget()
    # This is to show the 'Sprite' button to the user
    sprite_button.pack()


# TextBox Creation
inputtxt = tkinter.Text(w, height=5, width=20)
inputtxt.pack()

# Output label beneath textbox
output_label = tkinter.Label(w, text="")
output_label.pack()

'''
txt = Entry(w, width=10)
txt.grid(column=1, row=0)
'''
# 'Enter' button
btn = tkinter.Button(w, text='Enter', fg='Blue', command=clicked)
btn.pack()

# 'Sprite' button
sprite_button = Button(w, text="Sprite", command=show_sprite)
sprite_label = Label(w)
sprite_label.pack()

w.geometry("+%d+%d" % (x, y))
# Run Tkinter
w.mainloop()
