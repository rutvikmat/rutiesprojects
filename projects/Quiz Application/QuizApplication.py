import tkinter as tk
from tkinter import messagebox

# --- Quiz Data ---
quiz_data = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "New Delhi", "Kolkata", "Chennai"],
        "answer": "New Delhi"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": "Mars"
    },
    {
        "question": "What is the largest mammal?",
        "options": ["Elephant", "Blue Whale", "Giraffe", "Great White Shark"],
        "answer": "Blue Whale"
    }
]

# --- Global variables ---
current_question_index = 0
score = 0


# --- Functions ---
def display_question():
    """Displays the current question and options."""
    question_data = quiz_data[current_question_index]
    question_label.config(text=question_data["question"])

    # Set the text for the radio buttons
    for i, option in enumerate(question_data["options"]):
        option_vars[i].set(option)  # Set the value of the radio button
        radio_buttons[i].config(text=option)  # Set the display text

    # Clear previous selection
    selected_option.set(None)


def check_answer():
    """Checks the selected answer and updates the score."""
    global current_question_index, score

    answer = quiz_data[current_question_index]["answer"]
    if selected_option.get() == answer:
        score += 1

    # Move to the next question
    current_question_index += 1

    if current_question_index < len(quiz_data):
        display_question()
    else:
        # End of quiz
        messagebox.showinfo("Quiz Finished",
                            f"You have completed the quiz!\nYour final score is: {score}/{len(quiz_data)}")
        window.destroy()


# --- UI Setup ---
window = tk.Tk()
window.title("Quiz Application")
window.geometry("450x300")

question_label = tk.Label(window, text="", font=("Helvetica", 14), wraplength=400)
question_label.pack(pady=20)

# Variable to store the selected option (string)
selected_option = tk.StringVar(value=None)

# Variables and radio buttons for options
option_vars = [tk.StringVar() for _ in range(4)]
radio_buttons = []
for i in range(4):
    rb = tk.Radiobutton(window, text="", variable=selected_option, value="", font=("Helvetica", 12))
    rb.pack(anchor='w', padx=50)
    radio_buttons.append(rb)

# Link the radio button values to the option variables
for i in range(4):
    radio_buttons[i]['value'] = quiz_data[0]['options'][i]  # Set initial values

submit_button = tk.Button(window, text="Submit", command=check_answer)
submit_button.pack(pady=20)

# --- Start Quiz ---
display_question()
window.mainloop()