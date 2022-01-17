import tkinter as tk
from Levenshtein import levenshtein
from SpellCheckBottomUp import buttom_up_edit_distance
from InitWordBank import initWordBank
from insertionSort import insertionSort
from BubbleSort import bubbleSort
from ShellSort import shellSort
# edit distance functions
edit_func = {
    "levenshtein" : levenshtein,
    "bottom up edit distance" : buttom_up_edit_distance,
}

# sort function
sort_func = {
    "insertion sort": insertionSort,
    "bubble sort": bubbleSort,
    "shell sort": shellSort
}

# global index value
index = 0

# suggestion Label
sug_label = None

# next button
nextBut = None

def initialize():
    global textentry, wordBank
    sort_menu_label.pack_forget()
    edit_menu_label.pack_forget()
    edit_drop_down_menu.pack_forget()
    sort_drop_down_menu.pack_forget()
    initialize_but.pack_forget()
    # initialize the wordBank
    wordBank = initWordBank(edit_func[selected.get()])

    # create an information for the user to input a text to something
    tk.Label(window, text = "Enter any word to be checked", font = "none 12").place(x = 100, y = 15)

    # create a text entry for the user to enter a word
    textentry = tk.Entry(window, width = 20, justify = 'center')
    textentry.place(x = 142, y = 45)

    # Create a button for checking the inputted text
    tk.Button(window, text = "check", width = 6, command = Check).place(x=177, y=75)

# show the suggested text
def Check():
    global suggested, index, sug_label, nextBut
    if sug_label != None:
        sug_label.place_forget()
        nextBut.place_forget()
    index = 0
    text = textentry.get()
    suggested, found = wordBank.search(text, 2)
    insertionSort(suggested)
    if (not found) and text != '':
        sug_label = tk.Label(window, text = suggested[index][1], font = "none 12")
        sug_label.place(x=(152), y=(175))
        nextBut = tk.Button(window, text = "next", width = 6, command = Next)
        nextBut.place(x=(202), y=(175))

def Next():
    global index
    index += 1
    try:
        sug_label.config(text=suggested[index][1])
    except IndexError:
        index = 0
        sug_label.config(text=suggested[index][1])

# initialize the window
window = tk.Tk()
window.title("word suggestor")

selected = tk.StringVar()
selected.set("levenshtein")

sorting = tk.StringVar()
sorting.set("insertion sort")

edit_menu_label = tk.Label(window, text = "Choose the function for getting the minimum edit distance", font = "none 12")
edit_menu_label.pack()

edit_drop_down_menu = tk.OptionMenu(window, selected, "levenshtein", "bottom up edit distance")
edit_drop_down_menu.pack(pady=(0, 25))

sort_menu_label = tk.Label(window, text = "Choose the function to sort the suggestion result", font = "none 12")
sort_menu_label.pack()

sort_drop_down_menu = tk.OptionMenu(window, sorting, "insertion sort", "bubble sort", "shell sort")
sort_drop_down_menu.pack(pady=(0, 70))

initialize_but = tk.Button(window, text = "initialize", width = 6, command = initialize)
initialize_but.pack()

# create a label for the text suggestion
suggested = []

window.geometry("427x250")
window.minsize(427, 250)
window.maxsize(427, 250)
window.mainloop()