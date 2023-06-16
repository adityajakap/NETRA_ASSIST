import tkinter 
from tkinter import Tk, Label
import adit
import AH
from PIL import Image, ImageTk

#-- Fungsi untuk membuat gif menjadi bergerak.
def update_frame(idx):
    frame = frames[idx]
    idx = (idx + 1) % frame_count
    label.configure(image=frame)
    app.after(20, update_frame, idx)

#-- Fungsi untuk menyapa user.
def welcome():
    adit.engine.say("Hi! Welcome to Netra Asssist!, Please Say Buka Menu to open menu or say anything else to exit the program")
    adit.engine.runAndWait()

#-- Fungsi untuk binding keyboard.
def on_key_press(event):
    if event.keysym == "space":
        adit.running()
    if event.keysym == "Escape":
        exit()

#-- Main menu.
def menu():
    adit.engine.say("Welcome to main menu, Please press space to scan the expired products or press escape to exit the program")
    adit.engine.runAndWait()
    global app, label, frames, frame_count
    app = Tk()
    app.title("Netra Assist")
    app.geometry("500x500")

    frames = []
    frame_count = 0

    gif = Image.open("menun.gif")
    gif_frames = gif.n_frames

    for i in range(gif_frames):
        gif.seek(i)
        frame = ImageTk.PhotoImage(gif)
        frames.append(frame)
        frame_count += 1

    label = Label(app)
    label.pack()

    app.after(0, update_frame, 0)
    app.bind("<KeyPress>", on_key_press)
    app.mainloop()

# --Exit
def exit():
    adit.engine.say("Thank you for using Netra Assist! BYE BYE!")
    adit.engine.runAndWait()
    app.destroy()

def main():
    welcome()
    AH.start_speech()
    print(AH.text)
    if AH.text.lower() == "buka menu" or AH.text.lower() == "open menu":
        menu()
    else:
        adit.engine.say("Thank You!") 
        adit.engine.runAndWait()

if __name__ == '__main__':
    main()
