from tkinter import font, Tk, Label, Text, Button, Frame, LEFT, END, IntVar, Checkbutton
from arabic_reshaper import ArabicReshaper

__version__ = "v1.2.0"
configuration = {
    'delete_harakat': False
}
root = Tk()
root.geometry("400x650")
root.title("ara_resh ui v1")

reshaper = ArabicReshaper(configuration=configuration)

reverse_reshaper_dict = {
    'ﺍ': 'ا', 'ﺄ': 'ا', 'ﺇ': 'ا', 'ﺃ': 'ا',
    'ﺏ': 'ب', 'ﺐ': 'ب', 'ﺒ': 'ب', 'ﺑ': 'ب',
    'ﺕ': 'ت', 'ﺖ': 'ت', 'ﺘ': 'ت', 'ﺗ': 'ت',
    'ﺙ': 'ث', 'ﺚ': 'ث', 'ﺜ': 'ث', 'ﺛ': 'ث',
    'ﺝ': 'ج', 'ﺞ': 'ج', 'ﺠ': 'ج', 'ﺟ': 'ج',
    'ﺡ': 'ح', 'ﺢ': 'ح', 'ﺤ': 'ح', 'ﺣ': 'ح',
    'ﺥ': 'خ', 'ﺦ': 'خ', 'ﺨ': 'خ', 'ﺧ': 'خ',
    'ﺩ': 'د', 'ﺪ': 'د',
    'ﺫ': 'ذ', 'ﺬ': 'ذ',
    'ﺭ': 'ر', 'ﺮ': 'ر',
    'ﺯ': 'ز', 'ﺰ': 'ز',
    'ﺱ': 'س', 'ﺲ': 'س', 'ﺴ': 'س', 'ﺳ': 'س',
    'ﺵ': 'ش', 'ﺶ': 'ش', 'ﺸ': 'ش', 'ﺷ': 'ش',
    'ﺹ': 'ص', 'ﺺ': 'ص', 'ﺼ': 'ص', 'ﺻ': 'ص',
    'ﺽ': 'ض', 'ﺾ': 'ض', 'ﻀ': 'ض', 'ﺿ': 'ض',
    'ﻁ': 'ط', 'ﻂ': 'ط', 'ﻄ': 'ط', 'ﻃ': 'ط',
    'ﻅ': 'ظ', 'ﻆ': 'ظ', 'ﻈ': 'ظ', 'ﻇ': 'ظ',
    'ﻉ': 'ع', 'ﻊ': 'ع', 'ﻌ': 'ع', 'ﻋ': 'ع',
    'ﻍ': 'غ', 'ﻎ': 'غ', 'ﻐ': 'غ', 'ﻏ': 'غ',
    'ﻑ': 'ف', 'ﻒ': 'ف', 'ﻔ': 'ف', 'ﻓ': 'ف',
    'ﻕ': 'ق', 'ﻖ': 'ق', 'ﻘ': 'ق', 'ﻗ': 'ق',
    'ﻙ': 'ك', 'ﻚ': 'ك', 'ﻜ': 'ك', 'ﻛ': 'ك',
    'ﻝ': 'ل', 'ﻞ': 'ل', 'ﻠ': 'ل', 'ﻟ': 'ل',
    'ﻡ': 'م', 'ﻢ': 'م', 'ﻤ': 'م', 'ﻣ': 'م',
    'ﻥ': 'ن', 'ﻦ': 'ن', 'ﻨ': 'ن', 'ﻧ': 'ن',
    'ﻩ': 'ه', 'ﻪ': 'ه', 'ﻬ': 'ه', 'ﻫ': 'ه',
    'ﻭ': 'و', 'ﻮ': 'و',
    'ﻱ': 'ي', 'ﻲ': 'ي', 'ﻴ': 'ي', 'ﻳ': 'ي',
    'ﻻ': 'لا',
    'ﺎ': 'ا',
    'ﺔ': 'ة',
}


def take_input(event=None):
    input_word = inputtxt.get("1.0", 'end-1c')
    Output.delete("1.0", END)
    reshape = reshaper.reshape(input_word)
    if check_var.get() == 0:
        Output.insert(END, reshape)
    else:
        reshaped_lines = reshape.split('\n')
        reshaped_lines = ["{a:r:}" + line + "{a:r:}" for line in reshaped_lines]
        reshaped_text = '\n'.join(reshaped_lines)
        Output.insert(END, reshaped_text)


def copy_output(outtext):
    root.clipboard_clear()
    root.clipboard_append(outtext.get("1.0", 'end-1c'))


def paste_text():
    inputtxt.delete("1.0", END)
    inputtxt.insert(END, root.clipboard_get())
    take_input()


def reverse_text():
    reversedoutput.delete("1.0", END)
    reshaped_text = inputtxt.get("1.0", 'end-1c')
    reversedoutput.insert(END, reverse_reshaping(reshaped_text))


def reverse_reshaping(reshaped_text):
    recovered_text = ""
    i = 0
    while i < len(reshaped_text):
        if reshaped_text[i] in reverse_reshaper_dict:
            recovered_text += reverse_reshaper_dict[reshaped_text[i]]
            i += 1
        elif reshaped_text[i] == "ﻼ":
            recovered_text += "لا"
            i += 1
        else:
            recovered_text += reshaped_text[i]
            i += 1
    return recovered_text

def delete_text():
    inputtxt.delete("1.0", END)
    Output.delete("1.0", END)
    reversedoutput.delete("1.0", END)


arabic_font = font.Font(family="Arial", size=18)

l = Label(root, text="Enter text")
inputtxt = Text(root, height=5, width=40, bg="light yellow", font=arabic_font)
Output = Text(root, height=5, width=40, bg="light cyan", font=arabic_font)
reversedoutput = Text(root, height=5, width=40, bg="light gray", font=arabic_font)

inputtxt.bind("<KeyRelease>", take_input)

button_frame = Frame(root)
paste_button = Button(button_frame, text="Paste", command=paste_text)
copy_output_button = Button(button_frame, text="Copy Output", command=lambda: copy_output(Output))
delete_button = Button(button_frame, text="Delete", command=delete_text)

check_var = IntVar()
check = Checkbutton(root, text="Include {a:r:}", variable=check_var)
check_var.trace_add("write", lambda *args: take_input())

l2 = Label(root, text="Converted text")
l3 = Label(root, text="Reversed text")

rev_button_frame = Frame(root)
copy_reversed_button = Button(rev_button_frame, text="Copy reversed", command=lambda: copy_output(reversedoutput))
reverse_button = Button(rev_button_frame, text="Reverse", command=reverse_text)

l.pack()
inputtxt.pack()
button_frame.pack()
paste_button.pack(side=LEFT)
copy_output_button.pack(side=LEFT)
delete_button.pack(side=LEFT)
l2.pack()
Output.pack()
l3.pack()
rev_button_frame.pack()
reverse_button.pack(side=LEFT)
copy_reversed_button.pack(side=LEFT)
reversedoutput.pack()
check.pack()
root.mainloop()
