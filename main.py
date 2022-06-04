from tkinter import *


# Convert miles to Km
def miles_to_km(our_input):
    new_text = float(our_input)
    number = round((new_text * 1.6), 2)
    print(number)
    return number


# Set layer for our result
def set_the_layer(n):
    my_label00 = Label(text="", font=("Arial", 12))
    my_label00.grid(column=1, row=2)
    my_label00.config(text=n)


# Do on the click
def button_clicked():
    # Call  function, return the convert result
    num = miles_to_km(input.get())
    # Call function, to set up label for result
    set_the_layer(num)
    print("Calculate")

# Object window, setting basic parameter of window
window = Tk()
window.title("Convertor")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# List of texts and his positioning
text_t = ["Enter number: ", "Miles", "Km", "is equal to: "]
position_t = [[0, 0], [3, 0], [3, 2], [0, 2]]

# Loop through lists and set up the text and his position
for i in range(len(text_t)):
    my_label = Label(text="", font=("Arial", 12))
    my_label.config(text=text_t[i])
    my_label.grid(column=position_t[i][0], row=position_t[i][1])


# Button settings
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=3)

# Place for insert a number from user
input = Entry()
print(input.get())
input.grid(column=1, row=0)


window.mainloop()