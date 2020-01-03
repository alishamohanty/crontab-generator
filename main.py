import tkinter as tk


# Creates a new Cron Job
def add_cron_job():
    pass
    # code


# Checks the Status of Cron Jobs
def status():
    pass
    # code


# Create Button
def create_button(text, command, app):
    if text == "Status":
        b = "#24292E"
        f = "#BEBFC1"
    elif text == "Open YouTube":
        b = "#FF0000"
        f = "#FFFFFF"

    btn = tk.Button(app, bg=b, fg=f, text=text, command=command)
    btn.pack(ipadx=20, ipady=10, padx=20, pady=20)


def crontab_app(root, app):
    # ! Define the structure of the app
    root.title("Crontab Generator")

    root.geometry("500x500")

    # ! define the buttons
    create_button("Status", status, app)
    create_button("Add New Cron Job", add_cron_job, app)
    root.mainloop()


root = tk.Tk()
app = tk.Frame(root)
app.place(relwidth=1, relheight = 1)
crontab_app(root, app)
