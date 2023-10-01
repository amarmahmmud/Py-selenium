import sys
from tkinter import *
from selenium import webdriver

class WebPageAutomator:
    def __init__(self):
        self.mGui = Tk()
        self.ip = StringVar()
        self.mGui.geometry('450x450')
        self.mGui.title('URL')
        self.mlabel = Label(self.mGui, text="Please insert URL")
        self.mlabel.pack()
        self.mEntry = Entry(self.mGui, width=70, textvariable=self.ip)
        self.mEntry.pack()
        self.mbutton = Button(self.mGui, text="OK", command=self.go_url, fg='black', bg='grey')
        self.mbutton.pack()

    def go_url(self):
        URL = self.ip.get()
        driver = webdriver.Chrome("directory of chromedriver\\chromedriver.exe")
        driver.get(URL)
        driver.maximize_window()
        with open("Input_info.txt", "r+") as fo:
            context = fo.read()
            context2 = context.split("\n")
            counter = len(context2)
            for i in range(0, counter, 2):
                name = context2[i]
                key = context2[i + 1]
                try:
                    driver.find_element_by_name(name).send_keys(key)
                except:
                    pass

if __name__ == "__main__":
    automator = WebPageAutomator()
    automator.mGui.mainloop()
