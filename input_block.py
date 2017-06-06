from tkinter import *

class input_block(Frame):

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, side=TOP,fill=BOTH)
        self.ib_makewidgets()
        self.set_text_message('input_block\n')

    def ib_makewidgets(self,parent=None):

        # Rows of frame for drawing widgets
        row_1 = Frame(parent)
        row_2 = Frame(parent)

        # All set of widgets of input block
        sbar = Scrollbar(row_1)
        text = Text(row_1)
        btn = Button(row_2)

        # Setting of widgets
        text.config(yscrollcommand=sbar.set, width=40, height=5, relief=SUNKEN)
        sbar.config(command=text.yview)
        btn.config(text='Send', command=self.ib_press_button, width=10, state=DISABLED)

        row_1.pack(side=TOP, expand=YES, fill=BOTH)
        sbar.pack(side=RIGHT, fill=BOTH)
        text.pack(side=LEFT, expand=YES, fill=BOTH)

        row_2.pack(side=LEFT, fill=BOTH)
        btn.pack(side=LEFT)

        self.ib_btn = btn
        self.ib_text = text

    def set_text_message(self, text=''):
        self.ib_text.insert(END, text)

    def ib_gettext(self):
        return self.ib_text.get('1.0', END+'-1c')

    def ib_press_button(self,event=None):
        print(event)
        pass

if __name__ == '__main__':
    root = Tk()
    st = input_block()
    root.mainloop()
