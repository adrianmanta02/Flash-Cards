from tkinter import * 
import pandas
import random

# ----------------------------------- CONSTANT VARIABLES ----------------------------------- 
CARD_BACK = "C:\\Users\\Adrian\\Desktop\\vsc\\PYTHON\\day-30-flashcards\\card_back.png"
CARD_FRONT = "C:\\Users\\Adrian\\Desktop\\vsc\\PYTHON\\day-30-flashcards\\card_front.png"
RIGHT = "C:\\Users\\Adrian\\Desktop\\vsc\\PYTHON\\day-30-flashcards\\right.png"
WRONG = "C:\\Users\\Adrian\\Desktop\\vsc\\PYTHON\\day-30-flashcards\\wrong.png"
BACKGROUND_COLOR = "#aeb9e6"
CARD_COLOR_BACK = "#91c2af"
TOTAL_WORDS = 101

# ----------------------------------- SCREEN ------------------------------------------------
window = Tk() 
window.minsize(width= 900, height= 800)
window.title("Flashy")
window.config(bg= BACKGROUND_COLOR)

# ----------------------------------- CARDS -----------------------------------
image_card_back =  PhotoImage(file = CARD_BACK)
canvas_back = Canvas(width = 790, height = 520)
canvas_back.create_image(400, 260,image = image_card_back) 
canvas_back.config(bg = BACKGROUND_COLOR, highlightthickness = 0)

image_card_front = PhotoImage(file = CARD_FRONT)
canvas_front = Canvas(width = 790, height = 520)
canvas_front.create_image(400,260, image = image_card_front)
canvas_front.config(bg = BACKGROUND_COLOR, highlightthickness = 0)
canvas_front.place(x = 60, y = 95)

#  ----------------------------------- STARTING VALUES  -----------------------------------
already_guessed = []
random_number = random.randint(0, 100)
dict = None  # Vom inițializa acest dicționar în main()
image_right = None  # Vom inițializa aceste imagini în buttons()
image_wrong = None
label_language = None  # Vom inițializa aceste etichete în labels()
label_word = None

#  ----------------------------------- FUNCTIONS ------------------------------------------
def labels(starting_word):
    global label_language, label_word

    label_language = Label(text = "French", font = ("Times New Roman", 25, "italic"))
    label_language.place(x = 420, y = 200)
    label_language.config(bg = "white")

    label_word = Label(text= starting_word, font= ("Times New Roman", 40, "bold"))
    label_word.place(x = 380, y = 320)
    label_word.config(bg = "white")

def buttons(): 
    global button_right, button_wrong, image_right, image_wrong

    image_right = PhotoImage(file = RIGHT)
    image_wrong = PhotoImage(file = WRONG)

    button_right = Button(width = 100, height = 100, command = action_right, image = image_right, bg = BACKGROUND_COLOR, borderwidth = 0)
    button_right.config(activebackground= BACKGROUND_COLOR)
    button_right.place(x = 650, y = 650)

    button_wrong = Button(width = 100, height = 100, command = action_wrong, image = image_wrong, bg = BACKGROUND_COLOR, borderwidth = 0)
    button_wrong.config(activebackground= BACKGROUND_COLOR)
    button_wrong.place(x = 150 , y = 650)


def create_dataframe():
    dataframe = pandas.read_csv("C:\\Users\\Adrian\\Desktop\\vsc\\PYTHON\\day-30-flashcards\\french_words.csv")
    dataframe_dictionary = dataframe.to_dict()
    return dataframe_dictionary

def flip_cards(card_to_hide, card_to_show, language, index): 
    global dict  
    
    card_to_hide.place_forget()
    card_to_show.place(x=60, y=95)

    word = dict[language][index] 

    if language == "English": 
        color = CARD_COLOR_BACK
    else: 
        color = "white"
    label_language.config(text=language, font=("Times New Roman", 25, "italic"), bg= color)
    label_word.config(text=word, font=("Times New Roman", 40, "bold"), bg = color)

def get_index(already_guessed):
    random_number = random.randint(0, 100)
    while random_number in already_guessed and len(already_guessed) < 100: 
        random_number = random.randint(0, 100)
    return random_number

def setup():
    global random_number
    random_number = get_index(already_guessed)
    
    flip_cards(canvas_back, canvas_front, "French", random_number)
    window.after(3000, lambda:flip_cards(canvas_front, canvas_back, "English", random_number))

def action_right():
    already_guessed.append(random_number)
    setup()
    
def action_wrong(): 
    setup()

def main(): 
    global dict 
    
    dict = create_dataframe()
    starting_word = dict["French"][random_number]

    labels(starting_word)
    buttons()

    window.after(3000, lambda:flip_cards(canvas_front, canvas_back, "English", random_number))

# ----------------------------------- ----------------------------------- -----------------------------------

main()
window.mainloop()