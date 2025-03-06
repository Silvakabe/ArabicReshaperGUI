from tkinter import font, Tk, Label, Text, Button, Checkbutton, IntVar, END, Frame, LEFT
from arabic_reshaper import ArabicReshaper

configuration = {
    'delete_harakat': False
}
root = Tk()
root.geometry("400x500")
root.title("umi ara_resh test")

reshaper = ArabicReshaper(configuration=configuration)

def Take_input():
    INPUT = inputtxt.get("1.0",'end-1c')
    Output.delete(0.0,END)
    reshape = reshaper.reshape(INPUT)
    Output.insert(END, reshape)

def copy_output():
    root.clipboard_clear()
    root.clipboard_append(Output.get("1.0", 'end-1c'))

def paste_text():
    inputtxt.delete("1.0", END)
    inputtxt.insert(END, root.clipboard_get())

# استخدام خط يدعم الحركات
arabic_font = font.Font(family="Traditional Arabic", size=18)

l = Label(root, text="Enter text")
inputtxt = Text(root, height=5, width=40, bg="light yellow", font=arabic_font)
Output = Text(root, height=5, width=40, bg="light cyan", font=arabic_font)

button_frame = Frame(root)
paste_button = Button(button_frame, text="Paste", command=paste_text)
Display = Button(button_frame, text="Convert", command=Take_input)
copy_output_button = Button(button_frame, text="Copy Output", command=copy_output)



l.pack()
inputtxt.pack()
button_frame.pack()
paste_button.pack(side=LEFT)
Display.pack(side=LEFT)
copy_output_button.pack(side=LEFT)
Output.pack()


root.mainloop()