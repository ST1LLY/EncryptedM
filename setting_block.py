from tkinter import *

class setting_block(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH, side=RIGHT)
        self.sb_makewidgets()

    def sb_makewidgets(self,parent=None):

        # Rows of frame for drawing widgets (Ряды фрейма для отрисовки виджетов)
        row_1 = Frame(parent)
        row_2 = Frame(parent)

        row_3 = Frame(parent)
        row_4 = Frame(parent)

        # All set of widgets of setting block (Весь набор виджетов блока настроек)
        lab_ip = Label(row_1, width=15,text='destionation IP:')
        ent_ip = Entry(row_1)

        lab_my_ip = Label(row_2, width=15, text='my IP:')
        ent_my_ip = Entry(row_2)

        lab_port = Label(row_3, width=15, text='port:')
        ent_port = Entry(row_3)

        btn = Button(row_4, text='start', command=self.sb_press_button)

        # Drawing in 1st row of frame (Отрисовка на 1-м ряду фрейма)
        row_1.pack(side=TOP, fill=X)
        lab_ip.pack(side=LEFT, fill=X)
        ent_ip.pack(side=RIGHT, expand=YES,fill=X)
        ent_ip.insert(0, '192.168.1.10')

        # Drawing in 2nd row of frame (Отрисовка на 2-м ряду фрейма)
        row_2.pack(side=TOP, fill=X)
        lab_my_ip.pack(side=LEFT, fill=X)
        ent_my_ip.pack(side=RIGHT, expand=YES, fill=X)
        ent_my_ip.insert(0, '192.168.1.10')

        # Drawing in 3rd row of frame (Отрисовка на 3-м ряду фрейма)
        row_3.pack(side=TOP, fill=X)
        lab_port.pack(side=LEFT, fill=X)
        ent_port.pack(side=RIGHT, expand=YES, fill=X)
        ent_port.insert(0,'50007')

        # Drawing in 4th row of frame (Отрисовка на 4-м ряду фрейма)
        row_4.pack(side=TOP, fill=X)
        btn.pack(side=RIGHT)

        self.sb_ent_ip = ent_ip
        self.sb_ent_my_ip = ent_my_ip
        self.sb_ent_port = ent_port
        self.sb_btn = btn
        self.sb_press = FALSE
    def sb_press_button(self):
        pass
if __name__ == '__main__':
    root = Tk()
    sb = setting_block()
    root.mainloop()