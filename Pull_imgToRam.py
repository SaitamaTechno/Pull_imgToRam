import io
import requests
import tkinter as tk
from PIL import Image, ImageTk

url = 'https://m.media-amazon.com/images/I/614VmsFwoNL._SX355_.jpg'
data = requests.get(url).content
img = Image.open(io.BytesIO(data))

c=tk.Tk()
c.geometry('300x300+400+100') # size of the window and location on the screen
c.title('PROFILE')

#load=Image.open('untitled.png')
render=ImageTk.PhotoImage(img)
img=tk.Label(c,image=render)
img.pack()

c.mainloop()
