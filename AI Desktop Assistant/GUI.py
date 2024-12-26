from tkinter import *
from PIL import Image, ImageTk   # pip install pillow
import speech_to_text
import action

root = Tk()
root.title("AI Assistant")
root.geometry("550x675")  # width x height
root.resizable(False, False)  # window resizing off
root.config(bg="#5C7595")  # soft grayish background color

# ask function
def ask ():
    user_val = speech_to_text.speech_to_text()
    bot_val = action.Action(user_val)
    text.insert(END, 'USER--->'+user_val+"\n")
    if bot_val != None:
        text.insert(END, "BOT <---"+str(bot_val)+"\n")
    if bot_val == "Ok sir have a great day ahead shutting down":
        root.destroy()

# send function
def send ():
    send = entry.get()
    bot = action.Action(send)
    text.insert(END, 'USER--->'+send+"\n")
    if bot != None:
        text.insert(END, "BOT <---"+str(bot)+"\n")
    if bot == "Ok sir have a great day ahead shutting down":
        root.destroy()
    
# delete function
def del_text ():
    text.delete('1.0',"end")


# Frame
frame = LabelFrame(root, padx=100, pady=7, borderwidth=3, relief="raised")
frame.config(bg="#5C7595")
frame.grid(row=0, column=0, padx=55, pady=10)

# Text Label
text_label = Label(frame, text="AI Assistant", font=("Comic Sans MS", 14, "bold"), bg="#F8E1C6")
text_label.grid(row=0, column=0, padx=20, pady=10)

# Image
image = ImageTk.PhotoImage(Image.open("images/th.jpeg"))  # Ensure the path to "th.jpeg" is correct
image_label = Label(frame, image=image)
image_label.grid(row=1, column=0, pady=20)

# Adding a text window beneath the image
# The y-coordinate ensures the text box is below the frame (image position + padding)
text = Text(root, font=('Courier', 10, 'bold'), bg="#F8E1C6")
text.place(x=100, y=350, width=375, height=100)  # Adjust y for proper placement


# entry widget
entry = Entry(root, justify=CENTER)
entry.place(x=100, y = 475, width=350, height=30)

# button 1

Button1 = Button(root, text = "ASK", bg="#F8E1C6", pady=16, padx=40, borderwidth=3, relief=SOLID , command=ask)
Button1.place(x = 70, y = 575)

# button 2

Button2 = Button(root, text = "Send", bg="#F8E1C6", pady=16, padx=40, borderwidth=3, relief=SOLID , command=send)
Button2.place(x = 400, y = 575)

# button 3

Button3 = Button(root, text = "Delete", bg="#F8E1C6", pady=16, padx=40, borderwidth=3, relief=SOLID , command=del_text)
Button3.place(x = 225, y = 575)

root.mainloop()
