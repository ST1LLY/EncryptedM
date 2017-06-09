from tkinter import *

class output_block(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack(side=LEFT, expand=YES, fill=BOTH)
        self.ob_makewidgets()
        self.ob_settext('output_block\n')

    def ob_makewidgets(self,parent=None):
        sbar = Scrollbar(parent)
        text = Text(parent, relief=SUNKEN)
        sbar.config(command=text.yview)
        text.config(yscrollcommand=sbar.set, width=60,height=10)
        text.pack(side=LEFT, expand=YES, fill=BOTH)
        sbar.pack(side=LEFT, fill=Y)

        self.ob_text = text
        self.ob_sbar = sbar


    def ob_settext(self, text=''):

        #self.text.delete('1.0', END)
        self.ob_text.insert(END, text + '\n')
        #self.ob_text.mark_set(INSERT, END)
        #self.ob_text.focus()

    def gettext(self):
        return self.ob_text.get('1.0', END+'-1c') # whole text
    def send_text(self):
        pass

if __name__ == '__main__':
    root = Tk()
    st = output_block()
    root.mainloop()
