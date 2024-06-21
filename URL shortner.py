from tkinter import *
import pyshorteners

win = Tk()
win.geometry("400x270")  # for window size
win.configure(bg="gray")  # for background color
win.title("URL Shortener")

# Label for entering user URL
Label(win, text="Enter Your URL Link", bd=3, font="impact 20 italic", bg="black", fg="white").pack(fill="x")

# Entry Box for URL
entry1 = Entry(win, font='10', bd=3, width=30)
entry1.pack(pady=10)

# Entry Box for shortened URL
entry2 = Entry(win, bg="lightgray", font=14, width=30)
entry2.pack(pady=13)

def short_url():
    url = entry1.get()  # Get the URL from the entry box
    if url:
        s = pyshorteners.Shortener().tinyurl.short(url)  # Shorten the URL
        entry2.delete(0, END)  # Clear the entry box
        entry2.insert(END, s)  # Insert the shortened URL
def copy_to_clipboard():
    win.clipboard_clear()
    win.clipboard_append(entry2.get())
    msgbox.showinfo("Copied", "Shortened URL copied to clipboard")



# Button to trigger URL shortening
Button(win, text="Short URL", bg="blue", fg="white", width="20", command=short_url).pack()
#Button to copy shortened URL to clipboard
Button(win, text="Copy To Clipboard", bg ="green", fg = "white",width="20", command=copy_to_clipboard).pack(pady=5)

mainloop()
