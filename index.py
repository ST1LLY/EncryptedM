#   EncryptedM v1.0
#
#   Author: Savostyanov (ST1LLY) Konstantin - savostconst@yandex.ru

from tkinter import *
from socket import *
import time, json, _thread as thread

from Crypto.Cipher import AES
from Crypto import Random

from input_block import input_block
from setting_block import setting_block
from output_block import output_block

class form(input_block, setting_block, output_block):

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.makewidgets()

        self.AES_KEY_LENGTH = 16 #AES Key's bytes length to read from AES_KEY.txt

        self.AES_KEY = open('AES_KEY.txt','rb').read(self.AES_KEY_LENGTH)

    def makewidgets(self):
        row_1 = Frame()
        row_2 = Frame()

        row_1.pack(side=TOP, expand=YES, fill=BOTH)
        self.ob_makewidgets(parent=row_1)
        self.sb_makewidgets(parent=row_1)

        row_2.pack(side=TOP, expand=YES, fill=BOTH)
        self.ib_makewidgets(parent=row_2)

    def now(self):
        return time.asctime()

    #   Send message to destination host
    def set_message(self,status=0,message=""):

        json_request = None
        connect_ip = self.sb_ent_ip.get()
        serverPort = int(self.sb_ent_port.get())  # Get from form destination IP's port

        if status == 0:
            json_request = json.dumps({
                "status": 0
            }).encode('utf-8')
        else:
            iv = Random.new().read(AES.block_size)
            cipher = AES.new(self.AES_KEY, AES.MODE_CFB, iv)
            decoded_iv = iv.decode("latin-1")
            crypted_msg = cipher.encrypt(message)
            decoded_crypted_msg = crypted_msg.decode("latin-1")

            json_request = json.dumps({
                "iv": decoded_iv,
                "crypted_msg": decoded_crypted_msg,
                "status": 1
            }).encode('utf-8')


        try:
            self.sockobj = socket(AF_INET, SOCK_STREAM)
            self.sockobj.connect((connect_ip, serverPort))
            self.sockobj.send(json_request)
            self.sockobj.close()
            return 1
        except:
            self.set_connect_info("Error sending a message. Check out inputed data in setting block.")
            return 0

    #   Reset interface
    def reset_settings(self):
        self.sb_press = FALSE
        self.sb_btn.config(text='start')
        self.ib_btn.config(state=DISABLED)
        self.sockobj_listen.close()
        self.set_connect_info('Connection disabled')

    #   Open port and listen. Processing received messages.
    def able_connection(self,sockobj):
        flag = True
        while True:
            if flag == False: break
            connection, address = sockobj.accept()

            while True:
                data = connection.recv(1024)
                if not data: break

                decoded_data = json.loads(data.decode('utf-8'))
                status = decoded_data['status']

                if status == 0:
                    self.reset_settings()
                    flag = False
                    connection.close()
                    break

                iv = decoded_data['iv'].encode("latin-1")
                crypted_msg = decoded_data['crypted_msg'].encode("latin-1")
                decrypt_text = AES.new(self.AES_KEY, AES.MODE_CFB, iv).decrypt(crypted_msg)
                self.ob_settext('\nfrom: ' + self.now() + '\n' + decrypt_text.decode("utf-8"))
                self.ob_text.see(END)

    # "Send" button
    def ib_press_button(self,event=None):

        message = self.ib_gettext().encode()
        if self.set_message(1,message):
            self.ib_text.delete('1.0', END + '-1c')
            self.ib_text.mark_set(INSERT, 0.0)
            self.ib_text.focus()

            self.ob_settext('\nto: ' + self.now() + '\n' + message.decode())
            self.ob_text.see(END)

    def set_connect_info(self,text):
        self.ob_settext(25*'-' + '\n' + text + '\n' + 25*'-')
        self.ob_text.see(END)

    # "start/stop" button
    def sb_press_button(self):

        if not self.sb_press: # If clicked for "start" than initialize connection.
            myHost = self.sb_ent_my_ip.get()
            myPort = int(self.sb_ent_port.get())

            try:
                self.sockobj_listen = socket(AF_INET, SOCK_STREAM)
                self.sockobj_listen.bind((myHost, myPort))
                self.sockobj_listen.listen(1)
                thread.start_new_thread(self.able_connection, (self.sockobj_listen,))
            except:
                self.set_connect_info("Error of opening port. Check out inputed data in setting block.")
                return

            self.set_connect_info('Socket '+ str(myHost)+":"+ str(myPort) + ' opened and listening') # Output data about processing
            self.ib_btn.config(state=NORMAL) # Кнопка для отправки сообщений доступна. "Send" button is accessible
            self.sb_btn.config(text='stop') # Кнопка в блоке настроек меняет свою функцию на сброс соединения
            self.sb_press = TRUE # "Start" button pressed

        else: # If clicked "stop" than disable opened connection

            self.set_message()
            self.reset_settings()

if __name__ == '__main__':

    root = Tk()
    root.title('EncryptedM v1.0')
    fr = form()
    root.mainloop()