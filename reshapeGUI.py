from tkinter import font, Tk, Label, Text, Button, Frame, LEFT, END, IntVar, Checkbutton
from arabic_reshaper import ArabicReshaper

configuration = {
    'delete_harakat': False
}
root = Tk()
root.geometry("400x400")
root.title("umi ara_resh test")

reshaper = ArabicReshaper(configuration=configuration)

def Take_input(event=None):  # Event argument needed for key binding
    INPUT = inputtxt.get("1.0", 'end-1c')
    Output.delete("1.0", END)
    reshape = reshaper.reshape(INPUT)
    if check_var.get() == 0:
        Output.insert(END, reshape)
    else:
        reshaped_lines = reshape.split('\n')
        reshaped_lines = ["{a:r:}" + line + "{a:r:}" for line in reshaped_lines]
        reshaped_text = '\n'.join(reshaped_lines)
        Output.insert(END, reshaped_text)

def copy_output():
    root.clipboard_clear()
    root.clipboard_append(Output.get("1.0", 'end-1c'))

def paste_text():
    inputtxt.delete("1.0", END)
    inputtxt.insert(END, root.clipboard_get())
    Take_input()


arabic_font = font.Font(family="Arial", size=18)

l = Label(root, text="Enter text")
inputtxt = Text(root, height=5, width=40, bg="light yellow", font=arabic_font)
Output = Text(root, height=5, width=40, bg="light cyan", font=arabic_font)


inputtxt.bind("<KeyRelease>", Take_input)

button_frame = Frame(root)
paste_button = Button(button_frame, text="Paste", command=paste_text)
copy_output_button = Button(button_frame, text="Copy Output", command=copy_output)

check_var = IntVar()
check = Checkbutton(root, text="Include {a:r:}", variable=check_var)
check_var.trace_add("write", lambda *args: Take_input())  # Update output when check_var changes

l.pack()
inputtxt.pack()
button_frame.pack()
paste_button.pack(side=LEFT)
copy_output_button.pack(side=LEFT)
Output.pack()
check.pack()

root.mainloop()