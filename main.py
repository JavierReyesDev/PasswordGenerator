from random import choice, shuffle
from tkinter import Tk, Label, Button, Frame, Radiobutton, StringVar, Entry
from data import letters, numbers, symbols

FONT = ("Arial", 10)

# Window
window = Tk()
window.config(bg="white")
window.geometry("280x320")
window.resizable(False, False)
window.grid_columnconfigure(0, weight=1)
window.title("Password Generator")

# First frame
frame = Frame(window, bg="white", width=200, height=200)
frame.grid()

option = StringVar(value="sorted")


def create_password():
    """Creates a password based on user input"""
    password = ""
    try:
        letters_count = nr_letters.get()
        symbols_count = nr_symbols.get()
        numbers_count = nr_numbers.get()
        if letters_count == "" or symbols_count == "" or numbers_count == "":
            result.config(text="Missing argument")
        else:
            letters_count = int(letters_count)
            symbols_count = int(symbols_count)
            numbers_count = int(numbers_count)
    except ValueError:
        result.config(text="Please enter valid numbers")
        return
    
    if option.get() == "sorted":
        for _ in range(letters_count):
            password += choice(letters)
        for _ in range(symbols_count):
            password += choice(symbols)
        for _ in range(numbers_count):
            password += choice(numbers)
    elif option.get() == "unsorted":
        my_list = []
        for _ in range(letters_count):
            my_list.append(choice(letters))
        for _ in range(symbols_count):
            my_list.append(choice(symbols))
        for _ in range(numbers_count):
            my_list.append(choice(numbers))
        shuffle(my_list)
        password = ''.join(my_list)
        
    result.config(text=password)


def copy_to_clipboard():
    """Clears the clipboard and copies the result to it"""
    window.clipboard_clear()
    window.clipboard_append(result.cget("text"))


# Labels and entries
Label(frame, text="Number of Letters:", bg="white", font=FONT).grid(row=0, column=0, padx=5, pady=10, sticky="w")
nr_letters = Entry(frame, width=10)
nr_letters.grid(row=0, column=1, pady=5, padx=5)

Label(frame, text="Number of Symbols:", bg="white", font=FONT).grid(row=1, column=0, padx=5, pady=10, sticky="w")
nr_symbols = Entry(frame, width=10)
nr_symbols.grid(row=1, column=1, pady=5, padx=5)

Label(frame, text="Number of Numbers:", bg="white", font=FONT).grid(row=2, column=0, padx=5, pady=10, sticky="w")
nr_numbers = Entry(frame, width=10)
nr_numbers.grid(row=2, column=1, pady=5, padx=5)

# RadioButtons
Radiobutton(frame, text="Sorted", variable=option, value="sorted", bg="white", font=FONT)\
    .grid(row=3, column=0, padx=10, pady=5, sticky="w")
Radiobutton(frame, text="Unsorted", variable=option, value="unsorted", bg="white", font=FONT)\
    .grid(row=4, column=0, padx=10, pady=5, sticky="w")

# Second frame and Buttons
buttonsFrame = Frame(bg="white", width=280)
buttonsFrame.grid(sticky="s")

generate_button = Button(buttonsFrame, text="Generate", command=create_password, font=FONT)
generate_button.grid(row=5, column=0, padx=10, pady=10, sticky="w")  # Center the button by spanning both columns

copy_button = Button(buttonsFrame, text="Copy", command=copy_to_clipboard, font=FONT)
copy_button.grid(row=5, column=1, padx=10, pady=10, sticky="e")  # Position the "Copy" button to the right of "Generate"

# Result Label
result = Label(window, bg="light gray", font=FONT, height=3)
result.grid(row=6, padx=15, pady=5, sticky="ew")

window.mainloop()
