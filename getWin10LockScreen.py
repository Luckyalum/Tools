#-*- coding = utf8 -*-
# 2017/09/10 by Luckyalum
# This script is used to copy Win10's lock screen wallpaper to the user's picture directory


from tkinter import *
import os
import shutil

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameLabel = Label(self, text='Please input your windows user name:')
        self.nameLabel.pack()
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='start', command=self.hello)
        self.alertButton.pack()
        self.resultLabel = Label(self, text=' ')
        self.resultLabel.pack()

    def hello(self):
        self.resultLabel['text'] = "Running"
        user_name = self.nameInput.get()
        output_path = 'C:\\Users\\'+user_name+'\\Pictures\\Win10LockScreen'
        if os.path.exists(output_path):
            shutil.rmtree(output_path)
        mydirs = os.listdir('C:\\Users\\'+user_name+'\\AppData\\Local\\Packages')
        random_name = ''
        for dir in mydirs:
            if 'Microsoft.Windows.ContentDeliveryManager' in dir :
                random_name = dir
                break;
        path = 'C:\\Users\\'+user_name+'\\AppData\\Local\\Packages\\'+random_name+'\\LocalState\\Assets'
        shutil.copytree(path,output_path)
        imgs = os.listdir(output_path)
        for img in imgs:
            os.rename(output_path+'\\'+img,output_path+'\\'+img+'.jpg')

        self.resultLabel['text'] = "Finished"

app = Application()
app.master.title('getWin10LockScreen')
app.mainloop()
