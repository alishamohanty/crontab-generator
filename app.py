import tkinter as tk


class button:

    # Default design of button in CronTab
    text = ""
    background_color = "#FF0000"
    foreground_color = "#FFFFFF"

    def __init__(self, text, background_color, foreground_color):
        self.text = text
        self.background_color = background_color
        self.foreground_color = foreground_color

    def create_button(self, root, command):
        btn = tk.Button(root, text=self.text, bd=self.background_color, fg=self.foreground_color, command=command)
        return btn


class cronTabGUI:
    # Default values for cron tab GUI
    title = ""
    size = "100*100"

    def __init__(self, title, size):
        self.title = title
        self.size = size

    def add_button(self):
        pass


