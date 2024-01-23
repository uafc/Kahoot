###############################################################################
#    INCLUDES:
###############################################################################

import tkinter as tk # Used to create game interface.
from bs4 import BeautifulSoup
from webscraping import scrape_questions_and_answers

###############################################################################
#    CONSTANTS:
###############################################################################

GAME_DIMENSION = 400
NORMAL_FONT = ("consolas", 10)

###############################################################################
#    Functions:
###############################################################################

def start(question_number,score):

    num_choices = len(choices[question_number])
    button_height = int(GAME_DIMENSION/(num_choices+1))

    question_label = tk.Label(text=questions[question_number],
                              font=NORMAL_FONT,
                              bg="white",
                              fg="black",
                              wraplength=GAME_DIMENSION)

    question_label.place(width=GAME_DIMENSION,
                         height=button_height,
                         x=0,
                         y=0)

    for i in range(num_choices):

        choice = (choices[question_number])[i]

        choice_button = tk.Button(window,
                                  text=choice,
                                  wraplength=GAME_DIMENSION,
                                  font=NORMAL_FONT,
                                  bg="white",
                                  highlightbackground="white",
                                  fg="black",
                                  command=lambda choice=choice: check_answer(choice,question_number,score)
                                  )

        choice_button.place(width=GAME_DIMENSION,
                            height=button_height,
                            x=0,
                            y=(i+1)*button_height)

def check_answer(choice,question_number,score):


    if choice == answers_list[question_number]:
        score += 1
        score_label = tk.Label(text="Correct",
                                wraplength=GAME_DIMENSION,
                                font=NORMAL_FONT,
                                bg="green",
                                fg="black")
        
        score_label.place(width=GAME_DIMENSION,
                            height=GAME_DIMENSION,
                            x=0,
                            y=0)
    else:
        score_label = tk.Label(text="Incorrect",
                                wraplength=GAME_DIMENSION,
                                font=NORMAL_FONT,
                                bg="red",
                                fg="black")
        
        score_label.place(width=GAME_DIMENSION,
                            height=GAME_DIMENSION,
                            x=0,
                            y=0)

    window.after(500, lambda: next_question(question_number, score))


def next_question(question_number, score):

    # Remove past buttons and labels
    for item in canvas.winfo_children():
        item.destroy()

    question_number += 1

    if question_number < total_questions:
        start(question_number,score)
    else:
        end_label = tk.Label(text='Finished, score: ' + str(score),
                             wraplength=GAME_DIMENSION,
                             font=NORMAL_FONT,
                             bg="white",
                             fg="black")

        end_label.place(width=GAME_DIMENSION,
                        height=GAME_DIMENSION,
                        x=0,
                        y=0)

###############################################################################
#    MAIN:
###############################################################################

webscraping_data = scrape_questions_and_answers()

questions = list()
choices = list()
answers_list = list()
for question, answers in webscraping_data.items():
    questions.append(question)
    choices.append(answers[0])
    if answers[1]:
        answers_list.append(answers[1][0])

total_questions = len(questions)

window = tk.Tk()
window.title("Kahoot Game")
window.resizable(False, False)

# Create the canvas for the game.
canvas = tk.Canvas(window, bg="white", height=GAME_DIMENSION, width=GAME_DIMENSION)

# Pack the canvas.
canvas.pack()

# Start the game
start(0,0)

# Run the main loop of the program.
tk.mainloop()