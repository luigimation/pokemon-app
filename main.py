import requests  # for API
import tkinter  # for GUI
import os  # Sprite in the terminal

# Assign window
w = tkinter.Tk(screenName=None, baseName=None, className='Test', useTk=True)
w.geometry('500x500')

# Make window appear in the middle of the screen
# Get user screen width and height
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()

# Calculate position x and y coordinates
x = (screen_width / 2) - (500 / 2)
y = (screen_height / 2) - (500 / 2)

'''
pokemonInput = input('Name: ')

url = f'https://pokeapi.co/api/v2/pokemon/{pokemonInput}/'

response = requests.get(url)
responseJSN = response.json()

base_experience = responseJSN['base_experience']
height = responseJSN['height']
weight = responseJSN['weight']

print(f'Base experience: {base_experience}')
print(f'Height: {height}')
print(f'Weight: {weight}')

sprite_url = responseJSN['sprites']['front_default']
sprite_response = requests.get(sprite_url)

with open('sprite.png', 'wb') as f:
    f.write(sprite_response.content)

viewImage = input('Would you like to view the image? Y/N')

if viewImage == 'Y':
    os.system('cacaview sprite.png')
else:
    print('Goodbye!')
    quit()
'''

w.geometry("+%d+%d" % (x, y))
# Run Tkinter
w.mainloop()
